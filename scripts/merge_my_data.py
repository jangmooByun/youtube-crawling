"""Merge my-data/*.csv (curated) with data/total/*.csv (pipeline) into my-data/merged/.

my-data is the authoritative top; total rows are appended only when their
profile_url is not already present in the my-data file. See
plans/my-data-clever-dusk.md for context.
"""

from __future__ import annotations

import csv
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MY_DIR = ROOT / "my-data"
TOTAL_DIR = ROOT / "data" / "total"
OUT_DIR = MY_DIR / "merged"

JOBS = [
    ("fitness",    "merge",      "fitness.csv",    "fitness.csv"),
    ("mindset",    "merge",      "mindset.csv",    "mindset.csv"),
    ("nutrition",  "merge",      "nutrition.csv",  "nutrition.csv"),
    ("meditation", "dedup_my",   "meditation.csv", None),
    ("yoga",       "dedup_total", None,            "yoga.csv"),
]


def norm_url(u: str) -> str:
    return (u or "").strip().rstrip("/").lower()


def _read_csv(path: Path) -> tuple[list[str], list[dict]]:
    # Some upstream CSVs contain stray cp1252 bytes (e.g. 0x92). Replace on read
    # so a single bad byte does not abort the whole merge; output is utf-8 clean.
    with path.open(newline="", encoding="utf-8", errors="replace") as f:
        reader = csv.DictReader(f)
        header = list(reader.fieldnames or [])
        rows = list(reader)
    return header, rows


def _line_count(path: Path) -> int:
    with path.open("rb") as f:
        return sum(1 for _ in f)


def merge_one(my_path: Path, total_path: Path, out_path: Path, label: str) -> None:
    my_header, my_rows = _read_csv(my_path)

    if "profile_url" not in my_header:
        raise SystemExit(f"{my_path} missing profile_url column")

    _, total_rows = _read_csv(total_path)

    seen: set[str] = set()
    my_written = 0
    my_self_dup = 0
    appended = 0
    skipped_dup = 0
    skipped_empty = 0
    with out_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=my_header, extrasaction="ignore")
        writer.writeheader()
        for r in my_rows:
            key = norm_url(r.get("profile_url", ""))
            if key and key in seen:
                my_self_dup += 1
                continue
            if key:
                seen.add(key)
            writer.writerow(r)
            my_written += 1
        for r in total_rows:
            key = norm_url(r.get("profile_url", ""))
            if not key:
                skipped_empty += 1
                continue
            if key in seen:
                skipped_dup += 1
                continue
            seen.add(key)
            writer.writerow({col: r.get(col, "") for col in my_header})
            appended += 1

    total_n = len(total_rows)
    print(
        f"{label}: my={my_written}/{len(my_rows)} (self_dup={my_self_dup}) "
        f"+ total_new={appended} (dup={skipped_dup}, empty_url={skipped_empty}, total_in={total_n}) "
        f"-> {out_path.relative_to(ROOT)} (rows={my_written + appended})"
    )
    if appended + skipped_dup + skipped_empty != total_n:
        print(f"  WARN: counters do not sum to total_in for {label}", file=sys.stderr)


def copy_one(src: Path, out_path: Path, label: str) -> None:
    shutil.copyfile(src, out_path)
    n = _line_count(out_path) - 1
    print(f"{label}: copied {src.relative_to(ROOT)} -> {out_path.relative_to(ROOT)} (rows={n})")


def dedup_one(src: Path, out_path: Path, label: str) -> None:
    header, rows = _read_csv(src)
    seen: set[str] = set()
    written = 0
    self_dup = 0
    with out_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=header, extrasaction="ignore")
        writer.writeheader()
        for r in rows:
            key = norm_url(r.get("profile_url", ""))
            if key and key in seen:
                self_dup += 1
                continue
            if key:
                seen.add(key)
            writer.writerow(r)
            written += 1
    print(
        f"{label}: dedup {src.relative_to(ROOT)} -> {out_path.relative_to(ROOT)} "
        f"(rows={written}/{len(rows)}, self_dup={self_dup})"
    )


