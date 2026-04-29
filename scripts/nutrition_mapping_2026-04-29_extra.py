"""Per-row mapping for data/2026-04-29/nutrition_enriched_extra.csv (8 rows).

Combined-dict format (same as legacy_mapping / mindful_mapping):
  email → {category, niche, segment_original, industry, angle_to_take}

Surfaced via the 04-29 extra nutrition sweep (healthy meal prep / clean
eating / anti-inflammatory keywords, 3 × 1 page). 3 emails are duplicates
of S4 (Dr Shikha / Healthy Emmie / Mr B-fit) — same profile_url, dedup'd
by build_total. Category routing: nutrition 6 / drop 2.
"""

MAPPING: dict[str, dict[str, str]] = {

    # Same email + same profile_url as S4 row — build_total dedup keeps
    # whichever entry is richer. Routing must match S4 (nutrition).
    "drshikhasingh24@gmail.com": {
        "category": "nutrition",
        "niche": "IN clinical nutritionist + weight-loss coach (Hippocreators-managed) — 2.97M YouTube + 1.2M IG, paid weight-loss services + diet plans (Dr. Shikha Singh, 2.97M)",
        "segment_original": "IN Clinical Nutritionist + Weight-Loss Coach (mass-creator)",
        "industry": "Clinical Nutritionist (B2C, mass-market)",
        "angle_to_take": "Dr. Shikha Singh (2.97M, IN) — India's leading clinical nutritionist with paid weight-loss services + diet plans, currently managed by Hippocreators. Frame a branded Dr. Shikha app with diet-plan template library + weight-loss cohort tracker + paid 1-on-1 booking + brand-collab inquiry tab — replaces the email-based intake bottlenecking the paid services pipeline at her scale.",
    },

    "enquiries@chefjackovens.com": {
        "category": "nutrition",
        "niche": "AU Adelaide pro chef (14+ yrs commercial kitchens) — high-protein meal prep + comfort-food classics, no-BS recipe creator (Chef Jack Ovens, 1.62M)",
        "segment_original": "AU Pro Chef + High-Protein Meal-Prep Creator",
        "industry": "Pro Chef / Healthy-Cooking Creator (B2C)",
        "angle_to_take": "Chef Jack Ovens (1.62M, AU) — Adelaide pro chef with 14+ yrs commercial-kitchen experience running high-protein meal-prep + comfort-food classics. Frame a branded Chef Jack app with recipe library by protein-target + meal-prep cohort tracker + creator-store for cookware / merch + brand-collab inquiry tab — replaces the chefjackovens.com + IG-DM funnel with a single creator-controlled member surface.",
    },

    "kennedy@smallscreenmarketing.com": {
        "category": "nutrition",
        "niche": "Gluten-free + healthy recipes creator with self-published ebook (Healthy Food Made Easy, 85 recipes) — IBS-driven story (fitfoodieselma, 1.11M)",
        "segment_original": "Gluten-Free / IBS-Aware Healthy-Recipes Creator + Ebook",
        "industry": "Healthy-Recipes Creator + Ebook (B2C, agency-managed)",
        "angle_to_take": "fitfoodieselma (1.11M, agency-managed via Small Screen Marketing) — gluten-free + healthy-recipes creator with an IBS-driven brand story and a self-published ebook (Healthy Food Made Easy). Frame a branded fitfoodieselma app with gluten-free recipe library + IBS-friendly recipe filter + ebook-as-flagship + Stan-store-style merch surface — replaces the fitfoodieselma.com + IG funnel with a creator-controlled member tier (and keeps Small Screen agency for brand deals).",
    },

    # Same email as S4 nutrition row (different channel rows under same
    # role-based inbox).
    "mrbfitbusiness@gmail.com": {
        "category": "nutrition",
        "niche": "IN diet creator focused on easy + sustainable + tasty meals — collab-first inbox, IG + YouTube cross-channel (Mr. B-fit, 795K)",
        "segment_original": "IN Easy-Diet Creator (collab-first)",
        "industry": "Diet / Healthy-Eating Creator (B2C)",
        "angle_to_take": "Mr. B-fit (795K, IN) — diet creator with an easy + sustainable + tasty positioning, currently using a collab-first inbox. Frame a branded Mr. B-fit app with daily-recipe player + diet-plan tier (easy / sustainable / weight-loss) + IG-replacement community surface + brand-collab inquiry tab — replaces the email + IG-DM split with one paid member surface that doesn't dilute the brand-collab inbox.",
    },

    # Same email as S4 nutrition row.
    "emmie@modernmediaservices.com": {
        "category": "nutrition",
        "niche": "US plant-based + vegan weight-loss nutritionist — already runs SLIM App + Program at healthyemmieapp.org (Healthy Emmie, 745K)",
        "segment_original": "US Plant-Based Weight-Loss Nutritionist (own app + program)",
        "industry": "Vegan Nutritionist + Coach (B2C, productized)",
        "angle_to_take": "Healthy Emmie (745K, US, agency-managed via Modern Media Services) — plant-based + vegan weight-loss nutritionist who already runs a productized SLIM App + Program at healthyemmieapp.org. Note: she has her own app already — angle here is a v2 / sister-track app (e.g. SLIM-Lite for new members or transformation-cohort layer) rather than a full replacement, OR drop if her existing app is already saturated. Treat as low-priority because of own-app overlap.",
    },

    "sandy@blutribe.space": {
        "category": "nutrition",
        "niche": "IN healthy + high-protein recipes creator (veg + non-veg) — meal-prep + weight-loss + gut-friendly clean eating, blutribe.blubox-managed (Sandy Talkies, 68.1K)",
        "segment_original": "IN High-Protein Recipes + Clean-Eating Creator (agency-managed)",
        "industry": "Healthy-Recipes Creator (B2C, agency-managed)",
        "angle_to_take": "Sandy Talkies (68.1K, IN) — high-protein recipes creator (veg + non-veg) with meal-prep + clean-eating positioning, managed by blutribe.blubox. Frame a branded Sandy Talkies app with recipe library by protein-target + office-lunch / meal-prep tracker + IG-replacement community surface — replaces the IG-DM intake with a structured creator-tier (and keeps the agency for brand-collab pipeline).",
    },

    # Vague "Health & lifestyle diary" — vlog-style lifestyle content with
    # a manager email; not a nutrition coach with a method.
    "miranda@vivemanagement.com.au": {
        "category": "drop",
        "niche": "AU Perth lifestyle vlogger (Health & lifestyle diary) — multi-vertical (vlog + co-owner of @mademonday__) with manager email (Vive Management) (Miranda Brady, 42.3K)",
        "segment_original": "AU Lifestyle Vlogger (multi-vertical, manager-funneled)",
        "industry": "n/a (drop — lifestyle vlogger, not nutrition coach)",
        "angle_to_take": "Miranda Brady (42.3K, AU) is a Perth-base lifestyle vlogger with a multi-vertical mix (vlog + a co-owned brand @mademonday__) and a manager-email funnel. Vague 'Health & lifestyle diary' framing without a nutrition method or productized program. Drop.",
    },

    # Multi-vertical lifestyle (recipes + Melbourne life + home decor + travel)
    # — recipes are a side, not the primary niche.
    "toniiuh@gmail.com": {
        "category": "drop",
        "niche": "AU Melbourne multi-vertical lifestyle vlogger — healthy recipes mixed with home decor + travel + life-in-Melbourne, recipes are not the primary niche (Tonia Camachas, 28.3K)",
        "segment_original": "AU Multi-Vertical Lifestyle Vlogger (recipes + decor + travel)",
        "industry": "n/a (drop — multi-vertical lifestyle, not nutrition primary)",
        "angle_to_take": "Tonia Camachas (28.3K, AU) — Melbourne lifestyle vlogger blending healthy recipes with home decor + travel + life-in-Melbourne. Recipes are a side, not the primary niche. No method or productized program. Drop.",
    },
}
