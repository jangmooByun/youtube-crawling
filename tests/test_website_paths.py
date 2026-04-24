from influencer_finder.extractors.email_regex import ExtractedEmail
from influencer_finder.extractors.website import CrawlResult, WebsiteCrawler


def _make_crawler_with_stub(email_returning_paths: set[str]) -> WebsiteCrawler:
    crawler = WebsiteCrawler(user_agents=["UA/1.0"])

    def fake_crawl(url: str) -> CrawlResult:
        emails: list[ExtractedEmail] = []
        if any(p and p in url for p in email_returning_paths) or (
            "" in email_returning_paths and url.rstrip("/").count("/") == 2
        ):
            emails = [
                ExtractedEmail(
                    email="found@example.com",
                    raw_match="found@example.com",
                    raw_context="test",
                    method="regex_direct",
                )
            ]
        return CrawlResult(url=url, success=True, emails=emails)

    crawler.crawl = fake_crawl  # type: ignore[method-assign]
    return crawler


def test_priority_paths_visited_even_after_email_found():
    crawler = _make_crawler_with_stub({""})
    results = crawler.crawl_site_paths(
        "https://creator.com",
        priority_paths=["", "/contact", "/press"],
        fallback_paths=["/about"],
    )
    visited = [r.url for r in results]
    assert "https://creator.com/" in visited
    assert "https://creator.com/contact" in visited
    assert "https://creator.com/press" in visited
    assert "https://creator.com/about" not in visited


def test_fallback_short_circuits_once_email_found():
    crawler = _make_crawler_with_stub({"/about"})
    results = crawler.crawl_site_paths(
        "https://creator.com",
        priority_paths=[""],
        fallback_paths=["/about", "/collab", "/partnerships"],
    )
    visited = [r.url for r in results]
    assert "https://creator.com/about" in visited
    assert "https://creator.com/collab" not in visited
    assert "https://creator.com/partnerships" not in visited


def test_fallback_continues_when_no_email_yet():
    crawler = _make_crawler_with_stub({"/partnerships"})
    results = crawler.crawl_site_paths(
        "https://creator.com",
        priority_paths=[""],
        fallback_paths=["/about", "/collab", "/partnerships"],
    )
    visited = [r.url for r in results]
    assert "https://creator.com/about" in visited
    assert "https://creator.com/collab" in visited
    assert "https://creator.com/partnerships" in visited
