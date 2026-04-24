from __future__ import annotations

import logging
from pathlib import Path
from typing import Optional

import yaml
from rich.console import Console
from rich.progress import Progress

from . import db as db_module
from .db import (
    connect,
    init_db,
    insert_email,
    insert_source,
    mark_source_fetched,
    session,
    update_email_validation,
    upsert_profile,
)
from .discovery.youtube import YouTubeDiscovery
from .extractors.bio import extract_bio_links
from .extractors.email_regex import extract_emails
from .extractors.website import WebsiteCrawler
from .models import Email, Profile, Source
from .validators.mx import has_mx_record
from .validators.role import is_role_based
from .validators.syntax import is_valid_syntax

logger = logging.getLogger(__name__)
console = Console()


def load_config(path: str | Path = "config.yaml") -> dict:
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def discover_youtube(
    keyword: str,
    max_channels: int = 50,
    min_subscribers: Optional[int] = None,
    max_subscribers: Optional[int] = None,
    region_code: Optional[str] = None,
    relevance_language: Optional[str] = None,
    db_path: Optional[str] = None,
) -> int:
    init_db(db_path or db_module.DEFAULT_DB_PATH)
    yt = YouTubeDiscovery()
    console.print(f"[cyan]Searching YouTube:[/] {keyword!r} (max {max_channels})")

    channel_ids = yt.search_channels(
        keyword,
        max_results=max_channels,
        region_code=region_code,
        relevance_language=relevance_language,
    )
    console.print(f"  → found {len(channel_ids)} channel IDs")

    inserted = 0
    with session(db_path or db_module.DEFAULT_DB_PATH) as conn:
        for ch in yt.fetch_channels(channel_ids):
            subs = ch.subscriber_count or 0
            if min_subscribers and subs < min_subscribers:
                continue
            if max_subscribers and subs > max_subscribers:
                continue
            profile = Profile(
                platform="youtube",
                handle=ch.handle,
                display_name=ch.title,
                url=ch.url,
                follower_count=ch.subscriber_count,
                bio=ch.description,
                country=ch.country,
            )
            pid = upsert_profile(conn, profile)
            insert_source(
                conn,
                Source(
                    profile_id=pid,
                    url=ch.url,
                    type="channel_description",
                    success=True,
                ),
            )
            inserted += 1
    console.print(f"[green]Saved {inserted} YouTube profiles.[/]")
    return inserted


def extract_from_bios(db_path: Optional[str] = None) -> dict[str, int]:
    stats = {"profiles_processed": 0, "emails_found": 0, "links_found": 0}
    with session(db_path or db_module.DEFAULT_DB_PATH) as conn:
        rows = conn.execute(
            "SELECT id, url, bio FROM profiles WHERE bio IS NOT NULL AND bio != ''"
        ).fetchall()
        for row in rows:
            stats["profiles_processed"] += 1
            pid = row["id"]
            bio = row["bio"] or ""
            source_url = row["url"]

            for ex in extract_emails(bio):
                email = Email(
                    profile_id=pid,
                    email=ex.email,
                    source_url=source_url,
                    raw_context=ex.raw_context,
                    extraction_method=ex.method,
                )
                if insert_email(conn, email):
                    stats["emails_found"] += 1

            links = extract_bio_links(bio)
            for url in links.link_in_bio_urls + links.personal_domain_urls:
                if insert_source(conn, Source(profile_id=pid, url=url, type="external_link")):
                    stats["links_found"] += 1
            for h in links.instagram_handles:
                ig_url = f"https://www.instagram.com/{h}/"
                insert_source(conn, Source(profile_id=pid, url=ig_url, type="external_link"))
            for h in links.tiktok_handles:
                tt_url = f"https://www.tiktok.com/@{h}"
                insert_source(conn, Source(profile_id=pid, url=tt_url, type="external_link"))
    console.print(
        f"[green]Extracted:[/] {stats['emails_found']} emails, "
        f"{stats['links_found']} external links from {stats['profiles_processed']} profiles"
    )
    return stats


