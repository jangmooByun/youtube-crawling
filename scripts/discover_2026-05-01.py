"""0501 fresh-cycle discover (4 categories, new keywords).

Difference from 0429 standalone:
  - This script ONLY populates `profiles` in `influencer.db` (via the CLI's
    `discover_youtube` pipeline). Email extraction / bio crawl / validate run
    afterwards via `uv run influencer extract / crawl-links / validate / export`.
  - We KEEP a 180-day freshness filter (uploads playlist) before insert. The
    CLI's `discover_youtube` doesn't have freshness, so we replicate the 0429
    logic here as a pre-insert guard: search → filter by subs/country →
    freshness check → upsert into DB.

Why a fresh cycle: PAUSED_2026-04-30.md indicates the prior `influencer.db` was
lost. The 89 finalized leads from 0430 are preserved in
`data/2026-04-30/{cat}.csv` and `data/total/{cat}.csv` already; this cycle adds
a NEW pool with non-overlapping keywords across the same 4 categories.

Quota target ≤ 8K / 10K daily:
  - search.list: 24 keywords × 2 pages × 100 = 4,800
  - channels.list: ceil(channels / 50) × 1
  - playlistItems.list (freshness): 1 unit per surviving channel (~500 max)
"""

from __future__ import annotations

import os
import sys
import time
import warnings
from datetime import datetime, timedelta, timezone
from pathlib import Path

from dotenv import load_dotenv
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

warnings.filterwarnings("ignore")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from influencer_finder import db as db_module  # noqa: E402
from influencer_finder.db import init_db, insert_source, session, upsert_profile  # noqa: E402
from influencer_finder.models import Profile, Source  # noqa: E402

MIN_SUBS = 5_000
MAX_SUBS = 1_500_000
EXCLUDE_COUNTRIES = {"KR", "JP"}
FRESHNESS_DAYS = 180
PAGES_PER_KEYWORD = 2  # 50 results × 2 pages = up to 100 channels per keyword

# Non-overlapping with 0429 / 0430. Each category gets 5–7 phrases.
KEYWORDS: dict[str, list[str]] = {
    "fitness": [
        "no equipment workout",
        "calisthenics tutorial",
        "marathon training plan",
        "kettlebell flow workout",
        "mobility training routine",
        "functional strength training",
    ],
    "mindset": [
        "stoic philosophy",
        "self-improvement creator",
        "morning routine for productivity",
        "discipline coach",
        "mental clarity habits",
        "deep work coach",
    ],
    "yoga": [
        "yin yoga class",
        "vinyasa flow yoga",
        "yoga for runners",
        "kundalini yoga teacher",
        "hatha yoga teacher",
        "ashtanga yoga primary series",
    ],
    "nutrition": [
        "macro counting nutrition",
        "anti-inflammatory diet",
        "intuitive eating coach",
        "high protein meals",
        "registered dietitian channel",
        "plant based nutritionist",
    ],
}


def search_channel_ids(client, query: str, pages: int) -> list[str]:
    ids: list[str] = []
    page_token: str | None = None
    for _ in range(pages):
        kwargs = {
            "q": query,
            "type": "channel",
            "part": "id",
            "maxResults": 50,
            "regionCode": "US",
            "relevanceLanguage": "en",
        }
        if page_token:
            kwargs["pageToken"] = page_token
        try:
            resp = client.search().list(**kwargs).execute()
        except HttpError as e:
            if "quotaExceeded" in str(e):
                print(f"  [quota EXCEEDED] aborting further searches")
                raise
            print(f"  [search ERR] {query!r}: {e}")
            return ids
        for it in resp.get("items", []):
            cid = it.get("id", {}).get("channelId")
            if cid:
                ids.append(cid)
        page_token = resp.get("nextPageToken")
        if not page_token:
            break
    return ids


def fetch_channels(client, ids: list[str]) -> list[dict]:
    out: list[dict] = []
    for start in range(0, len(ids), 50):
        batch = ids[start: start + 50]
        try:
            resp = client.channels().list(
                id=",".join(batch),
                part="snippet,statistics,contentDetails",
                maxResults=50,
            ).execute()
        except HttpError as e:
            print(f"  [channels ERR] batch {start}: {e}")
            continue
        out.extend(resp.get("items", []))
    return out


def latest_upload_at(client, uploads_playlist_id: str) -> datetime | None:
    if not uploads_playlist_id:
        return None
    try:
        resp = client.playlistItems().list(
            playlistId=uploads_playlist_id,
            part="snippet",
            maxResults=1,
        ).execute()
    except HttpError:
        return None
    items = resp.get("items", []) or []
    if not items:
        return None
    pub = items[0].get("snippet", {}).get("publishedAt", "")
    if not pub:
        return None
    try:
        return datetime.fromisoformat(pub.replace("Z", "+00:00"))
    except ValueError:
        return None


