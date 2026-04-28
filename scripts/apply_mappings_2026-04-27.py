"""Apply per-row mapping files to data/2026-04-27/*.csv."""

from __future__ import annotations

import csv
import importlib.util
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATED = ROOT / "data" / "2026-04-27"
SCRIPTS = ROOT / "scripts"

CATEGORIES = ["fitness"]

_NL = re.compile(r"[\r\n]+")
_WS = re.compile(r"\s+")


def flatten(v: str) -> str:
    if not v:
        return ""
    return _WS.sub(" ", _NL.sub(" ", v)).strip()


def load(path: Path):
    spec = importlib.util.spec_from_file_location("m", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.MAPPING


def apply(csv_path: Path, mapping: dict) -> tuple[int, int]:
    with csv_path.open(newline="", encoding="utf-8-sig") as f:
        r = csv.DictReader(f)
        fieldnames = list(r.fieldnames or [])
        rows = list(r)
    updated = 0
    for row in rows:
        email = row.get("email", "").strip()
        m = mapping.get(email)
        if not m:
            continue
        for k in ("niche", "segment_original", "industry", "angle_to_take"):
            if k in m:
                row[k] = flatten(m[k])
        updated += 1
    with csv_path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)
    return updated, len(rows)


def main() -> None:
    csv.field_size_limit(sys.maxsize)
    for cat in CATEGORIES:
        base_path = SCRIPTS / f"{cat}_mapping_2026-04-27.py"
        if not base_path.exists():
            print(f"SKIP {cat}: no base mapping at {base_path.name}")
            continue
        mapping = load(base_path)
        for extra in ("_more", "_v3"):
            extra_path = SCRIPTS / f"{cat}_mapping_2026-04-27{extra}.py"
            if extra_path.exists():
                mapping = {**mapping, **load(extra_path)}
        for suffix in ["", "_enriched"]:
            p = DATED / f"{cat}{suffix}.csv"
            if not p.exists():
                print(f"SKIP {p.name}: not found")
                continue
            updated, total = apply(p, mapping)
            print(f"{p.name}: {updated}/{total} updated (mapping size={len(mapping)})")


if __name__ == "__main__":
    main()
