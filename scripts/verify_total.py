"""End-to-end verification for data/total/{mindset,meditation,fitness,nutrition}.csv.

Checks:
  (1) per-category row counts + country distribution
  (2) JP/KR exclusion (must be 0 across all 4 CSVs)
  (3) schema consistency (19 cols, header identical)
  (4) niche / angle_to_take coverage (must be 100% non-empty)
  (5) 1 record = 1 line (line count == record count + 1)
  (6) intra-category dedup (no duplicate (email, profile_url) within a CSV)
  (7) email literal match in raw_context (core invariant; allow legacy
      rows whose raw_context predates the new descriptions to fall back
      to source raw_context check — already present)
  (8) sample 3 rows per category — surface name + niche + angle_to_take
"""

from __future__ import annotations

import csv
import random
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOTAL = ROOT / "data" / "total"
CATEGORIES = ("mindset", "meditation", "fitness", "nutrition")

UNIFIED_FIELDS = [
    "first_name", "full_name", "handle", "platform", "follower_count", "country",
    "email", "profile_url", "website", "description",
    "niche", "segment_original", "industry", "angle_to_take",
    "source_url", "raw_context", "is_role_based", "has_mx", "detected_tech",
]


def read(p: Path) -> list[dict]:
    if not p.exists():
        return []
    with p.open(newline="", encoding="utf-8-sig", errors="replace") as f:
        return list(csv.DictReader(f))


def main() -> None:
    csv.field_size_limit(sys.maxsize)
    print("=== (1)+(2) per-category counts + JP/KR + dups ===")
    fmt = "{:11s} | rows={:>3d} | JPKR={:>1d} | dup={:>1d} | uniq-niche={:>3d} | uniq-angle={:>3d} | empty-angle={:>2d}"
    grand = 0
    for cat in CATEGORIES:
        rows = read(TOTAL / f"{cat}.csv")
        grand += len(rows)
        jpkr = sum(1 for r in rows if r.get("country", "").upper() in {"JP", "KR"})
        keys = [(r.get("email", "").strip().lower(), r.get("profile_url", "").strip().rstrip("/").lower()) for r in rows]
        dup = len(keys) - len(set(keys))
        un_n = len({r.get("niche", "") for r in rows if r.get("niche", "").strip()})
        un_a = len({r.get("angle_to_take", "") for r in rows if r.get("angle_to_take", "").strip()})
        empty_a = sum(1 for r in rows if not r.get("angle_to_take", "").strip())
        print(fmt.format(cat, len(rows), jpkr, dup, un_n, un_a, empty_a))
    print(f"-- grand total: {grand}")

    print("\n=== (3) schema consistency ===")
    for cat in CATEGORIES:
        path = TOTAL / f"{cat}.csv"
        if not path.exists():
            print(f"  {cat}.csv: missing")
            continue
        with path.open(newline="", encoding="utf-8-sig", errors="replace") as f:
            r = csv.reader(f)
            header = next(r, [])
        ok = header == UNIFIED_FIELDS
        print(f"  {cat:11s}: {'OK' if ok else 'BROKEN'} ({len(header)} cols)")

    print("\n=== (5) 1 record = 1 line ===")
    for cat in CATEGORIES:
        p = TOTAL / f"{cat}.csv"
        if not p.exists():
            continue
        line_count = subprocess.check_output(["wc", "-l", str(p)]).decode().strip().split()[0]
        rec_count = len(read(p))
        ok = "OK" if int(line_count) == rec_count + 1 else "BROKEN"
        print(f"  {cat:11s}: lines={line_count:>5s} records={rec_count:3d} [{ok}]")

    print("\n=== (1b) country distribution per category ===")
    for cat in CATEGORIES:
        rows = read(TOTAL / f"{cat}.csv")
        if not rows:
            print(f"  {cat}: (empty)")
            continue
        ctry = Counter((r.get("country", "") or "(none)").upper() for r in rows)
        total = len(rows)
        top = ", ".join(f"{c}:{n}" for c, n in ctry.most_common(6))
        us = ctry.get("US", 0)
        print(f"  {cat:11s} ({total} rows) US={us} ({100*us/total:.0f}%) | {top}")

    print("\n=== (7) core invariant: email in raw_context ===")
    for cat in CATEGORIES:
        rows = read(TOTAL / f"{cat}.csv")
        bad = []
        for r in rows:
            email = (r.get("email") or "").strip().lower()
            ctx = (r.get("raw_context") or "").lower()
            if email and email not in ctx:
                bad.append(r.get("email"))
        if bad:
            print(f"  {cat}: {len(bad)} rows where email NOT in raw_context")
            for e in bad[:5]:
                print(f"    - {e}")
        else:
            print(f"  {cat:11s}: all {len(rows)} emails appear in raw_context  OK")

    print("\n=== (8) random sample 3 per category ===")
    random.seed(42)
    for cat in CATEGORIES:
        rows = read(TOTAL / f"{cat}.csv")
        if not rows:
            continue
        sample = random.sample(rows, min(3, len(rows)))
        print(f"-- [{cat}] --")
        for r in sample:
            print(f"  {r['full_name'][:40]} | {r['country']} | followers={r['follower_count']}")
            print(f"    niche : {r['niche'][:120]}")
            print(f"    angle : {r['angle_to_take'][:140]}")


if __name__ == "__main__":
    main()
