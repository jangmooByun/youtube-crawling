"""Per-row mapping for data/2026-04-29/meditation_enriched.csv (36 rows).

Combined-dict format (same as legacy_mapping / mindful_mapping):
  email → {category, niche, segment_original, industry, angle_to_take}

Surfaced via the 14-keyword × 3-page meditation sweep on 2026-04-29
(quota ~5,050, 112 stale-drops by 6-month freshness filter).
Category routing: meditation 19 / mindset 9 / drop 8.
"""

MAPPING: dict[str, dict[str, str]] = {

    # IN holistic / subconscious-healing speaker — multi-modality (energy, vibration,
    # subconscious). Yoga + meditation are vehicles, not primary product. Mindset.
    "mail@anuragrishi.com": {
        "category": "mindset",
        "niche": "IN holistic-wellness speaker — subconscious healing + energy & vibrational work + keynote / paid sessions (Anurag Rishi, 2.75M)",
        "segment_original": "IN Holistic Healer / Keynote Speaker",
        "industry": "Spiritual / Mindset Speaker (B2C + corporate)",
        "angle_to_take": "Anurag Rishi (2.75M, IN) — large holistic-healing creator running paid sessions + keynote bookings. Frame a branded Anurag Rishi app with cohort booking + replay library + manifestation streak tracker — replaces a patchwork booking/email/payment stack with a single member surface that fits his subconscious-healing program structure.",
    },

    # IN Telugu broad-teaching channel — meditation is one of many topics (also
    # Spoken English, career skills, soft skills). Multi-vertical educator, not a
    # meditation creator.
    "dbhatnagar425@gmail.com": {
        "category": "drop",
        "niche": "IN Telugu broad teaching channel — Spoken English / Hindi / Life Skills / Soft Skills / Career Guidance + meditation as one topic (Devika Bhatnagar, 1.53M)",
        "segment_original": "IN Multi-Topic Educator (off-topic)",
        "industry": "n/a (drop)",
        "angle_to_take": "Multi-vertical Telugu educator (1.53M) where meditation is just one of many side topics. Not a method-teaching meditation creator. Drop.",
    },

    # Pyramid Meditation Channel India — already operates its own meditation app
    # with deep links across stores. AppBillChat fit weak (already productized).
    "contact@pmchindi.com": {
        "category": "drop",
        "niche": "IN Hindi Pyramid Meditation Channel — already runs PMC App on iOS/Android + Jio TV (PMC Hindi, 648K)",
        "segment_original": "IN Hindi Meditation Org (own app)",
        "industry": "n/a (drop — already has own app)",
        "angle_to_take": "PMC Hindi (648K) is a meditation org with its own deployed PMC App across iOS/Android/Jio TV. They have already solved the productization problem. Drop.",
    },

    "ally@sarovarayoga.ca": {
        "category": "yoga",
        "niche": "CA Yoga Nidra educator + Yoga Nidra & Restorative Teacher Trainings + Costa Rica / Kawarthas retreats (Ally Boothroyd, 380K)",
        "segment_original": "CA Yoga Nidra Teacher Trainer + Retreat Lead",
        "industry": "Yoga Nidra Teacher Trainer (B2C + TTC)",
        "angle_to_take": "Ally Boothroyd (380K, CA) runs Online Yoga Nidra TTC + retreats. Frame a branded Sarovara app with TTC cohort surface (modules / live-call calendar / homework upload), Nidra audio library, retreat waitlist, certification tracker — collapses the Teachable / Zoom / Mailchimp stack into one member surface that matches the structure of teacher-training cohorts.",
    },

    # Brahma Kumaris Madhuban Murli — copyright-protected content for BK students
    # only, multiple platform apps already. Org-controlled, not creator.
    "bksongchai@gmail.com": {
        "category": "drop",
        "niche": "IN Brahma Kumaris official Madhuban Murli channel — closed to BK students, multi-platform apps already deployed (Madhuban Murli, 256K)",
        "segment_original": "IN BK Org Channel (closed audience, own apps)",
        "industry": "n/a (drop — org-controlled, own apps)",
        "angle_to_take": "Brahma Kumaris official org channel (256K) with copyright restrictions and BKMultimedia apps already on Android/iOS/Windows. Closed audience, no fit. Drop.",
    },

    "divyasrijansamaj@gmail.com": {
        "category": "mindset",
        "niche": "IN online meditation course — Sun + Jupiter membership tiers covering Guided / Transcendental / Spiritual Healing (Divya Srijan Spiritual, 152K)",
        "segment_original": "IN Online Meditation Course (membership tiers)",
        "industry": "Meditation Course Creator (B2C)",
        "angle_to_take": "Divya Srijan (152K, IN) sells two-tier meditation memberships (Sun / Jupiter) for guided + transcendental + spiritual healing. Frame a branded app with tiered course gating, daily-practice streak, technique-progress tracker, and live-session booking — replaces the WhatsApp + manual-payment workflow common at this scale.",
    },

    "daniel.soderholm@telia.com": {
        "category": "mindset",
        "niche": "SE certified mental coach + behavioral scientist + yoga teacher — guided meditation / mindfulness / progressive muscle relaxation (Mind Forge, 131K)",
        "segment_original": "SE Mental Coach + Mindfulness Teacher",
        "industry": "Meditation / Mental-Training Coach (B2C)",
        "angle_to_take": "Mind Forge / Daniel Söderholm (131K, SE) blends mindfulness, mental training, and progressive muscle relaxation under a behavioral-scientist + yoga-teacher dual cert. Frame a branded Mind Forge app with focus-session player + sleep-meditation track + mental-training cohort program — replaces ad-hoc YT + email funnels with a paid member tier.",
    },

    "wellness@kristynroseyoga.ca": {
        "category": "mindset",
        "niche": "CA Yoga Nidra + nervous-system regulation + mindfulness — weekly drops, retreats, trainings (Kristyn Rose, 76.4K)",
        "segment_original": "CA Yoga Nidra + Nervous-System Teacher",
        "industry": "Yoga Nidra Teacher (B2C + TTC)",
        "angle_to_take": "Kristyn Rose (76.4K, CA) teaches Yoga Nidra + nervous-system regulation with weekly practices and retreat / training pipelines. Frame a branded Kristyn Rose app with Nidra audio library + practice streak + retreat waitlist + training cohort — collapses email-list + retreat-page + audio-host stack into one paid member surface.",
    },

    "yogashowstheway@yahoo.com": {
        "category": "yoga",
        "niche": "IN Sivananda Yoga Centre Gurgaon — Sivananda lineage TTC + classes (ERYT 500 Yoga Acharyas, 59.3K)",
        "segment_original": "IN Sivananda Yoga TTC School",
        "industry": "Yoga Teacher Training School (B2C + TTC)",
        "angle_to_take": "Sivananda Yoga Centre Gurgaon (59.3K, IN) — Sivananda-lineage TTC school. Frame a branded Sivananda Gurgaon app with TTC course module / homework / attendance + class booking + signup pipeline — collapses the bit.ly signup form and ad-hoc class scheduling into a structured teacher-training surface.",
    },

    # The harvested email is a Uscreen platform-support address, not the creator's.
    # False positive surfaced via bio crawl on the Uscreen-hosted member portal.
    "akhandayoga@uscreen.support": {
        "category": "drop",
        "niche": "Uscreen platform support address surfaced via Akhanda Yoga member portal — not the creator's actual contact (Yogrishi Vishvketu, 47.2K)",
        "segment_original": "Uscreen platform support email (false positive)",
        "industry": "n/a (drop — platform support email)",
        "angle_to_take": "akhandayoga@uscreen.support is Uscreen's platform support address surfaced from the member-portal footer. Not actionable for outreach. Drop.",
    },

    "gopal@heartnest.in": {
        "category": "mindset",
        "niche": "IN Past Life Regression coach + Hypno-Heal — IAOTH-accredited monthly 3-day live webinar (Dr. Gopal Maheshwari, 31.7K)",
        "segment_original": "IN Past Life Regression / Hypnotherapy Coach",
        "industry": "Hypnotherapy / Spiritual Coach (B2C + cert program)",
        "angle_to_take": "Dr. Gopal Maheshwari (31.7K, IN) runs an IAOTH-accredited Past Life Regression certification (monthly 3-day webinar) plus Hypno-Heal sessions. Frame a branded HeartNest app with cohort-tracker for the 3-day webinar + alumni community + 1-on-1 booking — replaces the WhatsApp + landing-page funnel with a structured certification surface.",
    },

    "bkdrraj@gmail.com": {
        "category": "mindset",
        "niche": "IN Brahma Kumaris Rajyoga Meditation — daily guided practice + happiness coaching (BK Dr Rajesh, MD radiologist, 31.1K)",
        "segment_original": "IN BK-affiliated Rajyoga Meditation Teacher",
        "industry": "Meditation Teacher (B2C, BK-affiliated)",
        "angle_to_take": "BK Dr Rajesh (31.1K, IN) — Brahma Kumaris-trained radiologist + Rajyoga meditation practitioner who runs his own personal channel with daily guided meditations. Frame a branded Rajyoga Daily app with morning-practice streak + soul-quality reflection journal + cohort intro course — fits the daily-practice rhythm his content is built around.",
    },

    "contact@aylanova.com": {
        "category": "mindset",
        "niche": "Yoga Nidra & Beyond — weekly nidra, mental fitness + radical self-acceptance (Ayla Nova, 31K)",
        "segment_original": "Yoga Nidra Sleep-Meditation Teacher",
        "industry": "Yoga Nidra Teacher (B2C)",
        "angle_to_take": "Ayla Nova (31K) runs Yoga Nidra & Beyond as a sleep-meditation + mental-fitness creator. Frame a branded app with nidra audio library + bedtime mode + practice-streak — clean fit for an audio-meditation creator at this scale who currently relies on bio.site links.",
    },

    "Rhi1122@icloud.com": {
        "category": "yoga",
        "niche": "US Kundalini Awakening membership — donation-based daily live Sadhana + group coaching + monthly retreats + private community (Kundalini Awakening & Embodiment Center, 21.5K)",
        "segment_original": "US Kundalini Awakening Membership Community",
        "industry": "Kundalini Membership / Online Retreat Lead (B2C)",
        "angle_to_take": "Kundalini Awakening & Embodiment (21.5K, US) — donation-based membership with daily live Sadhana, group coaching, monthly retreats, and a private thread. Frame a branded app with daily-live calendar + sadhana streak + private community feed + retreat schedule — replaces the Teachable + Mailchi quiz + ad-hoc community stack.",
    },

    "nikki@thetranquillity.co.uk": {
        "category": "mindset",
        "niche": "GB psychic + medium + QHHT/CBT/NLP + Past Life Regression + Akashic Records + meditation teacher + organic shop (Tranquillity with Nikki, 19.9K)",
        "segment_original": "GB Multi-Modality Spiritual Coach + Workshops",
        "industry": "Spiritual Coach + Workshop Lead (B2C)",
        "angle_to_take": "Nikki / Tranquillity (19.9K, GB) is a multi-modality spiritual coach (psychic + QHHT + NLP + Past Life Regression + Remote Viewing workshops). Frame a branded Tranquillity app with workshop cohort surface + 1-on-1 session booking + product shop tab — collapses the Wise/international-transfer + WhatsApp-booking pattern she runs today.",
    },

    "support@corymuscara.com": {
        "category": "mindset",
        "niche": "Former monk + mindfulness teacher + Columbia / Penn instructor — corporate keynotes, podcast, bestselling author, 25M+ meditation listens in 150+ countries (Cory Muscara, 19.1K)",
        "segment_original": "Mindfulness Teacher + Corporate Keynote / Author",
        "industry": "Mindfulness Teacher + Corporate B2B (keynote / workshop)",
        "angle_to_take": "Cory Muscara (19.1K YT but 1M+ across socials) — former monk, Penn / Columbia mindfulness instructor, corporate keynote speaker. Frame a branded Cory Muscara app with on-demand mindfulness library + corporate-cohort enrollment surface + keynote booking — distinguishes the consumer audio practice from his B2B workshop pipeline (Bank of America, Prudential, J&J).",
    },

    "aditi@dynamicmindsgroup.com": {
        "category": "mindset",
        "niche": "IN Digital Wellness Coach + memory / focus techniques + mindful-parenting + Guinness World Record holder (Aditi Singhal, 16.8K)",
        "segment_original": "IN Memory / Digital-Wellness Coach + Keynote",
        "industry": "Productivity / Mindset Coach + B2B Keynote",
        "angle_to_take": "Aditi Singhal (16.8K, IN) — Guinness-record memory / digital-wellness coach with corporate keynote + parenting workshops. Frame a branded Dynamic Minds app with focus / memory drill modules + screen-time tracker + parenting-program cohort + keynote booking — bridges B2C technique modules with B2B keynote / consultancy pipeline.",
    },

    "bereniceyoganidra@gmail.com": {
        "category": "mindset",
        "niche": "FR Yoga Nidra teacher + yoga therapist (trauma-specialized) — French-language donation-based community on YouTube (Berenice Mertens, 11.5K)",
        "segment_original": "FR Yoga Nidra / Yoga Therapy Teacher",
        "industry": "Yoga Nidra Teacher (B2C, donation-based)",
        "angle_to_take": "Berenice Mertens (11.5K, FR) shares Yoga Nidra in French with a donation-based community + trauma-informed yoga therapy practice. Frame a branded app with French nidra audio library + donation tier + trauma-therapy 1-on-1 booking — replaces shorturl donation + manual contact with a paid-tier surface.",
    },

    "wednesdaynightconversations@gmail.com": {
        "category": "mindset",
        "niche": "US music educator → mindfulness meditation teacher — short guided practices for beginners + meditation-skill progression (Wednesday Night Meditations, 8.87K)",
        "segment_original": "US Mindfulness Meditation Teacher (beginner-focused)",
        "industry": "Meditation Teacher (B2C, beginner)",
        "angle_to_take": "Wednesday Night Meditations (8.87K, US) — beginner-friendly mindfulness teacher with step-by-step skill progression. Frame a branded app with skill-tree (focus / breath / body-scan / loving-kindness) + daily short-practice streak + onboarding course — fits the explicit beginner-progression structure of his content.",
    },

    # Astrology + Vastu + Numerology + NLP + Tarot + Reiki — meditation is one of
    # many occult sciences. Off-topic for meditation.
    "rbjgurukulofficial@gmail.com": {
        "category": "drop",
        "niche": "IN multi-occult sciences gurukul — Astrology / Vastu / Numerology / NLP / Reiki + meditation as one topic (Rapto Bhara Jeevan, 7.57K)",
        "segment_original": "IN Astrology / Occult Sciences School (off-topic)",
        "industry": "n/a (drop — multi-occult, not meditation)",
        "angle_to_take": "RBJ Gurukul (7.57K, IN) is a multi-occult-sciences gurukul (astrology / vastu / numerology). Meditation is incidental. Off-topic for meditation bucket. Drop.",
    },

    # Placeholder email picked up from a website footer template.
    "email@address.com": {
        "category": "drop",
        "niche": "Placeholder email surfaced from website footer template — not the creator's actual email (Tanis Fishman, 6.83K)",
        "segment_original": "Placeholder email (false positive)",
        "industry": "n/a (drop — placeholder)",
        "angle_to_take": "email@address.com is a website-template placeholder, not actionable. Drop. Tanis Fishman (Yoga Nidra, schoolofsankalpa.com) could be re-surfaced in a future sweep with a real email.",
    },

    "mamtajain16772@gmail.com": {
        "category": "mindset",
        "niche": "IN Aakashganga Meditation — yoga + meditation + pranayama, Vipassana / Preksha seeker, NIOS-certified yoga teacher (Mamta Jain, 6.78K)",
        "segment_original": "IN Meditation + Pranayama Teacher",
        "industry": "Meditation / Pranayama Teacher (B2C)",
        "angle_to_take": "Aakashganga Meditation (6.78K, IN) — Vipassana / Preksha-trained meditation + pranayama teacher with channel-name explicitly meditation-first. Frame a branded app with daily pranayama / meditation sessions + sponsorship workflow + voice-over booking surface — fits her dual creator-and-service-provider model.",
    },

    "contactmagicalmind@gmail.com": {
        "category": "mindset",
        "niche": "IN Tarot Reader + Psychotherapist + Spiritual Guide + Meditation Teacher — multi-modal manifestation / emotional healing (Monika Singh, 6.25K)",
        "segment_original": "IN Tarot + Manifestation Coach (multi-modal)",
        "industry": "Spiritual / Manifestation Coach (B2C)",
        "angle_to_take": "Monika Singh (6.25K, IN) blends tarot + psychotherapy + manifestation + meditation under one personal brand. Frame a branded MagicalMind app with tarot-reading booking + manifestation cohort + emotional-healing journal + 1-on-1 calendar — replaces the WhatsApp-only intake she runs today.",
    },

    "hello@zuriretreats.com": {
        "category": "mindset",
        "niche": "US ex-Hollywood (Warner Bros / BET / MTV) → wellness retreat founder for Black women + women of color, Mindfulness Meditation Teacher + RYT-200 + Reiki Master, Yale Science of Wellbeing — Morocco / Tulum / Bali retreats (Shannon Amos, 5.3K)",
        "segment_original": "US Mindfulness Teacher + Retreat Founder",
        "industry": "Meditation Teacher + Retreat Lead (B2C + corporate)",
        "angle_to_take": "Shannon Amos / Zuri Retreats (5.3K, US) — mindfulness teacher with international luxury retreats + corporate wellness arm. Frame a branded Zuri app with retreat waitlist + cohort prep / packing surface + post-retreat alumni community + corporate-program booking — distinguishes consumer retreat funnel from corporate wellness pipeline.",
    },

    "hello@buddhadailywisdom.com": {
        "category": "mindset",
        "niche": "TH Buddhist teacher (David Roylance, since 2005) — Gotama Buddha teachings + courses + retreats globally (Daily Wisdom, 4.25K)",
        "segment_original": "TH Buddhist Teacher (English-language)",
        "industry": "Buddhist Meditation Teacher (B2C + retreat)",
        "angle_to_take": "Daily Wisdom (4.25K, TH) — David Roylance teaches Gotama Buddha's path with global courses + retreats. Frame a branded Buddha Daily Wisdom app with course module library + sutta-study cohort + retreat booking + LINE / WhatsApp consolidation — replaces the multi-channel contact stack he uses.",
    },

    "andy@freemeditationtv.com": {
        "category": "mindset",
        "niche": "CA Sahaja Yoga charity meditation — free guided sessions + Sahaja Yoga Basics + collaborations (Free Meditation TV, Vishwa Nirmala Dharma Educational Society, 3.97K)",
        "segment_original": "CA Sahaja Yoga Charity (free meditation)",
        "industry": "Meditation Charity / Org (donation-based)",
        "angle_to_take": "Free Meditation TV (3.97K, CA) — registered Canadian charity sharing Sahaja Yoga free meditation sessions. Frame a branded charity app with intro-course funnel + collab / hosted-session signup + donation tier — fits the volunteer-driven free-content model while creating a stable supporter base.",
    },

    "navneetisingh1432@gmail.com": {
        "category": "mindset",
        "niche": "IN Law of Assumption + manifestation channel + 1-on-1 meditation coaching (Manifest with Meditation, 2.88K)",
        "segment_original": "IN Manifestation / Law-of-Assumption Coach",
        "industry": "Manifestation Coach (B2C, 1-on-1)",
        "angle_to_take": "Manifest with Meditation (2.88K, IN) — Law of Assumption + manifestation creator with 1-on-1 meditation coaching. Frame a branded app with manifestation-script journal + affirmation library + 1-on-1 coaching booking + cohort program — fits the personalized-coaching workflow she advertises.",
    },

    # Unplug already runs its own world-first drop-in meditation app + 2 LA studios
    # + 1000+ guided meditations + 64 teachers in 92 countries. Already productized.
    "info@unplug.com": {
        "category": "drop",
        "niche": "US drop-in meditation studio + global meditation app already deployed in 92 countries with 64 teachers + 1000+ meditations (Unplug, 2.45K)",
        "segment_original": "US Meditation Studio + Own App (deployed)",
        "industry": "n/a (drop — already has own app)",
        "angle_to_take": "Unplug (2.45K) already runs its own meditation app in 92 countries with 64 teachers + 1000+ guided meditations + 2 LA studios. They are the productized solution. Drop.",
    },

    # Spotify platform-support address surfaced via bio-crawl footer of a Spotify
    # podcast page — not the creator's actual email.
    "support@spotify.com": {
        "category": "drop",
        "niche": "Spotify platform support address surfaced from podcast-page footer — not the creator's email (Tess Callahan, 1.76K)",
        "segment_original": "Spotify platform support email (false positive)",
        "industry": "n/a (drop — platform support)",
        "angle_to_take": "support@spotify.com is Spotify's platform-support address from a podcast page footer. Not actionable. Drop. Tess Callahan (Heart Haven Meditations) could be re-surfaced via tesscallahan.com in a later sweep.",
    },

    "kristi.kuttner@gmail.com": {
        "category": "yoga",
        "niche": "US (San Diego) Reiki Master + Yin Yoga + Meditation + Sound Healing + Yoga Nidra — 500hr E-RYT, in-person + virtual healing sessions, Reiki + Yin trainings (kristi kuttner, 1.61K)",
        "segment_original": "US Multi-Modal Yoga + Reiki Trainer",
        "industry": "Yoga + Reiki Trainer (B2C + TTC)",
        "angle_to_take": "kristi kuttner (1.61K, US) blends Reiki + Yin Yoga + Meditation + Sound Healing + Yoga Nidra under one teacher brand with online + in-person trainings. Frame a branded app with training cohort surface + 1-on-1 healing booking + nidra audio library + Flodesk-replacement signup — collapses the Squarespace + Flodesk + booking stack.",
    },

    "GuidedMeditationsKF@gmail.com": {
        "category": "mindset",
        "niche": "US Meditation Guide + Yoga Nidra + Breathwork + nervous-system regulation, 200-Hr TTC in progress (Kamara Farai, 1.3K)",
        "segment_original": "US Meditation + Nidra + Breathwork Guide",
        "industry": "Meditation Guide (B2C, early-stage)",
        "angle_to_take": "Kamara Farai (1.3K, US) — solo meditation + nidra + breathwork guide at early-channel scale. Frame a branded GuidedMeditationsKF app with audio-library + practice streak + collab inquiry tab — replaces a YT-only presence with a member surface as the channel grows past TTC certification.",
    },

    "hello@peacefulwellness.studio": {
        "category": "mindset",
        "niche": "US (Madison WI) Mindfulness + Meditation Teacher (since 1980) + Sound + Energy + Aromatherapist — Peaceful Wellness Studio + Institute + Skool community (Meditate with Deb, 1.3K)",
        "segment_original": "US Mindfulness Teacher + Studio + Skool Community",
        "industry": "Meditation Teacher + Wellness Studio (B2C)",
        "angle_to_take": "Meditate with Deb / Peaceful Wellness (1.3K, US) — 45-yr veteran mindfulness teacher running studio + institute + free Skool community. Frame a branded Peaceful Wellness app with sound-bath library + Skool-replacement community feed + studio session booking — collapses the multi-domain (peacefulwellness.org + institute + studio) into one paid member surface.",
    },

    "info@lionwisdom.org": {
        "category": "mindset",
        "niche": "US Buddhist meditation center (Washington Buddhist Vihara) — Bhante Yogavacara Rahula's Dhamma talks + classes + retreats + drop-in sessions (Paññāsīha / Lion of Wisdom, 1.28K)",
        "segment_original": "US Buddhist Meditation Center (org)",
        "industry": "Buddhist Meditation Center (B2C + retreat)",
        "angle_to_take": "Paññāsīha / Lion of Wisdom (1.28K, US) — Washington Buddhist Vihara meditation center with Dhamma talks + drop-in sessions + retreats. Frame a branded Lion Wisdom app with retreat registration + drop-in calendar + Dhamma-talk library + donation tier — replaces email-only registration with a structured center surface.",
    },

    "Adwaityoga@gmail.com": {
        "category": "yoga",
        "niche": "IN Rishikesh-based yoga school (Adwait Foundation) — TTC + workshops + retreats, founded by Sri Yogi Anand (Adwait Yoga School, 1.26K)",
        "segment_original": "IN Rishikesh Yoga School (TTC)",
        "industry": "Yoga Teacher Training School (B2C + TTC)",
        "angle_to_take": "Adwait Yoga School (1.26K, IN) — Rishikesh TTC school with 200/300/500-Hr trainings + Ayurveda + meditation + holistic-lifestyle modules. Frame a branded Adwait Yoga app with TTC-cohort surface + module library + retreat booking + India-base intake form — collapses the cross-domain (yogianand.in + adwaityoga.com) attendance and signup workflow.",
    },

    "deesideyogainstitute@gmail.com": {
        "category": "yoga",
        "niche": "GB E-RYT 500 + yoga therapist (C-IAYT in training) — Yin / Restorative / Somatic TTC + Substack + 1-on-1 yoga therapy (Yoga with Gem / Deeside Yoga Institute, 1.12K)",
        "segment_original": "GB Yin / Restorative / Somatic Yoga Trainer",
        "industry": "Yoga Teacher Trainer + 1-on-1 Therapy (B2C + TTC)",
        "angle_to_take": "Yoga with Gem / Deeside Yoga Institute (1.12K, GB) — Yin + Restorative + Somatic TTC trainer with 1-on-1 yoga therapy practice. Frame a branded Deeside app with TTC cohort + free-resource gating + 1-on-1 therapy booking + Substack-replacement post feed — collapses the Substack + Squarespace + email-only intake.",
    },

    "oshani@gmail.com": {
        "category": "mindset",
        "niche": "IL (Tel Aviv) tech entrepreneur → meditation teacher — mindfulness / Zen / shamanism / quantum-physics-inspired guided meditations, free across YouTube + Spotify + Apple (Ofer Shani, 1.08K)",
        "segment_original": "IL Meditation Teacher (Hebrew + English)",
        "industry": "Meditation Teacher (B2C, free distribution)",
        "angle_to_take": "Ofer Shani (1.08K, IL) — meditation teacher with multi-tradition guided meditations distributed free across YT / Spotify / Apple via Linktree. Frame a branded app with multi-language session library + creator-music-rights workflow + donation tier — gives a single creator-controlled surface vs the patchwork Linktree distribution he runs today.",
    },
}
