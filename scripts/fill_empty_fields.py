"""Fill empty niche / segment_original / industry / angle_to_take / website in
data/2026-04-24/{lifestyle,beatmakers,nutrition}*.csv.

Strategy (heuristic, not LLM per-row — scales to 100+ rows):
  - website: pulled from source_url when host is NOT a social/link-in-bio domain.
  - niche / segment_original / industry: derived from sub-vertical classifier
    (handle + full_name + raw_context matched against regex sets copied from
    scripts/personalize_all.py). Per-subvertical label mapping below.
  - angle_to_take: for lifestyle/beatmakers, pick a variant from
    LIFESTYLE_ANGLES / MUSIC_PROD_ANGLES (same dict used by personalize_all.py);
    variant is chosen deterministically from email hash so re-runs are stable.
    For the 3 newly appended nutrition rows, angle_to_take is already present —
    only niche/segment/industry are filled from angle-text analysis.
  - description: left empty. The source leads CSVs don't carry the YouTube bio,
    the influencer.db does not exist, and we do not fabricate bios
    (CLAUDE.md: no hallucinated data).

Only blank cells are filled — never overwrite existing values.
"""

from __future__ import annotations

import csv
import hashlib
import re
import sys
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path("/home/bjm/ABC/Marketing/youtube-crawling")
DATED = ROOT / "data" / "2026-04-24"

SOCIAL_HOSTS = {
    "youtube.com", "www.youtube.com", "youtu.be", "m.youtube.com",
    "instagram.com", "www.instagram.com",
    "tiktok.com", "www.tiktok.com",
    "linktr.ee", "www.linktr.ee",
    "linkedin.com", "www.linkedin.com",
    "twitter.com", "x.com", "www.x.com",
    "facebook.com", "www.facebook.com", "m.facebook.com",
    "patreon.com", "www.patreon.com",
    "threads.net",
    "linkin.bio", "beacons.ai", "bio.link",
    "twitch.tv", "www.twitch.tv",
    "pinterest.com", "www.pinterest.com",
    "snapchat.com",
    "discord.com", "discord.gg",
}


LIFESTYLE_SUBS = {
    "home_decor": [re.compile(r"home.?decor|decorat|interior|apartment|house.?tour|homedec|\bdecor\b", re.I)],
    "vlog": [re.compile(r"\bvlog|daily\b|routine", re.I)],
    "study": [re.compile(r"\bstudy\b|productiv|notion", re.I)],
    "minimal": [re.compile(r"minimal|\bmnml\b|simpl|zen", re.I)],
    "travel": [re.compile(r"travel|tiny.?house|rv\b|nomad", re.I)],
    "beauty_fashion": [re.compile(r"beauty|makeup|fashion|style\b|outfit|chic", re.I)],
    "minimalist_creative": [re.compile(r"\bapartment sessions\b|creative", re.I)],
    "media_house": [re.compile(r"condenast|houseandgarden|subscription\.co", re.I)],
}

LIFESTYLE_LABELS = {
    "home_decor":         ("Home decor & interior-style inspiration",
                            "Home Decor / Interior Design",
                            "Lifestyle / home & interior"),
    "vlog":               ("Daily vlog & lifestyle content",
                            "Daily Vlog / Lifestyle",
                            "Lifestyle / content creator"),
    "study":              ("Study & productivity content",
                            "Study / Productivity",
                            "Lifestyle / education-adjacent"),
    "minimal":            ("Minimalism & simple-living lifestyle",
                            "Minimalism / Lifestyle Coaching",
                            "Lifestyle / wellness"),
    "travel":             ("Travel & nomad lifestyle",
                            "Travel / Nomad",
                            "Lifestyle / travel"),
    "beauty_fashion":     ("Beauty & fashion content",
                            "Beauty / Fashion",
                            "Lifestyle / beauty & fashion"),
    "media_house":        ("Media house / publication brand",
                            "Media House",
                            "Publication / brand"),
    "minimalist_creative": ("Intimate creative sessions content",
                            "Creative Sessions",
                            "Lifestyle / creative"),
    "default":            ("General lifestyle content & personal brand",
                            "Lifestyle (general)",
                            "Lifestyle / content creator"),
}

