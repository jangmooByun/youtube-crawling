"""
Email extraction from text. **Never generates or infers emails** —
only returns strings that literally appear in the input.

Handles:
  - Standard:     name@domain.com
  - Obfuscated:   name (at) domain (dot) com, name[at]domain.com
  - Korean:       name 골뱅이 domain 점 com, name 엣 domain 닷 com
"""

from __future__ import annotations

import re
from dataclasses import dataclass

from ..models import ExtractionMethod

STRICT_EMAIL_RE = re.compile(
    r"(?<![A-Za-z0-9._%+\-])"
    r"([A-Za-z0-9._%+\-]+@[A-Za-z0-9][A-Za-z0-9.\-]*\.[A-Za-z]{2,})"
    r"(?![A-Za-z0-9\-])"
)

_AT_TOKEN = (
    r"(?:"
    r"\(\s*at\s*\)|\[\s*at\s*\]|\{\s*at\s*\}"
    r"|\s+at\s+"
    r"|\s*골뱅이\s*|\s*엣\s*"
    r")"
)
_DOT_TOKEN = (
    r"(?:"
    r"\(\s*dot\s*\)|\[\s*dot\s*\]|\{\s*dot\s*\}"
    r"|\s+dot\s+"
    r"|\s*점\s*|\s*닷\s*"
    r")"
)

OBFUSC_EMAIL_RE = re.compile(
    rf"([A-Za-z0-9._%+\-]+)\s*{_AT_TOKEN}\s*"
    rf"([A-Za-z0-9][A-Za-z0-9\-]*(?:\s*{_DOT_TOKEN}\s*[A-Za-z0-9\-]+)*)"
    rf"\s*{_DOT_TOKEN}\s*([A-Za-z]{{2,}})",
    re.IGNORECASE,
)


@dataclass
class ExtractedEmail:
    email: str
    raw_match: str
    raw_context: str
    method: ExtractionMethod


def extract_emails(text: str, context_chars: int = 100) -> list[ExtractedEmail]:
    if not text:
        return []

    found: dict[str, ExtractedEmail] = {}

    for m in STRICT_EMAIL_RE.finditer(text):
        raw = m.group(1)
        normalized = _normalize(raw)
        if normalized in found:
            continue
        found[normalized] = ExtractedEmail(
            email=normalized,
            raw_match=raw,
            raw_context=_context(text, m.start(), m.end(), context_chars),
            method="regex_direct",
        )

    for m in OBFUSC_EMAIL_RE.finditer(text):
        local = m.group(1)
        domain_body = m.group(2)
        tld = m.group(3)
        domain_parts = re.split(_DOT_TOKEN, domain_body, flags=re.IGNORECASE)
        domain = ".".join(p.strip() for p in domain_parts if p and p.strip())
        reconstructed = f"{local.strip()}@{domain}.{tld.strip()}"
        normalized = _normalize(reconstructed)
        if not _looks_like_email(normalized):
            continue
        if normalized in found:
            continue
        found[normalized] = ExtractedEmail(
            email=normalized,
            raw_match=m.group(0),
            raw_context=_context(text, m.start(), m.end(), context_chars),
            method="deobfuscated",
        )

    return list(found.values())


def _normalize(email: str) -> str:
    return email.strip().strip(".,;:)(<>\"'").lower()


def _looks_like_email(s: str) -> bool:
    return bool(STRICT_EMAIL_RE.fullmatch(s))


def _context(text: str, start: int, end: int, n: int) -> str:
    left = max(0, start - n)
    right = min(len(text), end + n)
    snippet = text[left:right]
    snippet = re.sub(r"\s+", " ", snippet).strip()
    return snippet


def extract_mailto_hrefs(hrefs: list[str]) -> list[str]:
    emails: list[str] = []
    seen: set[str] = set()
    for href in hrefs:
        if not href or not href.lower().startswith("mailto:"):
            continue
        addr = href[7:].split("?", 1)[0].strip()
        addr = _normalize(addr)
        if _looks_like_email(addr) and addr not in seen:
            seen.add(addr)
            emails.append(addr)
    return emails
