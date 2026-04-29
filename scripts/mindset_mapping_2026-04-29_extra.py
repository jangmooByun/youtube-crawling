"""Per-row mapping for data/2026-04-29/mindset_enriched_extra.csv (2 rows).

Combined-dict format (same as legacy_mapping / mindful_mapping):
  email → {category, niche, segment_original, industry, angle_to_take}

Surfaced via the 04-29 extra mindset sweep (호흡법 / 마음챙김 / 이완 keywords,
3 keywords × 1 page). Category routing: mindset 1 / yoga 1 (cross-route).
"""

MAPPING: dict[str, dict[str, str]] = {

    "info@studiofleur.co": {
        "category": "mindset",
        "niche": "NL ASMR creator (sleep / meditation / lifestyle / books) — Patreon + Vlog channel @studio-fleur, mental-health + relaxation framing (ASMR Fleur, 101K)",
        "segment_original": "NL ASMR Sleep / Relaxation Creator + Patreon",
        "industry": "ASMR / Relaxation Creator (B2C + Patreon)",
        "angle_to_take": "ASMR Fleur (101K, NL) — ASMR sleep + guided-meditation creator with a vlog spinoff and active Patreon. Frame a branded Studio Fleur app with ASMR session library by intensity + sleep-track player + Patreon-tier replacement (per-tier content access) + book-club reading list — collapses the Patreon + YouTube + Vlog split into one paid member surface anchored on her relaxation niche.",
    },

    # Surfaced by mindset (breathwork) keyword but channel name and primary
    # identity is "Ashtanga Yoga" — Level II Authorized teacher + Yoga Shala
    # studio founder. Cross-route to yoga.
    "krista@theyogashala.com": {
        "category": "yoga",
        "niche": "US (Florida) Level II Authorized Ashtanga Yoga teacher + founder of The Yoga Shala — body mechanics + nervous-system-safe practice + Bodymechanicsmethod sister channel (Yoga with Krista, 91.7K)",
        "segment_original": "US Authorized Ashtanga Yoga Teacher + Studio Founder",
        "industry": "Ashtanga Yoga Teacher + Studio (B2C + studio + practitioner-method)",
        "angle_to_take": "Yoga with Krista / The Yoga Shala (91.7K, US) — Level II Authorized Ashtanga Yoga teacher + Florida studio founder running a body-mechanics + nervous-system-safe Ashtanga method. Frame a branded Yoga Shala app with Ashtanga progression library + Body-Mechanics Method companion track + studio-class booking + newsletter-replacement member tier — collapses theyogashala.com + Bodymechanicsmethod cross-channel into one paid Ashtanga member surface.",
    },
}
