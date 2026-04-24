"""Apply LLM-classified niche/segment/industry/angle columns to an exported CSV.

Usage:
    uv run python scripts/llm_enrich.py <input.csv> <output.csv> <mapping.py>

The mapping module must expose MAPPING: dict[email, dict[str, str]] with keys
'niche', 'segment_original', 'industry', 'angle_to_take'.
"""
from __future__ import annotations

import csv
import importlib.util
import sys
from pathlib import Path


def load_mapping(mapping_path: Path) -> dict[str, dict[str, str]]:
    spec = importlib.util.spec_from_file_location("mapping_module", mapping_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {mapping_path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.MAPPING


def main() -> None:
    if len(sys.argv) != 4:
        print(__doc__)
        sys.exit(1)
    in_path, out_path, map_path = map(Path, sys.argv[1:])
    mapping = load_mapping(map_path)

    with in_path.open() as inf:
        reader = csv.DictReader(inf)
        rows = list(reader)
        fieldnames = reader.fieldnames or []

    filled = 0
    unmatched: list[str] = []
    for row in rows:
        email = row.get("email", "")
        entry = mapping.get(email)
        if entry is None:
            unmatched.append(email)
            continue
        for k in ("niche", "segment_original", "industry", "angle_to_take"):
            row[k] = entry.get(k, "")
        filled += 1

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", newline="") as outf:
        writer = csv.DictWriter(outf, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Filled {filled}/{len(rows)} rows → {out_path}")
    if unmatched:
        print(f"Unmatched emails ({len(unmatched)}):")
        for e in unmatched:
            print(f"  - {e}")


if __name__ == "__main__":
    main()
