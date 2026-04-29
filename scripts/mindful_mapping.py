"""Per-row mapping for data/0422/mindful/mindful_all.csv (25 rows).

Same dict-of-dict shape as legacy_mapping.py:
  email → {category, niche, segment_original, industry, angle_to_take}

Categories:
  meditation = pure meditation (Vipassana / mindfulness / Buddhist / MBSR)
  mindset    = yoga (incl. Yoga Nidra) / breathwork / mindset coach
  drop       = paper-craft / journaling false positives, generic platform
               inboxes (pr@patreon.com), placeholder emails (filler@godaddy.com)

Note on duplicates with main MAPPING / legacy_mapping:
  pr@patreon.com and filler@godaddy.com appear in multiple sources with
  different profile_urls. The email→category lookup happens per source CSV,
  so they each get their own classification here without collision.
"""

MAPPING: dict[str, dict[str, str]] = {

    # ---- breathwork → drop because pr@patreon.com is generic, not the creator
    "pr@patreon.com": {
        "category": "drop",
        "niche": "Generic Patreon support inbox surfaced via Breathe With Sandy / Teal and Tattered — not actionable",
        "segment_original": "Generic platform support address",
        "industry": "n/a (drop)",
        "angle_to_take": "Patreon's generic PR address — not the creator's inbox. Drop.",
    },

    # ---- paper-craft / journaling false positives ----
    "pam@thepaperoutpost.com": {
        "category": "drop",
        "niche": "US paper-craft / junk journal tutorials channel (The Paper Outpost / Pam) — surfaced via 'mindful' false positive",
        "segment_original": "Paper-craft tutorials (off-topic)",
        "industry": "n/a (drop)",
        "angle_to_take": "Paper-craft / junk-journal channel — not in the meditation/mindset target. Drop.",
    },
    "carriewalker321@gmail.com": {
        "category": "drop",
        "niche": "US journaling + faith + healthy-living lifestyle creator (Carrie Walker, 23yr) — cross-vertical false positive",
        "segment_original": "Journaling lifestyle (off-topic)",
        "industry": "n/a (drop)",
        "angle_to_take": "Journaling + faith + lifestyle creator — doesn't fit any of mindset/meditation/fitness/nutrition. Drop.",
    },
    "junkjournaljoy@gmail.com": {
        "category": "drop",
        "niche": "Junk journal / paper-craft tutorials channel (Junk Journal Joy)",
        "segment_original": "Paper-craft tutorials (off-topic)",
        "industry": "n/a (drop)",
        "angle_to_take": "Junk journaling channel — off-topic. Drop.",
    },
    "tealandtattered@gmail.com": {
        "category": "drop",
        "niche": "PL paper journal maker / junk-journal channel (Teal and Tattered Journals / Martyna)",
        "segment_original": "Paper-craft tutorials (off-topic)",
        "industry": "n/a (drop)",
        "angle_to_take": "Polish paper-craft / journaling creator — off-topic. Drop.",
    },
    "ktsjournal.contact@gmail.com": {
        "category": "drop",
        "niche": "Personal life-journal vlog channel (kt's journal) — cross-vertical lifestyle",
        "segment_original": "Personal life journaling (off-topic)",
        "industry": "n/a (drop)",
        "angle_to_take": "Personal life journaling vlog — off-topic. Drop.",
    },

    # ---- yoga / Yoga Nidra → mindset (per user rule: yoga goes to mindset) ----
    "hello@rosalieesilva.com": {
        "category": "yoga",
        "niche": "GB yoga teacher specializing in Yoga Nidra / NSDR + astral projection (RosalieYoga / Rosalie e Silva)",
        "segment_original": "GB Yoga Nidra + NSDR Teacher",
        "industry": "Yoga Teacher (online, Yoga Nidra niche)",
        "angle_to_take": "GB Yoga Nidra + NSDR teacher exploring expanded states. Frame a branded Rosalie app with bedtime-mode Yoga Nidra player + length filter (10/20/40 min) + journal prompt for inner-guidance work — replaces YouTube-only delivery with a paid evening-ritual surface. Cost saving on splintered Patreon + email funnel.",
    },
    "wellness@kristynroseyoga.ca": {
        "category": "yoga",
        "niche": "CA Yoga Nidra teacher for nervous-system healing + sleep + mindfulness (Kristyn Rose, wellness inbox)",
        "segment_original": "CA Yoga Nidra Teacher (NS regulation)",
        "industry": "Yoga Nidra (online)",
        "angle_to_take": "CA Yoga Nidra teacher framing practice around nervous-system regulation, sleep, and emotional balance. Frame a branded Kristyn-Rose app with nervous-system-state quiz + matched Yoga-Nidra audio + member-streak surface — turns her sleep/healing positioning into a daily-ritual revenue line.",
    },
    "kristynroseyoga@gmail.com": {
        "category": "drop",
        "niche": "CA Yoga Nidra teacher (Kristyn Rose, gmail inbox)",
        "segment_original": "CA Yoga Nidra Teacher (NS regulation)",
        "industry": "Yoga Nidra (online)",
        "angle_to_take": "Same Kristyn Rose channel — gmail inbox. Same branded Yoga-Nidra app pitch with nervous-system-state quiz + matched audio.",
    },

    # ---- pure meditation → meditation ----
    "info@jackkornfield.com": {
        "category": "mindset",
        "niche": "US Western mindfulness icon — Buddhist monk training (Thailand/India/Burma) + clinical psych PhD + co-founder Insight Meditation Society + Spirit Rock Meditation Center (Jack Kornfield)",
        "segment_original": "US Buddhist Mindfulness Teacher + Author + Founder",
        "industry": "Meditation Teacher (Buddhist / clinical-mindfulness)",
        "angle_to_take": "Jack Kornfield — Western mindfulness elder + co-founder of IMS + Spirit Rock. Pitch a branded Jack-Kornfield app spanning his archival dharma talks library + retreat scheduling + member-tier subscription — fits a public-figure brand stack better than Patreon. Approach via info@ as a brand-extension play; expect agency/team gatekeeping.",
    },

    # Insight Meditation Center — same channel, 10 different inboxes; all meditation.
    "hborison@sbcglobal.net": {
        "category": "drop",
        "niche": "US Insight Meditation Center (IMC) — community Vipassana / mindfulness Buddhist center (Gil Fronsdal + Andrea Fella) — personal admin email surfaced",
        "segment_original": "US Buddhist Insight-Meditation Center (admin)",
        "industry": "Meditation Center (Buddhist / Vipassana, B2C community)",
        "angle_to_take": "IMC admin email surfaced. Pitch a branded IMC sangha app: dharma talks library + retreat schedule + sitting-group registration + dāna (donation) flow — replaces fragmented mailman/Wordpress sangha tooling with a single member-tier surface.",
    },
    "earthcare.dharma@gmail.com": {
        "category": "drop",
        "niche": "IMC Earthcare Dharma program (eco-dharma / Buddhist environmental practice group)",
        "segment_original": "US IMC Earthcare program inbox",
        "industry": "Meditation Center (Buddhist)",
        "angle_to_take": "IMC Earthcare Dharma program inbox. Same branded IMC app pitch but with a niche tag for eco-dharma practitioners — separate program track within the unified app.",
    },
    "imc.volunteerdirector@gmail.com": {
        "category": "drop",
        "niche": "IMC Volunteer Director inbox — Buddhist community operations",
        "segment_original": "US IMC Volunteer Director (operations)",
        "industry": "Meditation Center (Buddhist)",
        "angle_to_take": "IMC Volunteer Director — operations contact. Pitch the branded IMC app with volunteer-shift sign-up + sangha announcements built-in — cost saving over current scattered scheduling tools.",
    },
    "asianimc2020@gmail.com": {
        "category": "drop",
        "niche": "IMC Asian-heritage practitioner program (asianimc2020) — affinity sangha within IMC",
        "segment_original": "US IMC Asian-heritage sangha",
        "industry": "Meditation Center (Buddhist)",
        "angle_to_take": "IMC Asian-heritage affinity sangha. Pitch a branded IMC app with affinity-sangha sub-spaces (queer / Asian-heritage / family) gated by member tier — reflects how IMC actually runs sub-communities today.",
    },
    "imc.familyprogram@gmail.com": {
        "category": "drop",
        "niche": "IMC Family Program — Buddhist meditation programming for families/children",
        "segment_original": "US IMC Family Program",
        "industry": "Meditation Center (Buddhist)",
        "angle_to_take": "IMC Family Program inbox. Branded IMC app with kids/teens-tier content + family-event RSVP — extends sangha membership down a generation.",
    },
    "eightfoldpath@insightmeditationcenter.org": {
        "category": "drop",
        "niche": "IMC Eightfold Path program inbox",
        "segment_original": "US IMC Eightfold Path program",
        "industry": "Meditation Center (Buddhist)",
        "angle_to_take": "IMC Eightfold Path teaching cohort inbox. Branded IMC app with course-module structure for the Eightfold Path syllabus — replaces email + zoom-only delivery.",
    },
    "imcsg22@gmail.com": {
        "category": "drop",
        "niche": "IMC sub-group inbox (imcsg22) — likely a 2022 study/practice group",
        "segment_original": "US IMC study/practice sub-group",
        "industry": "Meditation Center (Buddhist)",
        "angle_to_take": "IMC sub-group inbox. Same branded IMC app with sub-group cohort tier (closed-group + scheduled meeting calendar).",
    },
    "melodybaumgartner@gmail.com": {
        "category": "drop",
        "niche": "IMC named volunteer/staff (Melody Baumgartner) — internal champion contact",
        "segment_original": "US IMC named volunteer (champion)",
        "industry": "Meditation Center (Buddhist)",
        "angle_to_take": "Named IMC contact. Frame as warm internal-champion conversation about the branded IMC app — cost saving over Mailchimp + scattered spreadsheets.",
    },
    "imcqueersangha@gmail.com": {
        "category": "drop",
        "niche": "IMC Queer Sangha — LGBTQ+ affinity meditation community",
        "segment_original": "US IMC Queer Sangha",
        "industry": "Meditation Center (Buddhist)",
        "angle_to_take": "IMC Queer Sangha inbox. Same affinity-sangha sub-space pitch — LGBTQ+ affinity community as a member-tier within the unified IMC app.",
    },
    "contact@insightmeditationcenter.org": {
        "category": "mindset",
        "niche": "IMC main contact — community Vipassana / mindfulness Buddhist center (Gil Fronsdal + Andrea Fella)",
        "segment_original": "US Buddhist Insight-Meditation Center (main inbox)",
        "industry": "Meditation Center (Buddhist / Vipassana)",
        "angle_to_take": "Main IMC contact inbox — best primary outreach target. Branded IMC sangha app: dharma talks library + retreat schedule + sub-sangha tiers + dāna flow. Highlight cost-saving on splintered tooling stack and brand-coherent member experience.",
    },

    "meditationwithsk@gmail.com": {
        "category": "mindset",
        "niche": "IN Osho-philosophy meditation channel with guided meditation techniques + inner-peace teachings (Meditation With SK)",
        "segment_original": "IN Osho-Tradition Meditation Teacher",
        "industry": "Meditation Teacher (Osho / philosophy)",
        "angle_to_take": "IN Osho-philosophy meditation teacher with guided beginner-friendly techniques. Frame a branded SK app with daily-meditation calendar + guided-audio library + Osho-philosophy article module — replaces YouTube-only delivery with a paid member tier.",
    },

    "wednesdaynightconversations@gmail.com": {
        "category": "mindset",
        "niche": "US music-educator + 19yr mindfulness-meditation practitioner combining teaching with mindfulness practice (Wednesday Night Meditations)",
        "segment_original": "US Mindfulness Meditation Educator",
        "industry": "Meditation Teacher (mindfulness, educator)",
        "angle_to_take": "US 19-yr mindfulness practitioner + music educator. Frame a branded Wednesday-Night-Meditations app with weekly live-meditation Wednesday slot + recorded archive + member discussion tier — preserves the live-community ritual format.",
    },

    "filler@godaddy.com": {
        "category": "drop",
        "niche": "Placeholder GoDaddy parking email surfaced via MIDL Insight Meditation channel — not actionable",
        "segment_original": "Placeholder email (drop)",
        "industry": "n/a (drop)",
        "angle_to_take": "Filler GoDaddy domain-parking email — not the creator's inbox. Drop.",
    },

    "contact@laitattis.com.au": {
        "category": "mindset",
        "niche": "AU sleep hypnotherapist + life coach using guided meditation for anxiety/depression/OCD/addictions (Lai Tattis Sleep Hypnosis & Guided Meditation)",
        "segment_original": "AU Sleep Hypnotherapy + Guided-Meditation + Life Coach",
        "industry": "Hypnotherapy + Life Coaching",
        "angle_to_take": "AU sleep hypnotherapist combining guided meditation + life coaching for anxiety/OCD/addictions recovery. Frame a branded Lai-Tattis app with sleep-hypnosis player + 1:1 coaching booking + condition-tag filter (anxiety / OCD / addictions) — replaces splintered hypnotherapy intake + YouTube + Patreon stack.",
    },
}