LIFESTYLE_ANGLES = {
    "home_decor": [
        'Start with discovery around "where\'d you get that?" comment volume, affiliate-revenue ceilings on LTK/Amazon, and paid consulting demand. Position the app as a branded interior-style environment with room catalogs, moodboards, shop-link hubs, and 1:1 consult booking—more controlled than scattered Pinterest/IG affiliate links.',
        'Lead with questions around catalog browsing behavior, repeat-item requests, and the gap between inspirational content and paid service revenue. Frame the app as a branded home-decor member space with style guides, saved rooms, shop links, and consult slots—tighter than Amazon Storefront + LTK + blog patchwork.',
        'Ask about follower questions on product sourcing, seasonal-project demand, and consulting lead conversion. Position the app as a branded interior-design hub with before/after galleries, moodboards, affiliate catalogs, and paid design sessions—more polished than Pinterest links scattered across platforms.',
    ],
    "vlog": [
        'Lead with questions around fan loyalty vs. ad-revenue dependence, BTS-content demand, and direct-monetization levers beyond YouTube AdSense. Frame the app as a branded premium fan space with exclusive vlogs, BTS feed, paid community, and push alerts—far stronger than relying on platform algorithms.',
        'Start with discovery around daily-content rhythm, fan-DM overload, and converting passive viewers into paid insiders. Position the app as a branded daily-vlog insider environment with early-access episodes, private chat, and subscriber perks—more owned than Instagram Close Friends.',
        'Ask about content-calendar fatigue, fan-retention beyond watch time, and the ceiling of brand-deal revenue. Frame the app as a branded community + premium-content hub with gated episodes, fan-driven Q&A, and member-only perks—more durable than platform ads.',
    ],
    "study": [
        'Lead with questions around "study with me" cohort retention, accountability loops, and converting lonely studiers into paying community members. Position the app as a branded focus environment with live study rooms, timers, accountability pods, and a private cohort feed—more intimate than YouTube broadcast.',
        'Start with discovery around daily-study habit formation, Notion template sales ceiling, and peer-accountability demand. Frame the app as a branded study hub with study-with-me rooms, habit tracker, templates, and a members-only feed—going beyond one-off template drops on Gumroad.',
    ],
    "minimal": [
        'Lead with questions around 30-day challenge completion, decluttering follow-through, and the habit-formation gap after content consumption. Position the app as a branded behavior-change space with challenge tracker, declutter checklists, habit logs, and a small-group community—closing the gap between inspiration and real change.',
        'Start with discovery around audience-transformation evidence, peer support demand, and monetizing behind a paywall. Frame the app as a branded minimalist-lifestyle coaching environment with guided challenges, journal prompts, and a members circle—tighter than blog + newsletter + PDF patchwork.',
    ],
    "travel": [
        'Start with discovery around trip-planning requests from followers, destination-guide demand, and converting YouTube views into paid itineraries. Position the app as a branded travel companion with saved itineraries, gear lists, location guides, and member community—more useful than scattered blog posts and Amazon lists.',
        'Lead with questions around audience-interest in full itineraries, sponsor-fatigue, and branded travel content sales. Frame the app as a branded travel-insider space with trip guides, offline maps, gear vault, and paid community—stronger than affiliate-link-only monetization.',
    ],
    "beauty_fashion": [
        'Start with discovery around product-recommendation volume, affiliate-commission ceilings, and paid styling service demand. Position the app as a branded style environment with product catalogs, outfit inspo boards, styling sessions, and member perks—more polished than LTK/Amazon Storefront scatter.',
        'Lead with questions around shade-matching / fit questions, PR-haul repeat views, and conversion to paid consultations. Frame the app as a branded beauty/style space with product vaults, tutorial library, 1:1 virtual styling, and a member feed—more owned than brand-partnership revenue alone.',
    ],
    "media_house": [
        'Role-based media-house contact (Condé Nast / House & Garden channel) — this is a publication, not an individual creator. Frame any outreach as brand-partnership / sponsored-content conversation and skip the creator-app pitch.',
    ],
    "minimalist_creative": [
        'Lead with questions around intimate-performance content, paid session attendance, and converting YouTube viewers into supporters. Frame the app as a branded sessions environment with video archive, early access, and paid community—more durable than YouTube-dependent reach.',
    ],
    "default": [
        'Lead with questions around audience-loyalty depth, monetization beyond YouTube ads, and converting casual followers into paying insiders. Position the app as a branded lifestyle-insider environment with premium feed, member community, and exclusive drops—more owned than platform-dependent revenue.',
        'Start with discovery around fan-relationship depth, repeat-content demand, and the ceiling of affiliate/brand-deal revenue. Frame the app as a branded personal-lifestyle hub with exclusive content, community, and merch/resource drops—stronger than multi-platform sprawl.',
        'Ask about the gap between content impact and recurring revenue, audience retention mechanics, and brand-ownership. Position the app as a branded creator-led environment for paying followers with content vault, community, and member perks—far more controlled than platform-rented audience.',
        'Lead with questions around how much audience value is rented vs. owned, the ceiling of YouTube Partner Program revenue, and what a fan-paid tier would unlock. Frame the app as a branded creator environment with premium content vault, community tier, and merch/resource drops — more owned than platform payouts.',
        'Start with discovery around repeat-viewer behavior, comment-question volume, and converting deep fans into paying insiders. Position the app as a branded lifestyle-member space with subscriber feed, community, and paid drops — tighter than juggling YouTube + Instagram + affiliate links.',
        'Ask about fan-transformation outcomes, parasocial intimacy, and monetization levers beyond ad-share. Frame the app as a branded creator hub with premium episodes, insider community, and paid drops — far more polished than scattered platform presence.',
    ],
}


