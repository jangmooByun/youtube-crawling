"""Flatten embedded newlines inside CSV cells for data/2026-04-24/*.csv.

Multi-line quoted fields (bio/description, raw_context) are valid RFC 4180
but render as many sprawled lines in editors. This one-shot rewrites each
target CSV in place with: \\r\\n|\\n|\\r -> ' ', then collapses runs of
whitespace to a single space. Column order and record count are preserved.

Usage:
    uv run python scripts/flatten_csv_newlines.py
    uv run python scripts/flatten_csv_newlines.py path1.csv path2.csv ...
"""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path


DEFAULT_TARGETS = [
    Path("/home/bjm/ABC/Marketing/youtube-crawling/data/2026-04-24/career.csv"),
    Path("/home/bjm/ABC/Marketing/youtube-crawling/data/2026-04-24/career_enriched.csv"),
    Path("/home/bjm/ABC/Marketing/youtube-crawling/data/2026-04-24/fitness.csv"),
    Path("/home/bjm/ABC/Marketing/youtube-crawling/data/2026-04-24/fitness_enriched.csv"),
    Path("/home/bjm/ABC/Marketing/youtube-crawling/data/2026-04-24/nutrition.csv"),
    Path("/home/bjm/ABC/Marketing/youtube-crawling/data/2026-04-24/nutrition_enriched.csv"),
]

_NEWLINE_RE = re.compile(r"[\r\n]+")
_WS_RE = re.compile(r"\s+")


def flatten(value: str) -> str:
    v = _NEWLINE_RE.sub(" ", value)
    v = _WS_RE.sub(" ", v)
    return v.strip()


def count_raw_lines(path: Path) -> int:
    with path.open("rb") as f:
        return sum(1 for _ in f)


def process(path: Path) -> tuple[int, int, int, int]:
    before_lines = count_raw_lines(path)
    with path.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames or [])
        rows = [
            {k: flatten(v) if isinstance(v, str) else v for k, v in r.items()}
            for r in reader
        ]

    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    after_lines = count_raw_lines(path)
    return before_lines, after_lines, len(rows), len(fieldnames)


def main() -> None:
    csv.field_size_limit(sys.maxsize)
    targets = [Path(p) for p in sys.argv[1:]] or DEFAULT_TARGETS
    for path in targets:
        if not path.exists():
            print(f"SKIP (missing): {path}")
            continue
        before, after, records, cols = process(path)
        print(f"{path.name}: {before} -> {after} lines ({records} records, {cols} cols)")


if __name__ == "__main__":
    main()
