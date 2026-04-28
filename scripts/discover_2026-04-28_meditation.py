"""Meditation-only sweep into data/2026-04-28/ (running same day as fitness sweep).

Quota budget tight (~1000 today): PAGES_PER_KEYWORD=1, 10 keywords =
~1,000 search.list quota + ~50 channels.list quota = under 1,050 total.

Cross-date dedup against ALL prior category files so yoga/Pilates/PT
channels already in mindset/fitness/nutrition don't re-surface.

Output: data/2026-04-28/meditation.csv (+ meditation_enriched.csv copy).
"""

from __future__ import annotations

import csv
import os
import re
import sys
import time
import warnings
from pathlib import Path

from dotenv import load_dotenv
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import yaml

warnings.filterwarnings("ignore")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from influencer_finder.extractors.email_regex import (  # noqa: E402
    STRICT_EMAIL_RE,
    OBFUSC_EMAIL_RE,
)
from influencer_finder.extractors.bio import extract_bio_links  # noqa: E402
from influencer_finder.extractors.website import WebsiteCrawler  # noqa: E402

DATED_OLD_DIRS = [
    ROOT / "data" / "2026-04-24",
    ROOT / "data" / "2026-04-25",
    ROOT / "data" / "2026-04-27",
]
DATED_NEW = ROOT / "data" / "2026-04-28"

# Dedup across ALL prior categories so we don't re-surface yoga/PT/etc
DEDUP_CATEGORIES = ["fitness", "career", "nutrition", "lifestyle", "beatmakers", "meditation"]

MIN_SUBS = 1000
TARGET_PER_CATEGORY = 300
MAX_BIO_LINKS_PER_CHANNEL = 3
C_CRAWL_MIN_SUBS = 1000
PAGES_PER_KEYWORD = 1  # tight quota — 1 page only

EXCLUDE_COUNTRIES = {"KR", "JP"}

RUN_ORDER = ["meditation"]

# Meditation-only keywords. Avoid "yoga" / "yoga nidra" — those go to mindset
# per categorization rule; explicit meditation lineages chosen instead.
KEYWORDS = {
    "meditation": [
        # Mindfulness practice (general)
        ("guided meditation teacher", None),
        ("mindfulness meditation teacher", None),
        ("online meditation course", None),
        ("daily meditation practice teacher", None),
        # Buddhist / Vipassana / Zen
        ("vipassana meditation teacher", None),
        ("insight meditation teacher", None),
        ("zen meditation teacher", None),
        # MBSR / clinical
        ("MBSR teacher online", None),
        # Sleep / TM
        ("sleep meditation channel", None),
        ("transcendental meditation teacher", None),
    ],
}

TARGET_COLUMNS = [
    "first_name", "full_name", "handle", "platform", "follower_count", "country",
    "email", "profile_url", "website", "description", "niche", "segment_original",
    "industry", "angle_to_take", "source_url", "raw_context", "is_role_based",
    "has_mx", "detected_tech",
]

_NL = re.compile(r"[\r\n]+")
_WS = re.compile(r"\s+")
_NAME_TOKEN_RE = re.compile(r"[A-Za-zÀ-ɏ][A-Za-zÀ-ɏ'.\-]*")

ROLE_BASED_PREFIXES = {
    "info", "contact", "support", "help", "hello", "hi", "admin",
    "press", "media", "pr", "business", "biz", "team", "office",
    "inquiries", "enquiries", "collab", "collabs", "collaboration",
    "partnerships", "sales", "service", "customer_service",
    "customerservice", "noreply", "no-reply", "enquiry",
}


def flatten(v: str) -> str:
    if not v:
        return ""
    return _WS.sub(" ", _NL.sub(" ", v)).strip()


def first_name_of(full: str) -> str:
    if not full:
        return ""
    m = _NAME_TOKEN_RE.search(full)
    if m:
        return m.group(0)
    parts = full.split()
    return parts[0] if parts else ""


def is_role_based(email: str) -> bool:
    local = email.split("@", 1)[0].lower()
    return local in ROLE_BASED_PREFIXES


def extract_first_email(text: str):
    if not text:
        return None
    for m in STRICT_EMAIL_RE.finditer(text):
        email = m.group(1)
        s, e = m.span(1)
        ctx = text[max(0, s - 100): e + 100]
        return email, flatten(ctx)
    for m in OBFUSC_EMAIL_RE.finditer(text):
        local, domain, tld = m.group(1), m.group(2), m.group(3)
        domain_clean = re.sub(r"\s*[\(\[\{]?\s*(dot|점|닷)\s*[\)\]\}]?\s*", ".", domain, flags=re.I)
        domain_clean = re.sub(r"\s+", "", domain_clean).strip(".")
        candidate = f"{local}@{domain_clean}.{tld}"
        if STRICT_EMAIL_RE.search(candidate):
            s, e = m.span()
            ctx = text[max(0, s - 100): e + 100]
            return candidate, flatten(ctx)
    return None