def channel_passes_filters(it: dict) -> tuple[bool, str | None]:
    sn = it.get("snippet", {}) or {}
    st = it.get("statistics", {}) or {}
    cd = it.get("contentDetails", {}) or {}
    try:
        subs = int(st.get("subscriberCount", "0"))
    except (TypeError, ValueError):
        subs = 0
    if subs < MIN_SUBS or subs > MAX_SUBS:
        return False, None
    country = (sn.get("country") or "").strip().upper()
    if country in EXCLUDE_COUNTRIES:
        return False, None
    uploads_pl = (cd.get("relatedPlaylists", {}) or {}).get("uploads", "") or ""
    return True, uploads_pl


def channel_to_profile(it: dict) -> Profile:
    sn = it.get("snippet", {}) or {}
    st = it.get("statistics", {}) or {}
    title = (sn.get("title", "") or "").strip()
    desc = (sn.get("description", "") or "").strip()
    custom = sn.get("customUrl", "") or ""
    handle = custom.lstrip("@") if custom else it.get("id", "")
    url = (
        f"https://www.youtube.com/@{handle}"
        if custom else f"https://www.youtube.com/channel/{it.get('id','')}"
    )
    try:
        subs = int(st.get("subscriberCount", "0"))
    except (TypeError, ValueError):
        subs = 0
    country = (sn.get("country") or "").strip()
    return Profile(
        platform="youtube",
        handle=handle,
        display_name=title,
        url=url,
        follower_count=subs,
        bio=desc,
        country=country,
    )


def main() -> int:
    load_dotenv(ROOT / ".env", override=True)
    key = os.environ.get("YOUTUBE_API_KEY", "")
    if not key.startswith("AIza"):
        print(f"ERROR: bad YOUTUBE_API_KEY (prefix {key[:6]!r})")
        return 1
    client = build("youtube", "v3", developerKey=key, cache_discovery=False)

    init_db(db_module.DEFAULT_DB_PATH)
    freshness_cutoff = datetime.now(timezone.utc) - timedelta(days=FRESHNESS_DAYS)
    print(f"freshness cutoff: {freshness_cutoff.date().isoformat()}")

    grand_quota = 0
    inserted_per_cat: dict[str, int] = {}
    stale_per_cat: dict[str, int] = {}
    duplicate_per_cat: dict[str, int] = {}

    try:
        for category, kws in KEYWORDS.items():
            t0 = time.time()
            print(f"\n=== {category} ({len(kws)} keywords × {PAGES_PER_KEYWORD} pages) ===")
            ids: list[str] = []
            seen_ids: set[str] = set()
            try:
                for kw in kws:
                    cids = search_channel_ids(client, kw, pages=PAGES_PER_KEYWORD)
                    grand_quota += 100 * PAGES_PER_KEYWORD
                    new = sum(1 for c in cids if c not in seen_ids)
                    for c in cids:
                        if c not in seen_ids:
                            seen_ids.add(c)
                            ids.append(c)
                    print(f"  search '{kw}': pulled {len(cids)} ({new} new uniq; cumul={len(ids)})")
            except HttpError as e:
                if "quotaExceeded" in str(e):
                    print(f"  [!] quota during search; using {len(ids)} ids gathered so far")
                else:
                    raise

            items = fetch_channels(client, ids)
            grand_quota += -(-len(ids) // 50)
            print(f"  fetched {len(items)} channel snippets")

            inserted = 0
            stale = 0
            dup = 0
            with session(db_module.DEFAULT_DB_PATH) as conn:
                for it in items:
                    ok, uploads_pl = channel_passes_filters(it)
                    if not ok:
                        continue
                    last_at = latest_upload_at(client, uploads_pl) if uploads_pl else None
                    grand_quota += 1 if uploads_pl else 0
                    if last_at is None or last_at < freshness_cutoff:
                        stale += 1
                        continue
                    profile = channel_to_profile(it)
                    pid = upsert_profile(conn, profile)
                    new_source = insert_source(
                        conn,
                        Source(
                            profile_id=pid,
                            url=profile.url,
                            type="channel_description",
                            success=True,
                        ),
                    )
                    if new_source:
                        inserted += 1
                    else:
                        dup += 1

            inserted_per_cat[category] = inserted
            stale_per_cat[category] = stale
            duplicate_per_cat[category] = dup
            print(
                f"  inserted {inserted} new profiles "
                f"(stale-drop {stale}, duplicate-of-prior {dup}); "
                f"elapsed {time.time()-t0:.1f}s"
            )
    except HttpError as e:
        if "quotaExceeded" in str(e):
            print(f"\n[!] Stopped early due to quota exhaustion.")
        else:
            raise

    print(f"\nestimated quota used: {grand_quota}")
    print("\ninserts per category:")
    for cat in KEYWORDS:
        print(
            f"  {cat}: +{inserted_per_cat.get(cat, 0)} "
            f"(stale {stale_per_cat.get(cat, 0)}, dup {duplicate_per_cat.get(cat, 0)})"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
