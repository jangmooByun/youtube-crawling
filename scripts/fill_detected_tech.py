"""Fill empty `detected_tech` in data/2026-04-24/*.csv by fetching each row's
`website` URL via HTTP(S) and running detect_tech_stack on the HTML.

Uses `requests` (not Playwright) — detect_tech_stack only needs raw HTML
string + URL, and JS-rendered platforms are mostly detectable in the
pre-render HTML anyway. Keeps the etiquette bits from WebsiteCrawler
(robots.txt respect, UA rotation, random delay from config.yaml).

Only fills cells currently empty. Failures (blocked, 4xx/5xx, timeout)
→ row skipped, detected_tech stays empty — no fabrication.
"""

from __future__ import annotations

import csv
import random
import sys
import time
import urllib.robotparser
import warnings
from pathlib import Path
from urllib.parse import urlparse

import requests
import yaml

warnings.filterwarnings("ignore")

sys.path.insert(0, "/home/bjm/ABC/Marketing/youtube-crawling/src")
from influencer_finder.extractors.tech_stack import detect_tech_stack  # noqa: E402


ROOT = Path("/home/bjm/ABC/Marketing/youtube-crawling")
DATED = ROOT / "data" / "2026-04-24"
CONFIG = ROOT / "config.yaml"

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


def read(path: Path):
    with path.open(newline="", encoding="utf-8-sig") as f:
        r = csv.DictReader(f)
        return list(r.fieldnames or []), list(r)


def write(path: Path, fieldnames, rows) -> None:
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)


def collect_crawl_urls() -> set[str]:
    urls: set[str] = set()
    for p in TARGETS:
        _, rows = read(p)
        for r in rows:
            web = (r.get("website", "") or "").strip()
            tech = (r.get("detected_tech", "") or "").strip()
            if web and not tech:
                urls.add(web)
    return urls


_robots_cache: dict[str, urllib.robotparser.RobotFileParser] = {}


def robots_allows(url: str, ua: str) -> bool:
    try:
        p = urlparse(url)
        origin = f"{p.scheme}://{p.netloc}"
    except Exception:
        return True
    rp = _robots_cache.get(origin)
    if rp is None:
        rp = urllib.robotparser.RobotFileParser()
        rp.set_url(f"{origin}/robots.txt")
        try:
            rp.read()
        except Exception:
            _robots_cache[origin] = rp
            return True
        _robots_cache[origin] = rp
    try:
        return rp.can_fetch(ua, url)
    except Exception:
        return True


def fetch(url: str, ua: str, timeout_s: int) -> tuple[str, str | None]:
    """Return (html, error). error is None on success."""
    try:
        r = requests.get(
            url,
            headers={"User-Agent": ua, "Accept": "text/html,application/xhtml+xml"},
            timeout=timeout_s,
            allow_redirects=True,
        )
    except requests.exceptions.RequestException as e:
        return "", f"net:{e.__class__.__name__}"
    if r.status_code >= 400:
        return "", f"http:{r.status_code}"
    return r.text, None


def main() -> None:
    csv.field_size_limit(sys.maxsize)

    cfg = yaml.safe_load(CONFIG.read_text())
    crawl_cfg = cfg.get("crawl", {})
    user_agents = crawl_cfg.get("user_agents") or [
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    ]
    delay_min = float(crawl_cfg.get("request_delay_min_seconds", 2))
    delay_max = float(crawl_cfg.get("request_delay_max_seconds", 5))
    timeout_s = int(crawl_cfg.get("timeout_seconds", 20))

    urls = sorted(collect_crawl_urls())
    print(f"fetching {len(urls)} unique URLs (delay {delay_min}-{delay_max}s, timeout {timeout_s}s)")

    tech_by_url: dict[str, str] = {}
    failed: list[tuple[str, str]] = []

    for i, url in enumerate(urls, 1):
        ua = random.choice(user_agents)
        if not robots_allows(url, ua):
            failed.append((url, "blocked_by_robots"))
            continue
        time.sleep(random.uniform(delay_min, delay_max))
        html, err = fetch(url, ua, timeout_s)
        if err:
            failed.append((url, err))
        else:
            try:
                tech = detect_tech_stack(html, url)
            except Exception as e:
                failed.append((url, f"detect:{e.__class__.__name__}"))
                continue
            if tech:
                tech_by_url[url] = ",".join(sorted(set(tech)))
        if i % 5 == 0 or i == len(urls):
            print(f"  [{i}/{len(urls)}] hits={len(tech_by_url)} failed={len(failed)}")

    total_filled = 0
    for p in TARGETS:
        fieldnames, rows = read(p)
        here = 0
        for r in rows:
            web = (r.get("website", "") or "").strip()
            if not web or (r.get("detected_tech", "") or "").strip():
                continue
            if web in tech_by_url:
                r["detected_tech"] = tech_by_url[web]
                here += 1
        write(p, fieldnames, rows)
        total_filled += here
        print(f"  {p.name}: filled {here}")

    print(f"done. cells filled: {total_filled}, crawl hits: {len(tech_by_url)}, failed: {len(failed)}")
    if failed:
        print("failure samples:")
        for url, err in failed[:15]:
            print(f"  {err:25s} {url}")


if __name__ == "__main__":
    main()