def read_keys_from(paths: list[Path]) -> tuple[set, set]:
    emails, urls = set(), set()
    for p in paths:
        if not p.exists():
            continue
        with p.open(newline="", encoding="utf-8-sig", errors="replace") as f:
            for r in csv.DictReader(f):
                e = (r.get("email", "") or "").strip().lower()
                u = (r.get("profile_url", "") or "").strip().rstrip("/").lower()
                if e:
                    emails.add(e)
                if u:
                    urls.add(u)
    return emails, urls


def search_channel_ids_paginated(client, query: str, region: str | None,
                                  pages: int = PAGES_PER_KEYWORD) -> list[str]:
    ids: list[str] = []
    page_token: str | None = None
    for page_idx in range(pages):
        kwargs = {
            "q": query, "type": "channel", "part": "id",
            "maxResults": 50,
        }
        if region:
            kwargs["regionCode"] = region
        if page_token:
            kwargs["pageToken"] = page_token
        try:
            resp = client.search().list(**kwargs).execute()
        except HttpError as e:
            msg = str(e)
            if "quotaExceeded" in msg:
                print(f"    [quota EXCEEDED] aborting further searches")
                raise
            print(f"    [search ERR] {query!r} ({region}, page {page_idx + 1}): {e}")
            return ids
        items = resp.get("items", [])
        for it in items:
            cid = it.get("id", {}).get("channelId")
            if cid:
                ids.append(cid)
        page_token = resp.get("nextPageToken")
        if not page_token:
            break
    return ids


def fetch_channels(client, ids: list[str]) -> list[dict]:
    out = []
    for start in range(0, len(ids), 50):
        batch = ids[start: start + 50]
        try:
            resp = client.channels().list(
                id=",".join(batch),
                part="snippet,statistics",
                maxResults=50,
            ).execute()
        except HttpError as e:
            print(f"    [channels ERR] batch {start}: {e}")
            continue
        out.extend(resp.get("items", []))
    return out


def channel_to_partial(it: dict) -> dict | None:
    sn = it.get("snippet", {}) or {}
    st = it.get("statistics", {}) or {}
    desc = flatten(sn.get("description", "") or "")
    title = (sn.get("title", "") or "").strip()
    custom = sn.get("customUrl", "") or ""
    handle = custom.lstrip("@") if custom else it.get("id", "")
    profile_url = (
        f"https://www.youtube.com/@{handle}"
        if custom else f"https://www.youtube.com/channel/{it.get('id','')}"
    )
    try:
        subs = int(st.get("subscriberCount", "0"))
    except (TypeError, ValueError):
        subs = 0
    if subs < MIN_SUBS:
        return None
    country = (sn.get("country") or "").strip()
    if country.upper() in EXCLUDE_COUNTRIES:
        return None
    out = {c: "" for c in TARGET_COLUMNS}
    out["first_name"] = first_name_of(title)
    out["full_name"] = title
    out["handle"] = handle
    out["platform"] = "youtube"
    out["follower_count"] = str(subs)
    out["country"] = country
    out["profile_url"] = profile_url
    out["description"] = desc
    out["source_url"] = profile_url
    out["has_mx"] = ""
    return out


def fill_email_from_description(rec: dict) -> bool:
    found = extract_first_email(rec.get("description", ""))
    if not found:
        return False
    email, ctx = found
    rec["email"] = email
    rec["raw_context"] = ctx
    rec["source_url"] = rec["profile_url"]
    rec["is_role_based"] = "1" if is_role_based(email) else "0"
    return True


def fill_email_from_bio_crawl(rec: dict, crawler: WebsiteCrawler) -> bool:
    try:
        subs = int(rec.get("follower_count") or 0)
    except (TypeError, ValueError):
        subs = 0
    if subs < C_CRAWL_MIN_SUBS:
        return False
    bio = extract_bio_links(rec.get("description", ""))
    candidates = (bio.personal_domain_urls + bio.link_in_bio_urls)[:MAX_BIO_LINKS_PER_CHANNEL]
    if not candidates:
        return False
    for url in candidates:
        try:
            result = crawler.crawl(url)
        except Exception as e:
            print(f"      crawl error {url}: {e}")
            continue
        if not result.success or not result.emails:
            continue
        for em in result.emails:
            if not is_role_based(em.email):
                rec["email"] = em.email
                rec["raw_context"] = flatten(em.raw_context)
                rec["source_url"] = url
                rec["is_role_based"] = "0"
                rec["website"] = url
                return True
        em = result.emails[0]
        rec["email"] = em.email
        rec["raw_context"] = flatten(em.raw_context)
        rec["source_url"] = url
        rec["is_role_based"] = "1"
        rec["website"] = url
        return True
    return False


