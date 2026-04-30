"""
0430 매핑 적용 — data/2026-04-30/all.csv 를 mapping_2026_04_30.MAPPING 으로
enrich 후 카테고리별로 split 해서 4 카테고리 csv 출력.
drop 행은 어떤 csv 에도 들어가지 않음.
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from mapping_2026_04_30 import MAPPING  # noqa: E402

SRC = ROOT / "data" / "2026-04-30" / "all.csv"
OUT_DIR = ROOT / "data" / "2026-04-30"
CATS = ["fitness", "mindset", "yoga", "nutrition"]


def main() -> int:
    with SRC.open() as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    cat_rows: dict[str, list[dict]] = {c: [] for c in CATS}
    drops: list[str] = []
    unmapped: list[str] = []

    for row in rows:
        email = (row.get("email") or "").strip().lower()
        m = MAPPING.get(email)
        if not m:
            unmapped.append(email)
            continue
        cat = m["category"]
        if cat == "drop":
            drops.append(email)
            continue
        if cat not in CATS:
            unmapped.append(f"{email} (unknown cat: {cat})")
            continue
        new_row = dict(row)
        new_row["niche"] = m["niche"]
        new_row["segment_original"] = m["segment_original"]
        new_row["industry"] = m["industry"]
        new_row["angle_to_take"] = m["angle_to_take"]
        cat_rows[cat].append(new_row)

    for cat in CATS:
        out = OUT_DIR / f"{cat}.csv"
        with out.open("w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=fieldnames)
            w.writeheader()
            w.writerows(cat_rows[cat])
        print(f"{out.relative_to(ROOT)}: {len(cat_rows[cat])} rows")

    print(f"drops: {len(drops)} | unmapped: {len(unmapped)}")
    if unmapped:
        print("UNMAPPED rows (need mapping entry):")
        for e in unmapped:
            print(f"  {e}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
