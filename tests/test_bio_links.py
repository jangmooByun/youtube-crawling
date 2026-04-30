from influencer_finder.extractors.bio import extract_bio_links


def test_bare_domain_with_known_tld_is_picked_up():
    text = "Visit my site at anuragrishi.com for sessions"
    links = extract_bio_links(text)
    assert any("anuragrishi.com" in u for u in links.personal_domain_urls)


def test_bare_domain_does_not_match_version_string():
    text = "Tested on python3.10.com is not a real site, just numbers v1.0.com"
    links = extract_bio_links(text)
    assert not any("3.10.com" in u for u in links.personal_domain_urls)
    assert not any("1.0.com" in u for u in links.personal_domain_urls)


def test_bare_domain_skipped_when_already_seen_via_https():
    text = "Web: https://anuragrishi.com — also anuragrishi.com"
    links = extract_bio_links(text)
    matching = [u for u in links.personal_domain_urls if "anuragrishi.com" in u]
    assert len(matching) == 1


def test_new_link_in_bio_hosts_classified_correctly():
    text = "Links: https://carrd.co/me and https://direct.me/jane and https://koji.to/x"
    links = extract_bio_links(text)
    libs = " ".join(links.link_in_bio_urls)
    assert "carrd.co" in libs
    assert "direct.me" in libs
    assert "koji.to" in libs
    assert links.personal_domain_urls == []


def test_zero_width_space_stripped_from_url():
    text = "site: https://app.adjust.com/abc​ end"
    links = extract_bio_links(text)
    assert links.personal_domain_urls
    assert "​" not in links.personal_domain_urls[0]


def test_arrow_prefixed_url_still_matched():
    text = "► WEBSITE :- https://anuragrishi.com 👉 IG: instagram.com/foo"
    links = extract_bio_links(text)
    assert any("anuragrishi.com" in u for u in links.personal_domain_urls)


def test_youtube_and_social_domains_excluded_from_personal():
    text = "Sub here: https://www.youtube.com/@me and instagram.com/foo"
    links = extract_bio_links(text)
    assert links.personal_domain_urls == []
