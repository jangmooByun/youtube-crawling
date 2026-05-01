"""Merge data/2026-05-01/{cat}.csv into data/total/{cat}.csv.

Why a separate merger instead of extending build_total.py: build_total.py is
hard-coded to source files for 0424–0429 + legacy. Rather than thread 0501
into that logic, this script does the simpler thing — append-and-dedupe by
(email_lower, profile_url_lower), keep the richer row on conflict, and resort
by follower_count DESC.

Run AFTER `apply_mappings_2026-05-01.py` has produced the 4 category CSVs.
"""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = ROOT / "data" / "2026-05-01"
TOTAL_DIR = ROOT / "data" / "total"
CATS = ("fitness", "mindset", "yoga", "nutrition")

UNIFIED_FIELDS = [
    "first_name", "full_name", "handle", "platform", "follower_count", "country",
    "email", "profile_url", "website", "description",
    "niche", "segment_original", "industry", "angle_to_take",
    "source_url", "raw_context", "is_role_based", "has_mx", "detected_tech",
]

_NL = re.compile(r"[\r\n]+")
_WS = re.compile(r"\s+")


def _flatten(v: str) -> str:
    if not v:
        return ""
    return _WS.sub(" ", _NL.sub(" ", v)).strip()


def _key(row: dict) -> tuple[str, str]:
    e = (row.get("email") or "").strip().lower()
    u = (row.get("profile_url") or "").strip().rstrip("/").lower()
    return e, u


def _richness(row: dict) -> int:
    return (
        len(row.get("description", "") or "")
        + len(row.get("website", "") or "")
        + len(row.get("raw_context", "") or "")
        + len(row.get("niche", "") or "")
        + len(row.get("angle_to_take", "") or "")
    )


def _follower_int(row: dict) -> int:
    raw = (row.get("follower_count") or "").strip()
    try:
        return int(float(raw)) if raw else 0
    except ValueError:
        return 0


def _read(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8-sig", errors="replace") as f:
        return list(csv.DictReader(f))


def main() -> int:
    csv.field_size_limit(sys.maxsize)
    TOTAL_DIR.mkdir(parents=True, exist_ok=True)

    summary: dict[str, dict[str, int]] = {}
    for cat in CATS:
        existing = _read(TOTAL_DIR / f"{cat}.csv")
        new = _read(SRC_DIR / f"{cat}.csv")

        bucket: dict[tuple[str, str], dict] = {}
        for row in existing + new:
            if not (row.get("email") or "").strip():
                continue
            normalized = {k: row.get(k, "") or "" for k in UNIFIED_FIELDS}
            k = _key(normalized)
            prev = bucket.get(k)
            if prev is None or _richness(normalized) > _richness(prev):
                bucket[k] = normalized

        rows = sorted(bucket.values(), key=_follower_int, reverse=True)
        out = TOTAL_DIR / f"{cat}.csv"
        with out.open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=UNIFIED_FIELDS)
            w.writeheader()
            for r in rows:
                w.writerow({k2: _flatten(r.get(k2, "")) for k2 in UNIFIED_FIELDS})

        summary[cat] = {
            "existing": len(existing),
            "new_input": len(new),
            "final": len(rows),
            "added": len(rows) - len(existing),
        }

    print("merge summary (existing → final, +added from 0501):")
    for cat, s in summary.items():
        print(
            f"  {cat:9s}: {s['existing']:4d} → {s['final']:4d} "
            f"(+{s['added']:3d}; new input {s['new_input']:4d})"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
