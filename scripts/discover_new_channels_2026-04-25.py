"""Discover new YouTube channels for 5 categories, dedup against
data/2026-04-24/, and write 19-col base + _enriched CSVs to data/2026-04-25/.

Pipeline:
  1. For each category × keyword: search().list(type='channel', maxResults=50)
  2. Batch fetch channels.list(part='snippet,statistics') by ID
  3. Extract email from description (STRICT_EMAIL_RE / OBFUSC_EMAIL_RE)
  4. Filter: subs>=5000, has email, NOT in 2026-04-24
  5. Pick top-50 per category by subscriber count desc
  6. Write 19-col CSVs (base + _enriched siblings, identical content)

niche/segment_original/industry/angle_to_take are left empty here — Step 2
(per-person mapping files) will fill them in a later script.
"""

from __future__ import annotations

import csv
import os
import re
import sys
import time
import warnings
from pathlib import Path
from urllib.parse import urlparse

from dotenv import load_dotenv
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

warnings.filterwarnings("ignore")

ROOT = Path("/home/bjm/ABC/Marketing/youtube-crawling")
sys.path.insert(0, str(ROOT / "src"))

from influencer_finder.extractors.email_regex import (  # noqa: E402
    STRICT_EMAIL_RE,
    OBFUSC_EMAIL_RE,
)


DATED_OLD = ROOT / "data" / "2026-04-24"
DATED_NEW = ROOT / "data" / "2026-04-25"

CATEGORY_KEYWORDS = {
    "career": [
        "career coach",
        "resume writing coach",
        "interview preparation coach",
        "career development tips",
        "job search strategy",
        "linkedin coach",
        "tech career mentor",
        "career change coach",
        "executive coaching",
    ],
    "fitness": [
        "home workout trainer",
        "strength coach",
        "fitness transformation coach",
        "calisthenics tutorial",
        "personal trainer online",
        "weight loss coach",
        "yoga teacher youtube",
        "pilates instructor",
        "bodyweight workout coach",
    ],
    "nutrition": [
        "registered dietitian",
        "meal prep coach",
        "nutrition educator",
        "macro coaching",
        "plant based dietitian",
        "intuitive eating coach",
        "weight loss nutrition",
        "sports nutrition coach",
        "gut health nutritionist",
    ],
    "lifestyle": [
        "daily vlog",
        "home decor diy",
        "minimalism lifestyle",
        "productivity routine",
        "study with me",
        "morning routine vlog",
        "slow living vlog",
        "self care routine",
        "lifestyle blogger youtube",
    ],
    "beatmakers": [
        "beatmaker tutorial",
        "fl studio beat tutorial",
        "type beats tutorial",
        "music producer tutorial",
        "ableton tutorial",
        "lo-fi beat maker",
        "trap beat tutorial",
        "hip hop beat making",
        "music production beginner",
    ],
}

MIN_SUBS = 5000
TARGET_PER_CATEGORY = 50

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
    "customerservice", "noreply", "no-reply",
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


def extract_first_email(text: str) -> tuple[str, str] | None:
    """Return (email, raw_context_~100chars) or None. Prefers strict over obfuscated."""
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


def read_old_keys() -> tuple[set, set]:
    emails, urls = set(), set()
    for n in ["career", "fitness", "nutrition", "lifestyle", "beatmakers"]:
        p = DATED_OLD / f"{n}_enriched.csv"
        if not p.exists():
            continue
        with p.open(newline="", encoding="utf-8-sig") as f:
            for r in csv.DictReader(f):
                e = (r.get("email", "") or "").strip().lower()
                u = (r.get("profile_url", "") or "").strip().rstrip("/").lower()
                if e:
                    emails.add(e)
                if u:
                    urls.add(u)
    return emails, urls


def search_channel_ids(client, query: str, max_results: int = 50) -> list[str]:
    try:
        resp = client.search().list(
            q=query, type="channel", part="id",
            maxResults=min(50, max_results),
        ).execute()
    except HttpError as e:
        print(f"  [search ERR] {query}: {e}")
        return []
    return [it["id"]["channelId"] for it in resp.get("items", []) if it.get("id", {}).get("channelId")]


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
            print(f"  [channels ERR] batch {start}: {e}")
            continue
        out.extend(resp.get("items", []))
    return out


def channel_to_record(it: dict, category: str) -> dict | None:
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
    found = extract_first_email(desc)
    if not found:
        return None
    email, ctx = found
    out = {c: "" for c in TARGET_COLUMNS}
    out["first_name"] = first_name_of(title)
    out["full_name"] = title
    out["handle"] = handle
    out["platform"] = "youtube"
    out["follower_count"] = str(subs)
    out["country"] = sn.get("country") or ""
    out["email"] = email
    out["profile_url"] = profile_url
    out["description"] = desc
    out["source_url"] = profile_url
    out["raw_context"] = ctx
    out["is_role_based"] = "1" if is_role_based(email) else "0"
    out["has_mx"] = ""  # left blank — pipeline `validate` would fill; not done here
    return out


def write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=TARGET_COLUMNS)
        w.writeheader()
        w.writerows(rows)


def main() -> None:
    csv.field_size_limit(sys.maxsize)
    load_dotenv(ROOT / ".env", override=True)
    key = os.environ.get("YOUTUBE_API_KEY", "")
    if not key.startswith("AIza"):
        print(f"ERROR: bad YOUTUBE_API_KEY (prefix {key[:6]!r})")
        sys.exit(1)
    client = build("youtube", "v3", developerKey=key, cache_discovery=False)

    old_emails, old_urls = read_old_keys()
    print(f"old (2026-04-24) keys: {len(old_emails)} emails, {len(old_urls)} urls")

    grand_quota = 0
    for category, kws in CATEGORY_KEYWORDS.items():
        t0 = time.time()
        print(f"\n=== {category} ===")
        ids: list[str] = []
        seen_ids: set[str] = set()
        for kw in kws:
            cids = search_channel_ids(client, kw, max_results=50)
            grand_quota += 100
            for cid in cids:
                if cid not in seen_ids:
                    seen_ids.add(cid)
                    ids.append(cid)
            print(f"  search '{kw}': +{len(cids)} (cumulative unique={len(ids)})")
        items = fetch_channels(client, ids)
        grand_quota += -(-len(ids) // 50)
        print(f"  fetched {len(items)} channel snippets")

        records: list[dict] = []
        seen_emails_local: set[str] = set()
        seen_urls_local: set[str] = set()
        for it in items:
            rec = channel_to_record(it, category)
            if rec is None:
                continue
            e = rec["email"].strip().lower()
            u = rec["profile_url"].strip().rstrip("/").lower()
            if e in old_emails or u in old_urls:
                continue
            if e in seen_emails_local or u in seen_urls_local:
                continue
            seen_emails_local.add(e)
            seen_urls_local.add(u)
            records.append(rec)

        # sort by follower_count desc, take top N
        records.sort(key=lambda r: -int(r["follower_count"]))
        records = records[:TARGET_PER_CATEGORY]

        write_csv(DATED_NEW / f"{category}.csv", records)
        write_csv(DATED_NEW / f"{category}_enriched.csv", records)
        # Update cross-category seen sets so subsequent categories don't pick the same channel
        for r in records:
            old_emails.add(r["email"].strip().lower())
            old_urls.add(r["profile_url"].strip().rstrip("/").lower())

        print(f"  -> wrote {len(records)} records to {category}.csv & {category}_enriched.csv  ({time.time()-t0:.1f}s)")

    print(f"\nestimated quota used: {grand_quota}")


if __name__ == "__main__":
    main()
