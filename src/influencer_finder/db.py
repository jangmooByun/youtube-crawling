from __future__ import annotations

import os
import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator, Optional

from dotenv import load_dotenv

from .models import Email, Profile, Source

load_dotenv()

DEFAULT_DB_PATH = os.environ.get("DB_PATH", "./influencer.db")

SCHEMA = """
CREATE TABLE IF NOT EXISTS profiles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    platform TEXT NOT NULL,
    handle TEXT NOT NULL,
    display_name TEXT,
    url TEXT NOT NULL UNIQUE,
    follower_count INTEGER,
    bio TEXT,
    country TEXT,
    discovered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_profiles_platform ON profiles(platform);
CREATE INDEX IF NOT EXISTS idx_profiles_handle ON profiles(handle);

CREATE TABLE IF NOT EXISTS emails (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    profile_id INTEGER NOT NULL REFERENCES profiles(id) ON DELETE CASCADE,
    email TEXT NOT NULL,
    syntax_valid INTEGER,
    has_mx INTEGER,
    is_role_based INTEGER,
    source_url TEXT NOT NULL,
    raw_context TEXT,
    extraction_method TEXT,
    extracted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(profile_id, email)
);
CREATE INDEX IF NOT EXISTS idx_emails_profile ON emails(profile_id);
CREATE INDEX IF NOT EXISTS idx_emails_valid ON emails(syntax_valid, has_mx);

CREATE TABLE IF NOT EXISTS sources (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    profile_id INTEGER NOT NULL REFERENCES profiles(id) ON DELETE CASCADE,
    url TEXT NOT NULL,
    type TEXT NOT NULL,
    fetched_at TIMESTAMP,
    success INTEGER,
    detected_tech TEXT,
    UNIQUE(profile_id, url)
);
CREATE INDEX IF NOT EXISTS idx_sources_profile ON sources(profile_id);
CREATE INDEX IF NOT EXISTS idx_sources_type_success ON sources(type, success);
"""


def connect(db_path: str | Path = DEFAULT_DB_PATH) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db(db_path: str | Path = DEFAULT_DB_PATH) -> None:
    with connect(db_path) as conn:
        conn.executescript(SCHEMA)
        try:
            conn.execute("ALTER TABLE sources ADD COLUMN detected_tech TEXT")
        except sqlite3.OperationalError:
            pass
        conn.commit()


@contextmanager
def session(db_path: str | Path = DEFAULT_DB_PATH) -> Iterator[sqlite3.Connection]:
    conn = connect(db_path)
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def upsert_profile(conn: sqlite3.Connection, profile: Profile) -> int:
    cur = conn.execute(
        """
        INSERT INTO profiles (platform, handle, display_name, url, follower_count, bio, country)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(url) DO UPDATE SET
            display_name = excluded.display_name,
            follower_count = excluded.follower_count,
            bio = excluded.bio,
            country = COALESCE(excluded.country, profiles.country)
        RETURNING id
        """,
        (
            profile.platform,
            profile.handle,
            profile.display_name,
            profile.url,
            profile.follower_count,
            profile.bio,
            profile.country,
        ),
    )
    row = cur.fetchone()
    return int(row["id"])


def insert_email(conn: sqlite3.Connection, email: Email) -> Optional[int]:
    cur = conn.execute(
        """
        INSERT OR IGNORE INTO emails
            (profile_id, email, syntax_valid, has_mx, is_role_based,
             source_url, raw_context, extraction_method)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            email.profile_id,
            email.email,
            _bool(email.syntax_valid),
            _bool(email.has_mx),
            _bool(email.is_role_based),
            email.source_url,
            email.raw_context,
            email.extraction_method,
        ),
    )
    return cur.lastrowid if cur.rowcount else None


def insert_source(conn: sqlite3.Connection, source: Source) -> Optional[int]:
    cur = conn.execute(
        """
        INSERT OR IGNORE INTO sources (profile_id, url, type, fetched_at, success)
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            source.profile_id,
            source.url,
            source.type,
            source.fetched_at,
            _bool(source.success),
        ),
    )
    return cur.lastrowid if cur.rowcount else None


def mark_source_fetched(
    conn: sqlite3.Connection,
    source_id: int,
    success: bool,
    detected_tech: Optional[str] = None,
) -> None:
    if detected_tech:
        conn.execute(
            "UPDATE sources SET success=?, fetched_at=CURRENT_TIMESTAMP, detected_tech=? WHERE id=?",
            (1 if success else 0, detected_tech, source_id),
        )
    else:
        conn.execute(
            "UPDATE sources SET success=?, fetched_at=CURRENT_TIMESTAMP WHERE id=?",
            (1 if success else 0, source_id),
        )


def update_email_validation(
    conn: sqlite3.Connection,
    email_id: int,
    syntax_valid: bool,
    has_mx: bool,
    is_role_based: bool,
) -> None:
    conn.execute(
        """
        UPDATE emails
        SET syntax_valid = ?, has_mx = ?, is_role_based = ?
        WHERE id = ?
        """,
        (int(syntax_valid), int(has_mx), int(is_role_based), email_id),
    )


def _bool(value: Optional[bool]) -> Optional[int]:
    if value is None:
        return None
    return 1 if value else 0
