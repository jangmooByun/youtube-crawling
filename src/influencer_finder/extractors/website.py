"""
Crawl link-in-bio pages and personal websites to extract real emails.

All emails returned carry the exact source URL + surrounding context so the
user can manually verify each one. No inference, no LLM, no guessing.
"""

from __future__ import annotations

import logging
import random
import time
import urllib.robotparser
from dataclasses import dataclass
from typing import Optional
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup
from playwright.sync_api import TimeoutError as PWTimeout
from playwright.sync_api import sync_playwright

from .email_regex import ExtractedEmail, extract_emails, extract_mailto_hrefs
from .tech_stack import detect_tech_stack

logger = logging.getLogger(__name__)


@dataclass
class CrawlResult:
    url: str
    success: bool
    emails: list[ExtractedEmail]
    detected_tech: list[str] = None  # type: ignore[assignment]
    status: Optional[int] = None
    error: Optional[str] = None

    def __post_init__(self) -> None:
        if self.detected_tech is None:
            self.detected_tech = []


class WebsiteCrawler:
    def __init__(
        self,
        user_agents: list[str],
        delay_range: tuple[float, float] = (2.0, 5.0),
        timeout_ms: int = 20_000,
        respect_robots: bool = True,
    ):
        self.user_agents = user_agents or [_DEFAULT_UA]
        self.delay_range = delay_range
        self.timeout_ms = timeout_ms
        self.respect_robots = respect_robots
        self._robots_cache: dict[str, urllib.robotparser.RobotFileParser] = {}

    def __enter__(self) -> "WebsiteCrawler":
        self._pw = sync_playwright().start()
        self._browser = self._pw.chromium.launch(headless=True)
        return self

    def __exit__(self, *exc) -> None:
        try:
            self._browser.close()
        finally:
            self._pw.stop()

    def crawl(self, url: str) -> CrawlResult:
        if self.respect_robots and not self._robots_allows(url):
            return CrawlResult(url=url, success=False, emails=[], error="blocked_by_robots")

        self._sleep()
        ua = random.choice(self.user_agents)
        try:
            context = self._browser.new_context(user_agent=ua, viewport={"width": 1280, "height": 900})
            page = context.new_page()
            try:
                response = page.goto(url, timeout=self.timeout_ms, wait_until="domcontentloaded")
                status = response.status if response else None
                try:
                    page.wait_for_load_state("networkidle", timeout=5_000)
                except PWTimeout:
                    pass
                html = page.content()
            finally:
                context.close()
        except PWTimeout:
            return CrawlResult(url=url, success=False, emails=[], error="timeout")
        except Exception as e:
            logger.warning("crawl %s failed: %s", url, e)
            return CrawlResult(url=url, success=False, emails=[], error=str(e))

        emails = _extract_from_html(html, source_url=url)
        tech = detect_tech_stack(html, url)
        return CrawlResult(
            url=url, success=True, emails=emails, detected_tech=tech, status=status
        )

    def crawl_site_paths(
        self,
        base_url: str,
        priority_paths: list[str],
        fallback_paths: list[str] | None = None,
    ) -> list[CrawlResult]:
        results: list[CrawlResult] = []
        base = _origin(base_url)
        if not base:
            return results
        for path in priority_paths:
            candidate = urljoin(base + "/", path.lstrip("/"))
            results.append(self.crawl(candidate))
        have_email = any(r.emails for r in results)
        for path in fallback_paths or []:
            if have_email:
                break
            candidate = urljoin(base + "/", path.lstrip("/"))
            result = self.crawl(candidate)
            results.append(result)
            if result.emails:
                have_email = True
        return results

    def _robots_allows(self, url: str) -> bool:
        origin = _origin(url)
        if not origin:
            return True
        rp = self._robots_cache.get(origin)
        if rp is None:
            rp = urllib.robotparser.RobotFileParser()
            try:
                rp.set_url(urljoin(origin, "/robots.txt"))
                rp.read()
            except Exception:
                rp = None
            self._robots_cache[origin] = rp  # type: ignore[assignment]
        if rp is None:
            return True
        return rp.can_fetch("*", url)

    def _sleep(self) -> None:
        low, high = self.delay_range
        time.sleep(random.uniform(low, high))


def _extract_from_html(html: str, source_url: str) -> list[ExtractedEmail]:
    soup = BeautifulSoup(html, "lxml")

    mailto_hrefs = [a.get("href", "") for a in soup.find_all("a", href=True)]
    mailto_emails = extract_mailto_hrefs(mailto_hrefs)

    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()
    text = soup.get_text(" ", strip=True)

    regex_results = extract_emails(text)
    results: dict[str, ExtractedEmail] = {r.email: r for r in regex_results}

    for addr in mailto_emails:
        if addr not in results:
            results[addr] = ExtractedEmail(
                email=addr,
                raw_match=f"mailto:{addr}",
                raw_context=f"<a href='mailto:{addr}'> on {source_url}",
                method="mailto_href",
            )
    return list(results.values())


def _origin(url: str) -> Optional[str]:
    try:
        p = urlparse(url)
        if not p.scheme or not p.netloc:
            return None
        return f"{p.scheme}://{p.netloc}"
    except ValueError:
        return None


_DEFAULT_UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
)
