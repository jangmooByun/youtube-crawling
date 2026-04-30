"""
Extract external URLs from bio/description text:
  - Instagram / TikTok handles (cross-platform identity)
  - Link-in-bio aggregators (linktr.ee, beacons.ai, ...)
  - Personal domains (to be crawled for contact pages)
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from urllib.parse import urlparse

import tldextract

URL_RE = re.compile(
    r"https?://[^\s<>\"'()]+|(?<![A-Za-z0-9@/])(?:www\.)[^\s<>\"'()]+",
    re.IGNORECASE,
)

# Bare-domain match (no scheme, no www.) — restricted to a TLD whitelist and
# requires every label to start with an alpha char, so version strings like
# "python3.10.com" or "v1.0.com" don't false-match (the "10" / "0" labels fail).
BARE_DOMAIN_RE = re.compile(
    r"(?<![A-Za-z0-9@/.\-:])"
    r"(?:[a-z](?:[a-z0-9\-]{0,62}[a-z0-9])?\.)+"
    r"(?:com|co|net|org|io|app|me|bio|store|shop|live|tv|"
    r"studio|academy|world|fit|fitness|yoga|coach|life|"
    r"club|page|site|online|wellness|health)"
    r"(?:/[^\s<>\"'()]*)?"
    r"(?![A-Za-z0-9])",
    re.IGNORECASE,
)

INSTAGRAM_RE = re.compile(
    r"(?:https?://)?(?:www\.)?instagram\.com/([A-Za-z0-9_.]{1,30})/?",
    re.IGNORECASE,
)
TIKTOK_RE = re.compile(
    r"(?:https?://)?(?:www\.)?tiktok\.com/@([A-Za-z0-9_.]{1,24})/?",
    re.IGNORECASE,
)

LINK_IN_BIO_DOMAINS = {
    "linktr.ee",
    "beacons.ai",
    "stan.store",
    "campsite.bio",
    "lnk.bio",
    "bio.link",
    "solo.to",
    "komi.io",
    "allmylinks.com",
    "linkin.bio",
    "withkoji.com",
    "taplink.cc",
    "direct.me",
    "koji.to",
    "carrd.co",
    "popl.co",
    "mssg.me",
    "flowpage.com",
    "later.bio",
    "msha.ke",
    "znap.link",
    "linkr.bio",
    "magic.link",
}

SOCIAL_DOMAINS = {
    "youtube.com", "youtu.be", "instagram.com", "tiktok.com",
    "twitter.com", "x.com", "facebook.com", "threads.net",
    "pinterest.com", "snapchat.com", "twitch.tv",
    "t.me", "telegram.me", "whatsapp.com", "discord.gg", "discord.com",
    "spotify.com", "apple.com", "soundcloud.com",
    "amazon.com", "amzn.to",
}


@dataclass
class BioLinks:
    instagram_handles: list[str] = field(default_factory=list)
    tiktok_handles: list[str] = field(default_factory=list)
    link_in_bio_urls: list[str] = field(default_factory=list)
    personal_domain_urls: list[str] = field(default_factory=list)


def extract_bio_links(text: str) -> BioLinks:
    if not text:
        return BioLinks()

    result = BioLinks()
    seen = {"ig": set(), "tt": set(), "lib": set(), "pd": set()}

    for m in INSTAGRAM_RE.finditer(text):
        h = m.group(1).lower()
        if h in {"p", "reel", "reels", "tv", "explore", "accounts"}:
            continue
        if h not in seen["ig"]:
            seen["ig"].add(h)
            result.instagram_handles.append(h)

    for m in TIKTOK_RE.finditer(text):
        h = m.group(1).lower()
        if h not in seen["tt"]:
            seen["tt"].add(h)
            result.tiktok_handles.append(h)

    seen_hosts: set[str] = set()
    for raw_url in URL_RE.findall(text):
        url = _normalize_url(raw_url)
        if not url:
            continue
        host = _host(url)
        if not host:
            continue
        seen_hosts.add(host)
        if host in LINK_IN_BIO_DOMAINS:
            if url not in seen["lib"]:
                seen["lib"].add(url)
                result.link_in_bio_urls.append(url)
        elif host not in SOCIAL_DOMAINS and not _is_shortener(host):
            if url not in seen["pd"]:
                seen["pd"].add(url)
                result.personal_domain_urls.append(url)

    for raw_bare in BARE_DOMAIN_RE.findall(text):
        url = _normalize_url("https://" + raw_bare)
        if not url:
            continue
        host = _host(url)
        if not host or host in seen_hosts:
            continue
        seen_hosts.add(host)
        if host in LINK_IN_BIO_DOMAINS:
            if url not in seen["lib"]:
                seen["lib"].add(url)
                result.link_in_bio_urls.append(url)
        elif host not in SOCIAL_DOMAINS and not _is_shortener(host):
            if url not in seen["pd"]:
                seen["pd"].add(url)
                result.personal_domain_urls.append(url)

    return result


_ZERO_WIDTH = ("​", "‌", "‍", "﻿")


def _normalize_url(raw: str) -> str | None:
    url = raw.strip().rstrip(".,;:!?)(\"'")
    for ch in _ZERO_WIDTH:
        url = url.replace(ch, "")
    if url.lower().startswith("www."):
        url = "https://" + url
    try:
        parsed = urlparse(url)
        if not parsed.netloc:
            return None
        return url
    except ValueError:
        return None


def _host(url: str) -> str | None:
    try:
        netloc = urlparse(url).netloc.lower()
    except ValueError:
        return None
    if netloc.startswith("www."):
        netloc = netloc[4:]
    return netloc or None


def _is_shortener(host: str) -> bool:
    ext = tldextract.extract(host)
    domain = f"{ext.domain}.{ext.suffix}".lower()
    return domain in {
        "bit.ly", "tinyurl.com", "goo.gl", "t.co", "ow.ly",
        "buff.ly", "is.gd", "shorturl.at",
    }
