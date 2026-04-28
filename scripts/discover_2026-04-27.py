"""Re-sweep `fitness` with English-intent yoga / pilates / bodyweight keywords
into `data/2026-04-27/`.

Why: existing fitness data (2026-04-24, 2026-04-25) is heavy on IN/BR-localized
keywords and under-covers English-language yoga / pilates / bodyweight creators
who are the strongest AppBillChat ICP (mobile-app-native daily-routine product
fit: video class library, length filter, member tier).

Mirrors `scripts/discover_v3_2026-04-25.py` exactly (search → fetch → desc
email → bio-link crawl → CSV append, with KR/JP exclusion and cross-date
dedup against 2026-04-24 + 2026-04-25). Differences from v3:
  - MIN_SUBS = 5000 (per user)
  - TARGET_PER_CATEGORY = 100
  - RUN_ORDER = ["fitness"]
  - EXCLUDE_COUNTRIES = {"KR", "JP"} (v3 only had KR)
  - Portable ROOT (Path(__file__).resolve().parents[1])
  - Cross-date dedup loads 2026-04-24 AND 2026-04-25 enriched CSVs
  - English-only intent keywords, no region/language filter

Stops cleanly on quotaExceeded. Appends to existing CSVs; never overwrites.
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

DATED_OLD_DIRS = [ROOT / "data" / "2026-04-24", ROOT / "data" / "2026-04-25"]
DATED_NEW = ROOT / "data" / "2026-04-27"

MIN_SUBS = 5000
TARGET_PER_CATEGORY = 100
MAX_BIO_LINKS_PER_CHANNEL = 3
C_CRAWL_MIN_SUBS = 5000  # only crawl bio for channels >= this; saves time
PAGES_PER_KEYWORD = 2

EXCLUDE_COUNTRIES = {"KR", "JP"}

RUN_ORDER = ["fitness"]

# English-intent keywords only — no region/language filter, country-side
# filtering is done via EXCLUDE_COUNTRIES post-fetch. Chosen to be
# non-overlapping with prior fitness sweeps (v3 / _more / _new).
KEYWORDS = {
    "fitness": [
        # yoga
        ("online yoga teacher", None),
        ("yoga teacher training online", None),
        ("online vinyasa yoga", None),
        ("yin yoga online class", None),
        ("yoga membership program", None),
        # pilates
        ("online pilates instructor", None),
        ("online pilates course", None),
        ("mat pilates online", None),
        ("pilates teacher training online", None),
        # bodyweight (variants distinct from prior calisthenics keywords)
        ("bodyweight workout program", None),
        ("no equipment workout coach", None),
        ("calisthenics coach online", None),
        ("home strength training program", None),
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
    """Pull up to `pages` pages × 50 results for a single query."""
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
    """Return a record dict with as much filled as possible, but possibly no
    email yet. Returns None if the channel fails hard filters (subs, country)."""
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
    out["source_url"] = profile_url  # default, overwritten if email found via crawl
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
    """Crawl up to MAX_BIO_LINKS_PER_CHANNEL bio URLs to find an email."""
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

    old_paths: list[Path] = []
    for d in DATED_OLD_DIRS:
        old_paths.extend(d / f"{c}_enriched.csv" for c in RUN_ORDER)
    old_paths.extend(DATED_NEW / f"{c}_enriched.csv" for c in RUN_ORDER)
    seen_emails, seen_urls = read_keys_from(old_paths)
    print(f"seen keys (04-24 + 04-25 + 04-27): {len(seen_emails)} emails, {len(seen_urls)} urls")

    grand_quota = 0
    new_emails_per_cat: dict[str, list[str]] = {}

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
                    u = rec["profile_url"].strip().rstrip("/").lower()
                    if u in seen_urls:
                        continue
                    if fill_email_from_description(rec):
                        e = rec["email"].strip().lower()
                        if e in seen_emails:
                            continue
                        seen_emails.add(e)
                        seen_urls.add(u)
                        phase1.append(rec)
                    else:
                        phase2_pending.append(rec)

                print(f"  phase 1 (desc-email): {len(phase1)} new")
                print(f"  phase 2 (bio-crawl candidates): {len(phase2_pending)}")

                phase2: list[dict] = []
                for rec in phase2_pending:
                    if fill_email_from_bio_crawl(rec, crawler):
                        e = rec["email"].strip().lower()
                        u = rec["profile_url"].strip().rstrip("/").lower()
                        if e in seen_emails or u in seen_urls:
                            continue
                        seen_emails.add(e)
                        seen_urls.add(u)
                        phase2.append(rec)
                print(f"  phase 2 (bio-crawl): {len(phase2)} new")

                new_records = phase1 + phase2
                new_emails_per_cat[category] = [
                    f"{r['email']}\t(via {'bio' if r['source_url'] != r['profile_url'] else 'desc'})"
                    for r in new_records
                ]

                append_rows(DATED_NEW / f"{category}.csv", new_records)
                append_rows(DATED_NEW / f"{category}_enriched.csv", new_records)
                print(f"  appended {len(new_records)}; elapsed {time.time()-t0:.1f}s")
    except HttpError as e:
        if "quotaExceeded" in str(e):
            print(f"\n[!] Stopped early due to quota exhaustion.")
        else:
            raise

    print(f"\nestimated quota used in this run: {grand_quota}")
    print("\nNew rows per category (these need mapping_2026-04-27 entries):")
    for cat, items in new_emails_per_cat.items():
        print(f"  {cat}: {len(items)}")
        for line in items:
            print(f"    + {line}")


if __name__ == "__main__":
    main()
