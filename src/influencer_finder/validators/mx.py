from __future__ import annotations

import dns.exception
import dns.resolver

_CACHE: dict[str, bool] = {}


def has_mx_record(email: str, timeout: float = 5.0) -> bool:
    try:
        domain = email.rsplit("@", 1)[1].lower()
    except IndexError:
        return False

    if domain in _CACHE:
        return _CACHE[domain]

    resolver = dns.resolver.Resolver()
    resolver.lifetime = timeout
    resolver.timeout = timeout

    try:
        answers = resolver.resolve(domain, "MX")
        result = len(list(answers)) > 0
    except (
        dns.resolver.NoAnswer,
        dns.resolver.NXDOMAIN,
        dns.resolver.NoNameservers,
        dns.exception.Timeout,
    ):
        result = False
    except Exception:
        result = False

    _CACHE[domain] = result
    return result
