from __future__ import annotations

from email_validator import EmailNotValidError, validate_email


def is_valid_syntax(email: str) -> bool:
    try:
        validate_email(email, check_deliverability=False)
        return True
    except EmailNotValidError:
        return False
