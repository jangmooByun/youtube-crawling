"""Per-row mapping for data/2026-04-28/meditation_enriched.csv (21 rows).

Combined-dict format (same as legacy_mapping / mindful_mapping):
  email → {category, niche, segment_original, industry, angle_to_take}

All 21 rows discovered via the meditation-keyword sweep on 2026-04-28
(quota ~1040). Category distribution: meditation 19 / mindset 1 / drop 1.
"""

MAPPING: dict[str, dict[str, str]] = {

    # IN Tamil "Anatomic therapy" health speaker — not pure meditation; broad
    # health/wellness lectures. Off-topic for meditation bucket.
    "onestoneninemango@gmail.com": {
        "category": "drop",
        "niche": "IN Tamil 'Anatomic therapy' alt-health / wellness speaker (Healer Baskar) — non-profit org, broad health lectures",
        "segment_original": "IN Alt-Health Speaker (off-topic)",
        "industry": "n/a (drop)",
        "angle_to_take": "Healer Baskar — Tamil alt-health speaker behind Anatomic Therapy non-profit. Not a coaching creator with a paid offer; off-topic for meditation. Drop.",
    },

    "support@shaolin.online": {
        "category": "meditation",
        "niche": "DE Shaolin Temple Europe founder — Shaolin / Zen practice, body-mind unity, internal+external strength (Shi Heng Yi, 659K)",
        "segment_original": "DE Shaolin / Zen Master (online courses)",
        "industry": "Meditation Teacher (Zen / Shaolin)",
        "angle_to_take": "Shi Heng Yi (659K, DE) — Shaolin Temple Europe founder with global Shaolin Online courses. Frame a branded Shaolin-Online app with daily-practice calendar (sit / move / 5 hindrances tracking) + course library + retreat schedule — replaces patchwork Vimeo/Stripe/Mailchimp stack with branded member tier.",
    },

    "contact@newhorizonholisticcentre.co.uk": {
        "category": "meditation",
        "niche": "GB guided meditations + sleep stories for adults & kids, used by parents/teachers/therapists worldwide (New Horizon, 415K)",
        "segment_original": "GB Sleep Meditation + Guided Meditation Brand",
        "industry": "Meditation Audio Brand (B2C)",
        "angle_to_take": "New Horizon (415K, GB) — large guided-meditation + sleep-stories brand serving adults + kids. Frame a branded New-Horizon app with audio-player + bedtime-mode toggle + age-tier (kids/adult) + length filter — clear product fit for an audio-meditation creator at this scale.",
    },

    "ananddwivedi0369@gmail.com": {
        "category": "mindset",
        "niche": "IN writer/musician/artist + spiritual-development educator for teachers (Anand Dwivedi, APV Holistic Education founder, 124K)",
        "segment_original": "IN Spiritual Education / Holistic-Ed Founder",
        "industry": "Spiritual Education / Personal Development",
        "angle_to_take": "Anand Dwivedi (124K, IN) — APV Holistic Education founder. Frame a branded Anand app for educator-cohort spiritual-development with module-based course structure + reflective-journaling prompt + community tier — fits his teacher-focused audience.",
    },

    "info@carolinemccready.com": {
        "category": "meditation",
        "niche": "GB meditation teacher since 2011 — deep relaxation + breathwork + effortless-focus practice (Caroline McCready, 96.4K)",
        "segment_original": "GB Online Meditation Teacher (relaxation focus)",
        "industry": "Meditation Teacher (online)",
        "angle_to_take": "Caroline McCready (96.4K, GB) — 14-yr meditation teacher with relaxation + breathwork emphasis. Frame a branded Caroline app with daily-relaxation calendar + breath-pacer integration + member-tier subscription — replaces YouTube-only delivery with a paid daily-ritual surface.",
    },

    "info@jackkornfield.com": {
        "category": "meditation",
        "niche": "US Western mindfulness icon — Buddhist monk training + clinical-psych PhD + co-founder Insight Meditation Society + Spirit Rock (Jack Kornfield, 57.9K — duplicate of mindful row, will dedup)",
        "segment_original": "US Buddhist Mindfulness Teacher + Author + Founder",
        "industry": "Meditation Teacher (Buddhist / clinical-mindfulness)",
        "angle_to_take": "Jack Kornfield — Western mindfulness elder + co-founder of IMS + Spirit Rock. Pitch a branded Jack-Kornfield app with archival dharma talks library + retreat scheduling + member-tier subscription. Approach via info@ as a brand-extension play.",
    },

    "digital@silvamethod.com": {
        "category": "meditation",
        "niche": "US Silva Method International — Jose Silva's signature meditation method + healing + manifestation (Silva Method Official, 34.6K)",
        "segment_original": "US Silva Method Brand (legacy method)",
        "industry": "Meditation Method / Brand",
        "angle_to_take": "Silva Method Official (34.6K, US) — long-running Jose Silva meditation method brand. Frame a branded Silva-Method app with signature technique guides (Centering / Mental Screen / Mirror of the Mind) + course-library + alumni community — replaces fragmented course delivery with single brand-coherent member surface.",
    },

    "englishbuddhistmonk@gmail.com": {
        "category": "meditation",
        "niche": "GB-born Theravada Buddhist Monk Bhante Dhammarakkhita (English Buddhist Monk, 29K) — based across India/Thailand/Sri Lanka",
        "segment_original": "GB Theravada Buddhist Monk",
        "industry": "Meditation Teacher (Theravada)",
        "angle_to_take": "Bhante Dhammarakkhita (29K, GB) — English Theravada monk teaching from monastic settings. Frame a branded app with dharma-talks library + sutta study modules + dāna-flow donation tier (monastic-appropriate monetization) — fits monastic financial model better than Patreon.",
    },

    "gratitude@insightmeditationcenter.org": {
        "category": "meditation",
        "niche": "IMC gratitude / dāna inbox — community Vipassana / mindfulness Buddhist center (Gil Fronsdal + Andrea Fella, 28.8K — duplicate channel from mindful, additional email)",
        "segment_original": "US IMC dāna / gratitude inbox",
        "industry": "Meditation Center (Buddhist / Vipassana)",
        "angle_to_take": "IMC dāna / gratitude inbox — donation-flow contact. Branded IMC sangha app with built-in dāna donation flow + member tier + sub-sangha sub-spaces (queer / Asian-heritage / family / Earthcare / Eightfold Path) — preserves IMC's actual community structure.",
    },

    "contact@lbc.org.uk": {
        "category": "meditation",
        "niche": "GB London Buddhist Centre — Buddhism + meditation classes globally + Dharma talks (London Buddhist Centre, 24K)",
        "segment_original": "GB Buddhist Center (online + in-person)",
        "industry": "Meditation Center (Buddhist)",
        "angle_to_take": "London Buddhist Centre (24K, GB) — major UK Buddhist center with online + in-person classes. Frame a branded LBC app combining live-class calendar + Dharma talks library + retreat sign-up + global-sangha tier — fits the hybrid online-offline center structure.",
    },

    "support@breakthroughapps.io": {
        "category": "meditation",
        "niche": "US 'Chill Pill with Yogi Bryan' meditation app + sleep meditations + Skool teacher training (Yogi Bryan, 22.4K, already mobile-native)",
        "segment_original": "US Sleep / Meditation App + Teacher Training (already on Breakthrough Apps)",
        "industry": "Meditation App + Coach Training",
        "angle_to_take": "Yogi Bryan (22.4K, US) — already runs Chill Pill app + Skool meditation teacher training. Pitch is brand-coherent app upgrade angle: combine app + Skool + YouTube into a single Yogi-Bryan-branded surface, replacing the breakthroughapps.io white-label with a more coherent brand presentation.",
    },

    "hellograndmeditation@gmail.com": {
        "category": "meditation",
        "niche": "US Sivananda Yoga-cert teacher offering guided meditations + Kriya breathwork + chakra balancing + sleep meditations (Grand Meditation, 18.1K)",
        "segment_original": "US Multi-modal Meditation + Kriya Breathwork",
        "industry": "Meditation Teacher (online, multi-tradition)",
        "angle_to_take": "Grand Meditation (18.1K, US) — multi-tradition teacher with guided meditation + Kriya breathwork + chakra + sleep meditation. Frame a branded app with tradition-tag filter (Kriya / chakra / sleep / mantra) + length filter + theme-based playlist builder — supports the multi-modal catalog better than YouTube playlists.",
    },

    "idanim-product-team@tothenew.com": {
        "category": "meditation",
        "niche": "IN free meditation app from India with LIVE classes + 1000+ guided meditations Hindi/English (Idanim English, 8.83K, already mobile-native — built by ToTheNew agency)",
        "segment_original": "IN Meditation App (English channel, agency-built)",
        "industry": "Meditation App (B2C)",
        "angle_to_take": "Idanim (8.83K, IN) — already runs a meditation app built by ToTheNew agency. The pitch here isn't a new app — it's a branded white-label upgrade or a sub-vertical app (e.g. Idanim-corporate). Approach via product-team contact as a B2B partnership conversation.",
    },

    "socialmedia@heartfulness.org": {
        "category": "meditation",
        "niche": "IN Heartfulness Meditation — heart-based Raja-Yoga-rooted meditation with Yogic transmission (Practice Heartfulness, 8.62K)",
        "segment_original": "IN Heartfulness Meditation Org (global)",
        "industry": "Meditation Method / Org",
        "angle_to_take": "Practice Heartfulness (8.62K, IN) — global Heartfulness meditation org with Yogic-transmission feature. Frame a branded Heartfulness app with daily-practice calendar + transmission-session schedule + sangha community tier — replaces website + scattered meditation-track delivery.",
    },

    "training@zendust.org": {
        "category": "meditation",
        "niche": "US Zen Community of Oregon — Great Vow Zen Monastery led by Jan Chozen Bays Roshi + Hogen Bays Roshi (Great Vow Zen Monastery, 6.05K)",
        "segment_original": "US Soto Zen Monastery (training inbox)",
        "industry": "Meditation Center (Zen)",
        "angle_to_take": "Great Vow Zen Monastery (6.05K, US) — Jan Chozen Bays Roshi's Soto Zen lineage center. Frame a branded Zendust app with sesshin (retreat) schedule + Dharma talks archive + ango training calendar — fits the structured Zen training year better than Patreon.",
    },

    "hello@mcleanmeditation.com": {
        "category": "meditation",
        "niche": "US Sarah McLean — TM-trained, Deepak Chopra Center co-founder + 30yr meditation teacher (Sarah McLean Meditation & Mindfulness, 4.64K)",
        "segment_original": "US TM + Mindfulness Teacher (legacy creator)",
        "industry": "Meditation Teacher (TM / mindfulness, online)",
        "angle_to_take": "Sarah McLean (4.64K, US) — 30+ yr meditation teacher with Deepak Chopra Center co-founding history. Frame a branded McLean Meditation app with daily-practice calendar + TM-style mantra primer + retreat schedule — a legacy-creator app fits the established-teacher brand better than YouTube + email broadcasts.",
    },

    "info@mindfulnessassociation.net": {
        "category": "meditation",
        "niche": "GB Mindfulness Association — long-term systematic mindfulness training (foundation → compassion → insight) (Mindfulness Association, 3.48K)",
        "segment_original": "GB Mindfulness Training Org (B2C structured curriculum)",
        "industry": "Meditation Training (mindfulness curriculum)",
        "angle_to_take": "Mindfulness Association (3.48K, GB) — long-term mindfulness training curriculum (foundation → compassion → insight). Frame a branded MA app with structured course modules + cohort progress tracking + supervisor 1:1 booking — fits the structured-curriculum format better than ad-hoc Zoom classes.",
    },

    "anumodanasankalpa@gmail.com": {
        "category": "meditation",
        "niche": "IN Theravada Buddhist channel teaching step-by-step path to Nibbana for lay followers (Understanding Buddha's Teachings, 2.75K)",
        "segment_original": "IN Theravada Buddhist Teachings (lay-followers focus)",
        "industry": "Meditation Teacher (Theravada / sutta-based)",
        "angle_to_take": "Understanding Buddha's Teachings (2.75K, IN) — Theravada lay-follower-focused channel with sutta-verified instruction. Frame a branded app with sutta-cross-reference reader + step-by-step progression checkpoints + retreat-prep modules — fits the rigorous study/practice ICP that generic meditation apps miss.",
    },

    "keith@meditationbreaks.com": {
        "category": "meditation",
        "niche": "US in-person + online live guided meditation for offices/schools/communities (Meditation Breaks, 1.88K)",
        "segment_original": "US B2B Live Meditation Service (offices/schools)",
        "industry": "Meditation Service (B2B + B2C)",
        "angle_to_take": "Meditation Breaks (1.88K, US) — B2B live meditation for offices/schools. Frame a branded MB app with corporate-team rollout (per-org tier) + live-session join + recorded archive — fits the B2B sales motion better than scattered Zoom invites + email.",
    },

    "joy@thedailymeds.com": {
        "category": "meditation",
        "niche": "GB Natalie Lauraine — short real-life meditations for hangovers/comedowns/anxiety/loneliness (The Daily Meds, 1.82K)",
        "segment_original": "GB Modern Short-Form Meditation Brand (life-moment niche)",
        "industry": "Meditation Audio Brand (modern, niche-moments)",
        "angle_to_take": "The Daily Meds (1.82K, GB) — modern short-form meditations for specific life moments (hangover / comedown / anxiety / loneliness). Frame a branded Daily Meds app with mood-tag filter + 'right now' search + nervous-system-state quiz → matched audio — fits the hyper-specific 'in this moment' positioning.",
    },

    "info@aukana.org.uk": {
        "category": "meditation",
        "niche": "GB Paul Harris — Spiritual Director of House of Inner Tranquillity, a Buddhist Insight Meditation Retreat Centre in SW England (1.01K)",
        "segment_original": "GB Buddhist Insight Meditation Retreat Centre (Spiritual Director)",
        "industry": "Meditation Center (Buddhist / Insight)",
        "angle_to_take": "House of Inner Tranquillity (1.01K, GB) — Buddhist Insight Meditation Retreat Centre run by Paul Harris. Frame a branded Aukana app with retreat schedule + Dharma talks archive + retreatant-companion module (pre-retreat prep + post-retreat integration journaling) — fits the structured retreat practice cycle.",
    },
}
