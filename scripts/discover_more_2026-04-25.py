"""Supplementary discovery for data/2026-04-25/ — expands keywords with
multi-lingual / regional variants and APPENDS to existing per-category CSVs
(does NOT overwrite). Dedup against both 2026-04-24 and current 2026-04-25.
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

warnings.filterwarnings("ignore")

ROOT = Path("/home/bjm/ABC/Marketing/youtube-crawling")
sys.path.insert(0, str(ROOT / "src"))

from influencer_finder.extractors.email_regex import (  # noqa: E402
    STRICT_EMAIL_RE,
    OBFUSC_EMAIL_RE,
)


DATED_OLD = ROOT / "data" / "2026-04-24"
DATED_NEW = ROOT / "data" / "2026-04-25"

# (keyword, optional regionCode, optional order)
EXPANDED_KEYWORDS = {
    "career": [
        ("salary negotiation coach", None, None),
        ("tech interview prep", None, None),
        ("data science career mentor", None, None),
        ("career advice hindi", "IN", None),
        ("ssc coaching", "IN", None),
        ("coaching laboral", None, None),
        ("consultoria de carreira", "BR", None),
        ("취업 준비", "KR", None),
    ],
    "fitness": [
        ("ghar par workout hindi", "IN", None),
        ("yoga guide hindi", "IN", None),
        ("entrenador personal en casa", None, None),
        ("treino em casa", "BR", None),
        ("홈트 추천", "KR", None),
        ("宅トレ", "JP", None),
        ("kettlebell workout", None, None),
        ("running coach", None, None),
    ],
    "nutrition": [
        ("diet plan hindi", "IN", None),
        ("weight loss diet hindi", "IN", None),
        ("nutricionista", None, None),
        ("nutricionista", "BR", None),
        ("식단 관리", "KR", None),
        ("keto coach", None, None),
        ("intermittent fasting coach", None, None),
        ("diabetic diet", None, None),
    ],
    "beatmakers": [
        ("tutorial fl studio español", None, None),
        ("beatmaker español", None, None),
        ("fl studio tutorial portugues", "BR", None),
        ("fl studio tutorial deutsch", "DE", None),
        ("비트메이커", "KR", None),
        ("amapiano producer tutorial", None, None),
        ("afrobeat producer tutorial", None, None),
        ("drill beat tutorial", None, None),
    ],
    "lifestyle": [
        # already at 50; small variety pass for completeness
        ("japan slow living vlog", "JP", None),
        ("korean lifestyle vlog", "KR", None),
        ("vlog brasileira diario", "BR", None),
    ],
}

MIN_SUBS = 5000
TARGET_PER_CATEGORY = 80  # cap per file (existing + new)

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
        with p.open(newline="", encoding="utf-8-sig") as f:
            for r in csv.DictReader(f):
                e = (r.get("email", "") or "").strip().lower()
                u = (r.get("profile_url", "") or "").strip().rstrip("/").lower()
                if e:
                    emails.add(e)
                if u:
                    urls.add(u)
    return emails, urls


def search_channel_ids(client, query: str, region: str = None, order: str = None,
                       max_results: int = 50) -> list[str]:
    kwargs = {
        "q": query, "type": "channel", "part": "id",
        "maxResults": min(50, max_results),
    }
    if region:
        kwargs["regionCode"] = region
    if order:
        kwargs["order"] = order
    try:
        resp = client.search().list(**kwargs).execute()
    except HttpError as e:
        msg = str(e)
        if "quotaExceeded" in msg:
            print(f"  [quota EXCEEDED] aborting further searches")
            raise
        print(f"  [search ERR] {query} ({region}): {e}")
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


def channel_to_record(it: dict) -> dict | None:
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
    out["has_mx"] = ""
    return out


def append_rows(path: Path, new_rows: list[dict]) -> None:
    """Append new_rows to existing CSV at path. Preserves existing column order
    if the file exists; otherwise creates with TARGET_COLUMNS."""
    if path.exists():
        with path.open(newline="", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            fieldnames = list(reader.fieldnames or TARGET_COLUMNS)
            existing = list(reader)
    else:
        fieldnames = TARGET_COLUMNS
        existing = []

    # Sort combined by follower_count desc, cap to TARGET_PER_CATEGORY
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

    # Old keys = 2026-04-24 + current 2026-04-25 (we treat both as 'already seen')
    old_paths = (
        [DATED_OLD / f"{c}_enriched.csv" for c in ["career","fitness","nutrition","lifestyle","beatmakers"]]
        + [DATED_NEW / f"{c}_enriched.csv" for c in ["career","fitness","nutrition","lifestyle","beatmakers"]]
    )
    seen_emails, seen_urls = read_keys_from(old_paths)
    print(f"seen keys (old+today): {len(seen_emails)} emails, {len(seen_urls)} urls")

    grand_quota = 0
    new_emails_per_cat: dict[str, list[str]] = {}

    try:
        for category, kws in EXPANDED_KEYWORDS.items():
            t0 = time.time()
            print(f"\n=== {category} ({len(kws)} new keywords) ===")
            ids: list[str] = []
            seen_ids: set[str] = set()
            for kw, region, order in kws:
                cids = search_channel_ids(client, kw, region=region, order=order, max_results=50)
                grand_quota += 100
                added = 0
                for cid in cids:
                    if cid not in seen_ids:
                        seen_ids.add(cid)
                        ids.append(cid)
                        added += 1
                tag = f" region={region}" if region else ""
                print(f"  search '{kw}'{tag}: +{len(cids)} ({added} new unique; total={len(ids)})")
            items = fetch_channels(client, ids)
            grand_quota += -(-len(ids) // 50)
            print(f"  fetched {len(items)} channel snippets")

            new_records: list[dict] = []
            for it in items:
                rec = channel_to_record(it)
                if rec is None:
                    continue
                e = rec["email"].strip().lower()
                u = rec["profile_url"].strip().rstrip("/").lower()
                if e in seen_emails or u in seen_urls:
                    continue
                seen_emails.add(e)
                seen_urls.add(u)
                new_records.append(rec)
            print(f"  new records (passing filters): {len(new_records)}")

            new_emails_per_cat[category] = [r["email"] for r in new_records]

            # Append to both base + _enriched
            append_rows(DATED_NEW / f"{category}.csv", new_records)
            append_rows(DATED_NEW / f"{category}_enriched.csv", new_records)
            print(f"  appended; elapsed {time.time()-t0:.1f}s")
    except HttpError as e:
        if "quotaExceeded" in str(e):
            print(f"\n[!] Stopped early due to quota exhaustion.")
        else:
            raise

    print(f"\nestimated quota used in this run: {grand_quota}")
    print("\nNew emails per category (these need mapping entries):")
    for cat, emails in new_emails_per_cat.items():
        print(f"  {cat}: {len(emails)}")
        for e in emails:
            print(f"    + {e}")


if __name__ == "__main__":
    main()
