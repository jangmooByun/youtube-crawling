"""
Detect SaaS / tech stack signatures in rendered HTML.

Runs on the same HTML the website crawler already fetched — no extra
network requests. Catches:
  - Script/CDN patterns (e.g. cdn.shopify.com)
  - <meta name="generator"> tags (Webflow, Wix, Squarespace, ...)
  - <a href> domains on link-in-bio pages (Linktree buttons pointing to
    Teachable / Gumroad / Calendly are the main signal here)
"""

from __future__ import annotations

import re
from urllib.parse import urlparse


RULES: dict[str, list[re.Pattern]] = {
    # Course platforms
    "Teachable": [re.compile(r"(?:cdn|school)\.teachable\.com|\.teachable\.com", re.I)],
    "Thinkific": [re.compile(r"assets\.thinkific\.com|\.thinkific\.com", re.I)],
    "Kajabi": [re.compile(r"kajabi-app-assets|kajabi-cdn\.kajabi\.com|\.mykajabi\.com", re.I)],
    "Skool": [re.compile(r"\bskool\.com", re.I)],
    "Podia": [re.compile(r"\bpodia\.com", re.I)],
    # Community
    "Circle": [re.compile(r"\bcircle\.so|circleassets\.com", re.I)],
    "Mighty Networks": [re.compile(r"mightynetworks\.com", re.I)],
    "Discord": [re.compile(r"discord\.gg|discord\.com/invite", re.I)],
    # Membership
    "Memberful": [re.compile(r"memberful\.com", re.I)],
    "MemberSpace": [re.compile(r"memberspace\.com", re.I)],
    "Patreon": [re.compile(r"\bpatreon\.com", re.I)],
    # Store / digital goods
    "Gumroad": [re.compile(r"\bgumroad\.com", re.I)],
    "Shopify": [re.compile(r"cdn\.shopify\.com|\.myshopify\.com", re.I)],
    "Stan Store": [re.compile(r"stan\.store", re.I)],
    "Payhip": [re.compile(r"payhip\.com", re.I)],
    "Lemon Squeezy": [re.compile(r"lemonsqueezy\.com", re.I)],
    # Link-in-bio
    "Linktree": [re.compile(r"linktr\.ee|linktree\.com", re.I)],
    "Beacons": [re.compile(r"beacons\.ai", re.I)],
    "Carrd": [re.compile(r"carrd\.co", re.I)],
    "Koji": [re.compile(r"koji\.to|withkoji\.com", re.I)],
    # Website builders
    "Webflow": [
        re.compile(r'<meta[^>]+name=["\']generator["\'][^>]+Webflow', re.I),
        re.compile(r"webflow\.com/js|webflow\.io", re.I),
    ],
    "Wix": [
        re.compile(r'<meta[^>]+name=["\']generator["\'][^>]+Wix', re.I),
        re.compile(r"static\.wixstatic\.com", re.I),
    ],
    "Squarespace": [
        re.compile(r'<meta[^>]+name=["\']generator["\'][^>]+Squarespace', re.I),
        re.compile(r"static1\.squarespace\.com|squarespace-cdn\.com", re.I),
    ],
    "WordPress": [re.compile(r"wp-content/|wp-includes/", re.I)],
    "Framer": [re.compile(r"framerusercontent\.com|framer\.website", re.I)],
    # Email / newsletter
    "ConvertKit": [re.compile(r"convertkit\.com|ck\.page|\bkit\.com/", re.I)],
    "Mailchimp": [re.compile(r"mailchimp\.com|list-manage\.com", re.I)],
    "Klaviyo": [re.compile(r"klaviyo\.com", re.I)],
    "MailerLite": [re.compile(r"mailerlite\.com", re.I)],
    "Substack": [re.compile(r"substack\.com", re.I)],
    "Beehiiv": [re.compile(r"beehiiv\.com", re.I)],
    # Scheduling
    "Calendly": [re.compile(r"calendly\.com", re.I)],
    "Cal.com": [re.compile(r"\bcal\.com(?!/blog)", re.I)],
    "TidyCal": [re.compile(r"tidycal\.com", re.I)],
    # Booking / service-professional SaaS (salon, fitness, wellness, consulting)
    "Vagaro": [re.compile(r"vagaro\.com", re.I)],
    "Mindbody": [re.compile(r"mindbodyonline\.com|\bmindbody\.io", re.I)],
    "Acuity Scheduling": [re.compile(r"acuityscheduling\.com", re.I)],
    "SimplePractice": [re.compile(r"simplepractice\.com|clientsecure\.me", re.I)],
    "Practice Better": [re.compile(r"practicebetter\.io", re.I)],
    "Booksy": [re.compile(r"booksy\.com", re.I)],
    "Jane App": [re.compile(r"janeapp\.com", re.I)],
    "HoneyBook": [re.compile(r"honeybook\.com", re.I)],
    "Dubsado": [re.compile(r"dubsado\.com", re.I)],
    "Square Appointments": [re.compile(r"squareup\.com/appointments|square\.site", re.I)],
    # Forms
    "Typeform": [re.compile(r"typeform\.com", re.I)],
    "Tally": [re.compile(r"tally\.so", re.I)],
    # Payment / chat
    "Stripe": [re.compile(r"js\.stripe\.com", re.I)],
    "Intercom": [re.compile(r"intercom\.io|intercomcdn\.com", re.I)],
    "HubSpot": [re.compile(r"hs-scripts\.com|\.hubspot\.com", re.I)],
}


def detect_tech_stack(html: str, url: str | None = None) -> list[str]:
    """Return a sorted list of SaaS names detected in the HTML.

    The HTML is searched as a single string against the compiled rule patterns.
    If a URL is provided, its hostname is also matched (catches creators hosted
    directly at e.g. ``my.thinkific.com``).
    """
    if not html:
        html = ""
    hits: set[str] = set()
    for name, patterns in RULES.items():
        for p in patterns:
            if p.search(html):
                hits.add(name)
                break
    if url:
        host = urlparse(url).hostname or ""
        if host:
            for name, patterns in RULES.items():
                if name in hits:
                    continue
                if any(p.search(host) for p in patterns):
                    hits.add(name)
    return sorted(hits)