_YOGA_PAT = re.compile(
    r"\byoga\b|\byogi\b|\byin yoga\b|\byoga nidra\b|\bashtanga\b|\bvinyasa\b"
    r"|\bkundalini\b|\bjivamukti\b|\bkriya yoga\b|\bface yoga\b|\baerial yoga\b"
)
_MINDSET_PAT = re.compile(
    r"\b(meditation|mindset|mindfulness|hypnotherapy|asmr|nlp|eft|manifestation"
    r"|breathwork coach|stress coach|mental health|sahaja yoga|heartfulness|sleep medit)\b"
)
_INDUSTRY_LEADS_YOGA = re.compile(
    r"^\s*(wellness\s*/\s*(yoga|yin yoga|kundalini|jivamukti|kriya|aerial|face yoga"
    r"|vinyasa|christian yoga|performance yoga|yoga teacher|yoga insurance|yoga \+|yoga tt)"
    r"|fitness\s*/\s*yoga|yoga\s*/|yoga\s+|yoga teacher|yoga channel|yoga author"
    r"|yoga nidra teacher|yoga nidra \(|yoga school|yoga / qigong)"
)


def _is_yoga_row(r: dict) -> bool:
    """True when industry/segment signal yoga as the primary category.

    Mindset has many channels whose industry says "Wellness / yoga ..." — those
    belong in yoga.csv. Channels where meditation/mindfulness lead and yoga is
    incidental (e.g. Sahaja Yoga charity that runs meditation) stay in mindset.
    """
    industry = (r.get("industry") or "").lower()
    segment = (r.get("segment_original") or "").lower()
    target = industry + " | " + segment

    if not _YOGA_PAT.search(target):
        return False
    if not _MINDSET_PAT.search(target):
        return True
    # Both signals present — let industry's leading token decide.
    if _INDUSTRY_LEADS_YOGA.match(industry):
        return True
    # Fall back to segment's first '+' clause.
    seg_first = segment.split("+")[0]
    if re.search(r"\byoga\b", seg_first) and not _MINDSET_PAT.search(seg_first):
        return True
    return False


def reclassify_mindset_to_yoga(mindset_path: Path, yoga_path: Path) -> None:
    """Move yoga-leaning rows out of mindset.csv into yoga.csv (idempotent)."""
    m_header, m_rows = _read_csv(mindset_path)
    y_header, y_rows = _read_csv(yoga_path)
    if m_header != y_header:
        raise SystemExit(
            f"header mismatch — cannot move rows: mindset={m_header} vs yoga={y_header}"
        )

    existing_yoga = {norm_url(r.get("profile_url", "")) for r in y_rows}
    existing_yoga.discard("")

    keep_mindset: list[dict] = []
    moved_new: list[dict] = []
    moved_dup = 0
    for r in m_rows:
        if not _is_yoga_row(r):
            keep_mindset.append(r)
            continue
        key = norm_url(r.get("profile_url", ""))
        if key and key in existing_yoga:
            moved_dup += 1
            continue
        if key:
            existing_yoga.add(key)
        moved_new.append(r)

    with mindset_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=m_header, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(keep_mindset)

    with yoga_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=y_header, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(y_rows)
        writer.writerows(moved_new)

    print(
        f"reclassify: mindset->yoga moved {len(moved_new)} new + dropped {moved_dup} dup; "
        f"mindset rows {len(m_rows)}->{len(keep_mindset)}, "
        f"yoga rows {len(y_rows)}->{len(y_rows) + len(moved_new)}"
    )


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for label, mode, my_name, total_name in JOBS:
        out_path = OUT_DIR / f"{label}.csv"
        if mode == "merge":
            merge_one(MY_DIR / my_name, TOTAL_DIR / total_name, out_path, label)
        elif mode == "dedup_my":
            dedup_one(MY_DIR / my_name, out_path, label)
        elif mode == "dedup_total":
            dedup_one(TOTAL_DIR / total_name, out_path, label)
        else:
            raise SystemExit(f"unknown mode: {mode}")
    reclassify_mindset_to_yoga(OUT_DIR / "mindset.csv", OUT_DIR / "yoga.csv")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