MUSIC_PROD_SUBS = {
    "beatmaker": [re.compile(r"\bbeat|bpm|trap|lofi|phonk", re.I)],
    "daw_tutorial": [re.compile(r"fl.?studio|tutorial|tricks|tips|ableton|logic\b", re.I)],
    "school": [re.compile(r"school|classroom|academy|course|education", re.I)],
    "studio_production": [re.compile(r"studio|production|records|mvmt|mvmnt", re.I)],
    "software_vendor": [re.compile(r"wondershare|filmora|adobe|serum", re.I)],
}

MUSIC_PROD_LABELS = {
    "beatmaker":         ("Beatmaking & sample / preset packs",
                           "Beatmaker",
                           "Music / production"),
    "daw_tutorial":      ("DAW tutorials & production tricks",
                           "DAW Tutorial / Education",
                           "Music / education"),
    "school":            ("Music school / production academy",
                           "Music School",
                           "Music / education"),
    "studio_production": ("Studio production & artist services",
                           "Studio / Production",
                           "Music / production"),
    "software_vendor":   ("Audio/video software brand",
                           "Software Vendor",
                           "Music / software brand"),
    "default":           ("Music production content (general)",
                           "Music Production (general)",
                           "Music / production"),
}

MUSIC_PROD_ANGLES = {
    "beatmaker": [
        'Start with discovery around beat-pack repeat buyers, tutorial LTV, and the ceiling of BeatStars/Gumroad fee stack. Position the app as a branded producer environment with beat library, sample packs, tutorial tracks, and membership tiers — more polished than a BeatStars + Patreon + YouTube patchwork.',
        'Lead with questions around fan-to-student conversion, preset-pack drops, and producer-mentee communication overhead. Frame the app as a branded producer hub with beat vault, preset library, tutorial progression, and a private producer circle — tighter than running sales on BeatStars and support on Discord.',
        'Ask about repeat producer-students, sample-pack reorder rate, and direct-monetization leverage beyond marketplace fees. Position the app as a branded beatmaker environment with pack library, lessons, and member chat — more owned than platform-dependent payouts.',
    ],
    "daw_tutorial": [
        'Start with discovery around tutorial-to-student conversion, structured-progression demand beyond free YouTube, and DAW-specific bundle sales. Frame the app as a branded DAW-school environment with structured curriculum, projects, quizzes, and a student community — more polished than loose tutorial videos and PDF downloads.',
        'Lead with questions around repeated beginner questions, tutorial-series completion rates, and paid Q&A demand. Position the app as a branded DAW-learning hub with courses, project files, mentor Q&A, and a student channel — far stronger than Discord and scattered Drive links.',
    ],
    "school": [
        'Start with questions about enrollment-funnel friction, student dropoff, and teacher-to-student comms overhead. Position the app as a branded music-school member environment with cohort feeds, assignment tracking, video lessons, and mentor hours — more polished than Zoom + Google Classroom + email.',
        'Lead with questions around cohort identity, practice-accountability, and recurring-enrollment revenue. Frame the app as a branded music-school environment with cohorts, practice logs, live session replays, and a private student circle — tighter than LMS + email patchwork.',
    ],
    "studio_production": [
        'Start with discovery around artist-services pipeline, work-for-hire scheduling, and exclusive-beat sales. Frame the app as a branded studio environment with booking, beat vault, artist client portal, and private community — more controlled than spreadsheet + Gmail + DM workflow.',
        'Lead with questions around collective-brand LTV, tape drops, and artist-mentorship capacity. Position the app as a branded collective/label hub with releases, mentorship sessions, and a member feed — far stronger than scattered Soundcloud + Instagram posting.',
    ],
    "software_vendor": [
        'Role-based vendor support contact (video/audio software brand) — this is a tool company, not a creator. Frame any outreach as brand-partnership / affiliate conversation and skip the creator-app pitch.',
    ],
    "default": [
        'Lead with questions around music-audience loyalty, sample/beat sales reorder rate, and the ceiling of multi-platform revenue. Position the app as a branded music-creator environment with catalog, lessons, and community — more polished than Gumroad + YouTube + Discord patchwork.',
        'Start with discovery around producer-student retention, pack-drop cadence, and converting YouTube viewers into paying members. Frame the app as a branded music-production hub with vault, tutorials, and member feed — more owned than platform-rented distribution.',
    ],
}


