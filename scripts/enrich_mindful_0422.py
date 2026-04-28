"""Enrich data/0422/mindful/mindful_all.csv with YouTube channel description.

Same Playwright-based pattern as enrich_legacy.py but for the mindful folder
that the previous reclassification pass excluded. Output goes to
data/_mindful_enriched.csv (19-col schema), then a separate Claude-written
mindful_mapping.py classifies each row into meditation/mindset/drop.

No YouTube API quota used.
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
log = logging.getLogger("enrich_mindful")

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "data" / "0422" / "mindful" / "mindful_all.csv"
OUT = ROOT / "data" / "_mindful_enriched.csv"

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
    soup = BeautifulSoup(html, "lxml")
    desc = ""
    og = soup.find("meta", property="og:description")
    if og and og.get("content"):
        desc = str(og["content"]).strip()

    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()
    body_text = soup.get_text(" ", strip=True)
    if len(desc) < 80 and len(body_text) > 200:
        m = re.search(r"Description\s+(.+?)(?:Links|Stats|Joined|Subscribed|$)", body_text)
        if m:
            desc = (desc + " | " + m.group(1).strip()) if desc else m.group(1).strip()
        else:
            desc = (desc + " | " + body_text[:1500]) if desc else body_text[:1500]

    first_link = ""
    for a in soup.find_all("a", href=True):
        href = str(a["href"])
        if href.startswith("http") and "youtube.com" not in href and "youtu.be" not in href:
            first_link = href
            break

    return desc, first_link


def crawl_one(browser, profile_url: str) -> tuple[str, str, str | None]:
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
    except Exception as e:
        return "", "", str(e)

    desc, link = extract_about(html)
    return desc, link, None


def read_legacy(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8-sig", errors="replace") as f:
        return list(csv.DictReader(f))


def normalize(src_row: dict) -> dict:
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
    rows = read_legacy(SRC)
    log.info("loaded mindful: %d rows", len(rows))

    profile_to_desc: dict[str, tuple[str, str]] = {}
    out_rows: list[dict] = []

    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        try:
            for i, src in enumerate(rows, 1):
                row = normalize(src)
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
