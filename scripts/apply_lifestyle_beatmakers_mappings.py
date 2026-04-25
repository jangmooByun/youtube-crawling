"""Apply per-row lifestyle_mapping / beatmakers_mapping to their CSVs.

Overwrites niche / segment_original / industry / angle_to_take in both
base and _enriched versions (the prior sub-vertical-shared labels are
replaced with per-person ones).
"""

from __future__ import annotations

import csv
import importlib.util
import re
import sys
from pathlib import Path


ROOT = Path("/home/bjm/ABC/Marketing/youtube-crawling")
DATED = ROOT / "data" / "2026-04-24"
SCRIPTS = ROOT / "scripts"

_NL = re.compile(r"[\r\n]+")
_WS = re.compile(r"\s+")


def flatten(v: str) -> str:
    if not v:
        return ""
    return _WS.sub(" ", _NL.sub(" ", v)).strip()


def load_mapping(path: Path) -> dict[str, dict[str, str]]:
    spec = importlib.util.spec_from_file_location("mapping_mod", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.MAPPING


def apply(csv_path: Path, mapping: dict) -> dict:
    with csv_path.open(newline="", encoding="utf-8-sig") as f:
        r = csv.DictReader(f)
        fieldnames = list(r.fieldnames or [])
        rows = list(r)

    updated = 0
    missing: list[str] = []
    for row in rows:
        email = row.get("email", "").strip()
        m = mapping.get(email)
        if not m:
            missing.append(email)
            continue
        for k in ("niche", "segment_original", "industry", "angle_to_take"):
            if k in m:
                row[k] = flatten(m[k])
        updated += 1

    with csv_path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)

    return {"rows": len(rows), "updated": updated, "missing": missing}


def main() -> None:
    csv.field_size_limit(sys.maxsize)

    lifestyle_map = load_mapping(SCRIPTS / "lifestyle_mapping.py")
    beatmakers_map = load_mapping(SCRIPTS / "beatmakers_mapping.py")

    for p in [DATED / "lifestyle.csv", DATED / "lifestyle_enriched.csv"]:
        r = apply(p, lifestyle_map)
        print(f"{p.name}: {r['updated']}/{r['rows']} updated, missing={len(r['missing'])}")

    for p in [DATED / "beatmakers.csv", DATED / "beatmakers_enriched.csv"]:
        r = apply(p, beatmakers_map)
        print(f"{p.name}: {r['updated']}/{r['rows']} updated, missing={len(r['missing'])}")


if __name__ == "__main__":
    main()
