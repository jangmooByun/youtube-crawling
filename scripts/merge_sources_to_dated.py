"""Merge legacy leads CSVs into data/2026-04-24/ 19-col format with strict dedup.

Inputs (existing legacy files produced by older runs):
  - data/lifestyle_leads.csv      -> new data/2026-04-24/lifestyle.csv (+ _enriched)
  - data/beatmakers_leads.csv     -> new data/2026-04-24/beatmakers.csv (+ _enriched)
  - data/nutrition_all_enriched.csv -> APPEND to data/2026-04-24/nutrition.csv
                                                   AND data/2026-04-24/nutrition_enriched.csv

Dedup rules (strict):
  - Within each source: unique by (email) AND unique by (profile_url).
    If multiple rows share a profile_url (same YouTube channel, many emails),
    keep only the best row — priority: is_role_based=0, has_mx=1, syntax_valid=1,
    original-order ASC (matches src/influencer_finder/export.py).
  - Cross file: reject any row whose email OR profile_url already exists in
    data/2026-04-24/{career,fitness,nutrition}_enriched.csv (all three categories).
    Same email or same YouTube link = duplicate, no exceptions.

Target schema (19 cols, matches export.py COLUMNS):
  first_name, full_name, handle, platform, follower_count, country, email,
  profile_url, website, description, niche, segment_original, industry,
  angle_to_take, source_url, raw_context, is_role_based, has_mx, detected_tech

Cells containing newlines are flattened to single spaces on write
(so every record stays on one line, like the other 2026-04-24 files).
"""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path


ROOT = Path("/home/bjm/ABC/Marketing/youtube-crawling")
DATED = ROOT / "data" / "2026-04-24"

TARGET_COLUMNS = [
    "first_name", "full_name", "handle", "platform", "follower_count", "country",
    "email", "profile_url", "website", "description", "niche", "segment_original",
    "industry", "angle_to_take", "source_url", "raw_context", "is_role_based",
    "has_mx", "detected_tech",
]

EXISTING_FILES = [
    DATED / "career_enriched.csv",
    DATED / "fitness_enriched.csv",
    DATED / "nutrition_enriched.csv",
]

_NAME_TOKEN_RE = re.compile(r"[A-Za-zÀ-ɏ][A-Za-zÀ-ɏ'.\-]*")
_NEWLINE_RE = re.compile(r"[\r\n]+")
_WS_RE = re.compile(r"\s+")


def flat(v):
    if not isinstance(v, str):
        return v
    v = _NEWLINE_RE.sub(" ", v)
    v = _WS_RE.sub(" ", v)
    return v.strip()


def first_name_of(full_name: str) -> str:
    if not full_name:
        return ""
    m = _NAME_TOKEN_RE.search(full_name)
    if m:
        return m.group(0)
    parts = full_name.split()
    return parts[0] if parts else ""


def norm_email(x: str) -> str:
    return (x or "").strip().lower()


def norm_url(x: str) -> str:
    return (x or "").strip().rstrip("/").lower()


def read_rows(path: Path, enc: str = "utf-8-sig") -> list[dict]:
    with path.open(newline="", encoding=enc) as f:
        return list(csv.DictReader(f))


def _int_or(x, default=0):
    if x is None or x == "":
        return default
    try:
        return int(x)
    except (ValueError, TypeError):
        return default


def pick_best_per_profile(rows: list[dict]) -> list[dict]:
    """One row per profile_url, using export.py's priority ordering."""
    groups: dict[str, list[tuple[int, dict]]] = {}
    for i, r in enumerate(rows):
        u = norm_url(r.get("profile_url", ""))
        if not u:
            continue
        groups.setdefault(u, []).append((i, r))

    best = []
    for u, items in groups.items():
        items.sort(key=lambda t: (
            _int_or(t[1].get("is_role_based"), 1),     # ASC (0 first)
            -_int_or(t[1].get("has_mx"), 0),            # DESC (1 first)
            -_int_or(t[1].get("syntax_valid"), 0),      # DESC (1 first)
            t[0],                                        # original order ASC
        ))
        best.append(items[0][1])
    return best


def map_to_target(src: dict) -> dict:
    full = flat(src.get("name", "") or "")
    out = {c: "" for c in TARGET_COLUMNS}
    out["first_name"] = first_name_of(full)
    out["full_name"] = full
    out["handle"] = flat(src.get("handle", "") or "")
    out["platform"] = flat(src.get("platform", "") or "")
    out["follower_count"] = (src.get("follower_count", "") or "").strip()
    out["country"] = flat(src.get("country", "") or "")
    out["email"] = (src.get("email", "") or "").strip()
    out["profile_url"] = (src.get("profile_url", "") or "").strip()
    out["source_url"] = (src.get("source_url", "") or "").strip()
    out["raw_context"] = flat(src.get("raw_context", "") or "")
    out["is_role_based"] = (src.get("is_role_based", "") or "").strip()
    out["has_mx"] = (src.get("has_mx", "") or "").strip()
    out["detected_tech"] = flat(src.get("detected_tech", "") or "")
    out["angle_to_take"] = flat(src.get("angle_to_take", "") or "")
    # website / description / niche / segment_original / industry stay ""
    return out


