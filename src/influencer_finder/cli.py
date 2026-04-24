from __future__ import annotations

import logging
from datetime import date
from pathlib import Path
from typing import Optional

import typer
from rich.console import Console
from rich.table import Table

from . import db as db_module
from . import pipeline
from .db import connect, init_db
from .export import export_csv


def _default_out_path(out: Optional[Path], filename: str = "leads.csv") -> Path:
    """Fold bare filenames under data/<YYYY-MM-DD>/. Explicit paths pass through."""
    today = date.today().isoformat()
    if out is None:
        return Path("data") / today / filename
    if out.parent == Path("."):
        return Path("data") / today / out.name
    return out

logging.basicConfig(level=logging.WARNING, format="%(levelname)s %(name)s: %(message)s")

app = typer.Typer(
    help="Influencer email finder — discover real contact emails from public bios.",
    no_args_is_help=True,
)
discover_app = typer.Typer(help="Discover influencers on supported platforms.")
app.add_typer(discover_app, name="discover")
console = Console()


@app.command("init")
def init(db_path: str = typer.Option(db_module.DEFAULT_DB_PATH, help="SQLite path")):
    """Initialize the database schema."""
    init_db(db_path)
    console.print(f"[green]Initialized DB at {db_path}[/]")


@discover_app.command("youtube")
def discover_youtube(
    keyword: str = typer.Option(..., "--keyword", "-k"),
    max: int = typer.Option(50, "--max", help="Max channels to fetch"),
    min_subs: Optional[int] = typer.Option(None, "--min-subs"),
    max_subs: Optional[int] = typer.Option(None, "--max-subs"),
    region: Optional[str] = typer.Option(None, "--region", help="ISO country code"),
    language: Optional[str] = typer.Option(None, "--language"),
    db_path: str = typer.Option(db_module.DEFAULT_DB_PATH, "--db"),
):
    """Search YouTube channels by keyword and save metadata."""
    pipeline.discover_youtube(
        keyword=keyword,
        max_channels=max,
        min_subscribers=min_subs,
        max_subscribers=max_subs,
        region_code=region,
        relevance_language=language,
        db_path=db_path,
    )


@app.command("extract")
def extract(db_path: str = typer.Option(db_module.DEFAULT_DB_PATH, "--db")):
    """Extract emails + external links from stored bios."""
    pipeline.extract_from_bios(db_path=db_path)


@app.command("crawl-links")
def crawl_links(
    config: str = typer.Option("config.yaml", "--config"),
    db_path: str = typer.Option(db_module.DEFAULT_DB_PATH, "--db"),
    max_urls: Optional[int] = typer.Option(None, "--max"),
):
    """Fetch linktr.ee/beacons/personal sites and extract emails."""
    pipeline.crawl_external_links(config_path=config, db_path=db_path, max_urls=max_urls)


@app.command("validate")
def validate(db_path: str = typer.Option(db_module.DEFAULT_DB_PATH, "--db")):
    """Run syntax + MX + role-based validation on all unvalidated emails."""
    pipeline.validate_emails(db_path=db_path)


@app.command("export")
def export(
    out: Optional[Path] = typer.Option(
        None,
        "--out",
        help="Output CSV path. Bare filenames are folded under data/<today>/.",
    ),
    filter: Optional[str] = typer.Option(
        None,
        "--filter",
        help="SQL WHERE fragment, e.g. \"has_mx=1 AND is_role_based=0\"",
    ),
    db_path: str = typer.Option(db_module.DEFAULT_DB_PATH, "--db"),
):
    """Export verified emails to CSV."""
    resolved = _default_out_path(out)
    n = export_csv(output_path=resolved, db_path=db_path, where=filter)
    console.print(f"[green]Exported {n} rows → {resolved}[/]")


@app.command("stats")
def stats(db_path: str = typer.Option(db_module.DEFAULT_DB_PATH, "--db")):
    """Show counts of profiles / emails by stage."""
    conn = connect(db_path)
    try:
        profiles = conn.execute("SELECT COUNT(*) AS n FROM profiles").fetchone()["n"]
        emails = conn.execute("SELECT COUNT(*) AS n FROM emails").fetchone()["n"]
        syn = conn.execute("SELECT COUNT(*) AS n FROM emails WHERE syntax_valid=1").fetchone()["n"]
        mx = conn.execute("SELECT COUNT(*) AS n FROM emails WHERE has_mx=1").fetchone()["n"]
        non_role = conn.execute(
            "SELECT COUNT(*) AS n FROM emails WHERE has_mx=1 AND is_role_based=0"
        ).fetchone()["n"]
        sources = conn.execute("SELECT COUNT(*) AS n FROM sources").fetchone()["n"]
        crawled = conn.execute(
            "SELECT COUNT(*) AS n FROM sources WHERE fetched_at IS NOT NULL"
        ).fetchone()["n"]
    finally:
        conn.close()

    table = Table(title="Influencer Finder — Stats")
    table.add_column("Metric", style="cyan")
    table.add_column("Count", justify="right", style="green")
    table.add_row("Profiles", str(profiles))
    table.add_row("Emails (raw)", str(emails))
    table.add_row("  Syntax valid", str(syn))
    table.add_row("  MX passing", str(mx))
    table.add_row("  Personal (non-role) + MX", str(non_role))
    table.add_row("Sources tracked", str(sources))
    table.add_row("  Crawled", str(crawled))
    console.print(table)


@app.command("run-all")
def run_all(
    keyword: str = typer.Option(..., "--keyword", "-k"),
    max: int = typer.Option(50, "--max"),
    min_subs: Optional[int] = typer.Option(None, "--min-subs"),
    max_subs: Optional[int] = typer.Option(None, "--max-subs"),
    region: Optional[str] = typer.Option(None, "--region"),
    language: Optional[str] = typer.Option(None, "--language"),
    config: str = typer.Option("config.yaml", "--config"),
    out: Optional[Path] = typer.Option(
        None,
        "--out",
        help="Output CSV path. Bare filenames are folded under data/<today>/.",
    ),
    db_path: str = typer.Option(db_module.DEFAULT_DB_PATH, "--db"),
):
    """Run the full pipeline end-to-end for a single keyword."""
    pipeline.discover_youtube(
        keyword=keyword,
        max_channels=max,
        min_subscribers=min_subs,
        max_subscribers=max_subs,
        region_code=region,
        relevance_language=language,
        db_path=db_path,
    )
    pipeline.extract_from_bios(db_path=db_path)
    pipeline.crawl_external_links(config_path=config, db_path=db_path)
    pipeline.validate_emails(db_path=db_path)
    resolved = _default_out_path(out)
    n = export_csv(output_path=resolved, db_path=db_path, where="has_mx=1")
    console.print(f"[green]Done. {n} leads → {resolved}[/]")


if __name__ == "__main__":
    app()
