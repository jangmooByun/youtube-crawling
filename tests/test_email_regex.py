from influencer_finder.extractors.email_regex import (
    extract_emails,
    extract_mailto_hrefs,
)


def _addrs(results) -> list[str]:
    return sorted(r.email for r in results)


def test_standard_email_in_description():
    text = "Business inquiries: jane.doe+brand@example.com (Korean K-Beauty reviewer)"
    result = extract_emails(text)
    assert _addrs(result) == ["jane.doe+brand@example.com"]
    assert result[0].method == "regex_direct"
    assert "jane.doe+brand@example.com" in result[0].raw_context


def test_multiple_emails_deduplicated():
    text = "contact: foo@bar.com or FOO@BAR.COM for collabs"
    result = extract_emails(text)
    assert _addrs(result) == ["foo@bar.com"]


def test_english_obfuscation_at_dot():
    text = "email me at creator (at) gmail (dot) com for partnership"
    result = extract_emails(text)
    assert _addrs(result) == ["creator@gmail.com"]
    assert result[0].method == "deobfuscated"


def test_bracket_obfuscation():
    text = "biz[at]creator[dot]io"
    result = extract_emails(text)
    assert _addrs(result) == ["biz@creator.io"]


def test_korean_obfuscation_golbaengi():
    text = "문의: nara 골뱅이 naver 점 com"
    result = extract_emails(text)
    assert _addrs(result) == ["nara@naver.com"]
    assert result[0].method == "deobfuscated"


def test_korean_obfuscation_dat():
    text = "brand 엣 daum 닷 net 으로 연락주세요"
    result = extract_emails(text)
    assert _addrs(result) == ["brand@daum.net"]


def test_multi_level_tld_standard():
    text = "contact: press@studio.co.kr for media"
    result = extract_emails(text)
    assert _addrs(result) == ["press@studio.co.kr"]


def test_no_match_on_plain_text():
    assert extract_emails("this is just a sentence about cats and dogs") == []


def test_no_false_match_on_twitter_handle():
    assert extract_emails("follow @username on twitter") == []


def test_no_false_match_on_version_string():
    assert extract_emails("version 1.2.3 released 2024") == []


def test_mailto_hrefs():
    hrefs = [
        "mailto:contact@site.com",
        "mailto:foo@bar.com?subject=Hi",
        "MAILTO:BAR@BAZ.COM",
        "https://site.com",
        "tel:+821012345678",
        "",
        None,
    ]
    result = extract_mailto_hrefs([h for h in hrefs if h is not None])
    assert sorted(result) == ["bar@baz.com", "contact@site.com", "foo@bar.com"]


def test_context_window():
    prefix = "x" * 200
    suffix = "y" * 200
    text = f"{prefix} email: test@example.com {suffix}"
    result = extract_emails(text, context_chars=50)
    assert len(result) == 1
    ctx = result[0].raw_context
    assert "test@example.com" in ctx
    assert len(ctx) <= len("test@example.com") + 50 * 2 + 20


def test_trailing_punctuation_stripped():
    text = "write me at hello@creator.io."
    result = extract_emails(text)
    assert _addrs(result) == ["hello@creator.io"]


def test_extraction_preserves_real_value():
    """Guard against hallucination: extracted string MUST appear in source text."""
    text = "The real email is actual.person@company.io."
    result = extract_emails(text)
    assert len(result) == 1
    assert result[0].email in text.lower()
