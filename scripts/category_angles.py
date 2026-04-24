"""Apply one category-level angle_to_take per influencer_type.

Seven angles total, one per category. Overwrites angle_to_take for every row
based on influencer_type alone (no per-row or sub-vertical personalization).
Format follows the user's 7-example template:
  "Lead/Start/Ask ... [discovery]. Position/Frame the app as ... — [diff]."
"""

from __future__ import annotations

import csv
from pathlib import Path

MAIN = Path("/home/test1/ABC/Marketing/youtube-crawling/influencer_enriched.csv")


CATEGORY_ANGLES: dict[str, str] = {
    "Lifestyle": (
        "Lead with questions around building their own brand beyond rented platform audiences "
        "and unlocking direct monetization from loyal fans. Position the app as a branded "
        "lifestyle-creator environment with premium content feed, member community, exclusive "
        "drops, and push alerts — so they own both the audience and the revenue inside their "
        "own branded mobile app."
    ),
    "Music Prod": (
        "Lead with questions around music-course retention, paid-subscriber Q&A load, and "
        "own-beat-pack repeat-sale LTV. Position the app as a branded producer environment with "
        "lesson library, paid-member Q&A, beat vault, and private producer community — so they "
        "build their brand and monetize direct instead of renting audience from BeatStars, "
        "Patreon, and YouTube."
    ),
    "Pet Trainer": (
        "Lead with questions around running all client session-booking inside a branded app, "
        "with on-demand courses and paid-client Q&A as natural layers on top. Position the app "
        "as a branded training environment with in-app scheduling, video lessons, and client "
        "Q&A — so trainers own the booking flow and the brand instead of bouncing between "
        "Calendly, Zoom, email, and WhatsApp."
    ),
    "twitch": (
        "Lead with questions around moving paid-subscriber chat, fan community, and exclusive "
        "content into their own branded mobile app. Position the app as a branded streamer fan "
        "environment with subscriber-only chat, member community, and exclusive content — so "
        "they build their personal brand and own the fan relationship instead of depending on "
        "Twitch's shared platform."
    ),
    "finance": (
        "Lead with questions around packaging their own finance know-how into subscriber-only "
        "app content, paid-member Q&A, and a private community. Position the app as a branded "
        "finance-educator environment with course library, paid-member Q&A, subscriber-only "
        "content, and community — so they build their brand and monetize direct instead of "
        "renting audience from Substack, Kajabi, and Patreon."
    ),
    "fitness": (
        "Lead with questions around paid-member retention, workout tracking, and community "
        "engagement across Trainerize / MyFitnessPal / Kajabi. Position the app as a branded "
        "fitness-coach member environment with workout routines, progress tracking, video guides, "
        "and member community — so they build their own coaching brand and stop retention leaks "
        "across five separate tools."
    ),
    "mindful": (
        "Lead with questions around daily-practice retention, subscriber habit formation, and "
        "brand ownership versus Insight Timer or Calm. Position the app as a branded "
        "habit-formation space with a guided player, journal templates, subscriber-only 1:1 "
        "Q&A, habit tracker, and challenge community — so the daily practice lives inside your "
        "brand, not someone else's."
    ),
}


def main() -> None:
    with MAIN.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames or [])
        rows = list(reader)

    if "angle_to_take" not in fieldnames:
        fieldnames.append("angle_to_take")

    unknown = []
    for row in rows:
        itype = (row.get("influencer_type") or "").strip()
        angle = CATEGORY_ANGLES.get(itype)
        if angle is None:
            unknown.append(itype)
            angle = "cost saving"
        row["angle_to_take"] = angle

    with MAIN.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    from collections import Counter
    dist = Counter(r["influencer_type"] for r in rows)
    print(f"Wrote {len(rows)} rows")
    for t, n in sorted(dist.items(), key=lambda x: -x[1]):
        print(f"  {n:>4}  {t}")
    if unknown:
        print(f"\nUnknown types (fell back to 'cost saving'): {set(unknown)}")


if __name__ == "__main__":
    main()
