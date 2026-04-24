"""Enrich influencer.csv with segment_original / industry / angle_to_take columns.

Classifies each row based on influencer_type + username heuristics (for broad
Lifestyle rows). Writes a new CSV next to the input.

angle_to_take is written in English as a long-form narrative (observation →
observation → insight → proposal) since targets are US/CA/AU/NZ creators.
"""

from __future__ import annotations

import csv
from pathlib import Path


TWITCH_ANGLE = (
    "We noticed most streamers stitch together StreamElements, StreamLabs, Throne, and other "
    "third-party tools to monetize — the intent is clearly there, but the experience is "
    "fragmented across half a dozen dashboards. At the same time, fans send Bits, Subs, and "
    "donations and you're actively selling merch, so the real leverage is maximizing LTV "
    "through a tighter fan relationship, not chasing new viewers. The catch: when you're live "
    "8+ hours a day, designing a unified fan app between streams isn't happening. That's why "
    "we ship streamer template apps (fan alerts, go-live notifications, merch store, private "
    "community) in 7 days."
)

MUSIC_PROD_ANGLE = (
    "We noticed many beat producers run Gumroad, BeatStars, Patreon, and Kajabi in parallel — "
    "multiple revenue streams are working, but scattered across four platforms means fans "
    "never get one branded home. At the same time, fans rewatch tutorials and keep coming back "
    "for new beat packs, so the real LTV lever is repeat consumption and learning progress "
    "tracking. The catch: producing beats and recording lessons every day leaves no bandwidth "
    "to design an app. That's why we ship beat-producer template apps (beat pack library, "
    "tutorial progress tracking, preset drops, membership) in 7 days."
)

PET_TRAINER_ANGLE = (
    "We noticed many trainers combine Thinkific/Kajabi, Patreon, and Zoom to run online "
    "programs — the intent to scale beyond in-person is strong, but the client experience is "
    "split across too many tools. At the same time, dog parents want to track progress on "
    "video and you spend real hours on individualized feedback, so the winning structure is "
    "one space: training logs, video review, and 1:1 feedback together. The catch: training, "
    "filming, and client calls already fill your day. That's why we ship trainer template apps "
    "(training logs, video coaching, scheduling, client portal) in 7 days."
)

FINANCE_ANGLE = (
    "We noticed many finance creators run Substack/Beehiiv newsletters, Thinkific/Kajabi "
    "courses, and Patreon memberships side by side — the audience values the education, but "
    "LTV is hard to track across four platforms. At the same time, subscribers build their own "
    "budget trackers in spreadsheets or third-party apps, so there's real demand for a branded "
    "money-management app under your name. The catch: analyzing markets and writing "
    "newsletters daily leaves no cycles to spec an app. That's why we ship finance template "
    "apps (budget sync, challenge trackers, course access, community) in 7 days."
)

FITNESS_ANGLE = (
    "We noticed many fitness coaches layer Trainerize, MyFitnessPal, Instagram, Kajabi, and "
    "Teachable to run paid programs — acquisition is working, but retention leaks because "
    "workouts, videos, and community live in different places. At the same time, members want "
    "to log workouts, track nutrition, and cheer each other on inside one app, so the "
    "retention lever is a branded app under your name. The catch: training, filming, and "
    "editing already fill your day. That's why we ship fitness-coach template apps (workout "
    "routines, progress tracking, video guides, member community) in 7 days."
)

MINDFUL_ANGLE = (
    "We noticed many meditation and yoga creators either contribute to Insight Timer/Calm or "
    "distribute guided sessions via Patreon, Kajabi, and Substack — the audience forms habits, "
    "but the value accrues to third-party apps, not your brand. At the same time, "
    "practitioners return daily for meditations, journaling, and sleep stories, so a branded "
    "habit-tracker and guided-session app drives reorder and subscription retention. The "
    "catch: recording sessions and running workshops leaves no engineering time. That's why "
    "we ship mindfulness template apps (guided player, journal templates, habit tracker, "
    "challenge community) in 7 days."
)

HOME_DECOR_ANGLE = (
    "We noticed many home-decor creators run Pinterest, Instagram, Amazon Storefront, and LTK "
    "together — followers will spend based on your taste, but affiliate links are the ceiling "
    "of what you capture today. At the same time, followers keep asking \"where's the sofa "
    "from?\" and requesting checklists and moodboards, so a branded catalog and moodboard app "
    "is obvious leverage for affiliate conversion and paid consulting. The catch: shooting, "
    "styling, and editing leave no time to design an app. That's why we ship home-decor "
    "template apps (style catalog, moodboards, shop link hub, 1:1 consult booking) in 7 days."
)

STUDY_ANGLE = (
    "We noticed many study and productivity creators monetize through Notion template sales, "
    "Gumroad, Patreon, and YouTube ads — learners will pay for your workflow, but there's a "
    "ceiling to what duplicated Notion templates deliver. At the same time, fans use timers, "
    "planners, and checklists daily as routines, so a branded study-tracker and course app is "
    "the retention lever. The catch: filming study videos and building Notion templates "
    "already fill your days. That's why we ship study/productivity template apps (study timer, "
    "habit tracker, template marketplace, progress reports) in 7 days."
)

