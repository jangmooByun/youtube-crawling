"""Per-row LLM classification for data/2026-04-24/nutrition.csv.

Notes:
- coachrogueyt@gmail.com is a League of Legends gaming coach (pulled in by
  "macro coach" keyword ambiguity — gaming macros, not macro nutrition).
  Classified as esports/gaming; user may drop for nutrition outreach.
- rosemarycp24@gmail.com also appears in fitness.csv (same channel). Same
  classification used here for consistency.
"""

MAPPING = {
    "coachrogueyt@gmail.com": {
        "niche": "League of Legends coaching & esports content (miscategorized from macro-coach keyword)",
        "segment_original": "Esports Coaching",
        "industry": "Gaming / esports coaching",
        "angle_to_take": (
            "Lead with discovery around the Patreon + Discord + YouTube "
            "patchwork, how paid coaching VODs get delivered, and how the "
            "community scales beyond a public Discord. Position the app as a "
            "branded esports environment—VOD library, 1:1 coaching sessions, "
            "private community with push alerts, Patreon-tier content—more "
            "premium than three disconnected tools and retention-focused for "
            "a gaming audience that drifts between creators."
        ),
    },
    "rosemarycp24@gmail.com": {
        "niche": "Holistic nutrition & lifestyle coaching",
        "segment_original": "Holistic Nutrition & Lifestyle Coaching",
        "industry": "Wellness / nutrition",
        "angle_to_take": (
            "Ask how she delivers recipes and wellness content today, whether "
            "subscribers come back weekly without the algorithm picking them, "
            "and where the resource sprawl lives. Frame the app as a branded "
            "wellness hub for her recipes, nutrition guidance, and lifestyle "
            "content—with push reminders and personalization so engaged "
            "viewers become retained members instead of drifting between "
            "uploads."
        ),
    },
    "shelly@skinnylouisiana.com": {
        "niche": "Diabetes & prediabetes nutrition for women 40+",
        "segment_original": "Specialized Diabetes & Women's Nutrition Coaching",
        "industry": "Healthcare / nutrition / women's health",
        "angle_to_take": (
            "Lead with discovery around how clinic patients track blood "
            "sugar and protein/fiber between visits, how the Skinny "
            "Louisiana content library stays accessible, and how women 40+ "
            "feel supported without food guilt. Frame the app as a clinical-"
            "grade branded patient environment—recipe library, blood-sugar "
            "tracking, push reminders for protein targets, private Q&A—"
            "premium positioning that extends her clinic without relying on "
            "email."
        ),
    },
    "nicole@nicoleferrierfitness.com": {
        "niche": "Macro coaching & physique competition prep",
        "segment_original": "Macro Coaching & Physique Competition Prep",
        "industry": "Fitness / nutrition / competition prep",
        "angle_to_take": (
            "Ask about how macro clients track meals, how competition prep "
            "handoffs happen, and what engagement looks like between contest "
            "cycles. Position the app as a branded macro-coaching "
            "environment—daily macro logs, check-in workflows, competition "
            "timelines, push-based accountability—more premium than IG DMs "
            "and retention-focused for an audience that cycles on and off "
            "bikini prep."
        ),
    },
    "orders@nationalnutrition.ca": {
        "niche": "Supplement retail (Canadian e-commerce)",
        "segment_original": "Supplement Retail & Education",
        "industry": "E-commerce / supplements / nutrition retail",
        "angle_to_take": (
            "Start with questions about how Mailchimp list members convert "
            "into repeat store customers, how educational content ties back "
            "to product pages, and how they compete with Amazon on trust. "
            "Frame the app as a branded retail-plus-education environment—"
            "product feed, coupon drops, educational videos, push for "
            "reorder reminders and sales—zero-CPI retention that Mailchimp "
            "alone cannot deliver."
        ),
    },
    "neenarseth@gmail.com": {
        "niche": "Therapeutic diet planning & weight loss (online)",
        "segment_original": "Therapeutic & Weight Loss Dietetics",
        "industry": "Healthcare / dietetics",
        "angle_to_take": (
            "Lead with discovery around how online diet plans get delivered "
            "internationally, how she handles the WhatsApp + Facebook + "
            "Gmail funnel, and what retention looks like between diet-plan "
            "cycles. Position the app as a branded dietitian-led "
            "environment—personalized plan delivery, progress tracking, "
            "push check-ins, private Q&A—premium positioning for a "
            "scientifically-grounded practice that deserves more than a "
            "WhatsApp-plus-Facebook-page presence."
        ),
    },
    "eatwell@elainedietitian.com": {
        "niche": "Bilingual EN/CN registered dietitian",
        "segment_original": "Bilingual Registered Dietitian Coaching",
        "industry": "Healthcare / dietetics / bilingual",
        "angle_to_take": (
            "Lead with questions around the Jane App + Stripe + Wix workflow "
            "and how she delivers bilingual EN/CN content to a multicultural "
            "patient base. Frame the app as a branded clinic environment—"
            "appointment booking, recipe library, diabetes/cholesterol "
            "protocols, push check-ins in both languages—more premium and "
            "retention-focused than three disconnected tools, built for "
            "patients who deserve consistent bilingual support."
        ),
    },
    "career@finesseinstitute.in": {
        "niche": "Nutrition & dietetics certification training",
        "segment_original": "Nutrition Certification Training",
        "industry": "Education / vocational training / nutrition",
        "angle_to_take": (
            "Ask about how career aspirants move from free YouTube to paid "
            "diploma enrollment, and how they deliver certification "
            "coursework today. Position the app as a branded nutrition-"
            "education environment—course modules, progress tracking, exam "
            "prep, cohort community, push reminders—premium positioning that "
            "helps Chandigarh-based Finesse compete with bigger players on "
            "student experience."
        ),
    },
    "seb@influencernexus.com": {
        "niche": "Fat loss & flexible eating group coaching",
        "segment_original": "Fat Loss & Flexible Eating Coaching",
        "industry": "Wellness / nutrition / weight management",
        "angle_to_take": (
            "Start with discovery around how online course students and "
            "group program members stay accountable beyond the course, and "
            "how she scales without 1:1 burnout. Frame the app as a branded "
            "fat-loss environment—course library, group cohort feed, "
            "progress tracking, push-based accountability—more polished than "
            "course-host-plus-Gmail and retention-focused for an all-foods-"
            "fit audience."
        ),
    },
    "nsaffo@nk-fitness.com": {
        "niche": "Lifestyle dietitian (fitness + nutrition + beauty)",
        "segment_original": "Lifestyle Dietitian & Wellness Coaching",
        "industry": "Wellness / nutrition / lifestyle",
        "angle_to_take": (
            "Ask about how nutrition services sell through the NK-Fitness "
            "WordPress site, and how she ties her IG and TikTok audience "
            "back to paid coaching. Position the app as a branded lifestyle-"
            "dietitian environment—nutrition service bookings, recipes, "
            "beauty-plus-wellness content, push reminders—more premium than "
            "WordPress and retention-focused for an audience that cares "
            "about aesthetics as much as nutrition."
        ),
    },
    "prachi.nutritionist@gmail.com": {
        "niche": "Clinical nutrition (therapeutic diets)",
        "segment_original": "Clinical Dietetics & Therapeutic Diet Coaching",
        "industry": "Healthcare / dietetics",
        "angle_to_take": (
            "Start with questions around how online-and-offline "
            "consultations flow together, how PCOS/thyroid/diabetes clients "
            "stay on their plans between sessions, and how IG drives "
            "conversions. Frame the app as a branded clinical-nutrition "
            "environment—personalized plans by condition, progress check-"
            "ins, educational library, push reminders—premium positioning "
            "that matches her M.Sc. credentials beyond a free IG session "
            "funnel."
        ),
    },
    "dieticiangarima@gmail.com": {
        "niche": "Sustainable meal planning for busy people",
        "segment_original": "Busy-People Sustainable Meal Planning",
        "industry": "Healthcare / dietetics",
        "angle_to_take": (
            "Ask about how she delivers condition-focused plans (diabetes, "
            "PCOS, thyroid) to busy professionals and what retention looks "
            "like once they leave 1:1. Position the app as a branded "
            "dietitian environment—condition-specific meal plans, grocery-"
            "friendly swaps, push reminders, private Q&A—more premium than a "
            "free YouTube feed and retention-focused for busy clients who "
            "need actionable consistency."
        ),
    },
    "dietadvisory@gmail.com": {
        "niche": "Hospital-affiliated clinical dietitian",
        "segment_original": "Hospital-Affiliated Clinical Dietetics",
        "industry": "Healthcare / dietetics / hospital partnerships",
        "angle_to_take": (
            "Lead with discovery around how phone consultations schedule, "
            "how patients from Dharwad-Hubli stay engaged post-visit, and "
            "how hospital referrals flow. Frame the app as a clinical-grade "
            "branded environment—appointment booking, personalized plans, "
            "push reminders, secure Q&A—premium positioning that matches "
            "her 10-year consultant credibility and extends hospital care "
            "beyond phone calls."
        ),
    },
    "askus@inchealthy.com": {
        "niche": "Team-led evidence-based nutrition practice",
        "segment_original": "Evidence-Based Team Dietetics",
        "industry": "Healthcare / dietetics / group practice",
        "angle_to_take": (
            "Ask about how the team of RDs coordinates virtual "
            "consultations, how their evidence-based content library stays "
            "accessible, and what retention looks like between consults. "
            "Position the app as a branded dietetic-team environment—"
            "consultation booking across multiple RDs, content library, "
            "push reminders, private Q&A—premium positioning that matches a "
            "team practice and retention-focused in a field where annual "
            "checkups drift to yearly."
        ),
    },
    "meghanlkozlowski@gmail.com": {
        "niche": "Macro coaching with mindset-first approach",
        "segment_original": "Macro Coaching & Mindset Re-Wiring",
        "industry": "Wellness / nutrition / behavior change",
        "angle_to_take": (
            "Start with discovery around how 'all-or-nothing' thinkers "
            "break patterns, how 1:1 and group clients stay engaged between "
            "macro check-ins, and how mindset exercises actually land. "
            "Frame the app as a branded behavior-change environment—macro "
            "tracking, mindset prompts, group cohort feed, push "
            "accountability—premium positioning for an MPH-credentialed "
            "coach doing deeper work than generic macro apps."
        ),
    },
}