# Hand-crafted niche/segment/industry for the 3 newly appended nutrition rows,
# derived from the existing angle_to_take text (already in the file).
NUTRITION_NEW_LABELS = {
    "office@slaviclabs.com": (
        "PL-market diet coaching (Slavic Labs brand)",
        "Diet Coaching (PL)",
        "Nutrition / wellness",
    ),
    "robert@dietfreelife.com": (
        "Diet-Free-Life method & nutrition author",
        "Nutrition Author / Method Creator",
        "Nutrition / wellness",
    ),
    "hello@stephanielong.ca": (
        "Business coaching for nutrition professionals",
        "Nutrition Business Coach",
        "Coaching / nutrition B2B",
    ),
}


def host_of(u: str) -> str:
    try:
        h = urlparse(u or "").netloc.lower()
        return h
    except Exception:
        return ""


def is_social(h: str) -> bool:
    if not h:
        return True
    if h in SOCIAL_HOSTS:
        return True
    for bad in SOCIAL_HOSTS:
        if h.endswith("." + bad):
            return True
    return False


def website_from_source_url(source_url: str) -> str:
    if not source_url:
        return ""
    h = host_of(source_url)
    if not h or is_social(h):
        return ""
    try:
        p = urlparse(source_url)
        scheme = p.scheme or "https"
        return f"{scheme}://{p.netloc}/"
    except Exception:
        return ""


def classify(blob: str, subs: dict) -> str:
    for sub, pats in subs.items():
        for pat in pats:
            if pat.search(blob):
                return sub
    return "default"


def pick_variant(variants: list, key: str) -> str:
    if not variants:
        return ""
    idx = int(hashlib.md5((key or "_").encode()).hexdigest(), 16) % len(variants)
    return variants[idx]


def read_rows(path: Path) -> tuple[list[dict], list[str]]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        r = csv.DictReader(f)
        fn = list(r.fieldnames or [])
        rows = list(r)
    return rows, fn


def write_rows(path: Path, rows: list[dict], fieldnames: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)


def fill_set_only_empty(row: dict, key: str, value: str) -> bool:
    if value and not (row.get(key) or "").strip():
        row[key] = value
        return True
    return False


