"""Backfill `description` (and country/follower_count when empty) for the 113
newly-added rows in data/2026-04-24/{lifestyle,beatmakers,nutrition}*.csv by
calling the YouTube Data API v3 channels.list(forHandle=...) endpoint.

Only fills cells that are currently empty — existing data is never overwritten.
Descriptions are flattened (newlines -> space) so each record stays on one line.

Quota: 1 unit per handle. ~113 units for the full backfill (default quota 10k/day).
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
DATED = ROOT / "data" / "2026-04-24"

# Only fetch for the categories where rows were newly added.
TARGET_FILES = [
    DATED / "lifestyle.csv",
    DATED / "lifestyle_enriched.csv",
    DATED / "beatmakers.csv",
    DATED / "beatmakers_enriched.csv",
    DATED / "nutrition.csv",
    DATED / "nutrition_enriched.csv",
]

_NL = re.compile(r"[\r\n]+")
_WS = re.compile(r"\s+")


def flatten(v: str) -> str:
    if not v:
        return ""
    return _WS.sub(" ", _NL.sub(" ", v)).strip()


def read(path: Path):
    with path.open(newline="", encoding="utf-8-sig") as f:
        r = csv.DictReader(f)
        fn = list(r.fieldnames or [])
        rows = list(r)
    return rows, fn


def write(path: Path, rows, fieldnames):
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)


def collect_handles_needing_bio() -> set[str]:
    handles: set[str] = set()
    for p in TARGET_FILES:
        rows, _ = read(p)
        for r in rows:
            if (r.get("platform", "") or "").strip().lower() != "youtube":
                continue
            if not (r.get("description", "") or "").strip():
                h = (r.get("handle", "") or "").strip()
                if h:
                    handles.add(h)
    return handles


def fetch_channel_map(handles: list[str], client) -> dict[str, dict]:
    """Return {handle_lower: {'title','description','country','subscriber_count'}}."""
    out: dict[str, dict] = {}
    total = len(handles)
    for i, h in enumerate(handles, 1):
        try:
            resp = client.channels().list(
                forHandle=h,
                part="snippet,statistics",
            ).execute()
        except HttpError as e:
            print(f"  [{i}/{total}] {h}: HTTP error {e.resp.status}")
            continue
        items = resp.get("items", [])
        if not items:
            print(f"  [{i}/{total}] {h}: not found")
            continue
        it = items[0]
        sn = it.get("snippet", {}) or {}
        st = it.get("statistics", {}) or {}
        out[h.lower()] = {
            "title": sn.get("title", "") or "",
            "description": flatten(sn.get("description", "") or ""),
            "country": sn.get("country") or "",
            "subscriber_count": st.get("subscriberCount") or "",
        }
        if i % 20 == 0 or i == total:
            print(f"  progress: {i}/{total} fetched")
    return out


def apply_to_file(path: Path, data_by_handle: dict[str, dict]) -> dict:
    rows, fn = read(path)
    filled = {"description": 0, "country": 0, "follower_count": 0}
    for r in rows:
        h = (r.get("handle", "") or "").strip().lower()
        if not h or h not in data_by_handle:
            continue
        d = data_by_handle[h]
        # Fill only empty cells.
        if d["description"] and not (r.get("description", "") or "").strip():
            r["description"] = d["description"]
            filled["description"] += 1
        if d["country"] and not (r.get("country", "") or "").strip():
            r["country"] = d["country"]
            filled["country"] += 1
        if d["subscriber_count"] and not (r.get("follower_count", "") or "").strip():
            r["follower_count"] = d["subscriber_count"]
            filled["follower_count"] += 1
    write(path, rows, fn)
    return filled


def main() -> None:
    csv.field_size_limit(sys.maxsize)
    load_dotenv(ROOT / ".env", override=True)
    key = os.environ.get("YOUTUBE_API_KEY", "")
    if not key or not key.startswith("AIza"):
        print(f"ERROR: YOUTUBE_API_KEY missing or invalid (got prefix={key[:6]!r})")
        sys.exit(1)

    client = build("youtube", "v3", developerKey=key, cache_discovery=False)

    handles = sorted(collect_handles_needing_bio())
    print(f"need bio for {len(handles)} unique handles")

    t0 = time.time()
    data = fetch_channel_map(handles, client)
    dt = time.time() - t0
    print(f"fetched {len(data)}/{len(handles)} channels in {dt:.1f}s")

    for p in TARGET_FILES:
        stats = apply_to_file(p, data)
        print(f"  {p.name}: filled {stats}")


if __name__ == "__main__":
    main()
