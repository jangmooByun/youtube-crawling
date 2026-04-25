"""Fill empty `website` cells in data/2026-04-24/*.csv by parsing
`description` (YouTube bio) for personal-domain URLs.

Reuses src/influencer_finder/extractors/bio.py::extract_bio_links which
already filters out social / link-in-bio / URL-shortener domains.

Only fills cells that are currently empty — existing values are never
overwritten. Website is normalized to `https://<host>/` root form.
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path
from urllib.parse import urlparse

sys.path.insert(0, "/home/bjm/ABC/Marketing/youtube-crawling/src")
from influencer_finder.extractors.bio import extract_bio_links  # noqa: E402


ROOT = Path("/home/bjm/ABC/Marketing/youtube-crawling")
DATED = ROOT / "data" / "2026-04-24"

DATED_25 = ROOT / "data" / "2026-04-25"

TARGETS = [
    DATED_25 / "career.csv",
    DATED_25 / "career_enriched.csv",
    DATED_25 / "fitness.csv",
    DATED_25 / "fitness_enriched.csv",
    DATED_25 / "nutrition.csv",
    DATED_25 / "nutrition_enriched.csv",
    DATED_25 / "lifestyle.csv",
    DATED_25 / "lifestyle_enriched.csv",
    DATED_25 / "beatmakers.csv",
    DATED_25 / "beatmakers_enriched.csv",
]


def root_url(u: str) -> str:
    try:
        p = urlparse(u)
        if not p.netloc:
            return ""
        return f"{p.scheme or 'https'}://{p.netloc}/"
    except Exception:
        return ""


def process(path: Path) -> dict:
    with path.open(newline="", encoding="utf-8-sig") as f:
        r = csv.DictReader(f)
        fn = list(r.fieldnames or [])
        rows = list(r)

    filled = 0
    for row in rows:
        if (row.get("website", "") or "").strip():
            continue
        desc = row.get("description", "") or ""
        if not desc:
            continue
        links = extract_bio_links(desc)
        if not links.personal_domain_urls:
            continue
        chosen = root_url(links.personal_domain_urls[0])
        if chosen:
            row["website"] = chosen
            filled += 1

    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fn)
        w.writeheader()
        w.writerows(rows)

    return {"rows": len(rows), "filled": filled}


def main() -> None:
    csv.field_size_limit(sys.maxsize)
    for p in TARGETS:
        stats = process(p)
        print(f"{p.name}: filled {stats['filled']}/{stats['rows']}")


if __name__ == "__main__":
    main()
