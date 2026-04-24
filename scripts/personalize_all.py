"""Personalize angle_to_take for every row in influencer_enriched.csv.

Strategy:
- Merge: 5 _all_enriched.csv → (email → personalized_angle) dict, apply first
- Fallback: username keyword sub-vertical classification with round-robin
  variants so rows in same sub-vertical get different angles

Format (matches user's 7-example template):
  "Lead with/Start with/Ask about [discovery]. Position/Frame the app as
  [positioning] with [features 3-5] — [differentiator vs patchwork]."
"""

from __future__ import annotations

import csv
import hashlib
import re
from pathlib import Path

MAIN = Path("/home/test1/ABC/Marketing/youtube-crawling/influencer_enriched.csv")
ENRICHED_FILES = [
    Path("/home/test1/ABC/Marketing/youtube-crawling/my-data/productivity_all_enriched.csv"),
    Path("/home/test1/ABC/Marketing/youtube-crawling/my-data/fitness_all_enriched.csv"),
    Path("/home/test1/ABC/Marketing/youtube-crawling/my-data/mindful_all_enriched.csv"),
    Path("/home/test1/ABC/Marketing/youtube-crawling/my-data/finance_all_enriched.csv"),
    Path("/home/test1/ABC/Marketing/youtube-crawling/data/nutrition_all_enriched.csv"),
]


def load_personalized() -> dict[str, str]:
    out: dict[str, str] = {}
    for p in ENRICHED_FILES:
        with p.open(encoding="utf-8") as f:
            for r in csv.DictReader(f):
                email = (r.get("email") or "").strip().lower()
                angle = (r.get("angle_to_take") or "").strip()
                if email and angle and angle != "cost saving":
                    out[email] = angle
    return out


