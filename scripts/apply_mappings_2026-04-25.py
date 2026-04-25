"""Apply the 5 per-row mapping files to data/2026-04-25/*.csv."""

from __future__ import annotations

import csv
import importlib.util
import re
import sys
from pathlib import Path

ROOT = Path("/home/bjm/ABC/Marketing/youtube-crawling")
DATED = ROOT / "data" / "2026-04-25"
SCRIPTS = ROOT / "scripts"

CATEGORIES = ["career", "fitness", "nutrition", "lifestyle", "beatmakers"]

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
        mapping = load(SCRIPTS / f"{cat}_mapping_2026-04-25.py")
        more = SCRIPTS / f"{cat}_mapping_2026-04-25_more.py"
        if more.exists():
            mapping = {**mapping, **load(more)}
        for suffix in ["", "_enriched"]:
            p = DATED / f"{cat}{suffix}.csv"
            updated, total = apply(p, mapping)
            print(f"{p.name}: {updated}/{total} updated (mapping size={len(mapping)})")


if __name__ == "__main__":
    main()
