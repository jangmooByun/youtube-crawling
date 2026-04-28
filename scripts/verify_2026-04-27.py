"""End-to-end verification for data/2026-04-27/ after discover_2026-04-27.

Checks:
  (1) per-category row counts + bio-crawl-derived breakdown
  (2) JP/KR exclusion (must be 0)
  (3) cross-date dedup against 2026-04-24 + 2026-04-25 (must be 0)
  (4) per-row mapping coverage (uniq niche / uniq angle counts)
  (5) 1 record = 1 line — raw line count must equal record + 1
  (6) sample-5 random bio-crawl rows: surface email + source_url + raw_context
"""

from __future__ import annotations

import csv
import random
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OLD_DIRS = [ROOT / "data" / "2026-04-24", ROOT / "data" / "2026-04-25"]
NEW = ROOT / "data" / "2026-04-27"
CATS = ["fitness"]
OLD_CATS = ["career", "fitness", "nutrition", "lifestyle", "beatmakers"]


def read(p: Path) -> list[dict]:
    if not p.exists():
        return []
    with p.open(newline="", encoding="utf-8-sig", errors="replace") as f:
        return list(csv.DictReader(f))


def main() -> None:
    csv.field_size_limit(sys.maxsize)

    old_e, old_u = set(), set()
    for d in OLD_DIRS:
        for cat in OLD_CATS:
            for r in read(d / f"{cat}_enriched.csv"):
                e = (r.get("email", "") or "").strip().lower()
                u = (r.get("profile_url", "") or "").strip().rstrip("/").lower()
                if e:
                    old_e.add(e)
                if u:
                    old_u.add(u)

    print("=== (1)+(2)+(3)+(4) per-category audit ===")
    fmt = "{:11s} | rows={:>3d} | JPKR={:>1d} | xdate-dup={:>2d} | uniq-niche={:>3d} | uniq-angle={:>3d} | bio-derived={:>2d} | website={:>3d} | tech={:>3d}"
    grand_rows = 0
    grand_dup = 0
    for cat in CATS:
        rows = read(NEW / f"{cat}_enriched.csv")
        grand_rows += len(rows)
        jpkr = sum(1 for r in rows if r.get("country", "").upper() in {"JP", "KR"})
        dup = sum(1 for r in rows
                  if (r.get("email", "").strip().lower() in old_e)
                  or (r.get("profile_url", "").strip().rstrip("/").lower() in old_u))
        grand_dup += dup
        un_n = len({r.get("niche", "") for r in rows if r.get("niche", "")})
        un_a = len({r.get("angle_to_take", "") for r in rows if r.get("angle_to_take", "")})
        bio = sum(1 for r in rows
                  if r.get("source_url", "").strip().rstrip("/").lower() != r.get("profile_url", "").strip().rstrip("/").lower())
        web = sum(1 for r in rows if r.get("website", "").strip())
        tech = sum(1 for r in rows if r.get("detected_tech", "").strip())
        print(fmt.format(cat, len(rows), jpkr, dup, un_n, un_a, bio, web, tech))
    print(f"-- total rows: {grand_rows} | total cross-date dups: {grand_dup}")

    print("\n=== (5) 1 record = 1 line integrity ===")
    for cat in CATS:
        for suffix in ["", "_enriched"]:
            p = NEW / f"{cat}{suffix}.csv"
            if not p.exists():
                continue
            line_count = subprocess.check_output(["wc", "-l", str(p)]).decode().strip().split()[0]
            rec_count = len(read(p))
            ok = "OK" if int(line_count) == rec_count + 1 else "BROKEN"
            print(f"  {p.name:35s}: lines={line_count:>5s} records={rec_count:3d}  [{ok}]")

    print("\n=== (6) email-in-source-HTML spot check (5 random bio-crawl rows) ===")
    bio_rows: list[tuple[str, dict]] = []
    for cat in CATS:
        for r in read(NEW / f"{cat}_enriched.csv"):
            if r.get("source_url", "").strip().rstrip("/").lower() != r.get("profile_url", "").strip().rstrip("/").lower():
                bio_rows.append((cat, r))
    random.seed(42)
    sample = random.sample(bio_rows, min(5, len(bio_rows)))
    print(f"  bio-derived rows total: {len(bio_rows)}, sampling {len(sample)}")
    for cat, r in sample:
        print(f"  --- [{cat}] {r['full_name']} ({r['follower_count']}, {r['country']})")
        print(f"      email     : {r['email']}")
        print(f"      source_url: {r['source_url']}")
        print(f"      raw_context: {r['raw_context'][:160]}")


if __name__ == "__main__":
    main()