def process_lifestyle(path: Path) -> dict:
    rows, fn = read_rows(path)
    stats = {"website": 0, "niche": 0, "segment_original": 0, "industry": 0, "angle_to_take": 0}
    for r in rows:
        blob = f"{r.get('handle','').lower()} {r.get('full_name','').lower()} {r.get('raw_context','').lower()}"
        sub = classify(blob, LIFESTYLE_SUBS)
        niche, segment, industry = LIFESTYLE_LABELS[sub]
        angle = pick_variant(LIFESTYLE_ANGLES.get(sub, LIFESTYLE_ANGLES["default"]),
                             r.get("email", "") or r.get("handle", ""))
        website = website_from_source_url(r.get("source_url", ""))

        if fill_set_only_empty(r, "website", website): stats["website"] += 1
        if fill_set_only_empty(r, "niche", niche): stats["niche"] += 1
        if fill_set_only_empty(r, "segment_original", segment): stats["segment_original"] += 1
        if fill_set_only_empty(r, "industry", industry): stats["industry"] += 1
        if fill_set_only_empty(r, "angle_to_take", angle): stats["angle_to_take"] += 1
    write_rows(path, rows, fn)
    return stats


def process_beatmakers(path: Path) -> dict:
    rows, fn = read_rows(path)
    stats = {"website": 0, "niche": 0, "segment_original": 0, "industry": 0, "angle_to_take": 0}
    for r in rows:
        blob = f"{r.get('handle','').lower()} {r.get('full_name','').lower()} {r.get('raw_context','').lower()}"
        sub = classify(blob, MUSIC_PROD_SUBS)
        niche, segment, industry = MUSIC_PROD_LABELS[sub]
        angle = pick_variant(MUSIC_PROD_ANGLES.get(sub, MUSIC_PROD_ANGLES["default"]),
                             r.get("email", "") or r.get("handle", ""))
        website = website_from_source_url(r.get("source_url", ""))

        if fill_set_only_empty(r, "website", website): stats["website"] += 1
        if fill_set_only_empty(r, "niche", niche): stats["niche"] += 1
        if fill_set_only_empty(r, "segment_original", segment): stats["segment_original"] += 1
        if fill_set_only_empty(r, "industry", industry): stats["industry"] += 1
        if fill_set_only_empty(r, "angle_to_take", angle): stats["angle_to_take"] += 1
    write_rows(path, rows, fn)
    return stats


def process_nutrition(path: Path) -> dict:
    """Only fill niche/segment/industry for the 3 newly appended rows
    (existing rows already have full enrichment). Also fill website from source_url
    for any row that is missing it."""
    rows, fn = read_rows(path)
    stats = {"website": 0, "niche": 0, "segment_original": 0, "industry": 0}
    for r in rows:
        email = (r.get("email", "") or "").strip().lower()
        website = website_from_source_url(r.get("source_url", ""))
        if fill_set_only_empty(r, "website", website): stats["website"] += 1
        if email in NUTRITION_NEW_LABELS:
            niche, segment, industry = NUTRITION_NEW_LABELS[email]
            if fill_set_only_empty(r, "niche", niche): stats["niche"] += 1
            if fill_set_only_empty(r, "segment_original", segment): stats["segment_original"] += 1
            if fill_set_only_empty(r, "industry", industry): stats["industry"] += 1
    write_rows(path, rows, fn)
    return stats


def main() -> None:
    csv.field_size_limit(sys.maxsize)

    for name in ["lifestyle", "lifestyle_enriched"]:
        stats = process_lifestyle(DATED / f"{name}.csv")
        print(f"{name}.csv: filled {stats}")

    for name in ["beatmakers", "beatmakers_enriched"]:
        stats = process_beatmakers(DATED / f"{name}.csv")
        print(f"{name}.csv: filled {stats}")

    for name in ["nutrition", "nutrition_enriched"]:
        stats = process_nutrition(DATED / f"{name}.csv")
        print(f"{name}.csv: filled {stats}")


if __name__ == "__main__":
    main()
