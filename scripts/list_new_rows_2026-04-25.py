"""Identify rows in data/2026-04-25/<cat>_enriched.csv that are NOT yet covered
by any of {cat}_mapping_2026-04-25.py + {cat}_mapping_2026-04-25_more.py +
{cat}_mapping_2026-04-25_v3.py. Prints a per-category summary + emits a JSON
blob with row dicts for each unmapped row, ready to use as input for hand-
crafted _v3 mapping authoring.
"""

from __future__ import annotations

import csv
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path("/home/bjm/ABC/Marketing/youtube-crawling")
DATED = ROOT / "data" / "2026-04-25"
SCRIPTS = ROOT / "scripts"
CATEGORIES = ["career", "fitness", "nutrition", "lifestyle", "beatmakers"]


def load_mapping(path: Path) -> dict:
    if not path.exists():
        return {}
    spec = importlib.util.spec_from_file_location("m", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return getattr(mod, "MAPPING", {})


def main() -> None:
    csv.field_size_limit(sys.maxsize)
    out: dict[str, list[dict]] = {}
    for cat in CATEGORIES:
        mapping: dict = {}
        for suffix in ["", "_more", "_v3"]:
            mapping.update(load_mapping(SCRIPTS / f"{cat}_mapping_2026-04-25{suffix}.py"))
        with (DATED / f"{cat}_enriched.csv").open(newline="", encoding="utf-8-sig") as f:
            rows = list(csv.DictReader(f))
        unmapped = [r for r in rows if r.get("email", "").strip() not in mapping]
        out[cat] = [
            {
                "email": r.get("email", ""),
                "full_name": r.get("full_name", ""),
                "handle": r.get("handle", ""),
                "follower_count": r.get("follower_count", ""),
                "country": r.get("country", ""),
                "description": r.get("description", "")[:600],
                "source_url": r.get("source_url", ""),
                "website": r.get("website", ""),
                "raw_context": r.get("raw_context", "")[:200],
            }
            for r in unmapped
        ]
        print(f"{cat:12s}: {len(rows):3d} total, {len(unmapped):3d} unmapped")

    Path("/tmp/unmapped_2026-04-25.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2)
    )
    print("\nFull dump → /tmp/unmapped_2026-04-25.json")


if __name__ == "__main__":
    main()
