# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

Environment uses `uv` (Python 3.11+). Package installs editable — code changes require no reinstall.

```bash
# One-time setup
uv venv --python 3.11
uv pip install -e . pytest
uv run playwright install chromium

# Tests
uv run pytest                                  # all tests
uv run pytest tests/test_email_regex.py -v     # single file
uv run pytest -k "obfuscation"                 # by name pattern

# Full pipeline against live DB (requires YOUTUBE_API_KEY in .env)
uv run influencer init
uv run influencer discover youtube --keyword "..." --max 50 --min-subs 10000
uv run influencer extract
uv run influencer crawl-links
uv run influencer validate
uv run influencer export --filter "has_mx=1 AND is_role_based=0" --out leads.csv
uv run influencer stats                        # progress table
```

The DB (`influencer.db`) is cumulative — repeated `discover` runs with different keywords upsert by `url`.

## Core invariant: no hallucinated emails

**Every email in the DB must be a string that literally appears on a public page.** The extractors never infer, never guess, never use an LLM. When adding code that touches emails, preserve this guarantee:

- `emails.source_url` must point to the page the string was read from.
- `emails.raw_context` must contain the surrounding ~100 chars so a human can Ctrl+F verify it.
- `extraction_method` distinguishes `regex_direct` / `mailto_href` / `deobfuscated`.

`tests/test_email_regex.py::test_extraction_preserves_real_value` guards this invariant — do not weaken it. If you add an LLM call anywhere in the extraction path, you are breaking the product's reason to exist.

## Pipeline architecture

The CLI commands are thin wrappers around `pipeline.py` functions. Each pipeline stage is independently re-runnable against the shared SQLite DB — this is why work is staged instead of streamed.

```
discover  →  profiles table (with bio)
extract   →  emails table (from bio regex) + sources table (external URLs)
crawl-links → emails table (from crawled link-in-bio + personal sites)
validate  →  fills syntax_valid / has_mx / is_role_based on existing emails
export    →  CSV join of profiles × emails
```

Key idempotency: `profiles.url` is UNIQUE, `emails(profile_id, email)` is UNIQUE, `sources(profile_id, url)` is UNIQUE. Everything uses `INSERT OR IGNORE` / `ON CONFLICT DO UPDATE`.

## YouTube-as-anchor design

Only YouTube has a free official API. Instagram/TikTok discovery is not performed directly — instead, YouTube channel descriptions are mined for `instagram.com/<h>` / `tiktok.com/@<h>` / `linktr.ee/<s>` / personal-domain URLs. Those URLs get stored in `sources` with `type='external_link'` and the crawler (Playwright, in `extractors/website.py`) fetches them.

For personal domains the crawler tries root + paths from `config.yaml:website_paths_to_try` (`/contact`, `/about`, `/press`, `/문의`, etc.) and stops at the first page that yields emails.

Adding a new platform means: (1) a new `discovery/<platform>.py` with a class that yields profile metadata, (2) a pipeline function that inserts profiles with `platform='<name>'`, (3) regex additions in `extractors/bio.py` if the URL pattern is new. The rest of the pipeline is platform-agnostic.

## Email regex

`extractors/email_regex.py` has two compiled patterns:
- `STRICT_EMAIL_RE` — normal emails, with negative lookbehind/lookahead to avoid truncating TLDs. The lookahead deliberately excludes `.` so `foo@bar.com.` (sentence-terminator period) still matches.
- `OBFUSC_EMAIL_RE` — requires explicit `(at)`/`[at]`/`골뱅이`/`엣` + `(dot)`/`점`/`닷` tokens. Plain whitespace is NOT an obfuscation token (too many false positives).

Do not relax the obfuscated pattern to match bare spaces or bare `.` — review `test_no_false_match_on_version_string` before touching it.

## Validation does not delete

`validate` fills columns, never drops rows. Filtering is done at export time via the `--filter` WHERE fragment. The whitelist regex in `export.py::_ALLOWED_FILTER_RE` blocks SQL injection — when adding export filters, confirm the clause still matches.

SMTP connect-level verification is intentionally NOT implemented — it gets the source IP blacklisted. Keep it out.

## Crawling etiquette (load-bearing, not cosmetic)

`extractors/website.py:WebsiteCrawler` respects `robots.txt`, rotates User-Agents from `config.yaml`, and sleeps a random `delay_range` between requests. These are not optional polish — they are what keeps the tool out of ToS/legal trouble. If you need faster throughput, add concurrency via multiple `WebsiteCrawler` instances on separate hosts, not by shortening delays.

Instagram/TikTok direct scraping (`discovery/instagram.py`, `discovery/tiktok.py`) is intentionally out of the default path. The main email source is Phase 4 (link-in-bio crawl), which stays on public non-walled pages.