def load_existing_keys() -> tuple[set, set]:
    emails, urls = set(), set()
    for p in EXISTING_FILES:
        for r in read_rows(p):
            e = norm_email(r.get("email", ""))
            u = norm_url(r.get("profile_url", ""))
            if e:
                emails.add(e)
            if u:
                urls.add(u)
    return emails, urls


def dedup_and_filter(
    src_rows: list[dict],
    seen_emails: set,
    seen_urls: set,
) -> tuple[list[dict], dict]:
    """Apply per-source dedup then filter against seen_* (which is mutated)."""
    best = pick_best_per_profile(src_rows)
    mapped = [map_to_target(r) for r in best]

    kept = []
    skipped_existing = 0
    skipped_same_email = 0
    skipped_same_url = 0
    for row in mapped:
        e = norm_email(row["email"])
        u = norm_url(row["profile_url"])
        if e and e in seen_emails:
            # skip: email already used (in existing or earlier this run)
            if e in getattr(load_existing_keys, "_cached_emails", set()):
                skipped_existing += 1
            else:
                skipped_same_email += 1
            continue
        if u and u in seen_urls:
            if u in getattr(load_existing_keys, "_cached_urls", set()):
                skipped_existing += 1
            else:
                skipped_same_url += 1
            continue
        kept.append(row)
        if e:
            seen_emails.add(e)
        if u:
            seen_urls.add(u)

    return kept, {
        "in": len(src_rows),
        "after_profile_dedup": len(mapped),
        "kept": len(kept),
        "skipped_existing": skipped_existing,
        "skipped_same_email": skipped_same_email,
        "skipped_same_url": skipped_same_url,
    }


def write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=TARGET_COLUMNS)
        w.writeheader()
        w.writerows(rows)


def append_csv(path: Path, new_rows: list[dict]) -> tuple[int, int]:
    """Append new_rows to existing csv at path. Returns (existing_count, total_count)."""
    existing = read_rows(path)
    total = existing + [
        {c: r.get(c, "") for c in TARGET_COLUMNS} for r in new_rows
    ]
    csv.field_size_limit(sys.maxsize)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=TARGET_COLUMNS)
        w.writeheader()
        w.writerows(total)
    return len(existing), len(total)


def main() -> None:
    csv.field_size_limit(sys.maxsize)

    seen_emails, seen_urls = load_existing_keys()
    # cache for skip-reason attribution
    load_existing_keys._cached_emails = set(seen_emails)
    load_existing_keys._cached_urls = set(seen_urls)
    print(f"seeded from existing: {len(seen_emails)} emails, {len(seen_urls)} urls")

    # ---- lifestyle ----
    src = read_rows(ROOT / "data" / "lifestyle_leads.csv")
    kept, stats = dedup_and_filter(src, seen_emails, seen_urls)
    write_csv(DATED / "lifestyle.csv", kept)
    write_csv(DATED / "lifestyle_enriched.csv", kept)
    print(f"lifestyle: {stats} -> wrote {len(kept)} rows to lifestyle.csv & lifestyle_enriched.csv")

    # ---- beatmakers ----
    src = read_rows(ROOT / "data" / "beatmakers_leads.csv")
    kept, stats = dedup_and_filter(src, seen_emails, seen_urls)
    write_csv(DATED / "beatmakers.csv", kept)
    write_csv(DATED / "beatmakers_enriched.csv", kept)
    print(f"beatmakers: {stats} -> wrote {len(kept)} rows to beatmakers.csv & beatmakers_enriched.csv")

    # ---- nutrition (append) ----
    src = read_rows(ROOT / "data" / "nutrition_all_enriched.csv")
    kept, stats = dedup_and_filter(src, seen_emails, seen_urls)
    n1_before, n1_after = append_csv(DATED / "nutrition.csv", kept)
    n2_before, n2_after = append_csv(DATED / "nutrition_enriched.csv", kept)
    print(f"nutrition: {stats}")
    print(f"  nutrition.csv: {n1_before} -> {n1_after} rows (+{n1_after - n1_before})")
    print(f"  nutrition_enriched.csv: {n2_before} -> {n2_after} rows (+{n2_after - n2_before})")


if __name__ == "__main__":
    main()
