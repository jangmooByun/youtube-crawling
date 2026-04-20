from __future__ import annotations

ROLE_LOCAL_PARTS = {
    "admin", "administrator", "info", "information", "contact", "hello", "hi",
    "support", "help", "service", "team", "sales", "marketing",
    "press", "pr", "media",
    "business", "biz", "inquiry", "inquiries",
    "partnership", "partnerships", "partner", "collab", "collaboration",
    "booking", "bookings",
    "noreply", "no-reply", "donotreply",
    "webmaster", "postmaster", "hostmaster",
    "office",
}


def is_role_based(email: str) -> bool:
    try:
        local = email.split("@", 1)[0].lower().strip()
    except IndexError:
        return False
    local_norm = local.replace(".", "").replace("_", "").replace("-", "")
    if local in ROLE_LOCAL_PARTS or local_norm in {p.replace("-", "") for p in ROLE_LOCAL_PARTS}:
        return True
    return False
