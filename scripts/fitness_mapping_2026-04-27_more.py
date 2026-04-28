"""Supplementary per-row mapping for the aggressive _more sweep into
data/2026-04-27/fitness.csv. Covers the 70 newly added rows from the
PAGES=4 / MIN_SUBS=1000 deeper pull. Existing 35 rows are mapped in
fitness_mapping_2026-04-27.py and remain untouched.
"""

MAPPING = {
    # ──────────────────────────────────────────────────────────────────────
    # Mega tier (>1M)
    # ──────────────────────────────────────────────────────────────────────
    "xenia@xglow-mgmt.com": {
        "niche": "HK/BALI women's mentorship + fitness creator (emi wong, 7.42M)",
        "segment_original": "Global Women's Mentorship + Fitness Creator (manager-routed)",
        "industry": "Fitness / lifestyle + mentorship coaching",
        "angle_to_take": (
            "emi wong (7.42M, HK/Bali) — top-end fitness + lifestyle creator running a "
            "Women's Mentorship Community via google form. role-based xenia@ on xglow-mgmt.com "
            "(talent-management). Frame an AppBillChat pitch to the manager — branded emi-wong "
            "app with workout library + mentorship cohort + member-only journaling + length "
            "filter — owned mobile retention beyond the Google-form intake at this scale."
        ),
    },
    "contact@willtennyson.ca": {
        "niche": "CA fitness + food + lifestyle mega-creator (Will Tennyson, 4.79M)",
        "segment_original": "CA Fitness + Food Lifestyle Creator",
        "industry": "Fitness / food + lifestyle entertainment (CA)",
        "angle_to_take": (
            "Will Tennyson (4.79M, CA) — top-end fitness/food/lifestyle entertainer; biz "
            "inquiries split between contact@willtennyson.ca and willt@night.co (manager). "
            "role-based contact@ on personal domain. Frame a branded Will-Tennyson app with "
            "recipe + workout combo library + behind-the-scenes content + tier-gated long-form "
            "+ merch shelf — turning entertainment audience into a recurring-revenue mobile "
            "property beyond YouTube ad RPM."
        ),
    },
    "pregnancyandpostpartumtv@outloudtalent.com": {
        "niche": "CA prenatal + postpartum exercise specialist (Pregnancy and Postpartum TV / Jessica RD, 2.43M)",
        "segment_original": "CA Prenatal/Postpartum Exercise Brand (manager-routed)",
        "industry": "Wellness / prenatal + postpartum core + recovery (CA)",
        "angle_to_take": (
            "Pregnancy and Postpartum TV (2.43M, CA) — Jessica is RD + certified pregnancy / "
            "postpartum core exercise specialist; 400+ free workouts (prenatal yoga, gentle "
            "Pilates, diastasis recti-safe, postpartum strength, dance) + birth education. "
            "biz email routed via outloudtalent.com (talent agency); personal support@ also "
            "exists. Frame a branded P&P-TV app with trimester-aware class library + "
            "diastasis-recti-safe filter + birth-prep modules + member tier — natively the "
            "right form factor for the routine-based pregnancy audience the agency is "
            "monetizing."
        ),
    },
    "partnerships@midasmedia.ca": {
        "niche": "CA fitness/movement creator (Midas Movement, 1.43M)",
        "segment_original": "CA Movement Creator (low-context)",
        "industry": "Fitness / general (CA)",
        "angle_to_take": (
            "Midas Movement (1.43M, CA) — large channel with minimal description, partnerships "
            "routed via midasmedia.ca (small media co). role-based partnerships@. Pitch the "
            "agency on a branded Midas-Movement app with workout library + program tier + "
            "subscription monetization — agency-mediated outreach, framed as a creator-monetization "
            "upgrade beyond YouTube ad RPM."
        ),
    },
    # NOTE: Savikar Bhardwaj (savikarbhardwaj@gmail.com, 1.07M) was deduped out
    # — already exists in data/2026-04-25/nutrition_enriched.csv. Removed from
    # both fitness.csv rows here and from this mapping. The discover script's
    # dedup only scans RUN_ORDER categories' enriched CSVs in old dirs, so
    # cross-category overlaps (motivation/fat-loss → both nutrition + fitness)
    # slip through and need manual cleanup.

    # ──────────────────────────────────────────────────────────────────────
    # Large tier (200K~1M)
    # ──────────────────────────────────────────────────────────────────────
    "paul@teamonwardtalent.com": {
        "niche": "US 35-yr CSCS-certified strength trainer (PaulSklarXFit, 989K)",
        "segment_original": "US Strength + Functional Coach (manager-routed)",
        "industry": "Fitness / over-40/over-50 strength + functional (US)",
        "angle_to_take": (
            "Paul Sklar (989K, US) — 35-yr pro fitness trainer, CSCS, Wake Forest BS, sells "
            "PaulSklarXFit365 Training Program. biz routed via teamonwardtalent.com (manager). "
            "Frame a branded Paul-Sklar app with PaulSklarXFit365 program calendar + over-40 / "
            "over-50 progression tracker + form-cue library + member tier — manager-pitched "
            "creator-monetization upgrade for an audience that converts on structured programs."
        ),
    },
    "Connor@28thave.com": {
        "niche": "Online fitness coach + entertainer (Connor Sinann, 787K)",
        "segment_original": "Global Online Fitness Coach (manager-routed)",
        "industry": "Fitness / online 1:1 coaching",
        "angle_to_take": (
            "Connor Sinann (787K) — entertainer + online fitness coach with 1:1 Apply-To-Work-"
            "With-Me funnel; brand deals/contact via 28thave.com (mgmt). personal-name @ mgmt "
            "domain. Frame a branded Connor-Sinann app with cohort-based program calendar + "
            "form-cue library + 1:1 application intake + member tier — replacing the "
            "application-form funnel with mobile-native cohort onboarding."
        ),
    },
    "ccchhtt23@gmail.com": {
        "niche": "NZ at-home workout creator (Hailey C., 770K)",
        "segment_original": "NZ At-Home Workout Creator",
        "industry": "Fitness / at-home workouts (NZ)",
        "angle_to_take": (
            "Hailey C. (770K, NZ) — short-form at-home workouts that 'actually work', minimal "
            "description with biz funnel via instagram + gmail. personal gmail. Frame a branded "
            "Hailey-C app with short-workout library (5/10/15min) + length filter + workout-"
            "streak tracker + tier-gated programs — packaging the highly-engaged short-form "
            "audience into a daily-use mobile habit."
        ),
    },
    "management@scottburnhard.com": {
        "niche": "US calisthenics + street-workout celebrity trainer (Scott Burnhard, 562K)",
        "segment_original": "US Calisthenics + Street-Workout Coach",
        "industry": "Fitness / calisthenics + bodyweight (US)",
        "angle_to_take": (
            "Scott Burnhard (562K, US) — NYC-based motivational speaker + calisthenics / "
            "street-workout celebrity trainer with online + offline coaching off "
            "scottburnhard.com. role-based management@. Frame a branded Scott-Burnhard app "
            "with calisthenics progression tracker (push/pull/handstand milestones) + "
            "street-workout video library + 1:1 + offline-class scheduling + member tier — "
            "replacing the multi-channel coaching funnel with one mobile property."
        ),
    },
    "support@jennacollinsfitness.com": {
        "niche": "NZ at-home low-impact functional fitness with existing CaliFit Studio app (Jenna Collins Fitness, 546K)",
        "segment_original": "NZ Functional-Fitness Creator (already mobile-native)",
        "industry": "Fitness / low-impact functional + sculpt (NZ)",
        "angle_to_take": (
            "Jenna Collins Fitness (546K, NZ) — short home workouts + 12-Week CaliFit Body "
            "Method; already runs a CaliFit Studio app. role-based support@. Frame an upgrade "
            "angle for a refreshed CaliFit-Studio v2 app with deeper progression tracker + "
            "12-week program + length filter + sculpt/Pilates tagged tracks + member tier — "
            "feature-set parity push targeting retention beyond what the current app delivers."
        ),
    },
    "zthtraining@doubletapcontent.com": {
        "niche": "Soccer-skill training brand 'helped 5200 players' (ZTH Training, 532K)",
        "segment_original": "Global Soccer-Skill Training Brand (manager-routed)",
        "industry": "Sports training / soccer skill development",
        "angle_to_take": (
            "ZTH Training (532K) — soccer skill development brand 'helped 5200 players' with "
            "70% off relaunch sale; biz via doubletapcontent.com (content/manager). role-based "
            "zthtraining@. Frame a branded ZTH app with skill-progression tracker (1v1 / "
            "shooting / passing milestones) + drill video library + program calendar (8-week / "
            "12-week) + tier-gated sale onboarding — replacing the discount-based web funnel "
            "with mobile-native progression."
        ),
    },
    "meetsrim@satsang-foundation.org": {
        "niche": "IN Sri M Kriya Yoga + retreats foundation (The Satsang Foundation, 314K)",
        "segment_original": "IN Spiritual Yoga + Retreats Foundation",
        "industry": "Wellness / Kriya Yoga + retreats + community welfare (IN)",
        "angle_to_take": (
            "The Satsang Foundation / Sri M (314K, IN) — Bengaluru-based 26+yr foundation "
            "running Kriya Yoga initiation + retreats + nationwide welfare programs. "
            "role-based meetsrim@ on .org domain. Frame a branded Satsang-Foundation app with "
            "Kriya practice library + initiation/retreat-event registration + Sri M lecture "
            "archive + donation/sponsorship flow + community-program updates — mobile-native "
            "intake replacing the email-based event coordination at this scale."
        ),
    },
    "collab@yoursalbany.com": {
        "niche": "US easy at-home Pilates + Flow + Strength + Prenatal (Arianna Elizabeth / Bright x Salted Yoga, 300K)",
        "segment_original": "US At-Home Pilates + Yoga + Prenatal Creator",
        "industry": "Wellness / Pilates + yoga + prenatal (US)",
        "angle_to_take": (
            "Arianna Elizabeth (300K, US) — easy-to-follow Pilates / Flow / Strength / Prenatal "
            "at-home workouts on AriannaElizabeth.com under Bright x Salted Yoga. role-based "
            "collab@yoursalbany.com (mgmt-flavor inbox). Frame a branded Arianna app with "
            "Pilates + Flow + Strength + Prenatal-tagged class library + length filter + "
            "trimester filter + member tier — mobile-native packaging for the audience that "
            "stays for life-stage transitions."
        ),
    },
    "mukeshgahlot.management@gmail.com": {
        "niche": "IN bodybuilding + powerlifting champion training (Tips By Mukesh Gahlot, 244K)",
        "segment_original": "IN Bodybuilding + Powerlifting Coach (fan-channel, manager-routed)",
        "industry": "Fitness / bodybuilding + powerlifting (IN)",
        "angle_to_take": (
            "Mukesh Gahlot (244K, IN) — 2X Mr.Olympia powerlifting + 4X Mr.India + Asia/Europe "
            "champion; fan-based channel referring all training requests to Guruji's manager. "
            "role-based .management@gmail. Frame the AppBillChat pitch to the manager — "
            "branded Mukesh-Gahlot app with bodybuilding/powerlifting program library + "
            "1:1 paid-coaching application + supplement/product shelf + member tier — "
            "manager-mediated upgrade from the current phone-call referral funnel."
        ),
    },
    "sabahkadriofficial@gmail.com": {
        "niche": "IN Bollywood dance fitness creator with custom programs + Patreon (Workout with Sabah / Sabah Kadri, 216K)",
        "segment_original": "IN Bollywood Dance + Fitness Creator",
        "industry": "Fitness / Bollywood dance + workout (IN)",
        "angle_to_take": (
            "Workout with Sabah (216K, IN) — 10yr Bollywood dance + 8yr Bollywood fitness "
            "teacher (NASM-cert) selling custom online programs + monthly subs (sabahkadri.com) "
            "+ Patreon ad-free workouts. personal gmail. Frame a branded Sabah app with "
            "Bollywood-dance class library + fitness program calendar + ad-free tier + custom-"
            "program intake — consolidating sabahkadri.com + Patreon + monthly-subs split into "
            "one mobile property."
        ),
    },
    # ──────────────────────────────────────────────────────────────────────
    # Mid tier (50K~200K)
    # ──────────────────────────────────────────────────────────────────────
    "sk8973729@gmail.com": {
        "niche": "IN yoga + meditation + breathwork studio (Shivam Yoga Studio, 177K)",
        "segment_original": "IN Yoga + Meditation Studio",
        "industry": "Wellness / yoga + meditation + breathwork (IN)",
        "angle_to_take": (
            "Shivam Yoga Studio (177K, IN) — Yoga Master Shivam Sharma; dynamic sequences + "
            "meditation + breathwork on shivamyogastudio.com with WhatsApp coordination. "
            "personal gmail. Frame a branded Shivam-Yoga app with class library + style tags "
            "(Hatha/Vinyasa/Pranayama) + meditation tracks + length filter + member tier — "
            "replacing WhatsApp-coordinated class signups with mobile-native intake."
        ),
    },
    "saipoojayoga@gmail.com": {
        "niche": "IN online yoga teacher + 1:1 health consultations (Sai Pooja Yoga, 120K)",
        "segment_original": "IN Online Yoga Teacher + Therapy",
        "industry": "Wellness / yoga + therapeutic yoga (IN)",
        "angle_to_take": (
            "Sai Pooja Yoga (120K, IN) — certified yoga teacher running online classes "
            "(India + abroad) + 1:1 personal health consultation + therapeutic yoga, intake "
            "via WhatsApp + gmail. personal gmail. Frame a branded Sai-Pooja app with "
            "therapeutic-yoga class library + 1:1 consultation booking + flexibility-tracker "
            "+ posture-correction tagged tracks + member tier — mobile-native intake replacing "
            "the WhatsApp + email funnel."
        ),
    },
    "support@joinggstudio.com": {
        "niche": "US online sculpt + barre + Pilates + strength platform (Gabby George / GGStudio, 73.7K)",
        "segment_original": "US Online Sculpt + Pilates Platform",
        "industry": "Fitness / sculpt + barre + Pilates + strength (US)",
        "angle_to_take": (
            "Gabby George / GGStudio (73.7K, US) — certified PT + MPH Nutrition founder of "
            "joinggstudio.com online platform; sculpt + barre + Pilates + strength formats "
            "with 7-day free trial. role-based support@. Frame a branded GGStudio app with "
            "format-tagged class library (sculpt/barre/Pilates/strength) + 5-min quick-start "
            "filter + 7-day trial onboarding + member tier — natively the right form factor "
            "for the daily-routine audience the platform already monetizes."
        ),
    },
    # ──────────────────────────────────────────────────────────────────────
    # Long tail (10K~50K)
    # ──────────────────────────────────────────────────────────────────────
    "info@akramyoga.co.uk": {
        "niche": "GB Surrey-based yoga teacher trainer (Akram Yoga Academy / Zahir Akram, 37.2K)",
        "segment_original": "GB Yoga Teacher-Training Studio",
        "industry": "Wellness / yoga teacher training (GB)",
        "angle_to_take": (
            "Akram Yoga Academy (37.2K, GB) — Om Yoga Magazine 2024 studio + teacher of the "
            "year, Zahir Akram (author 'Yoga, Madness or Meditation?') runs in-house TT + "
            "online courses on akramyoga.co.uk. role-based info@. Frame a branded Akram-Yoga "
            "app with TT-curriculum modules (anatomy + breathwork + sequencing + philosophy) "
            "+ online-course library + studio-cohort tier + assessment tracker — mobile-native "
            "delivery for the yoga-teacher buyer audience."
        ),
    },
    "info@solinfitness.com": {
        "niche": "Tulum-based women's home workout coach with 6-week challenge (Kate Nolte / Tulum Trainer, 34.4K)",
        "segment_original": "Global Women's Home-Workout Coach (white-label on Solin)",
        "industry": "Fitness / women's home workouts + mobility (Tulum-based)",
        "angle_to_take": (
            "Kate Nolte / Tulum Trainer (34.4K) — 15+yr women's home-workout coach selling "
            "5-15min minimal-equipment workouts + lymphatic-drainage / Qi-Gong + 6-Week "
            "Challenge on solin.stream/tulumtrainer (white-label platform). role-based info@ "
            "on solinfitness.com. Frame a branded Kate-Nolte app with short-workout library + "
            "length filter (5/10/15min) + 6-week challenge program + lymphatic / Qi-Gong tagged "
            "tracks + member tier — owned mobile property replacing the Solin white-label."
        ),
    },
    "tauheedkhan0698@gmail.com": {
        "niche": "IN desi-style home + bodyweight channel (TK fitness zone, 24.3K)",
        "segment_original": "IN At-Home Bodyweight Channel",
        "industry": "Fitness / at-home bodyweight (IN, Hindi)",
        "angle_to_take": (
            "TK fitness zone (24.3K, IN) — desi-style home + bodyweight workouts in Hindi, "
            "muscle building / weight loss. personal gmail for sponsorship. Frame a branded "
            "TK-Fitness app with Hindi-cue bodyweight workout library + transformation program "
            "calendar + sponsor-friendly creator surface — packaging the audience for "
            "monetization beyond ad RPM."
        ),
    },
    "hello@camiyogair.com": {
        "niche": "LT aerial yoga teacher + studio founder + 50hr Aerial TT online (CamiYogAIR / Camille, 23.8K)",
        "segment_original": "LT Aerial Yoga Teacher + Equipment Brand",
        "industry": "Wellness / aerial yoga + equipment commerce (LT)",
        "angle_to_take": (
            "CamiYogAIR / Camille (23.8K, LT) — E-RYT500, founder of CAMIYOGA studio "
            "(Lithuania, est. 2014); runs online aerial-yoga classes + 50hr Aerial Yoga TT "
            "(Yin/L1/L2/L3) + sells aerial-yoga hammocks (17 colors) on camiyogair.com. "
            "role-based hello@. Frame a branded CamiYogAIR app with aerial-yoga class library "
            "+ TT-curriculum modules + silks/hammock shop + member tier — consolidating the "
            "class + course + commerce split into one mobile property."
        ),
    },
    "premanandyoga@gmail.com": {
        "niche": "IN Mumbai Govt-cert yoga institute with TT 200/500/900 hrs (Premanand Yoga, 19.1K)",
        "segment_original": "IN Yoga Institute + Teacher Training",
        "industry": "Wellness / yoga teacher training + therapy (IN, Mumbai)",
        "angle_to_take": (
            "Premanand Yoga (19.1K, IN) — Mumbai's Govt-of-India + ISO + International cert "
            "yoga institute running 200/500/900hr Diploma TTs + at-home personal teacher "
            "service across Mumbai (Dadar/Thane/Kandivali/Bhandup). personal gmail (also "
            "premanandyoga.net). Frame a branded Premanand-Yoga app with TT-curriculum "
            "modules + cohort tier + at-home-teacher booking + flexibility-class library — "
            "mobile-native intake replacing the multi-station phone-call funnel."
        ),
    },
    "bzwang43@gmail.com": {
        "niche": "US family fitness + kids strength + calisthenics creator with online programs + supplement brand (Bert Wang, 16.7K)",
        "segment_original": "US Family / Kids Strength Creator + Brand",
        "industry": "Fitness / family + kids strength + calisthenics (US)",
        "angle_to_take": (
            "Bert Wang (16.7K, US) — dad/coach offering kids strength + gymnastics + "
            "calisthenics + family workouts; sells online coaching programs + founder of "
            "Fit Chews High Performance Gummies. personal gmail for brand partnerships. "
            "Frame a branded Bert-Wang app with family/kids workout library + age-tagged "
            "progression tracker + program tier + Fit-Chews shelf — consolidating the "
            "creator + 1:1 coaching + supplement-brand split into one mobile property."
        ),
    },
    "gojudo81@gmail.com": {
        "niche": "IN traditional Indian wrestling + bodyweight workouts (Traditional INDIAN Workouts / Jitender Bhardwaj, 11.9K)",
        "segment_original": "IN Traditional Wrestling + Bodyweight Channel",
        "industry": "Fitness / traditional Indian wrestling + bodyweight (IN)",
        "angle_to_take": (
            "Traditional INDIAN Workouts (11.9K, IN) — Delhi University M.Ed PE, intl judoka + "
            "national medalist promoting traditional Indian wrestling + bodyweight workouts "
            "for PE teachers. personal gmail. Frame a branded Traditional-Indian-Workouts app "
            "with category-tagged workout library (wrestling/judo/bodyweight) + PE-teacher "
            "curriculum modules + program tier + 1:1 query intake — niche-targeted mobile "
            "delivery for the PE-educator + traditional-fitness audience."
        ),
    },
    "misskajal2025@gmail.com": {
        "niche": "IN Govt-certified yoga teacher with online classes (Kajal's YOGA, 11.1K, Hindi+English)",
        "segment_original": "IN Online Yoga Teacher (Govt-cert)",
        "industry": "Wellness / yoga (IN)",
        "angle_to_take": (
            "Kajal's YOGA (11.1K, IN) — Govt-cert yoga teacher offering free daily yoga / "
            "fitness / lifestyle videos + online yoga classes via gmail intake. personal "
            "gmail. Frame a branded Kajal-Yoga app with daily-yoga class library + length "
            "filter + Hindi-cue tracks + 1:1 online-class booking + member tier — mobile-"
            "native intake replacing the email-led class funnel."
        ),
    },
    "ayurvedaecosystem@gmail.com": {
        "niche": "IN AYUSH-affiliated ayurveda + medical-education channel (AYURVEDA ECOSYSTEM / Dr. Anurag Kushwaha BAMS, 10.2K)",
        "segment_original": "IN Ayurveda + Medical Education Creator",
        "industry": "Education / ayurveda + medical-exam prep (IN)",
        "angle_to_take": (
            "AYURVEDA ECOSYSTEM (10.2K, IN) — Dr. Anurag Kushwaha (BAMS, NIA Jaipur) covers "
            "NEET counselling + ayurveda awareness + medical-course exam prep + ayurvedic "
            "cure content with paid-membership tier on the channel. personal gmail. Frame a "
            "branded Ayurveda-Ecosystem app with NEET-prep modules + ayurveda content library "
            "+ exam-counselling Q&A tier + member-only deeper-dive tracks — mobile-native "
            "delivery for the medical-aspirant + ayurveda-curious audience."
        ),
    },
    # ──────────────────────────────────────────────────────────────────────
    # Sub 10K — the AppBillChat ICP sweet spot
    # ──────────────────────────────────────────────────────────────────────
    "ondemand@speirpilates.com": {
        "niche": "Pilates fusion (mat + reformer) on-demand platform (Speir On Demand / Andrea Speir, 7.87K)",
        "segment_original": "Online Pilates Fusion Platform",
        "industry": "Wellness / Pilates fusion mat + reformer",
        "angle_to_take": (
            "Speir On Demand (7.87K) — celebrity trainer Andrea Speir's Pilates fusion (mat + "
            "reformer) on-demand membership with 400+ workouts on speirpilates.com/on-demand. "
            "role-based ondemand@. Frame a branded Speir app with mat / reformer tagged class "
            "library + length + intensity + target filters + 400+ archive search + member tier "
            "— mobile-native upgrade for the on-demand subscription replacing web-only login."
        ),
    },
    "info@bendablebody.com": {
        "niche": "US NYC flexibility-training studio with True Flexibility Method (Bendable Body, 7.28K)",
        "segment_original": "US Flexibility / Mobility Studio",
        "industry": "Wellness / flexibility + fascia + resistance stretching (US, NYC)",
        "angle_to_take": (
            "Bendable Body (7.28K, US) — NYC studio specializing in True Flexibility Training "
            "(resistance stretching on fascia / energetic meridians). role-based info@. Frame "
            "a branded Bendable-Body app with flexibility-method curriculum + meridian-tagged "
            "stretch library + 1:1 NYC-studio booking + remote member tier — mobile-native "
            "delivery for a niche method that depends on consistent daily practice."
        ),
    },
    "raghvendrapatel96@gmail.com": {
        "niche": "IN desi-style home / bodyweight channel (village fitness hub, 7.0K)",
        "segment_original": "IN At-Home Bodyweight Channel",
        "industry": "Fitness / at-home bodyweight (IN)",
        "angle_to_take": (
            "village fitness hub (7.0K, IN) — Raghvendra Singh Patel; desi-style home + "
            "bodyweight workouts, muscle building / weight loss. personal gmail for queries. "
            "Frame a branded village-fitness-hub app with Hindi-cue bodyweight library + "
            "transformation program calendar + sponsor / Q&A tier — packaging the audience "
            "for retention beyond YouTube views."
        ),
    },
    "yogicali85@gmail.com": {
        "niche": "Calisthenics + yoga + bodyweight coach offering online classes (Divine yogi, 6.56K)",
        "segment_original": "Online Calisthenics + Yoga Coach",
        "industry": "Fitness / calisthenics + yoga (online)",
        "angle_to_take": (
            "Divine yogi (6.56K) — calisthenics + bodyweight + yoga coach offering online "
            "classes via phone (+91 6398216558) + gmail. personal gmail. Frame a branded "
            "Divine-Yogi app with calisthenics + yoga combined class library + skill-"
            "progression tracker + 1:1 online-class scheduling + member tier — mobile-native "
            "intake replacing the phone-call funnel."
        ),
    },
    "ps.jooga@gmail.com": {
        "niche": "FI Face Yoga teacher + author + teacher trainer (PS Yoga / Päivi Salminen, 6.22K)",
        "segment_original": "FI Face Yoga Teacher + Author",
        "industry": "Wellness / face yoga + face massage (FI)",
        "angle_to_take": (
            "PS Yoga / Päivi Salminen (6.22K, FI) — Finland's most experienced Face Yoga "
            "teacher + teacher trainer, author of 'A Happy and Relaxed Face with Face Yoga'. "
            "personal gmail. Frame a branded PS-Yoga app with face-yoga / face-massage tagged "
            "exercise library + length filter + author-book companion track + TT module + "
            "member tier — mobile-native delivery for a niche method that needs daily "
            "consistency."
        ),
    },
    "info@pilatesbysophie.be": {
        "niche": "BE online Pilates studio with existing app subdomain (Pilates By Sophie, 6.1K)",
        "segment_original": "BE Online Pilates Studio (already on app subdomain)",
        "industry": "Wellness / Pilates online studio (BE)",
        "angle_to_take": (
            "Pilates By Sophie (6.1K, BE) — Pilates online studio with existing 'PBS Studio' "
            "membership at app.pilatesbysophie.be (likely web-app); new workout every 10 days. "
            "role-based info@. Frame a branded PBS-Studio native-mobile app with Pilates class "
            "library + length filter + recipe / meal-plan tier + member-content drop calendar "
            "— upgrading the web-app subdomain into a true native mobile property."
        ),
    },
    "info@tiwariyoga.com": {
        "niche": "GB yoga + meditation + breathwork + Ayurveda coach with UNEARTHED membership (Angie Tiwari, 6.07K)",
        "segment_original": "GB Yoga + Ayurveda Coach + Membership",
        "industry": "Wellness / yoga + meditation + Ayurveda (GB)",
        "angle_to_take": (
            "Angie Tiwari (6.07K, GB) — yoga + meditation + breathwork coach + Ayurveda "
            "consultant + founder of UNEARTHED 7-day-trial membership; runs Ayurveda "
            "consultations + retreats off tiwariyoga.com. role-based info@. Frame a branded "
            "Tiwari-Yoga app with class library (yoga/meditation/breathwork) + dosha-quiz "
            "intake + Ayurveda-consultation booking + retreat registration + member tier — "
            "consolidating the multi-product flow into one mobile property."
        ),
    },
    "admin@manayoga.ca": {
        "niche": "Yoga teacher with 200hr YTT retreats (ShareenYoga / Mana Yoga, 4.38K)",
        "segment_original": "Online Yoga Teacher + YTT Retreats",
        "industry": "Wellness / yoga + teacher training",
        "angle_to_take": (
            "ShareenYoga / Mana Yoga (4.38K) — Shareen Woodford runs free online yoga + "
            "200hr YTT retreats + workshops + local YTT programs off manayoga.ca. role-based "
            "admin@. Frame a branded Mana-Yoga app with class library + YTT-cohort modules + "
            "retreat / workshop registration + member tier — mobile-native intake replacing "
            "web-only registration for international YTT students."
        ),
    },
    "kontakt@pilatesstudioonline.pl": {
        "niche": "PL Polish online Pilates studio for women (Pilates Studio Online / Ola Szymańska, 4.3K)",
        "segment_original": "PL Online Pilates Studio (Polish)",
        "industry": "Wellness / Pilates online (PL, Polish)",
        "angle_to_take": (
            "Pilates Studio Online / Ola Szymańska (4.3K) — Polish-language online Pilates "
            "studio for women, 'safe and effective' workouts on pilatesstudioonline.pl. "
            "role-based kontakt@. Frame a branded PSO app with Polish-cue Pilates class "
            "library + length filter + women's-focused program calendar + member tier — "
            "mobile-native delivery for the Polish-speaking Pilates audience."
        ),
    },
    "info@rainbowyogatraining.com": {
        "niche": "International yoga specialization teacher trainings (Rainbow Yoga Training, 4.05K)",
        "segment_original": "Global Yoga Specialization TT",
        "industry": "Wellness / yoga teacher training (interactive / family yoga)",
        "angle_to_take": (
            "Rainbow Yoga Training (4.05K) — globally-known interactive / family yoga "
            "specialization TT brand off rainbowyogatraining.com. role-based info@. Frame a "
            "branded Rainbow-Yoga app with TT-curriculum modules (interactive / partner / "
            "family yoga) + practice library + cohort tier + workshop registration — "
            "mobile-native delivery for international TT cohorts."
        ),
    },
    "iris@sculptwithiris.com": {
        "niche": "NL Modern Pilates + Strength method 'The Sculpt Method' (Sculpt with Iris, 3.78K)",
        "segment_original": "NL Pilates + Strength Method (women)",
        "industry": "Wellness / Pilates + light-weight strength (NL)",
        "angle_to_take": (
            "Sculpt with Iris (3.78K, NL) — Amsterdam-based Mat Pilates instructor + founder "
            "of 'Sculpt' method (classical Pilates + controlled light-weight strength); "
            "structured programs + 25-40min classes + weekly live sessions on "
            "sculptwithiris.com. personal-domain inbox iris@. Frame a branded Sculpt app with "
            "Pilates+strength tagged class library + length filter + structured program "
            "calendar + live-session calendar + member tier — mobile-native upgrade for the "
            "subscription audience."
        ),
    },
    "info@crossyoga.org": {
        "niche": "DK Christian Yoga + Yoga Instructor TT (CrossYoga with Rie / CrossYoga Academy, 3.66K)",
        "segment_original": "DK Christian Yoga + TT Academy",
        "industry": "Wellness / Christian yoga + teacher training (DK)",
        "angle_to_take": (
            "CrossYoga with Rie (3.66K, DK) — Christian Yoga teacher Rie Frilund Skårhøj "
            "running CrossYoga Academy with online + in-person Yoga Instructor Trainings + "
            "retreats + workshops + classes. role-based info@. Frame a branded CrossYoga app "
            "with class library + style tags (Slow / Vinyasa / Power / Yin / Workouts) + "
            "Christian-perspective tagged tracks + TT-cohort tier + retreat registration — "
            "mobile-native intake for the niche Christian-yoga audience."
        ),
    },
    "info@pilatesliebe.de": {
        "niche": "DE 15-min Pilates + 5-day Challenge for women 35+ (Pilatesliebe / Jennifer Schwinkowski, 3.43K)",
        "segment_original": "DE Pilates Brand for Women 35+",
        "industry": "Wellness / Pilates + cortisol-aware training (DE)",
        "angle_to_take": (
            "Pilatesliebe (3.43K, DE) — Jennifer Schwinkowski's Pilates brand for women 35+ "
            "with 15-min daily workouts + hormone-balance focus + free 5-day challenge funnel "
            "on pilatesliebe.com. role-based info@. Frame a branded Pilatesliebe app with "
            "15-min Pilates library + cortisol-aware program calendar + 5-day-challenge "
            "onboarding + deep-core tagged tracks + member tier — mobile-native upgrade for "
            "the women-35+ daily-practice audience."
        ),
    },
    "narberth@elliehermanpilates.com": {
        "niche": "Author of 'Pilates for Dummies' + Brooklyn studio + DVD library (Ellie Herman, 3.01K)",
        "segment_original": "US Pilates Author + Studio + DVDs",
        "industry": "Wellness / Pilates + Springboard equipment (US, Brooklyn)",
        "angle_to_take": (
            "Ellie Herman (3.01K) — internationally-recognized Pilates instructor + author of "
            "8 books incl. 'Pilates for Dummies' + inventor of the Pilates Springboard; runs "
            "Brooklyn studio + sells DVDs + books off elliehermanpilates.com. personal-name @ "
            "domain (narberth@). Frame a branded Ellie-Herman app with mat + Springboard "
            "tagged class library (DVD-derived) + book-companion modules + studio-session "
            "booking + member tier — mobile-native upgrade replacing the DVD/web-store funnel."
        ),
    },
    "info@sallyparkesyoga.com": {
        "niche": "GB international yoga teacher trainer + author (Sally Parkes Yoga School, 2.71K)",
        "segment_original": "GB Yoga TT Academy + Pre/Postnatal",
        "industry": "Wellness / yoga teacher training + pre/postnatal (GB)",
        "angle_to_take": (
            "Sally Parkes Yoga School (2.71K, GB) — international yoga teacher trainer + "
            "author ('Manual of Yoga Anatomy', 'Healing Yoga Bible'); runs predominantly "
            "online 200hr Hatha Flow + Pregnancy + Postnatal + Yin + Fertility Yoga TTs off "
            "sallyparkesyoga.com. role-based info@. Frame a branded Sally-Parkes app with "
            "TT-curriculum modules (Hatha / Pregnancy / Postnatal / Yin / Fertility) + "
            "anatomy-book companion + pre/postnatal class library + cohort tier — mobile-"
            "native intake for the niche yoga-teacher buyer audience."
        ),
    },
    "adrianne@thousandfoldlotus.com": {
        "niche": "Online Pilates studio + e-courses (Thousandfold Lotus / Adrianne, 2.64K)",
        "segment_original": "Online Pilates Studio + E-Courses",
        "industry": "Wellness / Pilates + healthy-lifestyle (online)",
        "angle_to_take": (
            "Thousandfold Lotus (2.64K) — Adrianne's online Pilates studio + e-courses with "
            "free 6-Day Foundations Course funnel on thousandfoldlotus.com. personal-domain "
            "inbox adrianne@. Frame a branded Thousandfold-Lotus app with Pilates class "
            "library + Foundations-Course onboarding + e-course modules + member tier — "
            "mobile-native upgrade for the women's busy-life audience."
        ),
    },
    "Poojajha24thjan@gmail.com": {
        "niche": "IN motivation + meditation + yoga creator with Membership Plan (Pooja Jha, 2.62K)",
        "segment_original": "IN Motivation + Meditation + Yoga Creator",
        "industry": "Wellness / motivation + mindfulness + yoga (IN)",
        "angle_to_take": (
            "Pooja Jha (2.62K, IN) — daily motivation + guided meditation + yoga + night "
            "affirmations creator with channel Membership Plan. personal gmail. Frame a "
            "branded Pooja-Jha app with daily-motivation feed + guided-meditation library + "
            "yoga class tracks + night-affirmation tier + member-only deeper modules — mobile-"
            "native upgrade for a daily-practice audience that already pays for membership."
        ),
    },
    "coljorgensen13@gmail.com": {
        "niche": "CA Osteopath + Pilates/Yoga/Somatics teacher with 12-week pain care program (Stillness in Motion / Colleen Jorgensen, 2.45K)",
        "segment_original": "CA Pain-Care Movement Educator",
        "industry": "Wellness / pain care + Pilates + somatics (CA)",
        "angle_to_take": (
            "Stillness in Motion / Colleen Jorgensen (2.45K, CA) — Osteopath + Pain Care "
            "educator + therapeutic Pilates / yoga / Somatics teacher running annual 12-week "
            "DARE TO HEAL online pain-care program off colleenjorgensen.org. personal gmail. "
            "Frame a branded Stillness-in-Motion app with pain-care movement library + 12-week "
            "DARE-TO-HEAL program calendar + anatomy / TT modules + cohort tier — mobile-"
            "native delivery for the chronic-pain audience that requires consistent daily "
            "practice."
        ),
    },
    "vladcalisthenicsman@gmail.com": {
        "niche": "UA online calisthenics coach since 2019 + book author (Calisthenicsman / Vlad, 2.44K)",
        "segment_original": "UA Online Calisthenics Coach + Author",
        "industry": "Fitness / calisthenics + bodyweight (UA)",
        "angle_to_take": (
            "Calisthenicsman / Vlad (2.44K, UA) — online calisthenics coach since 2019 having "
            "helped 400+ people, author of calisthenics books + 3 YouTube channels + 2 "
            "Telegram channels (20M+ views combined). personal gmail. Frame a branded "
            "Calisthenicsman app with calisthenics workout library + skill-progression tracker "
            "(pull-up / push-up variations) + book companion + 1:1 routine-creation intake + "
            "member tier — consolidating the multi-channel + Telegram + email funnel into one "
            "mobile property."
        ),
    },
    "reikilates@gmail.com": {
        "niche": "Reiki + Pilates fusion 'Reikilates' creator (Heal With Suha, 2.37K)",
        "segment_original": "Online Reiki + Pilates Fusion Creator",
        "industry": "Wellness / energy healing + Pilates fusion",
        "angle_to_take": (
            "Heal With Suha (2.37K) — wellness coach + founder of 'Reikilates' (Reiki + "
            "Pilates fusion); sells self-help energy-healing course on healyourselfsimplified.com. "
            "personal gmail. Frame a branded Reikilates app with fusion class library "
            "(Reiki / Pilates / meditation) + energy-healing course modules + intuitive-reading "
            "1:1 booking + member tier — mobile-native delivery for the niche energy-work "
            "audience."
        ),
    },
    "Info@NataliaPilates.co.uk": {
        "niche": "GB certified Pilates instructor with FREE online + in-person classes (Pilates with Natalia, 2.29K)",
        "segment_original": "GB Pilates Instructor (accessibility-focused)",
        "industry": "Wellness / Pilates (GB, accessible)",
        "angle_to_take": (
            "Pilates with Natalia (2.29K, GB) — certified Pilates instructor running free "
            "online + paid in-person classes off NataliaPilates.co.uk, mission of accessibility. "
            "role-based Info@. Frame a branded Natalia-Pilates app with quick-online Pilates "
            "library + length filter + in-person class booking + accessibility-tagged tracks "
            "(beginner-safe / time-pressed) + member tier — mobile-native upgrade for the "
            "free-online → paid-in-person funnel."
        ),
    },
    "edwardssophie@live.co.uk": {
        "niche": "GB Liverpool Pilates membership platform with live Zoom classes (Virtual Pilates Hub / Sophie, 2.25K)",
        "segment_original": "GB Online Pilates Membership Platform",
        "industry": "Wellness / Pilates online + live (GB, Liverpool)",
        "angle_to_take": (
            "Virtual Pilates Hub (2.25K, GB) — Sophie runs Pilates business in Liverpool + "
            "online platform on liverpoolpilateshub.co.uk (£35/mo, 170+ home workouts + 3 new "
            "classes/week + Saturday live Zoom). personal live.co.uk inbox. Frame a branded "
            "Virtual-Pilates-Hub app with full-class library + length filter + Zoom-live class "
            "calendar + 170+ archive search + tiered membership — mobile-native upgrade for "
            "the £35/mo subscriber audience."
        ),
    },
    "lifestyle@yogapadova.it": {
        "niche": "IT Vinyasa Yoga online teacher with 20yr experience (Yoga online - Elisabetta Baso, 2.2K)",
        "segment_original": "IT Online Vinyasa Yoga Teacher",
        "industry": "Wellness / Vinyasa yoga (IT)",
        "angle_to_take": (
            "Elisabetta Baso / Yoga online (2.2K, IT) — Padova-based Federazione Italiana "
            "Yoga-trained Vinyasa Yoga teacher with 20+ yr experience; online courses for "
            "beginners + experienced on yogapadova.it. role-based lifestyle@. Frame a branded "
            "Elisabetta-Baso app with Italian-cue Vinyasa class library + tutorial breakdowns "
            "+ chakra-music tracks + relaxation tagged tracks + member tier — mobile-native "
            "delivery for the Italian-speaking yoga audience."
        ),
    },
    "rishikeshyogkendra1@gmail.com": {
        "niche": "IN Rishikesh Yoga Alliance RYS 200 + aerial yoga TT school (Rishikesh Yog Kendra, 2.06K)",
        "segment_original": "IN Yoga Teacher-Training School (residential + online)",
        "industry": "Wellness / Yoga TT + aerial yoga (IN, Rishikesh)",
        "angle_to_take": (
            "Rishikesh Yog Kendra (2.06K, IN) — Yoga Alliance USA RYS 200 + YACEP-cert "
            "residential YTT school in Rishikesh; first to introduce classical YTT + aerial "
            "yoga, also runs Spanish-language online 200hr YTT. personal gmail. Frame a "
            "branded Rishikesh-Yog-Kendra app with TT-curriculum modules (Hatha / Vinyasa / "
            "Aerial / Pre-Postnatal) + Spanish-track variant + cohort tier + retreat / "
            "residential intake — mobile-native intake for the international YTT pipeline."
        ),
    },
    "info@theblackpranayoga.com": {
        "niche": "US Online Yoga Teacher Training $25 promo (Black Prana Yoga & Pole, 2.01K)",
        "segment_original": "US Online Yoga TT Brand",
        "industry": "Wellness / yoga teacher training + pole (US)",
        "angle_to_take": (
            "Black Prana Yoga & Pole (2.01K, US) — runs Online Yoga TT programs with $25 "
            "promotional pricing on theblackpranayoga.com/yttgoldenticket; minimal description "
            "indicates promo-funnel-led discovery. role-based info@. Frame a branded Black-"
            "Prana app with TT-curriculum modules + pole + yoga combined library + cohort tier "
            "+ promo-code onboarding flow — mobile-native upgrade for the $25-onboard funnel."
        ),
    },
    "laura@lauragreenyoga.co.uk": {
        "niche": "GB online yoga + Soul Retreats company (Laura Green Yoga, 1.96K)",
        "segment_original": "GB Online Yoga Studio + Retreats",
        "industry": "Wellness / yoga + retreats (GB, Tuscany/Morocco)",
        "angle_to_take": (
            "Laura Green Yoga (1.96K, GB) — international yoga teacher + founder of Soul "
            "Retreats running yoga retreats in Tuscany + Morocco off soulretreats.co.uk + "
            "online studio at lauragreenyoga.co.uk. personal-domain inbox laura@. Frame a "
            "branded Laura-Green-Yoga app with online-studio class library + retreat "
            "registration + workshop calendar + member tier — mobile-native intake for the "
            "international retreat audience."
        ),
    },
    "harmanrooprai122@gmail.com": {
        "niche": "IN desi-style home / bodyweight + blogging (Harman Rooprai, 1.9K)",
        "segment_original": "IN At-Home Bodyweight Channel",
        "industry": "Fitness / at-home bodyweight (IN)",
        "angle_to_take": (
            "Harman Rooprai (1.9K, IN) — desi-style home + bodyweight workouts + occasional "
            "blogging. personal gmail for sponsorship. Frame a branded Harman-Rooprai app "
            "with Hindi-cue bodyweight workout library + transformation program + sponsor / "
            "blog-content tier — packaging the audience for monetization beyond ad RPM."
        ),
    },
    "medtwalritu@gmail.com": {
        "niche": "ACE-cert PT + dance fitness master trainer with FREE 7-Day program (FITWITHRITU / Ritu Medtwal, 1.83K)",
        "segment_original": "Online Dance-Fitness + Strength Coach (5000+ trainees)",
        "industry": "Fitness / dance cardio + strength + Indian diet",
        "angle_to_take": (
            "FITWITHRITU / Ritu Medtwal (1.83K) — ACE-cert PT + Dance Fitness Master Trainer "
            "with 10+yr exp + 5000+ trainees online + offline; sells FREE 7-Day Home Fat Loss "
            "Program funnel + personalized fat-loss programs on fitwithritu.com. personal "
            "gmail. Frame a branded Ritu app with home-workout library + dance-cardio tagged "
            "tracks + Indian-diet plan modules + 7-day-trial onboarding + program tier — "
            "mobile-native intake for the 5000+ trainee pipeline."
        ),
    },
    "info@yoga-yin.com": {
        "niche": "Spanish-language Yin Yoga school (Paul Grilley method) (Yoga Yin / Escuela de Yin Yoga, 1.8K)",
        "segment_original": "ES Spanish-language Yin Yoga TT School",
        "industry": "Wellness / Yin Yoga teacher training (Spanish)",
        "angle_to_take": (
            "Yoga Yin / Escuela de Yin Yoga (1.8K) — Spanish-language Yin Yoga school based "
            "on Paul Grilley method (functional anatomy + skeletal variability + TCM + Taoist/"
            "Tantric philosophy); runs annual TT 'YYTT 2025' on yoga-yin.com + Spotify show. "
            "role-based info@. Frame a branded YogaYin app with Spanish-cue Yin-Yoga class "
            "library + TT-curriculum modules (anatomy + TCM + philosophy) + cohort tier + "
            "podcast feed integration — mobile-native delivery for Spanish-speaking Yin TT "
            "students."
        ),
    },
    "info@sarahbyoga.net": {
        "niche": "GB yoga teacher with Patreon membership (350+ classes) + workshops + retreats (Sarah B Yoga, 1.69K)",
        "segment_original": "GB Online Yoga Teacher + Patreon Membership",
        "industry": "Wellness / yoga (GB)",
        "angle_to_take": (
            "Sarah B Yoga (1.69K, GB) — experienced yoga teacher with Patreon membership "
            "(US$3+/mo, 350+ yoga classes + weekly drops + Sarah's Shorts) + workshops + "
            "retreats + teacher mentorship on sarahbyoga.net. role-based info@. Frame a "
            "branded Sarah-B app with full-class library + length filter + style tags + "
            "weekly-drop calendar + workshop / retreat registration + member tier — mobile-"
            "native upgrade replacing the Patreon-tier funnel with owned billing."
        ),
    },
    "info@gr8flex.com": {
        "niche": "US home-gym product brand with lifetime warranty (GR8FLEX Total Performance Gym, 1.54K)",
        "segment_original": "US Home-Gym Equipment Brand",
        "industry": "Fitness / home-gym equipment commerce (US)",
        "angle_to_take": (
            "GR8FLEX Total Performance Gym (1.54K, US) — physical product brand selling a "
            "high-end home gym (lifetime warranty, 8-country shipping); not a coach/creator. "
            "role-based info@. Pitch the brand on a companion AppBillChat app — branded "
            "GR8FLEX app with equipment-tagged workout library + program calendar (low-impact "
            "→ bodybuilding) + accessory-shelf upsell + member tier — turning the lifetime-"
            "warranty product into a recurring-engagement service tier."
        ),
    },
    "info@chriswongfitness.com": {
        "niche": "CA Oakville in-home + online personal trainer (In Home Trainer Oakville / Christopher Wong, 1.5K)",
        "segment_original": "CA Local + Online PT (Oakville, ON)",
        "industry": "Fitness / 1:1 personal training (CA)",
        "angle_to_take": (
            "Christopher Wong / In Home Trainer Oakville (1.5K, CA) — Oakville-based in-home "
            "+ online PT combining resistance + cardio + flexibility + martial arts + "
            "relaxation; phone (905-580-4722) + chriswongfitness.com intake. role-based info@. "
            "Frame a branded Chris-Wong-Fitness app with workout library + 1:1 in-home / "
            "online booking + group-session calendar + program tier — mobile-native upgrade "
            "replacing phone-call + Facebook intake for the Oakville/online split."
        ),
    },
    "hello@studio20.me": {
        "niche": "NL yin yoga creator (channel inactive, content lives on Studio20) (Yin Yoga with Marianne, 1.5K)",
        "segment_original": "NL Yin Yoga Teacher (legacy channel)",
        "industry": "Wellness / yin yoga + coaching (NL)",
        "angle_to_take": (
            "Yin Yoga with Marianne (1.5K, NL) — Marianne de Kuyper's legacy channel (no "
            "longer actively publishing); current work runs through Studio20.me (yoga + "
            "coaching + creative exploration in Dutch / English). role-based hello@. Frame a "
            "branded Studio20 app with archived yin-yoga library + new-format coaching modules "
            "+ Dutch / English language toggle + member tier — mobile-native packaging that "
            "consolidates the legacy YouTube + active website split."
        ),
    },
    "contact@practicewithjodie.com": {
        "niche": "AU yin yoga teacher with YINBODIED membership (Jodie / YINBODIED, 1.48K)",
        "segment_original": "AU Yin Yoga Teacher + Membership",
        "industry": "Wellness / yin yoga (AU)",
        "angle_to_take": (
            "Jodie & YINBODIED (1.48K, AU) — short-form yin yoga creator running YINBODIED "
            "membership on yinbodied.com/join. role-based contact@. Frame a branded YINBODIED "
            "app with short-form yin class library + length filter + meditation tracks + "
            "membership-tier onboarding — mobile-native upgrade for the existing membership "
            "audience."
        ),
    },
    "arjunsingh826448@gmail.com": {
        "niche": "IN desi-style bodyweight + religious framing (Arjun Baba Fitness, 1.45K)",
        "segment_original": "IN At-Home Bodyweight Channel",
        "industry": "Fitness / at-home bodyweight (IN)",
        "angle_to_take": (
            "Arjun Baba Fitness (1.45K, IN) — desi-style home + bodyweight workouts with "
            "Mehandipur Balaji religious framing. personal gmail for biz. Frame a branded "
            "Arjun-Baba app with Hindi-cue bodyweight library + transformation program + "
            "religious-content tagged tracks + sponsor tier — packaging the niche audience "
            "for retention beyond ad RPM."
        ),
    },
    "filler@godaddy.com": {
        "niche": "US 20yr Pilates + circuits + boot camp PT (Beth Pluemer Health Coaching, Training and Pilates, 1.39K)",
        "segment_original": "US Pilates + Circuit Trainer (placeholder email)",
        "industry": "Wellness / Pilates + circuits + boot camp (US)",
        "angle_to_take": (
            "Beth Pluemer (1.39K, US) — 20+yr fitness instructor + Stott Pilates instructor + "
            "Exercise Science U Northern Iowa, runs 1:1 + 10-12 week programs + Pilates / "
            "circuit videos on bethpluemer.com. NOTE: extracted email is filler@godaddy.com — "
            "a domain-registration placeholder, not a real contact. Frame the AppBillChat "
            "pitch via the website contact form, not email — branded Beth-Pluemer app with "
            "10-12 week program calendar + Pilates / circuit tagged class library + 1:1 "
            "session scheduling + member tier."
        ),
    },
    "coaching.liza@gmail.com": {
        "niche": "ZA certified PT with Patreon early-access + 1:1 plans (Liza Fitness, 1.37K)",
        "segment_original": "ZA Online Personal Trainer",
        "industry": "Fitness / home workouts + diet plans (ZA)",
        "angle_to_take": (
            "Liza Fitness (1.37K, ZA) — Certified PT offering home workouts + Patreon early-"
            "access + 1:1 eating-plan / training-program intake via gmail. personal gmail "
            "(coaching.liza@). Frame a branded Liza-Fitness app with home-workout library + "
            "length filter + 1:1 plan-intake form + Patreon-tier early-access onboarding + "
            "member tier — mobile-native intake replacing the Patreon + email funnel."
        ),
    },
    "theoceanyoga.info@gmail.com": {
        "niche": "PT Portuguese yoga + Pilates online (Vinyasa / Yin / Restaurativo / Mat Pilates) (The Ocean Yoga / Diana, 1.29K)",
        "segment_original": "PT Online Yoga + Pilates Teacher (Portuguese)",
        "industry": "Wellness / yoga + Pilates (PT, Portuguese)",
        "angle_to_take": (
            "The Ocean Yoga / Diana (1.29K, PT) — Yoga Alliance-cert teacher offering free "
            "Portuguese yoga + Pilates videos (Vinyasa Flow / Yin / Restaurativo / Yoga Nidra "
            "/ Mat Pilates) for individuals + companies. personal gmail (theoceanyoga.info@). "
            "Frame a branded Ocean-Yoga app with Portuguese-cue class library + style tags + "
            "Mat-Pilates tagged tracks + corporate-class booking + member tier — mobile-native "
            "delivery for the Portuguese-speaking + corporate-yoga audience."
        ),
    },
    "akshayrathodfitnesscoach@gmail.com": {
        "niche": "IN 90-day fat-to-fit transformation specialist (Akshay Rathod Fitness Coach, 1.29K)",
        "segment_original": "IN Online Transformation Coach (16+yr exp)",
        "industry": "Fitness / fat loss + muscle gain + Indian diet (IN)",
        "angle_to_take": (
            "Akshay Rathod (1.29K, IN) — 16+yr CSCS + rehab specialist + sports nutritionist "
            "+ supplement consultant; 3500+ clients transformed via 90 Days Fat-to-Fit "
            "Challenge with paid online coaching (workout + diet plan). personal gmail. Frame "
            "a branded Akshay-Rathod app with 90-day program calendar + Hindi-cue workout "
            "library + Indian-diet plan modules + supplement-shelf + 1:1 coaching intake + "
            "member tier — mobile-native upgrade for the 3500-client pipeline."
        ),
    },
    "anugraha6613@gmail.com": {
        "niche": "IN AYUSH-cert online yoga + TT classes (HEALTH IS WEALTH Online Yoga Classes, 1.28K)",
        "segment_original": "IN Govt-AYUSH-cert Online Yoga + TT",
        "industry": "Wellness / yoga + Govt-cert teacher training (IN)",
        "angle_to_take": (
            "HEALTH IS WEALTH Online Yoga Classes (1.28K, IN) — runs Yoga Certification Board "
            "Ministry of AYUSH-cert online yoga classes + Teacher Training course intake via "
            "Google Form + WhatsApp (9074062864). personal gmail. Frame a branded HIW-Yoga "
            "app with online yoga class library + AYUSH TT-curriculum modules + cohort tier + "
            "Google-Form-replacement registration flow + member tracker — mobile-native intake "
            "for the AYUSH-cert pipeline."
        ),
    },
    "seeu@ufitupilates.com": {
        "niche": "VN STOTT-trained Pilates+ Method founder with 1000+ clients across 2 HCMC studios (KHLOE TAM ANH / UFiTU PILATES+, 1.26K)",
        "segment_original": "VN Pilates Method Founder + Studios",
        "industry": "Wellness / Pilates+ Method + studios (VN, HCMC)",
        "angle_to_take": (
            "KHLOE TAM ANH (1.26K, VN) — STOTT-trained Pilates instructor + creator of "
            "Pilates+ Method (1000+ clients/members), runs 2 boutique UFiTU PILATES+ studios "
            "in HCMC + Thao Dien with online booking on ufitupilates.com. role-based seeu@. "
            "Frame a branded UFiTU-Pilates+ app with Pilates+ Method tagged class library + "
            "in-studio + online booking + private/duet/group tier intake + member tracker — "
            "mobile-native upgrade replacing the Acuity-style web-booking page."
        ),
    },
    "info@beyogi.com": {
        "niche": "US yoga insurance + teacher resources brand (beYogi, 1.15K)",
        "segment_original": "US Yoga Insurance + Teacher Resources Brand",
        "industry": "Wellness / yoga insurance + teacher business resources (US)",
        "angle_to_take": (
            "beYogi (1.15K, US) — yoga insurance + teacher business / class-planning "
            "resources brand on beyogi.com (B2B-flavor). role-based info@. Pitch the brand on "
            "a companion AppBillChat app — branded beYogi app with insurance-customer onboarding "
            "+ teacher-resource library (anatomy + sequencing + business advice) + insurance-"
            "claim flow + member tier — turning the insurance customer base into a daily-use "
            "teacher-tools mobile property."
        ),
    },
    "info@antarayoga.nl": {
        "niche": "NL Vinyasa krama yoga + chair yoga + corporate teacher (Antara Yoga / Irene, 1.01K)",
        "segment_original": "NL Vinyasa Krama Yoga + Corporate Teacher",
        "industry": "Wellness / yoga + corporate wellness (NL)",
        "angle_to_take": (
            "Antara Yoga / Irene (1.01K, NL) — Vinyasa krama yoga teacher offering "
            "personalized vinyasa + pranayama + mindfulness + chair yoga + corporate yoga on "
            "antarayoga.nl. role-based info@. Frame a branded Antara-Yoga app with Vinyasa "
            "krama tagged class library + chair-yoga accessibility track + corporate-class "
            "booking + member tier — mobile-native intake for the individual + corporate split."
        ),
    },
}
