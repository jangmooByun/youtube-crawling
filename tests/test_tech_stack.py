from influencer_finder.extractors.tech_stack import detect_tech_stack


def test_empty_html_returns_empty():
    assert detect_tech_stack("") == []
    assert detect_tech_stack("", "https://example.com") == []


def test_webflow_meta_generator():
    html = '<html><head><meta name="generator" content="Webflow"></head></html>'
    assert "Webflow" in detect_tech_stack(html, "https://creator.com")


def test_squarespace_cdn_signature():
    html = '<script src="https://static1.squarespace.com/static/abc.js"></script>'
    assert "Squarespace" in detect_tech_stack(html)


def test_linktree_page_detects_destinations():
    html = """
    <html><body>
      <a href="https://creator.teachable.com/courses">Course</a>
      <a href="https://gumroad.com/creator">Shop</a>
      <a href="https://calendly.com/creator/call">Book a call</a>
    </body></html>
    """
    result = set(detect_tech_stack(html, "https://linktr.ee/creator"))
    assert {"Teachable", "Gumroad", "Calendly", "Linktree"}.issubset(result)


def test_neutral_blog_detects_nothing():
    html = "<html><body><p>Just plain text about cooking.</p></body></html>"
    assert detect_tech_stack(html, "https://example.com") == []


def test_url_hostname_triggers_detection():
    assert "Thinkific" in detect_tech_stack("", "https://creator.thinkific.com/")
    assert "Kajabi" in detect_tech_stack("", "https://creator.mykajabi.com/")


def test_convertkit_variants():
    assert "ConvertKit" in detect_tech_stack('<script src="https://f.convertkit.com/ckjs.js"></script>')
    assert "ConvertKit" in detect_tech_stack('<a href="https://ck.page/creator">Subscribe</a>')


def test_wellness_booking_platforms():
    html = """
    <a href="https://www.vagaro.com/janespa">Book</a>
    <a href="https://clients.mindbodyonline.com/classic/ws">Classes</a>
    <a href="https://my.practicebetter.io/#/abc/booking">Consult</a>
    <a href="https://simplepractice.com">SimplePractice</a>
    <a href="https://booksy.com/en-us/123-salon">Salon</a>
    <a href="https://acuityscheduling.com/schedule.php?owner=123">Book now</a>
    """
    result = set(detect_tech_stack(html))
    assert {
        "Vagaro",
        "Mindbody",
        "Practice Better",
        "SimplePractice",
        "Booksy",
        "Acuity Scheduling",
    }.issubset(result)