MINIMALISM_ANGLE = (
    "We noticed many minimalism coaches combine blogs, newsletters, challenge PDFs, and "
    "Thinkific courses — there's a paying audience for lifestyle transformation, but the "
    "habit-formation step after content consumption is missing. At the same time, fans "
    "complete 30-day challenges and declutter checklists while wanting peer support, so a "
    "branded challenge and habit app is the core of retention and subscription conversion. "
    "The catch: writing, filming, and running workshops leave no time to spec an app. That's "
    "why we ship minimal-lifestyle template apps (challenge tracker, declutter checklists, "
    "habit logging, group community) in 7 days."
)

DAILY_VLOG_ANGLE = (
    "We noticed many daily-vlog creators juggle Instagram, YouTube, TikTok, and LTK — follower "
    "loyalty is strong, but every dollar depends on platform ads and affiliate clicks, with "
    "no direct monetization lever. At the same time, fans keep asking \"what did you eat "
    "today?\" and \"show me the BTS,\" so a premium fan-community app is the only path to "
    "converting loyalty into revenue you own. The catch: filming, editing, and uploading "
    "back-to-back leave no room for app development. That's why we ship vlog template apps "
    "(premium feed, BTS content, paid community, push alerts) in 7 days."
)

LIFESTYLE_GENERAL_ANGLE = (
    "We noticed many lifestyle creators stack YouTube, Instagram, affiliate marketing, and "
    "brand deals — the community is strong, but income sits at the mercy of ad rates and "
    "affiliate commissions, so you're not in control of the upside. At the same time, "
    "followers come back for your routines, product picks, and everyday advice, so a branded "
    "app converting fans into paid subscribers is the clearest axis for real diversification. "
    "The catch: planning, shooting, and editing content leave no time to design an app. "
    "That's why we ship lifestyle template apps (premium subscription feed, recommendation "
    "catalog, community, notifications) in 7 days."
)


MAPPING = {
    "Music Prod": (
        "Creator-Educator",
        "Music Production / Beat Making",
        MUSIC_PROD_ANGLE,
    ),
    "Pet Trainer": (
        "Coach",
        "Dog Training / Pet Care",
        PET_TRAINER_ANGLE,
    ),
    "finance": (
        "Creator-Educator",
        "Personal Finance",
        FINANCE_ANGLE,
    ),
    "fitness": (
        "Creator-Coach",
        "Fitness / Personal Training",
        FITNESS_ANGLE,
    ),
    "mindful": (
        "Creator-Coach",
        "Meditation / Yoga / Wellness",
        MINDFUL_ANGLE,
    ),
    "twitch": (
        "Creator",
        "Live Streaming / Gaming",
        TWITCH_ANGLE,
    ),
}


def classify_lifestyle(username: str, email: str) -> tuple[str, str, str]:
    u = (username or "").lower()
    e = (email or "").lower()
    blob = u + " " + e

    if any(k in blob for k in ["home decor", "home-decor", "homedecor", "decorat", "interior", "apartment", "decor", "house"]):
        return ("Creator-Solopreneur", "Home Decor / Interior Design", HOME_DECOR_ANGLE)
    if any(k in blob for k in ["study", "productiv", "notion", "be prroductive"]):
        return ("Creator-Educator", "Study / Productivity", STUDY_ANGLE)
    if "minimal" in blob:
        return ("Creator-Coach", "Minimalism / Lifestyle Coaching", MINIMALISM_ANGLE)
    if any(k in blob for k in ["vlog", "daily", "lifestyletales", "random lifestyle"]):
        return ("Creator", "Daily Vlog / Lifestyle", DAILY_VLOG_ANGLE)
    return ("Creator", "Lifestyle (general)", LIFESTYLE_GENERAL_ANGLE)


def enrich_row(row: dict) -> dict:
    itype = (row.get("influencer_type") or "").strip()
    username = row.get("username") or ""
    email = row.get("email") or ""

    if itype in MAPPING:
        seg, ind, angle = MAPPING[itype]
    elif itype == "Lifestyle":
        seg, ind, angle = classify_lifestyle(username, email)
    else:
        seg, ind, angle = ("Creator", "Unknown", "Evaluate manually")

    row["segment_original"] = seg
    row["industry"] = ind
    row["angle_to_take"] = angle
    return row


def main() -> None:
    src = Path("/home/test1/ABC/Marketing/youtube-crawling/influencer_real.csv")
    dst = Path("/home/test1/ABC/Marketing/youtube-crawling/influencer_enriched.csv")

    with src.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        rows = [enrich_row(dict(r)) for r in reader]
        fieldnames = list(reader.fieldnames or []) + ["segment_original", "industry", "angle_to_take"]

    with dst.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"wrote {len(rows)} rows → {dst}")


if __name__ == "__main__":
    main()
