"""Per-row mapping for data/2026-04-29/nutrition_enriched.csv (11 rows).

Combined-dict format (same as legacy_mapping / mindful_mapping):
  email → {category, niche, segment_original, industry, angle_to_take}

Surfaced via the 6-keyword × 2-page nutrition sub-niche sweep on 2026-04-29
(quota ~1,430, 19 stale-drops by 6-month freshness filter). Targets sports
nutrition / gut health / fasting / hormonal / functional / metabolic.
Category routing: nutrition 7 / mindset 1 / drop 3.
"""

MAPPING: dict[str, dict[str, str]] = {

    # Metabolic Health Initiative is a B2B medical-education platform with CME
    # credits and a scientific conference — not a creator-coach.
    "info@metabolicinitiative.com": {
        "category": "drop",
        "niche": "US B2B medical-education platform — CME-centered metabolic-health curriculum + scientific conference + Metabolic Link podcast (Metabolic Health Summit, 49.7K)",
        "segment_original": "US B2B Medical Education / Conference",
        "industry": "n/a (drop — B2B medical CME platform)",
        "angle_to_take": "Metabolic Health Initiative (49.7K, US) is a B2B medical-education platform serving the medical / scientific community with CME credit + a flagship conference. Not a creator-coach with a method-teaching consumer product. Drop.",
    },

    # Multi-modal life / wellbeing coach — meditation + life coach + podcast,
    # mostly Mindvalley-style life coaching, with no specific nutrition signal
    # despite being surfaced by metabolic-keyword.
    "coachdrmahmud@gmail.com": {
        "category": "mindset",
        "niche": "BD-base (US-listed) Mindvalley + Flourishing-certified life coach + 6-Phase Meditation trainer — generic life / health / wellbeing 1-on-1 (Coach Dr. Mahmud, 10.1K)",
        "segment_original": "Mindvalley-Certified Life Coach (multi-vertical)",
        "industry": "Life Coach (B2C, multi-vertical)",
        "angle_to_take": "Coach Dr. Mahmud (10.1K) — Mindvalley + Flourishing-certified life coach (re-routed to mindset; surfaced via metabolic keyword but description is generic life coaching, no nutrition signal). Frame a branded Coach Mahmud app with 1-on-1 booking + 6-Phase meditation cohort + life-coaching intake form — collapses the wise-head + facebook + mailchi stack into a single coaching member surface.",
    },

    "optimizewithmanana@gmail.com": {
        "category": "nutrition",
        "niche": "US Functional Medicine Health Coach (FMCA) — anti-inflammatory / low-glycemic nutrition + cooking-as-life-skill, Hoboken NJ + NYC + online, free 20-min Calendly intake (Manana Khiskiadze, 8.39K)",
        "segment_original": "US Functional Medicine Nutrition Coach (FMCA)",
        "industry": "Functional Nutrition Coach (B2C + corporate / healthcare)",
        "angle_to_take": "Optimize with Manana (8.39K, US) — FMCA-certified functional medicine health coach with private + group + corporate / healthcare programs. Frame a branded Optimize with Manana app with 5-pillar (sleep / nutrition / hydration / movement / mindset) tracker + recipe library + cohort program + corporate-program inquiry tab — replaces the Calendly + Squarespace stack with a tiered member surface.",
    },

    "gabrielle@dietitiangabrielle.com": {
        "category": "nutrition",
        "niche": "Chicago RD focused on gut health + fiber education — Stan-store Fiber Guide + private nutrition community, 1:1 coaching application (Dietitian Gabrielle, 4.85K)",
        "segment_original": "US Chicago RD (Gut Health + Fiber)",
        "industry": "Registered Dietitian (B2C, niche=gut health)",
        "angle_to_take": "Dietitian Gabrielle (4.85K) — Chicago RD with sharp gut-health + fiber positioning, currently selling via Stan-store + IG / TikTok. Frame a branded Fiber Fairy app with fiber-tracking + recipe library + symptom journal + 1-on-1 coaching application — replaces the Stan-store + IG-DM funnel with a creator-controlled member surface (and lets brand-deal pipeline stay separate).",
    },

    "nicki@happyhormonesforlife.com": {
        "category": "nutrition",
        "niche": "GB hormone-health coach for women 40+ — diet / supplements / lifestyle for stress, fatigue, weight gain, hormone imbalances, free Hormone Balancing Guide funnel (Nicki Williams, 2.32K)",
        "segment_original": "GB Hormone-Health Coach (women 40+)",
        "industry": "Functional Nutrition / Hormone Coach (B2C)",
        "angle_to_take": "Nicki Williams / Happy Hormones (2.32K, GB) — hormone-health coach for women 40+ with a free Hormone Balancing Guide → discovery-call funnel. Frame a branded Happy Hormones app with 12-week hormone-protocol cohort + symptom tracker + supplement / lifestyle library + discovery-call booking — collapses the email-only funnel into a structured cohort surface that fits the 40+ audience's protocol expectation.",
    },

    "Babydharani@gmail.com": {
        "category": "nutrition",
        "niche": "IN wellness coach (Worth While Wellness Center) — daily online live workouts + nutrition + diet guidance + transformation challenges, multi-modal lifestyle correction (Worth While Wellness, 2.3K)",
        "segment_original": "IN Live-Workout + Nutrition Wellness Center",
        "industry": "Wellness Center (B2C, multi-modal)",
        "angle_to_take": "Worth While Wellness (2.3K, IN) — wellness center running daily live workouts (6 + 8 AM) + nutrition + diet guidance + fitness challenges. Frame a branded WWW app with daily-live calendar + nutrition-protocol library + challenge cohort + paid-promotion inquiry tab — replaces the WhatsApp-only intake that bottlenecks the live + transformation workflow.",
    },

    # Metabolic Research Center is a 40-yr-old chain weight-loss center brand
    # (not a creator-coach). support@ is a generic franchise inbox.
    "support@emetabolic.com": {
        "category": "drop",
        "niche": "US chain weight-loss center brand (40-yr-old franchise) — pre-purchased grocery-food protocols, support@ generic inbox (Metabolic Research Center, 1.94K)",
        "segment_original": "US Chain Weight-Loss Center (franchise brand)",
        "industry": "n/a (drop — multi-location franchise brand)",
        "angle_to_take": "Metabolic Research Center (1.94K, US) is a 40-yr-old multi-location chain weight-loss brand — not a creator-coach. Drop.",
    },

    "andy@healthcoachandy.com": {
        "category": "nutrition",
        "niche": "AU BHSc Nutrition Bioscience health coach — 12-week 40+ Rebuild program for men (metabolic syndrome, blood sugar, food addiction, body weight) (Health Coach Andy, 1.83K)",
        "segment_original": "AU Health Coach (Men 40+, 12-week program)",
        "industry": "Functional Nutrition Coach (B2C, niche=men 40+)",
        "angle_to_take": "Health Coach Andy (1.83K, AU) — BHSc Nutrition coach running a 12-week 40+ Rebuild program for men with 24/7 email support. Frame a branded 40+ Rebuild app with 12-week cohort tracker + biomarker / behavior-change milestones + 24/7 message thread (replacing email support) — fits the high-contact program format he sells.",
    },

    # BestSource Nutrition is a supplement / wellness e-commerce brand, not a
    # single creator-coach with a method.
    "care@bestsourcenutrition.com": {
        "category": "drop",
        "niche": "IN supplement + wellness e-commerce brand — supplement reviews + diet tips + free phone consultation (BestSource Nutrition, 1.73K)",
        "segment_original": "IN Supplement E-Commerce Brand (off-format)",
        "industry": "n/a (drop — e-commerce brand, not creator-coach)",
        "angle_to_take": "BestSource Nutrition (1.73K, IN) is a supplement / wellness e-commerce brand with a generic care@ inbox. Brand voice, not a method-teaching creator. Drop.",
    },

    "hello@wholesomeliving.my": {
        "category": "nutrition",
        "niche": "MY (Australia-trained) certified Naturopath + Nutritionist (18 yrs clinical) — women's health / sleep / hormones / digestion, primarily Mandarin-speaking audience (Amanda Teh, 1.57K)",
        "segment_original": "MY Naturopath + Nutritionist (CN-language audience)",
        "industry": "Naturopath / Nutritionist (B2C, regional)",
        "angle_to_take": "Amanda Teh / Wholesome Living (1.57K, MY) — Australia-trained naturopath + nutritionist with 18 yrs clinical, primarily Mandarin-speaking women's-health audience. Frame a branded Wholesome Living app with bilingual (CN / EN) supplement-breakdown library + women's-cycle tracker + live-stream replay surface — gives a single creator-tier vs the current website + weekly-livestream split.",
    },

    "uche@rehyahealth.com": {
        "category": "nutrition",
        "niche": "Fat Loss + Metabolic Health coach — biology-first framing for insulin / muscle / inflammation, no-hype / no-punishment positioning (Dr. Uche / Rehya Health, 1.18K)",
        "segment_original": "Fat Loss + Metabolic-Health Coach (B2C)",
        "industry": "Metabolic Health Coach (B2C)",
        "angle_to_take": "Dr. Uche / Rehya Health (1.18K) — fat-loss + metabolic-health coach with a biology-first / anti-hype voice. Frame a branded Rehya Health app with metabolic-marker tracker (insulin / muscle / inflammation proxies) + fat-loss-strategy module library + cohort program — replaces the rehyahealth.com + IG-DM funnel with a structured biological-clarity member surface.",
    },
}
