"""Merge 8 source CSVs into 4 master CSVs at data/total/.

Inputs (sources #1~#8 per the approved plan):
  #1 data/2026-04-24/fitness_enriched.csv         (19-col, mapping by category_split)
  #2 data/2026-04-24/nutrition_enriched.csv       (19-col, mapping by category_split)
  #3 data/2026-04-25/fitness_enriched_0425.csv    (19-col, mapping by category_split)
  #4 data/2026-04-25/nutrition_enriched_0425.csv  (19-col, mapping by category_split)
  #5 data/2026-04-27/fitness_enriched.csv         (19-col, mapping by category_split)
  #6 data/2026-04-28/fitness_enriched.csv         (19-col, mapping by category_split, drops 5 OFF-TOPIC)
  #7+#8 data/_legacy_enriched.csv                 (19-col, mapping by legacy_mapping
                                                   — overrides niche/seg/industry/angle if missing)

Outputs:
  data/total/mindset.csv      (meditation + breathwork + mindset coach)
  data/total/yoga.csv         (asana/vinyasa/hatha/kundalini/Rishikesh/yoga TTC)
  data/total/fitness.csv      (PT/CrossFit/Pilates/strength/...)
  data/total/nutrition.csv    (dietitian/RD/diet coach/healthy lifestyle/...)

Behavior:
  - Each row's category is looked up via category_split_mapping (for #1~#6)
    or legacy_mapping (for #7+#8). Missing rows abort the build.
  - Rows mapped to "drop" are excluded.
  - Dedup key: (email_lower, profile_url_lower). When duplicates exist,
    pick the row whose description+website+raw_context combined length is
    largest (richer signal).
  - Output sorted by follower_count DESC.
"""

from __future__ import annotations

import csv
import importlib.util
import re
import sys
from pathlib import Path

_NL = re.compile(r"[\r\n]+")
_WS = re.compile(r"\s+")


def _flatten(v: str) -> str:
    if not v:
        return ""
    return _WS.sub(" ", _NL.sub(" ", v)).strip()

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
DATA = ROOT / "data"
OUT = DATA / "total"

UNIFIED_FIELDS = [
    "first_name", "full_name", "handle", "platform", "follower_count", "country",
    "email", "profile_url", "website", "description",
    "niche", "segment_original", "industry", "angle_to_take",
    "source_url", "raw_context", "is_role_based", "has_mx", "detected_tech",
]

CATEGORIES = ("mindset", "yoga", "fitness", "nutrition")

SOURCES_19COL = [
    DATA / "2026-04-24" / "fitness_enriched.csv",
    DATA / "2026-04-24" / "nutrition_enriched.csv",
    DATA / "2026-04-25" / "fitness_enriched_0425.csv",
    DATA / "2026-04-25" / "nutrition_enriched_0425.csv",
    DATA / "2026-04-27" / "fitness_enriched.csv",
    DATA / "2026-04-28" / "fitness_enriched.csv",
]
SOURCE_LEGACY = DATA / "_legacy_enriched.csv"
SOURCE_MINDFUL = DATA / "_mindful_enriched.csv"
SOURCE_MEDITATION_0428 = DATA / "2026-04-28" / "meditation_enriched.csv"
SOURCE_29_MEDITATION = DATA / "2026-04-29" / "meditation_enriched.csv"
SOURCE_29_MINDSET = DATA / "2026-04-29" / "mindset_enriched.csv"
SOURCE_29_FITNESS = DATA / "2026-04-29" / "fitness_enriched.csv"
SOURCE_29_NUTRITION = DATA / "2026-04-29" / "nutrition_enriched.csv"
SOURCE_29_YOGA_EXTRA = DATA / "2026-04-29" / "yoga_enriched_extra.csv"
SOURCE_29_MINDSET_EXTRA = DATA / "2026-04-29" / "mindset_enriched_extra.csv"
SOURCE_29_NUTRITION_EXTRA = DATA / "2026-04-29" / "nutrition_enriched_extra.csv"