def crawl_external_links(
    config_path: str | Path = "config.yaml",
    db_path: Optional[str] = None,
    max_urls: Optional[int] = None,
) -> dict[str, int]:
    cfg = load_config(config_path)
    crawl_cfg = cfg.get("crawl", {})
    priority_paths = cfg.get("website_paths_priority", cfg.get("website_paths_to_try", [""]))
    fallback_paths = cfg.get("website_paths_fallback", [])

    stats = {"fetched": 0, "succeeded": 0, "emails_found": 0}

    with session(db_path or db_module.DEFAULT_DB_PATH) as conn:
        rows = conn.execute(
            """
            SELECT s.id, s.profile_id, s.url
            FROM sources s
            WHERE s.type IN ('external_link', 'website')
              AND s.fetched_at IS NULL
              AND s.url NOT LIKE 'https://www.instagram.com/%'
              AND s.url NOT LIKE 'https://www.tiktok.com/%'
            """
        ).fetchall()

    if max_urls:
        rows = rows[:max_urls]

    if not rows:
        console.print("[yellow]No external links to crawl.[/]")
        return stats

    console.print(f"[cyan]Crawling {len(rows)} external links...[/]")

    with WebsiteCrawler(
        user_agents=crawl_cfg.get("user_agents", []),
        delay_range=(
            crawl_cfg.get("request_delay_min_seconds", 2),
            crawl_cfg.get("request_delay_max_seconds", 5),
        ),
        timeout_ms=crawl_cfg.get("timeout_seconds", 20) * 1000,
    ) as crawler:
        with Progress(console=console) as progress:
            task = progress.add_task("[cyan]crawl", total=len(rows))
            for row in rows:
                sid = row["id"]
                pid = row["profile_id"]
                url = row["url"]

                if _is_personal_domain(url):
                    results = crawler.crawl_site_paths(url, priority_paths, fallback_paths)
                else:
                    results = [crawler.crawl(url)]

                with session(db_path or db_module.DEFAULT_DB_PATH) as conn:
                    primary_ok = any(r.success for r in results)
                    tech_union: set[str] = set()
                    for r in results:
                        tech_union.update(r.detected_tech or [])
                    tech_str = ",".join(sorted(tech_union)) if tech_union else None
                    mark_source_fetched(conn, sid, primary_ok, detected_tech=tech_str)
                    stats["fetched"] += 1
                    if primary_ok:
                        stats["succeeded"] += 1
                    for result in results:
                        for ex in result.emails:
                            email = Email(
                                profile_id=pid,
                                email=ex.email,
                                source_url=result.url,
                                raw_context=ex.raw_context,
                                extraction_method=ex.method,
                            )
                            if insert_email(conn, email):
                                stats["emails_found"] += 1
                progress.advance(task)

    console.print(
        f"[green]Crawl done.[/] fetched={stats['fetched']} "
        f"ok={stats['succeeded']} new_emails={stats['emails_found']}"
    )
    return stats


def validate_emails(db_path: Optional[str] = None) -> dict[str, int]:
    stats = {"checked": 0, "syntax_valid": 0, "has_mx": 0, "role_based": 0}
    with session(db_path or db_module.DEFAULT_DB_PATH) as conn:
        rows = conn.execute(
            "SELECT id, email FROM emails WHERE syntax_valid IS NULL OR has_mx IS NULL"
        ).fetchall()
        for row in rows:
            eid = row["id"]
            addr = row["email"]
            syn = is_valid_syntax(addr)
            mx = has_mx_record(addr) if syn else False
            role = is_role_based(addr)
            update_email_validation(conn, eid, syn, mx, role)
            stats["checked"] += 1
            if syn:
                stats["syntax_valid"] += 1
            if mx:
                stats["has_mx"] += 1
            if role:
                stats["role_based"] += 1
    console.print(
        f"[green]Validated:[/] {stats['checked']} total, "
        f"{stats['syntax_valid']} valid syntax, {stats['has_mx']} with MX, "
        f"{stats['role_based']} role-based"
    )
    return stats


def _is_personal_domain(url: str) -> bool:
    from urllib.parse import urlparse

    host = urlparse(url).netloc.lower().removeprefix("www.")
    lib_domains = {
        "linktr.ee", "beacons.ai", "stan.store", "campsite.bio",
        "lnk.bio", "bio.link", "solo.to", "komi.io", "taplink.cc",
        "allmylinks.com",
    }
    return host not in lib_domains
