"""Per-row mapping for legacy sources #7+#8 (42 rows).

Inputs:
  - data/0422/fitness/fitness_all.csv          (26 rows, no niche/seg/industry/angle)
  - data/nutrition_all_enriched.csv            (16 rows, has angle_to_take)

Output keys per email:
  category          → mindset | meditation | fitness | nutrition | drop
  niche             → 1-line factual niche label
  segment_original  → segment label (AppBillChat ICP framing)
  industry          → broad industry tag
  angle_to_take     → outreach angle copy (English, AppBillChat tone)

For nutrition_all_enriched rows the angle_to_take from the source CSV is
preserved verbatim — those were already user-approved.
"""

MAPPING: dict[str, dict[str, str]] = {

    # ============================================================
    # 0422/fitness/fitness_all.csv (26 rows)
    # ============================================================
    "movewithagnes@gmail.com": {
        "category": "fitness",
        "niche": "CA at-home pilates + yoga + strength coach for women (Akshaya Agnes / IISM-cert)",
        "segment_original": "Pilates / Yoga / Strength Coach (CA)",
        "industry": "Online Personal Training (multi-modality)",
        "angle_to_take": "IISM-cert health & fitness coach with Pilates + Yoga + Strength multi-modality. Frame a branded daily-routine app that lets her toggle modality (pilates / yoga / strength) per session — replaces split YouTube playlists with a single client-facing portal. Cost saving on email + scattered tool sprawl.",
    },
    "lottie@lottiemurphy.com": {
        "category": "fitness",
        "niche": "GB online Pilates teacher with 13yr studio + on-demand library (Lottie Murphy)",
        "segment_original": "Online Pilates Studio (GB)",
        "industry": "Pilates Studio (online)",
        "angle_to_take": "GB Pilates teacher with 13yr classes + on-demand library. Position a branded Lottie-Murphy app with daily-class calendar + length filter (5/15/30 min) + member tier — replaces splintered membership platform with a single branded studio app. Cost saving on Stripe/Vimeo/Mailchimp stack.",
    },
    "hello@lottiemurphy.com": {
        "category": "fitness",
        "niche": "GB online Pilates teacher with 13yr studio + on-demand library (Lottie Murphy, hello inbox)",
        "segment_original": "Online Pilates Studio (GB)",
        "industry": "Pilates Studio (online)",
        "angle_to_take": "Same Lottie Murphy channel — alternate hello@ inbox. Frame the branded studio-app pitch with same modality but emphasize that a single app collapses both inboxes into one in-app messaging surface — cost saving on duplicate inbox monitoring.",
    },
    "info@yoqi.com": {
        "category": "mindset",
        "niche": "US yoga + qigong + mindfulness-in-motion school (Yoqi)",
        "segment_original": "Yoga + Qigong Hybrid School (US)",
        "industry": "Yoga / Qigong School (online)",
        "angle_to_take": "US yoga + qigong school teaching mindfulness-in-motion. Frame a branded Yoqi app that bundles yoga + qigong daily routines with energy-tracking journal + breathwork timer — replaces YouTube + free-resource site sprawl with a single member-tier portal. Cost saving on multi-platform delivery.",
    },
    "yogaworldtx@gmail.com": {
        "category": "mindset",
        "niche": "US multi-instructor yoga collective (YOGATX, weekly drops + bonus eps)",
        "segment_original": "Yoga Multi-Instructor Channel (US)",
        "industry": "Yoga Channel (multi-creator)",
        "angle_to_take": "US yoga collective with weekly Monday drops + Wednesday bonus. Position a branded multi-instructor app where each teacher gets a roster card + tag-filter (instructor / level / length) and patrons tier in via in-app subscription — replaces Patreon as the membership backbone. Cost saving on Patreon take-rate.",
    },
    "pr@patreon.com": {
        "category": "drop",
        "niche": "Generic Patreon support inbox surfaced via YOGATX channel — not actionable",
        "segment_original": "Generic platform support address",
        "industry": "n/a (drop)",
        "angle_to_take": "Patreon's generic PR address — not the creator's inbox. Drop from outreach.",
    },
    "preeti@yogbela.com": {
        "category": "mindset",
        "niche": "IN online yoga tutorials with class-like experience (YogBela / Preeti)",
        "segment_original": "IN Online Yoga Teacher",
        "industry": "Yoga Teacher (online)",
        "angle_to_take": "IN solo yoga teacher with focus on real-class-experience tutorials. Frame a branded YogBela app with live + on-demand class calendar + Q&A surface — moves her free YouTube audience into a paid member tier with brand identity intact.",
    },
    "office@greenblau.com": {
        "category": "mindset",
        "niche": "US yoga teacher + author (Jessamyn Stanley) routed via talent agency Greenblau",
        "segment_original": "US Yoga Teacher + Author (talent-rep'd)",
        "industry": "Yoga Author / Speaker",
        "angle_to_take": "Jessamyn Stanley — author + yoga teacher routed via Greenblau talent agency. Position a branded Jessamyn app spanning yoga classes + book companion + speaker-event calendar — fits a public-figure brand stack better than off-the-shelf platforms. Pitch through the agency contact (Greenblau) as a brand-extension play.",
    },
    "hello@joellefixson.com": {
        "category": "mindset",
        "niche": "DE bite-sized yoga for body+mind aches (Yoga with Joelle)",
        "segment_original": "DE Online Yoga Teacher (bite-sized format)",
        "industry": "Yoga Teacher (online)",
        "angle_to_take": "DE yoga teacher with bite-sized class format addressing aches/pains. Frame a branded Joelle app with length filter (5/10/15 min) + body-area tag (neck / lower back / hips) + daily-routine builder — replaces YouTube-only delivery with a paid member tier.",
    },
    "collab@yoursalbany.com": {
        "category": "fitness",
        "niche": "US easy at-home Pilates + Flow + Strength + Prenatal (Arianna Elizabeth / Bright x Salted)",
        "segment_original": "US At-Home Pilates + Yoga + Prenatal Creator",
        "industry": "Pilates / Multi-modality Coaching",
        "angle_to_take": "US at-home Pilates + Flow + Strength + Prenatal creator. Frame a branded Arianna app with modality toggle (Pilates / Flow / Strength / Prenatal) + length filter + life-stage tier (general / prenatal) — handles her unusual prenatal+general blend better than off-the-shelf fitness apps.",
    },
    "melania.antuchas@gmail.com": {
        "category": "fitness",
        "niche": "Online sculpt training for women + Pulse community + 'Forever Fit Blueprint' ebook (melania antuchas)",
        "segment_original": "Sculpt Trainer + Membership Creator",
        "industry": "Online Sculpt / Strength Coaching",
        "angle_to_take": "Online sculpt-training creator with 'Pulse by Melania' membership + ebook. Frame a branded Melania app collapsing Pulse member videos + ebook companion + dream-physique tracker into one paid-app surface — replaces link-in-bio + Stripe + ebook PDF sprawl.",
    },
    "kirra@strongsistersunited.com": {
        "category": "fitness",
        "niche": "US beginner-women dumbbell strength coach (Kirra Mitlo / Strong Sisters United)",
        "segment_original": "US Beginner-Women Strength Coach",
        "industry": "Strength Coaching (women's)",
        "angle_to_take": "US beginner-women strength coach with 9yr coaching practice. Frame a branded Strong Sisters app with dumbbell-only workout library + weekly progression chart + women-only community — replaces free-PDF + Instagram delivery with a single paid member portal. Cost saving on PDF distribution + DM-based support.",
    },
    "holisticmovementpilates@gmail.com": {
        "category": "fitness",
        "niche": "Certified Pilates instructor + Holistic Nutritionist with weekly + members-only video drops",
        "segment_original": "Pilates Instructor + Holistic Nutritionist",
        "industry": "Pilates Studio (online) + Nutrition Side",
        "angle_to_take": "Pilates instructor + Holistic Nutritionist with weekly drops + Friday members-only bonus. Frame a branded studio app combining Pilates routine library + nutrition-companion module + members-only Friday tier — replaces dual-channel split (YouTube + members) with single branded membership.",
    },
    "bigsis.biz.global@gmail.com": {
        "category": "fitness",
        "niche": "US BIGSIS music-only side channel paired with KR main BIGSIS workout brand (at-home routines)",
        "segment_original": "US BIGSIS Side-Channel (music)",
        "industry": "At-Home Workout (multi-channel)",
        "angle_to_take": "BIGSIS global side-channel for music-only routines paired to her main KR BIGSIS workout brand. Frame a branded BIGSIS app combining workout-video + corresponding-music track switcher — perfect fit for her dual-channel architecture (workout vs music). Cost saving over running 2 YouTubes.",
    },
    "pilatesplatform44@gmail.com": {
        "category": "fitness",
        "niche": "CA Pilates board-equipment workout channel (Pilates Platform)",
        "segment_original": "CA Pilates Board Workout (equipment-led)",
        "industry": "Pilates Equipment Brand + Channel",
        "angle_to_take": "CA Pilates board-equipment channel. Frame a branded Pilates-Platform companion app bundling board-specific workouts + community for board buyers — turns the equipment sale into an ongoing member-tier relationship. Cost saving over ad-hoc community management.",
    },
    "hello@nancysidhu.com": {
        "category": "mindset",
        "niche": "CA yoga teacher with mind+body+life class series (Yoga With Nancy)",
        "segment_original": "CA Online Yoga Teacher",
        "industry": "Yoga Teacher (online)",
        "angle_to_take": "CA yoga teacher framing classes around positive mind+body+life change. Frame a branded Nancy app with daily-class calendar + journaling prompt after each session — extends her positive-change framing into a daily ritual surface. Cost saving over Patreon + email broadcasts.",
    },
    "rachel@rnaagency.com": {
        "category": "fitness",
        "niche": "US RA Pilates daily at-home Pilates with consistency framing (Rachel Andrews via RNA agency)",
        "segment_original": "US At-Home Pilates Coach (agency-routed)",
        "industry": "Pilates Coaching (online)",
        "angle_to_take": "US RA Pilates with daily at-home Pilates focus, routed via RNA agency. Position a branded RA-Pilates app with streak tracker + at-home equipment filter (mat / dumbbell / band) + members-only program ladder — anchors her daily-consistency framing. Pitch as agency brand-extension.",
    },
    "help@skool.com": {
        "category": "drop",
        "niche": "Generic Skool platform support inbox surfaced via HOME WORKOUT STUDIO — not actionable",
        "segment_original": "Generic platform support address",
        "industry": "n/a (drop)",
        "angle_to_take": "Skool's generic help inbox — not the creator's. Drop from outreach.",
    },
    "myleedance@daum.net": {
        "category": "drop",
        "niche": "KR MYLEEFit at-home fitness — KR-origin channel (excluded by region policy)",
        "segment_original": "KR At-Home Fitness Channel",
        "industry": "n/a (drop, KR)",
        "angle_to_take": "Korean MYLEEFit channel — KR is excluded per outreach policy. Drop.",
    },
    "support@onlineyogateaching.com": {
        "category": "mindset",
        "niche": "US online yoga teacher with 350+ free classes + paid modules (Online Yoga Teaching / Cat de Rham)",
        "segment_original": "US Online Yoga Teacher (free + paid mix)",
        "industry": "Yoga Teacher (online)",
        "angle_to_take": "US yoga teacher with 350+ free classes + paid modules. Frame a branded app collapsing the free/paid split into a single class-library with member-tier gating — preserves her free-funnel-to-paid model but removes the platform-juggling tax.",
    },
    "morganchurch8050@gmail.com": {
        "category": "fitness",
        "niche": "US fitness creator routed via paid-promotion manager (Courteney Fisher Fitness)",
        "segment_original": "US Fitness Creator (paid-promo manager)",
        "industry": "Fitness Creator (manager-routed)",
        "angle_to_take": "Paid-promotion manager inbox for Courteney Fisher Fitness. Lead with manager-friendly pitch: a branded Courteney app as a non-conflicting brand-deal supplement (her own product, no sponsor compete) — cost saving over relying solely on rotating brand deals.",
    },
    "katy@sculptpilates.co.uk": {
        "category": "fitness",
        "niche": "GB online Pilates virtual studio (Katy Bath / Sculpt Pilates)",
        "segment_original": "GB Online Pilates Studio (virtual subscription)",
        "industry": "Pilates Studio (online)",
        "angle_to_take": "GB Pilates teacher running katybathpilates.com virtual studio. Position a branded Sculpt-Pilates app replacing the standalone web studio — same subscription model, native mobile experience + push retention. Cost saving on web-app dev/maintenance vs branded app.",
    },
    "strengthteacher@gmail.com": {
        "category": "fitness",
        "niche": "CA strength coach selling ebooks + coaching via stan.store (The Strength Classroom)",
        "segment_original": "CA Online Strength Coach (Stan-store funnel)",
        "industry": "Strength Coaching (online)",
        "angle_to_take": "CA strength coach with Stan-store ebook + coaching funnel. Frame a branded Strength-Classroom app collapsing ebook delivery + coaching intake + program library into one paid-app surface — replaces stan.store + DM-driven onboarding. Cost saving on funnel sprawl.",
    },
    "homeworkout011@gmail.com": {
        "category": "fitness",
        "niche": "IN HOME WORKOUT physical-fitness + healthy-living tutorial channel",
        "segment_original": "IN Home Workout Channel (general fitness)",
        "industry": "At-Home Fitness Channel",
        "angle_to_take": "IN home-workout tutorial channel covering exercise + physical fitness + healthy-living. Frame a branded HOME-WORKOUT app with category-tabs (workout / nutrition / wellness) + daily-routine builder — converts free YouTube views into member-tier subscribers. Cost saving over ad-only monetization.",
    },
    "asaptheworkout@gmail.com": {
        "category": "fitness",
        "niche": "US ASAP Athletic Strength And Power — educational behind-the-scenes top training centers (Ted Lambrinides)",
        "segment_original": "US Athletic Strength Education Channel",
        "industry": "Strength & Conditioning Education",
        "angle_to_take": "US ASAP educational channel with behind-the-scenes content from top training centers. Frame a branded ASAP app aggregating educational deep-dives + member-tier coaching plans + program-library — turns one-off video views into paid pro-coach subscriptions. Cost saving over per-program landing pages.",
    },
    "erin@ecfitstrength.com": {
        "category": "fitness",
        "niche": "US science-based strength training for endurance athletes (ECFIT Performance Strength / Erin)",
        "segment_original": "US Endurance-Athlete Strength Coach",
        "industry": "Strength Coaching (endurance niche)",
        "angle_to_take": "US strength coach for runners/cyclists/triathletes with science-based programming. Frame a branded ECFIT app with sport-specific program tracks (running / cycling / triathlon) + endurance-strength session builder — fits the multi-sport ICP that off-the-shelf strength apps miss. Cost saving over per-sport email funnels.",
    },

    # ============================================================
    # data/nutrition_all_enriched.csv (16 rows)
    # angle_to_take preserved verbatim from source.
    # ============================================================
    "kiransagar@shredfix.com": {
        "category": "fitness",
        "niche": "IN ISSA-cert nutritionist + S&C coach + ShredFix online program founder (Kiran Sagar)",
        "segment_original": "IN Online S&C + Nutrition Coach (ShredFix)",
        "industry": "Online Personal Training + Nutrition",
        "angle_to_take": "Lead with questions around his \"Esthetic Transformation\" worldwide online-coaching program and client-gallery funnel (Wix site). Position the app as a branded ShredFix client companion with transformation tracker + Wix funnel replacement.",
    },
    "shredfixteam@gmail.com": {
        "category": "fitness",
        "niche": "ShredFix team email for appointment booking + WhatsApp +91-9019169276",
        "segment_original": "IN Online S&C + Nutrition Coach (ShredFix, team inbox)",
        "industry": "Online Personal Training + Nutrition",
        "angle_to_take": "Team email for appointment booking (+91-9019169276 phone intake). Frame a branded client-intake + appointment portal replacing phone-and-Wix workflow—cost saving on admin overhead.",
    },
    "rosemarycp24@gmail.com": {
        "category": "nutrition",
        "niche": "Certified nutrition coach with recipe-led healthy-food content (Nutrition Coach Rose)",
        "segment_original": "Holistic Nutrition + Recipe Creator",
        "industry": "Nutrition Coaching (online)",
        "angle_to_take": "Lead with questions around recipe-content monetization and fitness-advice cross-sell. Position the app as a branded Rose-nutrition companion with recipes, workouts, and styling tips—cost saving over YouTube-only monetization.",
    },
    "orders@nationalnutrition.ca": {
        "category": "nutrition",
        "niche": "CA online vitamin/supplement/sports-nutrition retailer (National Nutrition, 25yr Orillia store)",
        "segment_original": "CA Supplement Retailer (B2B2C)",
        "industry": "Supplement E-Commerce",
        "angle_to_take": "Retailer orders address for National Nutrition (CA health-products store). Frame as B2B2C branded shopping-companion app for retail customers—cost saving on scattered role-inbox coordination.",
    },
    "cnpa@nationalnutrition.ca": {
        "category": "nutrition",
        "niche": "CA National Nutrition CNPA (Certified Natural Health Products Advisor) channel",
        "segment_original": "CA Supplement Retailer (CNPA advisor)",
        "industry": "Supplement E-Commerce",
        "angle_to_take": "National Nutrition CNPA (Certified Natural Health Products Advisor) channel. Position a branded shopping + advisor-consult app unifying multiple role inboxes—cost saving as primary.",
    },
    "francais@nationalnutrition.ca": {
        "category": "nutrition",
        "niche": "CA National Nutrition FR-language customer inbox",
        "segment_original": "CA Supplement Retailer (FR inbox)",
        "industry": "Supplement E-Commerce",
        "angle_to_take": "National Nutrition FR-language customer inbox. Frame a branded multilingual shopping-companion app with FR/EN toggle—cost saving on per-language inbox fragmentation.",
    },
    "hr@nationalnutrition.ca": {
        "category": "nutrition",
        "niche": "CA National Nutrition HR inbox (internal, not customer-pitch)",
        "segment_original": "CA Supplement Retailer (HR inbox — internal)",
        "industry": "Supplement E-Commerce",
        "angle_to_take": "HR inbox for National Nutrition — internal, not a customer-pitch target. Cost-saving angle only if pursuing a corporate-team app; otherwise skip.",
    },
    "darren@nationalnutrition.ca": {
        "category": "nutrition",
        "niche": "CA National Nutrition named contact (Darren) for warm internal-champion outreach",
        "segment_original": "CA Supplement Retailer (named champion)",
        "industry": "Supplement E-Commerce",
        "angle_to_take": "Named personal contact inside National Nutrition. Frame as warm internal-champion conversation around a branded customer-shopping app—cost saving over Mailchimp + scattered inboxes.",
    },
    "neenarseth@gmail.com": {
        "category": "nutrition",
        "niche": "IN dietitian + therapeutic-diet/weight-loss expert with WhatsApp +91 9811762690 funnel (Dietitian NEENA Sseth)",
        "segment_original": "IN Therapeutic-Diet Coach (WhatsApp funnel)",
        "industry": "Nutrition Coaching (online)",
        "angle_to_take": "Lead with questions around her paid-diet-plan order volume and WhatsApp-based client management (+91 9811762690). Position the app as a branded diet-plan delivery + WhatsApp-replacement with meal-plan modules.",
    },
    "career@finesseinstitute.in": {
        "category": "nutrition",
        "niche": "IN Finesse Institute of Hospitality and Wellness Management — Chandigarh nutrition+dietitian certification school",
        "segment_original": "IN Nutrition Certification School",
        "industry": "Nutrition Education (B2C)",
        "angle_to_take": "Institute with multi-domain career/enrollment inboxes (IN). Frame a branded course-delivery + student-community app replacing scattered enrollment inboxes—cost saving on admin overhead.",
    },
    "career.finesseinstitute@gmail.com": {
        "category": "nutrition",
        "niche": "IN Finesse Institute alternate enrollment inbox (gmail)",
        "segment_original": "IN Nutrition Certification School (alt inbox)",
        "industry": "Nutrition Education (B2C)",
        "angle_to_take": "Alternate Finesse Institute enrollment inbox. Same angle: branded course + student-community app consolidating both inboxes—cost saving as primary.",
    },
    "office@slaviclabs.com": {
        "category": "nutrition",
        "niche": "PL Sroka Dietcoach (Slavic Labs) — biohacking/diet/peptide content with Klaviyo+Shopify+WordPress stack",
        "segment_original": "PL Diet Coach (multi-platform stack)",
        "industry": "Nutrition Coaching (online, EU)",
        "angle_to_take": "Slavic Labs brand with Klaviyo/Shopify/WordPress sprawl (PL dietcoach). Position the app as a consolidated branded Sroka-Dietcoach companion absorbing email/shop/content—cost saving across three-tool stack.",
    },
    "seb@influencernexus.com": {
        "category": "nutrition",
        "niche": "Danielle the Dietitian — fat-loss + flexible-eating online course / group nutrition program (InfluencerNexus agency)",
        "segment_original": "Online Dietitian (agency-routed)",
        "industry": "Nutrition Coaching (online)",
        "angle_to_take": "InfluencerNexus agency address for Danielle the Dietitian. Frame partnership around a branded online course + group nutrition program app—complementary to agency brand deals.",
    },
    "robert@dietfreelife.com": {
        "category": "nutrition",
        "niche": "US Robert Ferguson — clinical nutritionist + author with Calendly/Kajabi/Linktree/WordPress stack (Diet Free Life)",
        "segment_original": "US Clinical Nutrition Author (multi-platform stack)",
        "industry": "Nutrition Coaching + Author",
        "angle_to_take": "Diet Free Life author with Calendly/Kajabi/Linktree/WordPress stack. Position the app as a branded Diet-Free-Life environment consolidating booking/course/link-in-bio/site—cost saving across four tools.",
    },
    "info@dietfreelife.com": {
        "category": "nutrition",
        "niche": "Diet Free Life role-based inbox (alt to robert@)",
        "segment_original": "US Clinical Nutrition Author (alt inbox)",
        "industry": "Nutrition Coaching + Author",
        "angle_to_take": "Role-based Diet Free Life contact — same four-tool stack (Calendly/Kajabi/Linktree/WordPress). Cost-saving angle: single branded app absorbing all four into one stack.",
    },
    "hello@stephanielong.ca": {
        "category": "nutrition",
        "niche": "CA Stephanie Long — business coach for nutritionists with ConvertKit/Kajabi/Squarespace stack",
        "segment_original": "CA Nutrition-Business Coach (B2B for nutritionists)",
        "industry": "Nutrition Coaching (B2B)",
        "angle_to_take": "Nutrition-business coach with ConvertKit/Kajabi/Squarespace stack (CA). Position the app as a branded nutrition-coach companion replacing the three-tool sprawl—cost saving and brand-coherent.",
    },
}