def _load_module(path: Path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    mod = importlib.util.module_from_spec(spec)  # type: ignore[arg-type]
    spec.loader.exec_module(mod)  # type: ignore[union-attr]
    return mod


def _read(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8-sig", errors="replace") as f:
        return list(csv.DictReader(f))


def _norm(row: dict) -> dict:
    return {k: row.get(k, "") or "" for k in UNIFIED_FIELDS}


def _row_richness(row: dict) -> int:
    return (len(row.get("description", "") or "")
            + len(row.get("website", "") or "")
            + len(row.get("raw_context", "") or "")
            + len(row.get("niche", "") or "")
            + len(row.get("angle_to_take", "") or ""))


def _follower_int(row: dict) -> int:
    raw = (row.get("follower_count") or "").strip()
    try:
        return int(float(raw)) if raw else 0
    except ValueError:
        return 0


def _key(row: dict) -> tuple[str, str]:
    e = (row.get("email") or "").strip().lower()
    u = (row.get("profile_url") or "").strip().rstrip("/").lower()
    return e, u


def main() -> None:
    csv.field_size_limit(sys.maxsize)

    cat_split = _load_module(SCRIPTS / "category_split_mapping.py").MAPPING
    legacy_map = _load_module(SCRIPTS / "legacy_mapping.py").MAPPING
    mindful_path_mod = SCRIPTS / "mindful_mapping.py"
    mindful_map = _load_module(mindful_path_mod).MAPPING if mindful_path_mod.exists() else {}
    meditation_0428_mod = SCRIPTS / "meditation_2026-04-28.py"
    meditation_0428_map = _load_module(meditation_0428_mod).MAPPING if meditation_0428_mod.exists() else {}

    def _maybe_load(name: str) -> dict:
        p = SCRIPTS / name
        return _load_module(p).MAPPING if p.exists() else {}

    map_29_meditation = _maybe_load("meditation_mapping_2026-04-29.py")
    map_29_mindset = _maybe_load("mindset_mapping_2026-04-29.py")
    map_29_fitness = _maybe_load("fitness_mapping_2026-04-29.py")
    map_29_nutrition = _maybe_load("nutrition_mapping_2026-04-29.py")
    map_29_yoga_extra = _maybe_load("yoga_mapping_2026-04-29_extra.py")
    map_29_mindset_extra = _maybe_load("mindset_mapping_2026-04-29_extra.py")
    map_29_nutrition_extra = _maybe_load("nutrition_mapping_2026-04-29_extra.py")

    buckets: dict[str, dict[tuple[str, str], dict]] = {c: {} for c in CATEGORIES}
    counters = {"drops": 0, "jpkr": 0}
    missing: list[tuple[str, str]] = []

    def insert_simple(row: dict, cat: str) -> None:
        k = _key(row)
        existing = buckets[cat].get(k)
        if existing is None or _row_richness(row) > _row_richness(existing):
            buckets[cat][k] = row

    def insert_with_mapping(row: dict, cat: str, m: dict) -> None:
        for key in ("niche", "segment_original", "industry", "angle_to_take"):
            if not (row.get(key) or "").strip() and m.get(key):
                row[key] = m[key]
        k = _key(row)
        # Cross-source dedup: keep the original category if it already exists
        # in another bucket from sources #1~#6 (don't move e.g. kiransagar).
        moved_from = None
        for other_cat in CATEGORIES:
            if other_cat == cat:
                continue
            if k in buckets[other_cat]:
                moved_from = other_cat
                break
        if moved_from is not None:
            existing = buckets[moved_from][k]
            if _row_richness(row) > _row_richness(existing):
                merged = existing.copy()
                if row.get("description"):
                    merged["description"] = row["description"]
                if row.get("website"):
                    merged["website"] = row["website"]
                for key in ("niche", "segment_original", "industry", "angle_to_take"):
                    if not (merged.get(key) or "").strip() and row.get(key):
                        merged[key] = row[key]
                buckets[moved_from][k] = merged
            return
        insert_simple(row, cat)

    # 1) sources #1~#6 — apply category_split_mapping (simple email→category)
    for path in SOURCES_19COL:
        for r in _read(path):
            email = (r.get("email") or "").strip()
            if not email:
                continue
            cat = cat_split.get(email)
            if cat is None:
                missing.append((path.name, email))
                continue
            if cat == "drop":
                counters["drops"] += 1
                continue
            if cat not in CATEGORIES:
                raise RuntimeError(f"Unknown category {cat!r} for {email}")
            country = (r.get("country") or "").upper()
            if country in {"JP", "KR"}:
                counters["jpkr"] += 1
                continue
            insert_simple(_norm(r), cat)

    # 2) legacy / mindful / meditation-04-28 / 04-29 sweep — full-dict mapping
    #    (category + niche/seg/industry/angle)
    for src_path, mapping in [
        (SOURCE_LEGACY, legacy_map),
        (SOURCE_MINDFUL, mindful_map),
        (SOURCE_MEDITATION_0428, meditation_0428_map),
        (SOURCE_29_MEDITATION, map_29_meditation),
        (SOURCE_29_MINDSET, map_29_mindset),
        (SOURCE_29_FITNESS, map_29_fitness),
        (SOURCE_29_NUTRITION, map_29_nutrition),
        (SOURCE_29_YOGA_EXTRA, map_29_yoga_extra),
        (SOURCE_29_MINDSET_EXTRA, map_29_mindset_extra),
        (SOURCE_29_NUTRITION_EXTRA, map_29_nutrition_extra),
    ]:
        if not src_path.exists() or not mapping:
            continue
        for r in _read(src_path):
            email = (r.get("email") or "").strip()
            if not email:
                continue
            m = mapping.get(email)
            if m is None:
                missing.append((src_path.name, email))
                continue
            cat = m["category"]
            if cat == "drop":
                counters["drops"] += 1
                continue
            if cat not in CATEGORIES:
                raise RuntimeError(f"Unknown category {cat!r} for {email}")
            country = (r.get("country") or "").upper()
            if country in {"JP", "KR"}:
                counters["jpkr"] += 1
                continue
            insert_with_mapping(_norm(r), cat, m)

    if missing:
        print("MISSING mappings:", file=sys.stderr)
        for src, e in missing[:30]:
            print(f"  {src}: {e}", file=sys.stderr)
        raise SystemExit(f"{len(missing)} rows have no category mapping; aborting")

    OUT.mkdir(parents=True, exist_ok=True)
    for cat in CATEGORIES:
        rows = list(buckets[cat].values())
        rows.sort(key=_follower_int, reverse=True)
        path = OUT / f"{cat}.csv"
        with path.open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=UNIFIED_FIELDS)
            w.writeheader()
            for r in rows:
                w.writerow({k: _flatten(r.get(k, "") or "") for k in UNIFIED_FIELDS})
        print(f"  {path.name:20s}: {len(rows):4d} rows")

    total = sum(len(buckets[c]) for c in CATEGORIES)
    print(f"\nwritten total: {total} rows | drop: {counters['drops']} | skipped JP/KR: {counters['jpkr']}")


if __name__ == "__main__":
    main()