LIFESTYLE_SUBS = {
    "home_decor": [
        re.compile(r"home.?decor|decorat|interior|apartment|house.?tour|homedec|\bdecor\b", re.I),
    ],
    "vlog": [
        re.compile(r"\bvlog|daily\b|routine", re.I),
    ],
    "study": [
        re.compile(r"\bstudy\b|productiv|notion", re.I),
    ],
    "minimal": [
        re.compile(r"minimal|\bmnml\b|simpl|zen", re.I),
    ],
    "travel": [
        re.compile(r"travel|tiny.?house|rv\b|nomad", re.I),
    ],
    "beauty_fashion": [
        re.compile(r"beauty|makeup|fashion|style\b|outfit|chic", re.I),
    ],
    "minimalist_creative": [
        re.compile(r"\bapartment sessions\b|creative", re.I),
    ],
    "media_house": [
        re.compile(r"condenast|houseandgarden|subscription\.co", re.I),
    ],
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
    "beatmaker": [
        re.compile(r"\bbeat|bpm|trap|lofi|phonk", re.I),
    ],
    "daw_tutorial": [
        re.compile(r"fl.?studio|tutorial|tricks|tips|ableton|logic\b", re.I),
    ],
    "school": [
        re.compile(r"school|classroom|academy|course|education", re.I),
    ],
    "studio_production": [
        re.compile(r"studio|production|records|mvmt|mvmnt", re.I),
    ],
    "software_vendor": [
        re.compile(r"wondershare|filmora|adobe|serum", re.I),
    ],
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


PET_TRAINER_ANGLES = [
    'Lead with questions around client follow-through between sessions, video-feedback load, and group-class vs. 1:1 monetization ceilings. Position the app as a branded training companion with training logs, video review, session scheduling, and a client portal — more polished than Zoom + email + WhatsApp follow-ups.',
    'Start with discovery around puppy-class retention, behavior-case documentation, and converting YouTube viewers into paying clients. Frame the app as a branded dog-training environment with training plans, progress photos/video, and mentor chat — tighter than spreadsheets + text threads.',
    'Ask about owner-accountability between lessons, program graduation rates, and the limits of a 1:1 private-consult model. Position the app as a branded K9-training member space with progress tracking, video assignments, and community Q&A — far stronger than a patchwork of Google Drive and text.',
    'Start with discovery around reactive-dog cases, alumni-client churn, and course-pricing ceiling vs. 1:1. Frame the app as a branded training-course environment with video modules, owner homework, private Q&A, and mentor hours — more polished than Thinkific + Zoom + Messenger patchwork.',
    'Lead with questions around trainer-reputation moat, paid-community demand, and turning educational YouTube fans into graduates. Position the app as a branded dog-training member environment with courses, progress tracking, mentor office hours, and alumni community — tighter than scattered LMS + social stack.',
]


TWITCH_SUBS = {
    "art": [
        re.compile(r"ink|draw|paint|\bart\b|sketch|doodle|canvas", re.I),
    ],
    "music": [
        re.compile(r"music|song|beat(?!s?moo)|singer|piano|drum", re.I),
    ],
    "gaming_heavy": [
        re.compile(r"game|gaming|play|ranked|fps|\bpro\b|clutch|sniper|fortnite|valorant|apex|\bow\b|mmr", re.I),
    ],
    "asmr_chill": [
        re.compile(r"asmr|chill|sleep|calm|\bzen\b|soft", re.I),
    ],
    "irl_variety": [
        re.compile(r"\birl\b|variety|chat|talk|just\s?chat", re.I),
    ],
    "cosplay_vtuber": [
        re.compile(r"cosplay|vtuber|\bkawaii\b|\bmoe\b|\bchan\b|\buki\b|vtub", re.I),
    ],
}

TWITCH_ANGLES = {
    "art": [
        'Lead with questions around commission-queue management, livestream-to-portfolio conversion, and the ceiling of tip-based support. Position the app as a branded art-studio space with commission intake, portfolio gallery, timelapse archive, and member tipping — more polished than juggling Patreon, Ko-fi, and Twitch subs.',
        'Start with discovery around art-drop timing, print-on-demand bottlenecks, and viewer-to-patron conversion. Frame the app as a branded artist hub with work-in-progress feed, commission forms, print store, and private collector chat — tighter than Instagram + Etsy + Patreon stack.',
        'Ask about commission-client retention, WIP preview pricing, and monetizing the stream archive. Position the app as a branded artist-member environment with WIP feeds, sketch drops, commission forms, and a collector tier — far stronger than Twitch subs + Ko-fi tip jar alone.',
    ],
    "music": [
        'Lead with questions around live-performance monetization, setlist-repeat demand, and converting Twitch viewers into paying fans. Frame the app as a branded music-creator environment with live-stream VOD archive, release drops, tipping, and fan community — more polished than Twitch + Spotify + Patreon scatter.',
        'Start with discovery around fan-concert attendance intent, merch-timing, and the gap between viewer loyalty and direct revenue. Position the app as a branded musician fan hub with album drops, live replay, and a private community — stronger than platform-dependent monetization.',
        'Ask about set-list repeat value, release-drop conversion, and pre-release listener intent. Frame the app as a branded musician fan space with early tracks, tipping, and listener community — more owned than splitting audience across Spotify, Twitch, and Patreon.',
    ],
    "gaming_heavy": [
        'Lead with questions around sub-retention, coaching-side-hustle capacity, and how the StreamElements / Throne / Merch stack holds together. Position the app as a branded streamer fan environment with go-live alerts, merch, coaching booking, and sub perks — more polished than a patchwork of third-party tools.',
        'Start with discovery around community-Discord noise, sponsor-fit, and converting casual viewers into paying subs. Frame the app as a branded gaming-creator hub with private community, coaching slots, merch store, and live alerts — tighter than Twitch + Discord + StreamElements scatter.',
        'Ask about raid retention, sub-tier differentiation, and a dedicated home for fan-only content. Position the app as a branded gaming fan space with exclusive vods, coaching booking, merch, and community — far stronger than relying on Twitch subs alone.',
        'Start with discovery around coaching demand from viewers, ranked-session bookings, and tournament-team logistics. Frame the app as a branded gaming pro hub with coaching booking, clip archive, and a member tier — more polished than Calendly + Discord + Twitch patchwork.',
        'Lead with questions around sub-tier perks, gameplay VOD archive usage, and fan-favorite clip monetization. Position the app as a branded gaming creator space with clip vault, coaching slots, and tipping — tighter than Twitch + YouTube + Ko-fi sprawl.',
    ],
    "asmr_chill": [
        'Lead with questions around sleep-session repeat usage, soft-content retention, and converting ad-revenue fatigue into direct fan support. Frame the app as a branded calm-content environment with session library, sleep mode, private community, and member tips — more polished than ad-dependent streaming.',
        'Start with discovery around nightly-routine habit formation, audience wellness outcomes, and monetization beyond Twitch subs. Position the app as a branded ASMR/chill space with archives, tier perks, and intimate community — far stronger than platform-only delivery.',
        'Ask about late-night cadence, fan-sleep routine dependency, and direct-support conversion. Frame the app as a branded calm-stream space with sleep-mode replays, tier perks, and a quiet community feed — more intimate than public Twitch chat.',
    ],
    "irl_variety": [
        'Lead with questions around chat-community identity, loyalty depth, and tip-jar vs. sub LTV. Position the app as a branded variety-streamer fan space with private chat, tip perks, exclusive stream archive, and member-only IRL drops — tighter than Twitch + Discord + Ko-fi stack.',
        'Start with discovery around viewer-to-paying-fan conversion, branded merch sales, and private-community stickiness. Frame the app as a branded IRL-creator hub with archive, merch, and members-only chat — more owned than platform-rented audience.',
        'Ask about just-chatting loyalty, VIP-fan identity, and merch-drop repeat rate. Position the app as a branded variety fan space with inside-joke feed, merch drops, and premium tier — far stronger than scattered Twitch + Discord integrations.',
    ],
    "cosplay_vtuber": [
        'Lead with questions around character-identity retention, cosplay/merch drops, and superfan conversion beyond Twitch Bits. Frame the app as a branded vtuber/cosplay fan space with exclusive clips, merch drops, and private fan community — more polished than Twitch + Throne + Merchline scatter.',
        'Start with discovery around persona-driven content cadence, donation rituals, and converting casual viewers to core supporters. Position the app as a branded vtuber/cosplay hub with exclusive streams, fan alerts, and member-only drops — far stronger than platform-dependent support.',
    ],
    "default": [
        'Lead with questions around StreamElements / Throne / Merch stack coherence, sub retention, and converting fan loyalty into real LTV. Position the app as a branded streamer fan environment with live alerts, merch, tipping, and private community — more polished than the usual third-party patchwork.',
        'Start with discovery around Bits/Subs rhythm, Discord noise, and monetization beyond Twitch payouts. Frame the app as a branded streamer hub with exclusive VODs, merch, and members-only space — tighter than Twitch + Discord + StreamElements sprawl.',
        'Ask about super-fan identification, sub-tier differentiation, and whether the current tool stack captures LTV. Position the app as a branded streamer environment with fan alerts, merch store, tip perks, and exclusive community — far stronger than a scattered integration list.',
        'Lead with questions around how much of each dollar leaves through Twitch / Patreon / Throne fees and how to pull that LTV in-house. Position the app as a branded creator-owned fan hub with alerts, merch, tipping, and private community — tighter than a third-party bolt-on stack.',
        'Start with discovery around hyped-drop moments (new emote, merch launch, charity stream) and whether fans have a home to rally around between them. Frame the app as a branded fan HQ with drop calendar, merch, and member-only replays — more durable than Twitch-only attention.',
        'Ask about follower-to-sub conversion funnel, lapsed-sub win-back, and the role of branded merch in fan identity. Position the app as a branded streamer fan environment with retention levers, merch store, and exclusive content — far stronger than Twitch default tools.',
        'Lead with questions around branded-fan identity, insider-joke culture, and whether fan-only content lives anywhere controllable. Frame the app as a branded streamer fan home with exclusive clips, merch, and member feed — more polished than Discord + Twitch fragmentation.',
        'Start with discovery around mod-team load, Discord spam, and keeping top fans close without burning out. Position the app as a branded fan space with tiered access, light community tools, and merch — tighter than running Discord as a community substitute.',
    ],
}


def classify_lifestyle(username: str, email: str) -> str:
    blob = f"{username.lower()} {email.lower()}"
    for sub, pats in LIFESTYLE_SUBS.items():
        for p in pats:
            if p.search(blob):
                return sub
    return "default"


def classify_music_prod(username: str, email: str) -> str:
    blob = f"{username.lower()} {email.lower()}"
    for sub, pats in MUSIC_PROD_SUBS.items():
        for p in pats:
            if p.search(blob):
                return sub
    return "default"


def classify_twitch(username: str, email: str) -> str:
    blob = f"{username.lower()} {email.lower()}"
    for sub, pats in TWITCH_SUBS.items():
        for p in pats:
            if p.search(blob):
                return sub
    return "default"


def pick_variant(variants: list[str], key: str) -> str:
    idx = int(hashlib.md5(key.encode()).hexdigest(), 16) % len(variants)
    return variants[idx]


def personalize(row: dict, personalized: dict[str, str]) -> str:
    email = (row.get("email") or "").strip().lower()
    itype = (row.get("influencer_type") or "").strip()
    username = row.get("username") or ""

    if email in personalized:
        return personalized[email]

    key = email or username

    if itype == "Lifestyle":
        sub = classify_lifestyle(username, email)
        variants = LIFESTYLE_ANGLES.get(sub, LIFESTYLE_ANGLES["default"])
        return pick_variant(variants, key)

    if itype == "Music Prod":
        sub = classify_music_prod(username, email)
        variants = MUSIC_PROD_ANGLES.get(sub, MUSIC_PROD_ANGLES["default"])
        return pick_variant(variants, key)

    if itype == "Pet Trainer":
        return pick_variant(PET_TRAINER_ANGLES, key)

    if itype == "twitch":
        sub = classify_twitch(username, email)
        variants = TWITCH_ANGLES.get(sub, TWITCH_ANGLES["default"])
        return pick_variant(variants, key)

    return row.get("angle_to_take") or "cost saving"


def main() -> None:
    personalized = load_personalized()
    print(f"Loaded {len(personalized)} personalized angles from _all enriched files")

    with MAIN.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames or [])
        rows = list(reader)

    if "angle_to_take" not in fieldnames:
        fieldnames.append("angle_to_take")

    merged_count = 0
    fallback_count = 0
    from collections import Counter
    dist: Counter = Counter()

    for row in rows:
        email = (row.get("email") or "").strip().lower()
        new_angle = personalize(row, personalized)
        row["angle_to_take"] = new_angle
        if email in personalized:
            merged_count += 1
        else:
            fallback_count += 1
        dist[(row.get("influencer_type"), new_angle[:60])] += 1

    with MAIN.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Total rows: {len(rows)}")
    print(f"  merged from _all: {merged_count}")
    print(f"  fallback sub-vertical: {fallback_count}")
    print()
    print("Variant usage (top repetitions):")
    for (t, prefix), n in dist.most_common(15):
        print(f"  {n:>4}  [{t}] {prefix}...")


if __name__ == "__main__":
    main()
