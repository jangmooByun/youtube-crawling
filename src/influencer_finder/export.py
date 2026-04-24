from __future__ import annotations

import csv
import re
from pathlib import Path
from typing import Optional
from urllib.parse import urlparse

from .db import connect
from .extractors.bio import LINK_IN_BIO_DOMAINS, SOCIAL_DOMAINS

COLUMNS = [
    "first_name",
    "full_name",
    "handle",
    "platform",
    "follower_count",
    "country",
    "email",
    "profile_url",
    "website",
    "description",
    "niche",
    "segment_original",
    "industry",
    "angle_to_take",
    "source_url",
    "raw_context",
    "is_role_based",
    "has_mx",
    "detected_tech",
]

LLM_FILLED_COLUMNS = ("niche", "segment_original", "industry", "angle_to_take")

_ALLOWED_FILTER_RE = re.compile(
    r"^[\sA-Za-z0-9_=<>!'.()%\-]+(?:AND|OR|\s|[\sA-Za-z0-9_=<>!'.()%\-])*$",
    re.IGNORECASE,
)

_EXCLUDED_WEBSITE_DOMAINS = SOCIAL_DOMAINS | LINK_IN_BIO_DOMAINS

_NAME_TOKEN_RE = re.compile(r"[A-Za-zÀ-ɏ][A-Za-zÀ-ɏ'.\-]*")


def export_csv(
    output_path: str | Path,
    db_path: Optional[str | Path] = None,
    where: Optional[str] = None,
) -> int:
    sql = """
        SELECT
            p.id AS profile_id,
            p.display_name AS display_name,
            p.handle AS handle,
            p.platform AS platform,
            p.follower_count AS follower_count,
            p.country AS country,
            p.bio AS description,
            p.url AS profile_url,
            e.email AS email,
            e.source_url AS source_url,
            e.raw_context AS raw_context,
            e.is_role_based AS is_role_based,
            e.has_mx AS has_mx,
            e.syntax_valid AS syntax_valid,
            (
                SELECT GROUP_CONCAT(s.url, CHAR(10))
                FROM sources s
                WHERE s.profile_id = p.id
                  AND s.type IN ('external_link', 'website')
            ) AS source_urls,
            (
                SELECT GROUP_CONCAT(s.detected_tech)
                FROM sources s
                WHERE s.profile_id = p.id
                  AND s.detected_tech IS NOT NULL
                  AND s.detected_tech != ''
            ) AS detected_tech_raw
        FROM profiles p
        JOIN (
            SELECT
                em.id, em.profile_id, em.email, em.source_url, em.raw_context,
                em.is_role_based, em.has_mx, em.syntax_valid,
                ROW_NUMBER() OVER (
                    PARTITION BY em.profile_id
                    ORDER BY COALESCE(em.is_role_based, 1) ASC,
                             COALESCE(em.has_mx, 0) DESC,
                             COALESCE(em.syntax_valid, 0) DESC,
                             em.id ASC
                ) AS rn
            FROM emails em
        ) e ON e.profile_id = p.id AND e.rn = 1
    """
    if where:
        if not _ALLOWED_FILTER_RE.match(where):
            raise ValueError(f"Unsafe filter expression: {where!r}")
        sql += f" WHERE {where}"
    sql += " ORDER BY p.follower_count DESC NULLS LAST, p.id"

    conn = connect(db_path) if db_path else connect()
    try:
        rows = conn.execute(sql).fetchall()
    finally:
        conn.close()

    by_email: dict[str, dict] = {}
    for row in rows:
        record = _row_to_record(row)
        email = record["email"]
        if not email:
            continue
        prev = by_email.get(email)
        if prev is None or (record["follower_count"] or 0) > (prev["follower_count"] or 0):
            by_email[email] = record

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    sorted_records = sorted(
        by_email.values(),
        key=lambda r: (-(r["follower_count"] or 0), r["email"]),
    )
    with output_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNS)
        writer.writeheader()
        for record in sorted_records:
            writer.writerow(record)

    return len(sorted_records)


def _row_to_record(row) -> dict:
    full_name = (row["display_name"] or "").strip()
    return {
        "first_name": _first_name_of(full_name),
        "full_name": full_name,
        "handle": row["handle"] or "",
        "platform": row["platform"] or "",
        "follower_count": row["follower_count"],
        "country": row["country"] or "",
        "email": row["email"],
        "profile_url": row["profile_url"] or "",
        "website": _pick_personal_website(row["source_urls"]),
        "description": row["description"] or "",
        "niche": "",
        "segment_original": "",
        "industry": "",
        "angle_to_take": "",
        "source_url": row["source_url"] or "",
        "raw_context": row["raw_context"] or "",
        "is_role_based": row["is_role_based"],
        "has_mx": row["has_mx"],
        "detected_tech": _dedupe_tech(row["detected_tech_raw"]),
    }


def _first_name_of(full_name: str) -> str:
    if not full_name:
        return ""
    m = _NAME_TOKEN_RE.search(full_name)
    if m:
        return m.group(0)
    parts = full_name.split()
    return parts[0] if parts else ""


def _pick_personal_website(source_urls: Optional[str]) -> str:
    if not source_urls:
        return ""
    for url in source_urls.split("\n"):
        url = url.strip()
        if not url:
            continue
        host = _host_of(url)
        if host and not _is_excluded_host(host):
            return url
    return ""


def _host_of(url: str) -> str:
    try:
        netloc = urlparse(url).netloc.lower()
    except ValueError:
        return ""
    if netloc.startswith("www."):
        netloc = netloc[4:]
    return netloc


def _is_excluded_host(host: str) -> bool:
    if host in _EXCLUDED_WEBSITE_DOMAINS:
        return True
    for bad in _EXCLUDED_WEBSITE_DOMAINS:
        if host.endswith("." + bad):
            return True
    return False


def _dedupe_tech(raw: Optional[str]) -> str:
    if not raw:
        return ""
    items = sorted({x.strip() for x in raw.split(",") if x.strip()})
    return ",".join(items)
