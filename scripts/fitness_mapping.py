"""Per-row LLM classification for data/2026-04-24/fitness.csv."""

MAPPING = {
    "kiransagar@shredfix.com": {
        "niche": "Online fat loss & women's health coaching",
        "segment_original": "Specialized Health Coaching (Women's Health & Weight Loss)",
        "industry": "Wellness / women's health",
        "angle_to_take": (
            "Lead with discovery around client follow-through, protocol adherence "
            "between sessions, and how PCOS and women's-health clients stay engaged "
            "after a transformation starts. Position the app as a branded client "
            "companion for plans, daily check-ins, and private community—replacing "
            "a patchwork of Wix, WhatsApp, and DMs with a premium environment "
            "clients feel supported inside every day."
        ),
    },
    "kontakt@coachlatif.com": {
        "niche": "Multi-language fitness transformation",
        "segment_original": "Multi-Language Transformation Coaching",
        "industry": "Fitness / online coaching",
        "angle_to_take": (
            "Lead with questions around content localization across EN/AR/DE, "
            "store conversions, and client retention across markets. Frame the "
            "app as a branded transformation environment where programs, store, "
            "and push-based accountability live in one place—more polished and "
            "retention-focused than WordPress + email for a 7M-follower audience "
            "that deserves premium positioning."
        ),
    },
    "rich@theviralistgroup.com": {
        "niche": "1:1 online fitness & body confidence coaching",
        "segment_original": "Body Confidence & Physique Coaching",
        "industry": "Fitness / mindset",
        "angle_to_take": (
            "Start with discovery around audience ownership—right now his traffic "
            "runs through Beacons and YouTube, and none of it is his. Position the "
            "app as a zero-CPI branded home for 1:1 application flow, program "
            "delivery, and push-based accountability, so he owns the audience, the "
            "data, and the retention loop instead of renting them on public "
            "platforms."
        ),
    },
    "rosemarycp24@gmail.com": {
        "niche": "Holistic nutrition & lifestyle coaching",
        "segment_original": "Holistic Nutrition & Lifestyle Coaching",
        "industry": "Wellness / nutrition",
        "angle_to_take": (
            "Ask how she delivers recipes and wellness content today, whether "
            "subscribers come back weekly without the algorithm picking them, and "
            "where the resource sprawl lives. Frame the app as a branded wellness "
            "hub for her recipes, nutrition guidance, and lifestyle content—with "
            "push reminders and personalization so engaged viewers become retained "
            "members instead of drifting between uploads."
        ),
    },
    "jennclayton@yahoo.com": {
        "niche": "Peer-led Weight Watchers community coaching",
        "segment_original": "Community-Driven Weight Loss Coaching",
        "industry": "Wellness / weight management",
        "angle_to_take": (
            "Lead with questions about consolidating the Facebook group and Square "
            "Appointments into one branded member environment. Position the app as "
            "a premium community space for her weight-loss tribe—vlogs, macros "
            "content, private check-ins, and coupon drops for programs—with push "
            "retention that a Facebook group can no longer give her."
        ),
    },
    "email@typeform.com": {
        "niche": "Busy-professional fat loss coaching",
        "segment_original": "Time-Efficient Transformation Coaching",
        "industry": "Fitness / online coaching",
        "angle_to_take": (
            "Start with discovery around how applicants move from Typeform into "
            "actual program delivery, and what engagement looks like across a "
            "180-day arc. Frame the app as a branded program environment with "
            "structured milestones, push accountability, and personalized "
            "check-ins—replacing Typeform plus email drip with a premium retention "
            "surface built for long programs."
        ),
    },
    "opbisht@gmail.com": {
        "niche": "Evidence-based fitness & nutrition education",
        "segment_original": "Science-Based Fitness & Nutrition Coaching",
        "industry": "Fitness / education",
        "angle_to_take": (
            "Ask about how students consume his ACE-level content once they move "
            "past free YouTube, and where he keeps certifications, programs, and "
            "audience engaged. Position the app as a branded education hub with "
            "structured modules, progress tracking, and push reminders—premium "
            "positioning that matches his certified authority instead of a "
            "Facebook profile + YouTube mix."
        ),
    },
    "wellnessdrmeghan@gmail.com": {
        "niche": "Physician-led medical weight management",
        "segment_original": "Medical Weight Management Coaching",
        "industry": "Healthcare / obesity medicine",
        "angle_to_take": (
            "Lead with clinical context—how patients track progress between "
            "visits, how medication reminders land, and how she delivers education "
            "without compromising privacy. Frame the app as a clinical-grade "
            "branded patient environment—secure Q&A, weight tracking, medication "
            "check-ins, educational library—more polished and privacy-minded than "
            "email, and a premium extension of her Boston practice."
        ),
    },
    "kaushikbose222@gmail.com": {
        "niche": "Hybrid home & online personal training",
        "segment_original": "Hybrid Home & Online Personal Training",
        "industry": "Fitness / personal training",
        "angle_to_take": (
            "Ask about session scheduling, client reminders, and what happens "
            "between 12 monthly sessions to keep clients on track. Position the "
            "app as a branded hybrid environment for booking, workout library, "
            "progress tracking, and push reminders—replacing Wix and WhatsApp "
            "with one premium surface clients feel their Mr-India-bronze coach "
            "personally runs."
        ),
    },
    "asaptheworkout@gmail.com": {
        "niche": "Athletic strength & performance education",
        "segment_original": "Athletic Performance & Strength Coaching",
        "industry": "Sports science / athletic training",
        "angle_to_take": (
            "Start with discovery around how training centers and athletes consume "
            "their deep library, and how new drops reach subscribers instead of "
            "the algorithm. Frame the app as a branded athlete resource hub—"
            "behind-the-scenes content, program releases, push notifications for "
            "new episodes—premium positioning for a library that deserves more "
            "than a free YouTube feed."
        ),
    },
    "spandanamorem95@gmail.com": {
        "niche": "Prenatal & postnatal yoga and maternal health",
        "segment_original": "Prenatal & Postnatal Yoga Coaching",
        "industry": "Wellness / maternal health",
        "angle_to_take": (
            "Lead with privacy, emotional safety, and continuity between pregnancy "
            "trimesters and postpartum. Frame the app as a confidential members-"
            "only space for prenatal/postnatal yoga, nutrition guidance, and "
            "kids-yoga content—structured programs, private Q&A, and push "
            "reminders—far more supportive than public platforms for pregnancy-"
            "sensitive coaching."
        ),
    },
    "fitnessbyraviverma@gmail.com": {
        "niche": "Short-cycle WhatsApp-led transformation",
        "segment_original": "Fast-Track 21-Day Transformation Coaching",
        "industry": "Fitness / transformation",
        "angle_to_take": (
            "Ask how he tracks 21-day transformation clients across WhatsApp, "
            "Instagram, and Facebook, and what falls through the cracks between "
            "platforms. Position the app as a branded 21-day environment with "
            "daily push reminders, progress tracking, and a private member feed—"
            "replacing WhatsApp chaos with a premium surface where he owns the "
            "audience and client data, not Meta."
        ),
    },
    "transcripts@crooked.com": {
        "niche": "Midlife women's strength & menopause coaching",
        "segment_original": "Menopause & Women's Strength Coaching",
        "industry": "Wellness / women's fitness",
        "angle_to_take": (
            "Lead with questions around the patchwork of ConvertKit, Patreon, and "
            "Squarespace, and how menopause-specific conversations stay safe and "
            "ongoing. Frame the app as a branded midlife-women's environment for "
            "strength programs, podcast, private Q&A, and member-only content—"
            "more premium and retention-focused than three disconnected tools, "
            "and more personal than a Patreon tier."
        ),
    },
    "kwnfit@gmail.com": {
        "niche": "Anti-diet body reclamation coaching",
        "segment_original": "Anti-Diet Sustainable Fitness Coaching",
        "industry": "Wellness / women's empowerment",
        "angle_to_take": (
            "Lead with privacy, emotional safety, and how body-reclamation "
            "conversations feel on public platforms. Position the app as a "
            "private members-only space for anti-diet coaching, flexible-eating "
            "frameworks, and sensitive Q&A—push accountability and structured "
            "programs in one branded environment that matches the seriousness of "
            "the work."
        ),
    },
    "strengthcoachjazz@gmail.com": {
        "niche": "Kettlebell & functional strength coaching",
        "segment_original": "Kettlebell & Functional Strength Coaching",
        "industry": "Fitness / strength coaching",
        "angle_to_take": (
            "Ask how he delivers StrongFirst-level kettlebell education, training "
            "goals, and client retention between YouTube uploads. Frame the app "
            "as a branded strength environment—program library, technique "
            "breakdowns, personalized training plans, push-based check-ins—"
            "premium positioning that matches his SFG1 certification and keeps "
            "clients engaged beyond email."
        ),
    },
}
