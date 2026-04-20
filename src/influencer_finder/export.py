from __future__ import annotations

import csv
import re
from pathlib import Path
from typing import Optional

from .db import connect

COLUMNS = [
    "name",
    "handle",
    "platform",
    "follower_count",
    "country",
    "email",
    "is_role_based",
    "has_mx",
    "syntax_valid",
    "source_url",
    "raw_context",
    "profile_url",
]


_ALLOWED_FILTER_RE = re.compile(
    r"^[\sA-Za-z0-9_=<>!'.()%\-]+(?:AND|OR|\s|[\sA-Za-z0-9_=<>!'.()%\-])*$",
    re.IGNORECASE,
)


def export_csv(
    output_path: str | Path,
    db_path: Optional[str | Path] = None,
    where: Optional[str] = None,
) -> int:
    sql = """
        SELECT
            p.display_name AS name,
            p.handle AS handle,
            p.platform AS platform,
            p.follower_count AS follower_count,
            p.country AS country,
            e.email AS email,
            e.is_role_based AS is_role_based,
            e.has_mx AS has_mx,
            e.syntax_valid AS syntax_valid,
            e.source_url AS source_url,
            e.raw_context AS raw_context,
            p.url AS profile_url
        FROM emails e
        JOIN profiles p ON p.id = e.profile_id
    """
    if where:
        if not _ALLOWED_FILTER_RE.match(where):
            raise ValueError(f"Unsafe filter expression: {where!r}")
        sql += f" WHERE {where}"
    sql += " ORDER BY p.follower_count DESC NULLS LAST, p.id"

    conn = connect(db_path) if db_path else connect()
    try:
        rows = conn.execute(sql).fetchall()
    finally:
        conn.close()

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNS)
        writer.writeheader()
        for row in rows:
            writer.writerow({col: row[col] for col in COLUMNS})

    return len(rows)
