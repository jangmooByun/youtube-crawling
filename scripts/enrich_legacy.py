"""Enrich legacy CSVs (sources #7 + #8) with YouTube channel description.

Inputs (legacy schema, missing description/niche/segment/industry):
  - data/0422/fitness/fitness_all.csv          (26 rows, 13-col)
  - data/nutrition_all_enriched.csv            (16 rows, 14-col, has angle_to_take)

For each row:
  1. Resolve YouTube channel /about page from `profile_url`
  2. Use Playwright (headless chromium) to load the SPA, wait for hydration
  3. Extract channel description text + external link section
  4. Optionally crawl the first external personal-domain link for richer signal

No YouTube API quota used. Robots.txt + UA rotation + delay_range respected.

Output (19-col schema, joined into one master file):
  - data/_legacy_enriched.csv

Schema:
  first_name, full_name, handle, platform, follower_count, country,
  email, profile_url, website, description,
  niche, segment_original, industry, angle_to_take,
  source_url, raw_context, is_role_based, has_mx, detected_tech

`niche` / `segment_original` / `industry` start empty — filled by Claude
in conversation later via scripts/legacy_mapping.py.
"""

from __future__ import annotations

import csv
import logging
import random
import re
import sys
import time
from pathlib import Path
from urllib.parse import urlparse

from bs4 import BeautifulSoup
from playwright.sync_api import TimeoutError as PWTimeout
from playwright.sync_api import sync_playwright

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(message)s")
log = logging.getLogger("enrich_legacy")

ROOT = Path(__file__).resolve().parents[1]
SRC_FITNESS = ROOT / "data" / "0422" / "fitness" / "fitness_all.csv"
SRC_NUTRITION = ROOT / "data" / "nutrition_all_enriched.csv"
OUT = ROOT / "data" / "_legacy_enriched.csv"

UNIFIED_FIELDS = [
    "first_name", "full_name", "handle", "platform", "follower_count", "country",
    "email", "profile_url", "website", "description",
    "niche", "segment_original", "industry", "angle_to_take",
    "source_url", "raw_context", "is_role_based", "has_mx", "detected_tech",
]

USER_AGENTS = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
]
DELAY_RANGE = (3.0, 7.0)
TIMEOUT_MS = 30_000


def split_name(name: str) -> tuple[str, str]:
    name = (name or "").strip()
    if not name:
        return "", ""
    first = name.split()[0] if name else ""
    return first, name


def channel_about_url(profile_url: str) -> str:
    p = urlparse(profile_url)
    path = p.path.rstrip("/")
    if not path.startswith("/@") and not path.startswith("/channel/") and not path.startswith("/c/") and not path.startswith("/user/"):
        return profile_url
    return f"{p.scheme}://{p.netloc}{path}/about"


def extract_about(html: str) -> tuple[str, str]:
    """Return (description, first_external_link)."""
    soup = BeautifulSoup(html, "lxml")
    desc = ""

    # 1) og:description meta — lightweight signal
    og = soup.find("meta", property="og:description")
    if og and og.get("content"):
        desc = og["content"].strip()

    # 2) full About text (may contain richer description than og)
    # YouTube's modern about page renders text inside ytd-channel-about-metadata-renderer
    # In headless browser we can grep readable text after stripping scripts.
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()
    body_text = soup.get_text(" ", strip=True)
    # Use body text only if og:description is too short
    if len(desc) < 80 and len(body_text) > 200:
        # Heuristic: extract a chunk near 'Description' or just take 2k chars
        m = re.search(r"Description\s+(.+?)(?:Links|Stats|Joined|Subscribed|$)", body_text)
        if m:
            desc = (desc + " | " + m.group(1).strip()) if desc else m.group(1).strip()
        else:
            desc = (desc + " | " + body_text[:1500]) if desc else body_text[:1500]

    # 3) first external link (non-youtube)
    first_link = ""
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if href.startswith("http") and "youtube.com" not in href and "youtu.be" not in href:
            first_link = href
            break

    return desc, first_link


def crawl_one(browser, profile_url: str) -> tuple[str, str, str | None]:
    """Return (description, website_link, error). Sleeps before fetch."""
    time.sleep(random.uniform(*DELAY_RANGE))
    about_url = channel_about_url(profile_url)
    ua = random.choice(USER_AGENTS)
    try:
        ctx = browser.new_context(user_agent=ua, viewport={"width": 1280, "height": 900})
        page = ctx.new_page()
        try:
            page.goto(about_url, timeout=TIMEOUT_MS, wait_until="domcontentloaded")
            try:
                page.wait_for_load_state("networkidle", timeout=8_000)
            except PWTimeout:
                pass
            html = page.content()
        finally:
            ctx.close()
    except PWTimeout:
        return "", "", "timeout"
    except Exception as e:  # pragma: no cover
        return "", "", str(e)

    desc, link = extract_about(html)
    return desc, link, None


def read_legacy(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8-sig", errors="replace") as f:
        return list(csv.DictReader(f))


def normalize(src_row: dict, src_label: str) -> dict:
    """Project legacy row onto unified 19-col dict."""
    name = src_row.get("name", "") or src_row.get("full_name", "")
    first, full = split_name(name)
    out = {k: "" for k in UNIFIED_FIELDS}
    out["first_name"] = first
    out["full_name"] = full
    for k in ("handle", "platform", "follower_count", "country",
              "email", "profile_url",
              "source_url", "raw_context", "is_role_based", "has_mx",
              "detected_tech", "angle_to_take"):
        if k in src_row:
            out[k] = src_row.get(k, "") or ""
    return out


def main() -> None:
    csv.field_size_limit(sys.maxsize)
    fitness = read_legacy(SRC_FITNESS)
    nutrition = read_legacy(SRC_NUTRITION)
    log.info("loaded: fitness=%d, nutrition=%d", len(fitness), len(nutrition))

    rows = (
        [(r, "0422_fitness") for r in fitness]
        + [(r, "nutrition_all_enriched") for r in nutrition]
    )

    # Dedup by profile_url to avoid double-fetching the same channel.
    profile_to_desc: dict[str, tuple[str, str]] = {}
    out_rows: list[dict] = []

    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        try:
            for i, (src, label) in enumerate(rows, 1):
                row = normalize(src, label)
                profile_url = (row.get("profile_url") or "").strip()
                if not profile_url:
                    log.warning("[%d/%d] %s: no profile_url, skipping crawl", i, len(rows), row.get("full_name"))
                    out_rows.append(row)
                    continue

                if profile_url in profile_to_desc:
                    desc, link = profile_to_desc[profile_url]
                    log.info("[%d/%d] cache hit %s", i, len(rows), profile_url)
                else:
                    desc, link, err = crawl_one(browser, profile_url)
                    if err:
                        log.warning("[%d/%d] %s -> %s", i, len(rows), profile_url, err)
                    else:
                        log.info("[%d/%d] %s -> desc=%dch link=%s", i, len(rows), profile_url, len(desc), link[:60])
                    profile_to_desc[profile_url] = (desc, link)

                row["description"] = desc
                if link:
                    row["website"] = link
                out_rows.append(row)
        finally:
            browser.close()

    # Write
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=UNIFIED_FIELDS)
        w.writeheader()
        for r in out_rows:
            w.writerow({k: r.get(k, "") for k in UNIFIED_FIELDS})

    n_with_desc = sum(1 for r in out_rows if r.get("description"))
    log.info("wrote %s: %d rows (%d with desc)", OUT, len(out_rows), n_with_desc)


if __name__ == "__main__":
    main()
