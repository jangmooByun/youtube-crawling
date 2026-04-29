"""Per-row mapping for data/2026-04-29/yoga_enriched_extra.csv (8 rows).

Combined-dict format (same as legacy_mapping / mindful_mapping):
  email → {category, niche, segment_original, industry, angle_to_take}

Surfaced via the 04-29 extra yoga sweep (3 keywords × 1 page, ~600 quota).
Targets Hatha + Kundalini + Vinyasa + yoga TTC. Category routing:
yoga 7 / drop 1.
"""

MAPPING: dict[str, dict[str, str]] = {

    "yogaurmi@gmail.com": {
        "category": "yoga",
        "niche": "International yoga teacher (Ashtanga + Ancient Hatha) — Urmi Yoga Academy with group + 1:1 training, urmipandya.com (Yoga with Urmi Pandya, 834K, IN)",
        "segment_original": "IN International Yoga Teacher (Ashtanga + Ancient Hatha) + Yoga Academy",
        "industry": "Yoga Teacher (B2C, group + 1:1)",
        "angle_to_take": "Yoga with Urmi Pandya (834K, IN) — international yoga teacher running Urmi Yoga Academy with Ashtanga + Ancient Hatha training. Frame a branded Urmi Yoga Academy app with group + 1-on-1 booking + style-track program (Ashtanga vs Ancient Hatha) + alumni community — replaces the urmipandya.com + IG funnel with a structured member surface for the academy.",
    },

    "hallo@charan-amrit-kaur.de": {
        "category": "yoga",
        "niche": "DE Kundalini Yoga teacher + Sat Nam Rasayan healer — 6 yrs of teaching + 20 yrs personal practice, beginner→advanced live practice (Kundalini Yoga Tribe / Charan Amrit Kaur, 10.6K)",
        "segment_original": "DE Kundalini Yoga + Sat Nam Rasayan Healing Teacher",
        "industry": "Kundalini Yoga Teacher (B2C, lineage-rooted)",
        "angle_to_take": "Kundalini Yoga Tribe / Charan Amrit Kaur (10.6K, DE) — certified Kundalini Yoga teacher + Sat Nam Rasayan healer running live practice. Frame a branded Kundalini Yoga Tribe app with live-practice schedule + Sat Nam Rasayan healing session booking + lineage-track program for beginners→advanced — collapses the charan-amrit-kaur.de + live-only model into a German-language member surface.",
    },

    "lotusiyoga@gmail.com": {
        "category": "yoga",
        "niche": "Georgia Kundalini Yoga teacher (Arjan Bakti Kaur lineage) + clinical psychologist + Reiki Master — Georgian-language Kundalini practice + meditation, kundaliniyoga.ge (Marina Kvataia, 6.87K)",
        "segment_original": "GE Kundalini Yoga + Clinical Psychology Practitioner (Georgian-language)",
        "industry": "Kundalini Yoga Teacher + Clinical Psychologist (B2C, regional)",
        "angle_to_take": "Marina Kvataia / Kundaliniyoga.ge (6.87K, GE) — Kundalini yoga teacher + clinical psychologist with 10-yr practice serving Georgian-speaking audience. Frame a branded Marina app with Georgian-language Kundalini practice library + 1-on-1 booking (psychology + Reiki) + Telegram-replacement community surface — collapses the kundaliniyoga.ge + Telegram + Instagram fragmentation into one member tier.",
    },

    "rishikeshyogkulam@gmail.com": {
        "category": "yoga",
        "niche": "IN Rishikesh-base E-RYT 500 yoga teacher (Master D) — 30-min universal sequence + advanced asana, rishikeshyogkulam.com TTC with Italian-language track (Yoga with Master D, 6.72K)",
        "segment_original": "IN Rishikesh Yoga TTC + E-RYT 500 Teacher",
        "industry": "Yoga Teacher + TTC (B2C + TTC)",
        "angle_to_take": "Yoga with Master D / Rishikesh Yogkulam (6.72K, IN) — E-RYT 500 teacher running Rishikesh-based TTC. Frame a branded Rishikesh Yogkulam app with TTC cohort surface + 30-min universal-sequence library + advanced-asana progression track + Italian-track inquiry tab — replaces the rishikeshyogkulam.com + WhatsApp intake with a structured TTC-applicant + alumni surface.",
    },

    "rishikeshvinyasayogaschool@gmail.com": {
        "category": "yoga",
        "niche": "IN Rishikesh Vinyasa Yoga School — 100/200/300-Hr Vinyasa TTC, Yoga Alliance USA RYS 200 accredited (Rishikesh Vinyasa Yoga School, 3.56K)",
        "segment_original": "IN Rishikesh Vinyasa Yoga TTC School",
        "industry": "Yoga TTC School (B2C + TTC)",
        "angle_to_take": "Rishikesh Vinyasa Yoga School (3.56K, IN) — Yoga Alliance-accredited 100/200/300-Hr Vinyasa TTC operator. Frame a branded RVYS app with TTC cohort surface (100/200/300-Hr tracks) + visa/travel intake form + lineage-style Vinyasa progression library + alumni network — replaces the rishikeshvinyasayogaschool.com + phone intake with a single TTC-applicant + alumni member surface.",
    },

    "info@yogimukesh.com": {
        "category": "yoga",
        "niche": "HU-listed yoga TTC operator running 200/300-Hr training in India, Bali, Europe — multi-region TTC (Bindusar yoga / Yogi Mukesh, 3.09K)",
        "segment_original": "HU Multi-Region Yoga TTC Operator (IN + Bali + EU)",
        "industry": "Yoga TTC School (B2C + TTC, multi-region)",
        "angle_to_take": "Bindusar yoga / Yogimukesh (3.09K, HU) — multi-region TTC operator (India / Bali / Europe). Frame a branded Yogimukesh app with TTC cohort surface (location filter India / Bali / Europe) + visa-and-travel logistics tab + alumni map — replaces the email-only intake bottlenecking the multi-region TTC pipeline.",
    },

    # Spiritual ashram + lineage foundation, not a creator-coach. Org-led with
    # role-based inbox; founded by Siddha Yogi Sri Nageswara Maharshi since 1995.
    "sivasiddhi@sivasiddhikundaliniyoga.org": {
        "category": "drop",
        "niche": "IN Vijayawada-base spiritual ashram (Siva Siddhi Kundalini Yoga Foundation) — Siddha Yogi Sri Nageswara Maharshi lineage initiation since 1995, organization-led not creator-coach (1.54K)",
        "segment_original": "IN Spiritual Ashram / Lineage Foundation (org-led)",
        "industry": "n/a (drop — ashram organization, not creator-coach)",
        "angle_to_take": "Siva Siddhi Kundalini Yoga Foundation (1.54K, IN) is a Vijayawada-base spiritual ashram running 30+ years of lineage initiation under Siddha Yogi Sri Nageswara Maharshi. Org-led with role-based inbox, not creator-coach. Drop.",
    },

    "satyayogaashram@gmail.com": {
        "category": "yoga",
        "niche": "FR-base (with Rishikesh + Sri Lanka campuses) Satya Yoga Ashram — bilingual FR+EN 100/200/300-Hr TTC across Hatha + Kundalini + Mantra Yoga, Yoga Alliance certified (Satya Yoga Ashram, 1.48K)",
        "segment_original": "FR Multi-Style Yoga TTC (Rishikesh + France + Sri Lanka)",
        "industry": "Yoga TTC School (B2C + TTC, bilingual)",
        "angle_to_take": "Satya Yoga Ashram (1.48K, FR) — bilingual (FR+EN) Yoga TTC across Rishikesh + France + Sri Lanka campuses. Frame a branded Satya Yoga app with TTC cohort surface (campus filter + style filter Hatha/Kundalini/Mantra) + bilingual content library + retreat booking — replaces satyayogaashram.com + phone intake with a structured multi-campus TTC-applicant surface.",
    },
}