def append_rows(path: Path, new_rows: list[dict]) -> None:
    if path.exists():
        with path.open(newline="", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            fieldnames = list(reader.fieldnames or TARGET_COLUMNS)
            existing = list(reader)
    else:
        fieldnames = TARGET_COLUMNS
        existing = []

    combined = existing + [{c: r.get(c, "") for c in fieldnames} for r in new_rows]

    def fc(r):
        try:
            return -int(r.get("follower_count") or 0)
        except (TypeError, ValueError):
            return 0
    combined.sort(key=fc)
    combined = combined[:TARGET_PER_CATEGORY]

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(combined)


def main() -> None:
    csv.field_size_limit(sys.maxsize)
    load_dotenv(ROOT / ".env", override=True)
    key = os.environ.get("YOUTUBE_API_KEY", "")
    if not key.startswith("AIza"):
        print(f"ERROR: bad YOUTUBE_API_KEY (prefix {key[:6]!r})")
        sys.exit(1)
    client = build("youtube", "v3", developerKey=key, cache_discovery=False)

    cfg = yaml.safe_load((ROOT / "config.yaml").read_text())
    crawl_cfg = cfg.get("crawl", {}) or {}
    user_agents = crawl_cfg.get("user_agents") or [
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/123 Safari/537.36"
    ]
    delay_range = (
        float(crawl_cfg.get("request_delay_min_seconds", 1.0)),
        float(crawl_cfg.get("request_delay_max_seconds", 2.5)),
    )
    timeout_ms = int(crawl_cfg.get("timeout_seconds", 15)) * 1000

    # Cross-date + cross-category dedup (don't re-surface channels already classified)
    old_paths: list[Path] = []
    for d in DATED_OLD_DIRS + [DATED_NEW]:
        for c in DEDUP_CATEGORIES:
            old_paths.append(d / f"{c}_enriched.csv")
            old_paths.append(d / f"{c}_enriched_0425.csv")
            old_paths.append(d / f"{c}.csv")
    seen_emails, seen_urls = read_keys_from(old_paths)
    print(f"seen keys (cross-date + all categories): {len(seen_emails)} emails, {len(seen_urls)} urls")

    grand_quota = 0

    try:
        with WebsiteCrawler(
            user_agents=user_agents,
            delay_range=delay_range,
            timeout_ms=timeout_ms,
            respect_robots=True,
        ) as crawler:
            for category in RUN_ORDER:
                kws = KEYWORDS[category]
                t0 = time.time()
                print(f"\n=== {category} ({len(kws)} keywords × {PAGES_PER_KEYWORD} pages) ===")
                ids: list[str] = []
                seen_ids: set[str] = set()
                try:
                    for kw, region in kws:
                        cids = search_channel_ids_paginated(client, kw, region=region,
                                                            pages=PAGES_PER_KEYWORD)
                        grand_quota += 100 * PAGES_PER_KEYWORD
                        added = 0
                        for cid in cids:
                            if cid not in seen_ids:
                                seen_ids.add(cid)
                                ids.append(cid)
                                added += 1
                        tag = f" region={region}" if region else ""
                        print(f"  search '{kw}'{tag}: pulled {len(cids)} ({added} new uniq; cumul={len(ids)})")
                except HttpError as e:
                    if "quotaExceeded" in str(e):
                        print(f"  [!] quota during search; using {len(ids)} ids gathered so far")
                    else:
                        raise

                items = fetch_channels(client, ids)
                grand_quota += -(-len(ids) // 50) * 5
                print(f"  fetched {len(items)} channel snippets")

                phase1: list[dict] = []
                phase2_pending: list[dict] = []
                for it in items:
                    rec = channel_to_partial(it)
                    if rec is None:
                        continue
                    url_key = rec["profile_url"].rstrip("/").lower()
                    if url_key in seen_urls:
                        continue
                    if fill_email_from_description(rec):
                        e_key = rec["email"].strip().lower()
                        if e_key in seen_emails:
                            continue
                        phase1.append(rec)
                        seen_emails.add(e_key)
                        seen_urls.add(url_key)
                    else:
                        phase2_pending.append(rec)

                print(f"  phase 1 (description email): {len(phase1)} new")

                phase2: list[dict] = []
                for rec in phase2_pending:
                    if fill_email_from_bio_crawl(rec, crawler):
                        e_key = rec["email"].strip().lower()
                        url_key = rec["profile_url"].rstrip("/").lower()
                        if e_key in seen_emails or url_key in seen_urls:
                            continue
                        phase2.append(rec)
                        seen_emails.add(e_key)
                        seen_urls.add(url_key)

                print(f"  phase 2 (bio-crawl email): {len(phase2)} new")

                new_rows = phase1 + phase2
                if new_rows:
                    raw_path = DATED_NEW / f"{category}.csv"
                    enr_path = DATED_NEW / f"{category}_enriched.csv"
                    append_rows(raw_path, new_rows)
                    append_rows(enr_path, new_rows)

                dt = time.time() - t0
                print(f"  category total new: {len(new_rows)} (took {dt:.1f}s)")

    except HttpError as e:
        if "quotaExceeded" in str(e):
            print(f"\n[!] quota exceeded mid-run — partial results written")
        else:
            raise

    print(f"\nestimated quota used: ~{grand_quota}")


if __name__ == "__main__":
    main()
