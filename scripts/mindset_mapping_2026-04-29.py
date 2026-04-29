"""Per-row mapping for data/2026-04-29/mindset_enriched.csv (12 rows).

Combined-dict format (same as legacy_mapping / mindful_mapping):
  email → {category, niche, segment_original, industry, angle_to_take}

Surfaced via the 6-keyword × 2-page mindset (breathwork + coach) sweep on
2026-04-29 (quota ~1,430, 20 stale-drops by 6-month freshness filter).
Category routing: mindset 8 / fitness 1 / drop 3.
"""

MAPPING: dict[str, dict[str, str]] = {

    "mahendradogneylifecoach@gmail.com": {
        "category": "mindset",
        "niche": "IN Hindi motivational speaker + life coach + podcast — 1000+ live events, rural-India seminars, Tatvam Life brand (Mahendra Dogney, 4.48M)",
        "segment_original": "IN Motivational Speaker + Life Coach (live events)",
        "industry": "Motivational Speaker / Life Coach (B2C + B2B keynote)",
        "angle_to_take": "Mahendra Dogney (4.48M, IN) — India's largest Hindi motivational + life-coach channel running 1000+ live events including rural-India seminars. Frame a branded Tatvam Life app with event-RSVP / livestream surface + cohort program for paid mentees + alumni community — replaces the multi-platform Spotify / Gaana / FB / IG distribution with a single mentee-tier app.",
    },

    # Surface email is Google Play user-support address surfaced from the
    # Korean-language Play Store footer — not Cosmic Kids' actual contact. They
    # also already operate their own Cosmic Kids App on Apple / Android / Roku.
    "gpk-usersupport@google.com": {
        "category": "drop",
        "niche": "Google Play user-support address surfaced from Play Store footer — not creator contact, and Cosmic Kids already runs its own app on iOS/Android/Roku (Cosmic Kids Yoga, 1.94M)",
        "segment_original": "Google Play platform support email (false positive)",
        "industry": "n/a (drop — platform support email)",
        "angle_to_take": "gpk-usersupport@google.com is Google Play's user-support address, not the Cosmic Kids team's. They also already have their own Cosmic Kids App across iOS / Android / Roku. Drop on both grounds.",
    },

    # Akshaya Agnes is a Health & Fitness Coach (IISM) running pilates + yoga +
    # cardio + strength + weights — multi-modal fitness rather than yoga-as-mindset.
    "movewithagnes@gmail.com": {
        "category": "fitness",
        "niche": "CA Health & Fitness Coach (IISM cert) — pilates + yoga + cardio + strength + weights, 15-yr industry vet (Akshaya Agnes, 469K)",
        "segment_original": "CA Multi-Modal Fitness Coach (pilates + strength)",
        "industry": "Fitness Coach (B2C, multi-modal)",
        "angle_to_take": "Akshaya Agnes (469K, CA) — IISM-certified fitness coach blending pilates + yoga + cardio + strength + weights. Frame a branded MoveWithAgnes app with workout-type filter (pilates / cardio / strength) + program calendar + brand-collab inquiry tab — replaces the IG + business-email-only intake she runs today.",
    },

    "yogadeep1909@gmail.com": {
        "category": "yoga",
        "niche": "IN-origin yoga teacher (20+ yrs, based Hanoi) — full classes for all levels, paid promotions + brand collabs across IN/VN (Yoga with Sandeep, 201K)",
        "segment_original": "IN/VN Yoga Teacher + Brand-Collab Creator",
        "industry": "Yoga Teacher (B2C + brand collabs)",
        "angle_to_take": "Yoga with Sandeep (201K) — Indian yoga teacher based in Hanoi running classes + brand-collab pipeline. Frame a branded Yoga with Sandeep app with class-level filter (beginner → advanced) + workshop booking + brand-collab inquiry surface — replaces the WhatsApp + Gmail intake that bottlenecks his collab workflow.",
    },

    "aymindia@gmail.com": {
        "category": "yoga",
        "niche": "IN Rishikesh-based yoga school — 200/300/500-Hr TTC covering Hatha + Ashtanga Vinyasa + Power + Flow + Iyengar (AYM Yoga School, 8.37K)",
        "segment_original": "IN Rishikesh Yoga TTC School (multi-style)",
        "industry": "Yoga TTC School (B2C + TTC)",
        "angle_to_take": "AYM Yoga School (8.37K, IN) — Rishikesh-base TTC across multiple yoga styles. Frame a branded AYM app with TTC cohort surface + style-track selection (Hatha / Ashtanga / Iyengar / etc.) + travel-pickup intake + alumni network — collapses the Indian Yoga Association cross-link + manual phone intake into one TTC-applicant surface.",
    },

    # Psychedelic Support is a B2B / professional-ed platform (CE/CME credit,
    # therapist directory) — not a creator-coach with a method-teaching product.
    "info@psychedelic.support": {
        "category": "drop",
        "niche": "US psychedelic-medicine education + verified-therapist directory + CE/CME credit platform — B2B professional ed, not creator-coach (Psychedelic Support, 7.7K)",
        "segment_original": "US B2B Psychedelic Education Platform",
        "industry": "n/a (drop — B2B platform, not creator)",
        "angle_to_take": "Psychedelic Support (7.7K, US) is a B2B platform connecting verified therapists + offering CE/CME credit. Not a single creator running a method-teaching product. Drop.",
    },

    "contact@intothedeep.info": {
        "category": "mindset",
        "niche": "DE breathwork coach (consciously-connected breathwork + voice dialogue + body-centered healing) + neuroscientist — Ko-fi-backed community (Into The Deep, 6.71K)",
        "segment_original": "DE Breathwork + Body-Centered Healing Coach",
        "industry": "Breathwork Coach (B2C, donation-backed)",
        "angle_to_take": "Into The Deep (6.71K, DE) — neuroscientist + breathwork coach running a Ko-fi-supported community. Frame a branded breathwork app with session-player by intensity + cohort program + biometric (HRV / cold-exposure) log + donation / member tier — replaces Ko-fi-only support with a structured paid offering.",
    },

    "suyashpukale24@gmail.com": {
        "category": "mindset",
        "niche": "IN Marathi-language NLP + EFT certified coach — 1-on-1 personal coaching + online NLP / EFT courses (Suyash NLP in Marathi, 4.34K)",
        "segment_original": "IN Marathi NLP + EFT Coach",
        "industry": "NLP / EFT Coach (B2C, regional)",
        "angle_to_take": "Suyash Pukale (4.34K, IN) — certified NLP + EFT coach teaching in Marathi with 1-on-1 sessions + online courses. Frame a branded app with course modules + EFT-tapping practice player + 1-on-1 booking + WhatsApp-replacement intake — fits the personal-coaching workflow he advertises and gives him a regional-language member surface.",
    },

    "alison@happisoul.com": {
        "category": "mindset",
        "niche": "AU EFT Master Trainer + Matrix Reimprinting — stress / trauma coaching, 15-min discovery call funnel (HappiSoul, 2.52K)",
        "segment_original": "AU EFT Trauma / Stress Coach",
        "industry": "EFT / Stress Coach (B2C + trauma support)",
        "angle_to_take": "HappiSoul / Alison (2.52K, AU) — EFT Master Trainer + Matrix Reimprinting practitioner running a discovery-call funnel. Frame a branded HappiSoul app with EFT-tapping session library + 1-on-1 booking (replacing SimplyBook) + cohort program for stress / trauma + practitioner-cert track — collapses the multi-tool funnel into one paid member surface.",
    },

    "mindsetcoachmaria@gmail.com": {
        "category": "mindset",
        "niche": "US Christian mindset coach — guided visualizations for nervous-system calm + faith-anchored encouragement (Mindset Coach Maria, 1.67K)",
        "segment_original": "US Faith-Anchored Mindset Coach",
        "industry": "Mindset / Visualization Coach (B2C)",
        "angle_to_take": "Mindset Coach Maria (1.67K, US) — Christian mindset coach using guided visualizations + faith framing for nervous-system calm. Frame a branded Maria app with visualization-session player + daily affirmation + faith-anchored journaling prompts — gives a low-clinical-claim member tier appropriate to her disclaimer-heavy positioning.",
    },

    "info@divine-light-yoga.com": {
        "category": "yoga",
        "niche": "GB kids-yoga teacher trainer (Yoga Alliance RCYT) — classroom brain-breaks + behaviour regulation + online Kids Yoga TTC (Divine Light Yoga, 1.47K)",
        "segment_original": "GB Kids Yoga Teacher Trainer (B2B school PD)",
        "industry": "Kids Yoga TTC + School PD (B2B + B2C)",
        "angle_to_take": "Divine Light Yoga (1.47K, GB) — RCYT kids-yoga trainer running TTC + school PD workshops. Frame a branded app with Kids Yoga TTC cohort surface + classroom-resource library (brain breaks / regulation tools) + school-PD booking pipeline — splits B2C parent / teacher resources from B2B school engagement.",
    },

    "helpdesk@coachdeepadivaakar.com": {
        "category": "mindset",
        "niche": "IN dynamic motivational speaker + life / mindset coach for individuals + organizations (Life Coach Deepa Divaakar, 1.04K)",
        "segment_original": "IN Life / Mindset Coach + Corporate Speaker",
        "industry": "Mindset Coach + B2B Keynote (B2C + corporate)",
        "angle_to_take": "Life Coach Deepa Divaakar (1.04K, IN) — life / mindset / motivational coach serving individuals + organizations. Frame a branded Coach Deepa app with 1-on-1 coaching booking + corporate-keynote inquiry tab + cohort mindset-program — clarifies the B2C vs B2B funnel her current single-help-center page can't separate.",
    },
}
