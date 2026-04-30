"""
0430 사이클 매핑 — Fitness / Mindset / Yoga / Nutrition + drop.

키 = email (소문자). 값 = {category, niche, segment_original, industry, angle_to_take}.
drop 행은 angle_to_take 등 빈 문자열.
"""

MAPPING = {
    # ============================================================
    # FITNESS — PT / CrossFit / Pilates / 홈트 / 댄스 피트니스
    # ============================================================
    "xenia@xglow-mgmt.com": {
        "category": "fitness",
        "niche": "HK/BALI female fitness + lifestyle creator running a paid Women's Mentorship community",
        "segment_original": "Asia-based home-workout creator (Emi Wong, 7.42M)",
        "industry": "Fitness Creator + Female Mentorship Coach (B2C, agency-managed)",
        "angle_to_take": "Emi Wong (7.42M, HK/BALI) — runs a Women's Mentorship community alongside home-workout content. Frame a branded Emi Wong app: paid mentorship cohorts + replay library + workout streak tracker, replacing the Google Form + email + Discord patchwork with one member surface that scales her mentorship without 1:1 burnout.",
    },
    "walkathome@streaming-subscription.com": {
        "category": "fitness",
        "niche": "30-year at-home walking workout brand (Leslie Sansone)",
        "segment_original": "Legacy fitness IP (Walk at Home, 5.91M)",
        "industry": "Fitness Brand / Subscription Streaming",
        "angle_to_take": "Walk at Home (5.91M) already runs a streaming subscription. Frame a co-branded native app that consolidates streaming + program tracking + walk-streak gamification — a member surface tuned to a 50+ audience that won't navigate a generic OTT clone.",
    },
    "zumbaclass.fitness@gmail.com": {
        "category": "fitness",
        "niche": "Zumba dance-fitness tutorial channel (weekly cardio/weight-loss focus)",
        "segment_original": "Dance-fitness mass channel (Zumba Class, 3.33M)",
        "industry": "Fitness Creator (B2C, dance vertical)",
        "angle_to_take": "Zumba Class (3.33M) ships two new sessions a week on a fixed schedule. Frame a branded app that turns the schedule into a routine: weekly drop notifications, dance-streak tracker, downloadable choreography library — replaces YT-only viewing with retention you can monetize.",
    },
    "imizimage@gmail.com": {
        "category": "fitness",
        "niche": "KR lifestyle + wellness creator with a 30-Day Fast Weight-Loss program",
        "segment_original": "KR weight-loss / lifestyle coach (MIZI, 3.13M)",
        "industry": "Fitness + Lifestyle Coach (B2C, KR market)",
        "angle_to_take": "MIZI (3.13M, KR) sells a 30-Day Fast Weight-Loss plan via miziwellness.com. Frame a branded MIZI app: 30-day cohort onboarding + daily check-in + weight-tracking — replaces the email-PDF program format with a habit surface, and gives the KR audience a Korean-first UX they actually finish.",
    },
    "joannasohofficial@gmail.com": {
        "category": "fitness",
        "niche": "ACE-certified PT + NASM Women's Fitness Specialist + Nutrition Coach",
        "segment_original": "Women's fitness coach with mental-health credential (Joanna Soh, 3.11M)",
        "industry": "Fitness Creator / Certified Coach (B2C)",
        "angle_to_take": "Joanna Soh (3.11M) holds PT + Women's Fitness + Mental Health credentials — a rare combo. Frame a branded app combining women-specific workouts + nutrition + mood check-ins in one membership: cohort programs + period-aware training plans, replacing the multi-platform funnel with one signature surface.",
    },
    "gunjanshouts@gmail.com": {
        "category": "fitness",
        "niche": "Founder of I'MWOW Health & Fitness + India's #1 Health/Wellness podcast host",
        "segment_original": "IN female fitness founder + podcaster (GunjanShouts, 3.03M)",
        "industry": "Fitness Founder / Podcaster (B2C, IN market)",
        "angle_to_take": "Gunjan (3.03M, IN) runs a fitness company + a podcast. Frame a branded I'MWOW app: workout programs + podcast episodes + transformation community — single login replacing the YT/podcast/website split, with referral tracking she can give to brand partners as a measurable channel.",
    },
    "management@heatherrobertson.com": {
        "category": "fitness",
        "niche": "Certified PT + Nutrition Coach with at-home fitness programs",
        "segment_original": "CA at-home workout creator (Heather Robertson, 2.85M)",
        "industry": "Fitness Creator + Coach (B2C)",
        "angle_to_take": "Heather Robertson (2.85M, CA) already sells at-home programs. Frame a branded Heather Robertson app: program library + calendar-driven plans + nutrition guides + streak tracking — moves a course buyer into a recurring app subscription she fully owns.",
    },
    "danceyog2019@gmail.com": {
        "category": "fitness",
        "niche": "Indian-style dance-fitness cardio with the DWD SMART Formula",
        "segment_original": "Dance fitness creator (DanceWithDeepti, 2.19M)",
        "industry": "Fitness Creator (B2C, dance / IN market)",
        "angle_to_take": "DanceWithDeepti (2.19M) sells a structured \"SMART Formula\" workout method. Frame a branded app: numbered Day 1–N flows + streak tracking + before/after gallery — converts free YT viewers into paying members of a method-driven program.",
    },
    "fullcurvenet@gmail.com": {
        "category": "fitness",
        "niche": "Science + fitness creator (PhD in pathology, lifting/training content)",
        "segment_original": "Strength + science fitness creator (Stephanie Buttermore, 1.18M)",
        "industry": "Fitness Creator (B2C, science angle)",
        "angle_to_take": "Stephanie Buttermore (1.18M, US) blends lab-grade science with strength training. Frame a branded app for evidence-based lifters: study-summary feed + lifting program library + form-check submissions — turns her credibility into a subscription product instead of one-off video views.",
    },
    "melania.antuchas@gmail.com": {
        "category": "fitness",
        "niche": "Online sculpt training (Pulse by Melania) — toned-body program for women",
        "segment_original": "Sculpt-training female creator (Melania Antuchas, 289K)",
        "industry": "Fitness Coach (B2C)",
        "angle_to_take": "Melania (289K) runs Pulse — a paid sculpt program. Frame a branded Pulse app: program calendar + macros-without-obsession food log + accountability cohort — pulls members off Patreon/Stan-style funnels into a real native product she controls.",
    },
    "holisticmovementpilates@gmail.com": {
        "category": "fitness",
        "niche": "Certified Pilates Instructor + Holistic Nutritionist with Mon/Wed releases + members-only Friday",
        "segment_original": "Pilates + holistic nutrition creator (HolisticMovementPilates, 81K)",
        "industry": "Pilates Coach (B2C)",
        "angle_to_take": "HolisticMovementPilates (81K) already runs a Members Only tier on YT. Frame a branded app: Pilates flows library + member-only Friday class behind a paywall + nutrition recipes — replaces YT memberships (where YT keeps 30%) with a direct app subscription.",
    },
    "bk27718@gmail.com": {
        "category": "fitness",
        "niche": "Private personalized Pilates coaching (Miami-based, premium positioning)",
        "segment_original": "Premium Pilates instructor (Elle Pilates, 18.8K)",
        "industry": "Pilates Coach (B2C, premium / NYC-Miami)",
        "angle_to_take": "Elle Pilates (18.8K) sells precision and luxury — a premium booking play. Frame a branded Elle Pilates app: 1:1 booking + on-demand library + form-feedback chat — a high-touch surface that justifies her premium pricing better than DM scheduling.",
    },
    "maddiemilton.social@gmail.com": {
        "category": "fitness",
        "niche": "Pilates Instructor in Denver covering recipes/workouts/hormonal health",
        "segment_original": "Pilates + women's health creator (Maddie Milton, 16.8K)",
        "industry": "Pilates Coach (B2C)",
        "angle_to_take": "Maddie Milton (16.8K) blends Pilates + hormonal-health content. Frame a branded app: cycle-aware Pilates programming + recipe library + hormone check-ins — a niche product that the broad fitness apps don't serve.",
    },

    # ============================================================
    # MINDSET — meditation / breathwork / hypnotherapy / mindset coach
    # ============================================================
    "alunirpro@proton.me": {
        "category": "mindset",
        "niche": "Guided meditations for relaxation, manifestation, and reality shifting",
        "segment_original": "Manifestation / meditation creator (Alunir Meditations, 142K)",
        "industry": "Meditation Creator (B2C, esoteric niche)",
        "angle_to_take": "Alunir (142K) sells via Patreon — flat tiers, no on-demand audio app. Frame a branded Alunir app: themed meditation library + manifestation streak tracker + sleep-loop player — replaces Patreon's listening UX with one she owns and prices independently.",
    },
    "guido-ludwigs@galtam.de": {
        "category": "mindset",
        "niche": "Deep-sleep hypnosis + guided meditations (Elwood Hartlee voice)",
        "segment_original": "Sleep-hypnosis brand (Galtam, 118K)",
        "industry": "Meditation / Hypnosis Brand (B2C, DE-origin global)",
        "angle_to_take": "Galtam (118K) is a sleep-hypnosis brand built around a single signature voice. Frame a branded Galtam app: bedtime-trigger automation + sleep-tracking integration + new-session unlocks for subscribers — premium audio app that mirrors Calm's UX but loyal to one creator's library.",
    },
    "mark@markbowden.org": {
        "category": "mindset",
        "niche": "Clinical hypnotherapist focused on sleep and life improvement",
        "segment_original": "Hypnotherapy creator (Mark Bowden, 71.3K)",
        "industry": "Hypnotherapy / Coach (B2C, GB)",
        "angle_to_take": "Mark Bowden (71.3K, GB) sells sleep-hypnosis sessions and books. Frame a branded app: progressive-track hypnosis library + sleep-routine reminders + 1:1 session booking — turns episodic YT listeners into a recurring subscription with measurable sleep outcomes.",
    },
    "trustandsafety@rebrand.ly": {
        "category": "mindset",
        "niche": "20-year hypnotherapy career (Glenn Harrold) — 10M+ apps sold",
        "segment_original": "Established hypnosis IP (Glenn Harrold, 37.4K YT)",
        "industry": "Meditation / Hypnotherapy IP",
        "angle_to_take": "Glenn Harrold has shipped 10M+ apps already, so the team knows the genre. Frame a refreshed all-in-one app that consolidates the 7-book IP + meditation library + new daily releases — one upgrade SKU instead of dozens of single-session app store listings that fragment the audience.",
    },

    # ============================================================
    # YOGA — vinyasa / yin / hatha / 요가 강사
    # ============================================================
    "richburg.jessica@gmail.com": {
        "category": "yoga",
        "niche": "500-hour certified yoga instructor — mindful movement and balance",
        "segment_original": "US yoga instructor (Jess Yoga, 918K)",
        "industry": "Yoga Teacher (B2C)",
        "angle_to_take": "Jess Yoga (918K, US) teaches across multiple class lengths/styles. Frame a branded app: time-filtered class picker (10/20/45 min) + program tracks (back-care, beginner, hips) + on-mat streak gamification — turns YT casual viewers into paying members with progression they can see.",
    },
    "lucia@yogaembarazadas.com": {
        "category": "yoga",
        "niche": "Spanish-language yoga, with a pregnancy-yoga sub-brand (yogaembarazadas)",
        "segment_original": "ES pregnancy/general yoga teacher (Lucia Liencres, 159K)",
        "industry": "Yoga Teacher (B2C, ES market)",
        "angle_to_take": "Lucia (159K, ES) runs both general yoga and a pregnancy-yoga site. Frame a branded app split by life-stage tracks: prenatal trimester programs + postpartum recovery + general flows — Spanish-first UX that the generic English yoga apps don't cover well.",
    },
    "patrickbeachyoga@gmail.com": {
        "category": "yoga",
        "niche": "Global-touring yoga teacher (Commune Yoga, Seattle) + 200hr YTT co-founder",
        "segment_original": "US yoga teacher + studio + YTT (Patrick Beach, 108K)",
        "industry": "Yoga Teacher / Studio Owner / YTT Provider",
        "angle_to_take": "Patrick Beach (108K) runs a studio + a 200hr Yoga Teacher Training. Frame a branded app: on-demand classes for retail + a separate gated YTT track with attendance, assignment turn-in, and certification tracking — replaces Kajabi-style course tools with a yoga-native member surface.",
    },
    "mail@verenaleuze.de": {
        "category": "yoga",
        "niche": "German Vinyasa-flow yoga for beginners through advanced",
        "segment_original": "DE yoga teacher (Verena Leuze, 70.5K)",
        "industry": "Yoga Teacher (B2C, DE market)",
        "angle_to_take": "Verena Leuze (70.5K, DE) covers all levels in German. Frame a branded German-first yoga app: leveled progression paths + body-region focus filters + offline downloads — fills the gap left by English-default yoga apps for the German-speaking audience.",
    },
    "-prem40216@gmail.com": {
        "category": "yoga",
        "niche": "Hindi-language certified senior yoga teacher (Patanjali) — disease-specific yoga + Ayurveda",
        "segment_original": "Hindi yoga + Ayurveda channel (PK. Yoga Teacher, 67.8K)",
        "industry": "Yoga Teacher (B2C, IN market)",
        "angle_to_take": "PK. Yoga Teacher (67.8K, IN) maps yoga poses to specific health conditions. Frame a branded Hindi-first app: condition-indexed pose library + Ayurveda food guides + daily routine builder — a clinical-grade yoga app for the IN market that monetizes a disease-resolution niche the global apps miss.",
    },
    "teachers@yinyoga.com": {
        "category": "yoga",
        "niche": "Yin Yoga authority — paired with YinYoga.com explainer site",
        "segment_original": "Niche yin yoga authority (Bernie Clark, 30.8K)",
        "industry": "Yoga Teacher / Author (B2C, niche authority)",
        "angle_to_take": "Bernie Clark (30.8K) is the named authority for Yin Yoga. Frame a branded Yin app: pose-by-pose deep-dive library + sequence builder + companion-to-the-book tracks — small-but-loyal audience that pays a premium for canonical content from a category figurehead.",
    },

    # ============================================================
    # NUTRITION — 영양사 / dietitian / 식단 / 다이어트
    # ============================================================
    "drshikhasingh24@gmail.com": {
        "category": "nutrition",
        "niche": "Doctor + Certified Clinical Nutritionist with science-backed nutrition content",
        "segment_original": "IN clinical nutritionist + doctor (Dr. Shikha Singh, 2.97M)",
        "industry": "Nutritionist / Doctor (B2C, IN market)",
        "angle_to_take": "Dr. Shikha Singh (2.97M, IN) sells credibility on \"clinical\" framing. Frame a branded app: condition-indexed diet plans + weekly meal templates + grocery list generator — a clinical-style food planner the generic Indian diet apps don't match, and a paid surface beyond YT ad rev.",
    },
    "kyliesakaida@select.co": {
        "category": "nutrition",
        "niche": "RD + NYT Bestselling Cookbook Author — realistic-and-fun healthy eating",
        "segment_original": "US dietitian + cookbook author (Kylie Sakaida, 1.95M)",
        "industry": "Dietitian / Author (B2C, agency-managed)",
        "angle_to_take": "Kylie Sakaida (1.95M, US) just sold a bestselling cookbook. Frame a branded companion app: cookbook-recipe interactive index + grocery list + meal-plan calendar + bonus video lessons — turns a one-time book buyer into a subscription with new content monthly.",
    },
    "enquiries@chefjackovens.com": {
        "category": "nutrition",
        "niche": "Pro chef (14yr) covering high-protein meal prep + comfort food",
        "segment_original": "AU chef + meal-prep creator (Chef Jack Ovens, 1.62M)",
        "industry": "Chef + Nutrition-adjacent Creator (B2C, AU)",
        "angle_to_take": "Chef Jack (1.62M, AU) leans into high-protein meal prep. Frame a branded app: recipe library with macro tags + weekly meal-prep planner + grocery list export — gives gym-going home cooks a real planning tool instead of saving recipes in the YT-app's bookmark list.",
    },
    "foodfitnessfun.official@gmail.com": {
        "category": "nutrition",
        "niche": "Certified Dietitian + Nutritionist + fitness enthusiast (healthy IN-style recipes)",
        "segment_original": "IN dietitian + fitness creator (FoodFitness&Fun, 1.52M)",
        "industry": "Dietitian (B2C, IN market)",
        "angle_to_take": "Manju Malik (1.52M, IN) covers dietitian-grade recipes. Frame a branded IN-first app: regional Indian diet plans + festival/seasonal recipe rotation + nutrition Q&A — a Hindi/English app for an audience that the global nutrition apps barely localize.",
    },
    "mail@liezljayne.com": {
        "category": "nutrition",
        "niche": "Healthy easy recipes + personal weight-loss journey (40+ lb)",
        "segment_original": "US recipe + weight-loss creator (Liezl Jayne, 1.26M)",
        "industry": "Nutrition / Recipes Creator (B2C)",
        "angle_to_take": "Liezl Jayne (1.26M, US) sells transformation through recipes. Frame a branded app: searchable recipe library + meal-plan templates + before/after community wall — moves email-list buyers of her ebooks into a recurring subscription product.",
    },
    "kennedy@smallscreenmarketing.com": {
        "category": "nutrition",
        "niche": "Healthy quick recipes (HEALTHY FOOD MADE EASY ebook, 85 recipes)",
        "segment_original": "Recipe + ebook creator (fitfoodieselma, 1.11M)",
        "industry": "Nutrition / Recipes Creator (B2C, agency-managed)",
        "angle_to_take": "Selma (1.11M) just launched a recipe ebook. Frame a branded app companion: interactive recipe index + grocery list + minimal-effort weekday meal planner — converts ebook one-shot buyers into monthly app members with new recipes added each week.",
    },
    "mrbfitbusiness@gmail.com": {
        "category": "nutrition",
        "niche": "Easy/sustainable/tasty diet content (IN market)",
        "segment_original": "IN diet creator (Mr. B-fit, 795K)",
        "industry": "Nutrition Creator (B2C, IN market)",
        "angle_to_take": "Mr. B-fit (795K, IN) positions on \"easy diet\". Frame a branded IN diet app: regional Indian meal plans + macro-friendly substitutions + diet-streak tracker — a paid surface for an audience that's outgrown free YT meal videos.",
    },
    "emmie@modernmediaservices.com": {
        "category": "nutrition",
        "niche": "Nutritionist for plant-based + vegan weight loss (creator of SLIM App + Program)",
        "segment_original": "US plant-based weight-loss coach (Healthy Emmie, 745K)",
        "industry": "Nutrition Coach (B2C, vegan vertical)",
        "angle_to_take": "Healthy Emmie (745K) already runs the SLIM App — so they're sold on the app model. Frame a v2 with cohort-based onboarding + macro-aware vegan meal plans + accountability messaging — replaces a basic recipe-only app with a measurable weight-loss program platform.",
    },
    "rimislunchbox29@gmail.com": {
        "category": "nutrition",
        "niche": "Certified Nutritionist specialized in weight management — full-day diet plans",
        "segment_original": "IN weight-management nutritionist (Rimi's Lunch Box, 252K)",
        "industry": "Nutritionist (B2C, IN market)",
        "angle_to_take": "Rimi (252K, IN) sells a paid program already (\"Enroll My Program\"). Frame a branded app for the program: Day-1-to-N diet timeline + recipe rotation + transformation gallery — converts WhatsApp/PDF program delivery into a member surface with retention you can measure.",
    },
    "ewl.adoretrust@gmail.com": {
        "category": "nutrition",
        "niche": "Dr. Dixit Diet — 55-minute Effortless Weight-Loss + Intermittent Fasting (anti-obesity/diabetes campaign)",
        "segment_original": "IN clinical weight-loss campaign (Dr Dixit Lifestyle, 113K)",
        "industry": "Diet / Anti-Obesity Campaign (B2C, IN market)",
        "angle_to_take": "Dr Dixit Lifestyle (113K, IN) drives a structured 55-minute eating-window method. Frame a branded app: fasting-window timer + Indian-meal templates that fit the window + diabetes/HbA1c tracking — turns a free YT method into a paid clinical-grade companion.",
    },
    "rosemarycp24@gmail.com": {
        "category": "nutrition",
        "niche": "Certified nutrition coach focused on healthy lifestyle awareness",
        "segment_original": "Nutrition coach (Nutrition Coach Rose, 78.6K)",
        "industry": "Nutrition Coach (B2C)",
        "angle_to_take": "Rose (78.6K) is early in her funnel. Frame a branded starter app: onboarding quiz + personalized 7-day plan + weekly habit nudges — the lightweight first product that turns YT subs into a paid trial without requiring a flagship cohort program upfront.",
    },
    "theblessedfam555@gmail.com": {
        "category": "nutrition",
        "niche": "Nutrition Bachelors + Health Coach + 22kg personal weight-loss diet plans",
        "segment_original": "US health coach (Kainat Abbas, 74.3K)",
        "industry": "Nutrition / Diet Coach (B2C, mom audience)",
        "angle_to_take": "Kainat (74.3K, US) sells diet plans on a personal-transformation hook. Frame a branded app for moms: family-meal-friendly diet plans + busy-mom 15-min recipe filter + weight check-ins — a niche the generic diet apps don't position for.",
    },
    "shivangilostit@gmail.com": {
        "category": "nutrition",
        "niche": "50kg personal weight-loss — sharing recipes + lifestyle (with travel sub-content)",
        "segment_original": "IN weight-loss creator (ShivangiLostit, 55K)",
        "industry": "Diet / Weight-Loss Creator (B2C, IN market)",
        "angle_to_take": "Shivangi (55K, IN) sells transformation evidence (50kg loss). Frame a branded app: weight-loss recipe library + IN-specific calorie reference + transformation-journal feature — converts \"watched her story\" YT viewers into paying members of her method.",
    },
    "james@nutritiontriathlon.com": {
        "category": "nutrition",
        "niche": "Triathlon-specific nutrition for 70.3 / Ironman athletes (MSc-credentialed)",
        "segment_original": "GB endurance-sport nutritionist (Nutrition Triathlon, 31.2K)",
        "industry": "Sports Nutritionist (B2C, niche endurance)",
        "angle_to_take": "James (31.2K, GB) serves a high-pay-willingness niche (Ironman racers). Frame a branded app: race-distance-specific fueling plans + workout-day macro calculator + race-week taper protocols — small audience but premium pricing the broad fitness apps can't justify.",
    },
    "hetalg82@gmail.com": {
        "category": "nutrition",
        "niche": "Foods & Nutrition postgrad with 16yr experience — broad healthy-food channel",
        "segment_original": "IN nutritionist (Nutritionist Hetal Chheda, 20.4K)",
        "industry": "Nutritionist (B2C, IN market)",
        "angle_to_take": "Hetal (20.4K, IN) brings deep credentials to a small audience. Frame a branded app: 1:1 consult booking + personalized diet-plan delivery + adherence check-ins — a clinical-style nutrition surface that beats running the practice over WhatsApp.",
    },

    # ============================================================
    # DROP — 음악 / 게임 / SW / 모호한 라이프스타일 / 브랜드
    # ============================================================
    "matt@humanmg.com":                   {"category": "drop", "niche": "", "segment_original": "", "industry": "", "angle_to_take": ""},
    "skip@leadingline.online":            {"category": "drop", "niche": "", "segment_original": "", "industry": "", "angle_to_take": ""},
    "customer_service@wondershare.com":   {"category": "drop", "niche": "", "segment_original": "", "industry": "", "angle_to_take": ""},
    "ryini@ryinibeats.com":               {"category": "drop", "niche": "", "segment_original": "", "industry": "", "angle_to_take": ""},
    "customerservice@aloyoga.com":        {"category": "drop", "niche": "", "segment_original": "", "industry": "", "angle_to_take": ""},
    "management@trapmasters.io":          {"category": "drop", "niche": "", "segment_original": "", "industry": "", "angle_to_take": ""},
    "classroom@underdogmusicschool.com":  {"category": "drop", "niche": "", "segment_original": "", "industry": "", "angle_to_take": ""},
    "padmashreehelpful01@gmail.com":      {"category": "drop", "niche": "", "segment_original": "", "industry": "", "angle_to_take": ""},
    "rlybeats@rlybeats.com":              {"category": "drop", "niche": "", "segment_original": "", "industry": "", "angle_to_take": ""},
    "studioplug.net@gmail.com":           {"category": "drop", "niche": "", "segment_original": "", "industry": "", "angle_to_take": ""},
    "lollypopbeatz@gmail.com":            {"category": "drop", "niche": "", "segment_original": "", "industry": "", "angle_to_take": ""},
    "faizan@wethemvmnt.com":              {"category": "drop", "niche": "", "segment_original": "", "industry": "", "angle_to_take": ""},
    "movecutclone@gmail.com":             {"category": "drop", "niche": "", "segment_original": "", "industry": "", "angle_to_take": ""},
    "shyybeats1@gmail.com":               {"category": "drop", "niche": "", "segment_original": "", "industry": "", "angle_to_take": ""},
    "lna@lnamusic.com":                   {"category": "drop", "niche": "", "segment_original": "", "industry": "", "angle_to_take": ""},
    "teamred808@gmail.com":               {"category": "drop", "niche": "", "segment_original": "", "industry": "", "angle_to_take": ""},
    "jeetubeats@gmail.com":               {"category": "drop", "niche": "", "segment_original": "", "industry": "", "angle_to_take": ""},
    "badhabit.biz@gmail.com":             {"category": "drop", "niche": "", "segment_original": "", "industry": "", "angle_to_take": ""},
    "contact.beatsbyai@gmail.com":        {"category": "drop", "niche": "", "segment_original": "", "industry": "", "angle_to_take": ""},
    "saksham.jha029@gmail.com":           {"category": "drop", "niche": "", "segment_original": "", "industry": "", "angle_to_take": ""},
    "markmywords.beats@gmail.com":        {"category": "drop", "niche": "", "segment_original": "", "industry": "", "angle_to_take": ""},
    "hypernestdigitalmedia@gmail.com":    {"category": "drop", "niche": "", "segment_original": "", "industry": "", "angle_to_take": ""},
    "studioninekolkata@gmail.com":        {"category": "drop", "niche": "", "segment_original": "", "industry": "", "angle_to_take": ""},
    "toniiuh@gmail.com":                  {"category": "drop", "niche": "", "segment_original": "", "industry": "", "angle_to_take": ""},
    "ambitiouskid403@gmail.com":          {"category": "drop", "niche": "", "segment_original": "", "industry": "", "angle_to_take": ""},
    "engagemusicproduction@gmail.com":    {"category": "drop", "niche": "", "segment_original": "", "industry": "", "angle_to_take": ""},
    "uranus040220@gmail.com":             {"category": "drop", "niche": "", "segment_original": "", "industry": "", "angle_to_take": ""},
    "tipshindiflstudio@gmail.com":        {"category": "drop", "niche": "", "segment_original": "", "industry": "", "angle_to_take": ""},
    "rmakesbeats@gmail.com":              {"category": "drop", "niche": "", "segment_original": "", "industry": "", "angle_to_take": ""},
    "beatpro.in@gmail.com":               {"category": "drop", "niche": "", "segment_original": "", "industry": "", "angle_to_take": ""},
    "makenobeats@gmail.com":              {"category": "drop", "niche": "", "segment_original": "", "industry": "", "angle_to_take": ""},
    "morflstricks@yahoo.com":             {"category": "drop", "niche": "", "segment_original": "", "industry": "", "angle_to_take": ""},
    "beatsmake6@gmail.com":               {"category": "drop", "niche": "", "segment_original": "", "industry": "", "angle_to_take": ""},

    # ============================================================
    # 0430 ROUND 2 — 영상 description 추출 + crawl 보강으로 회수된 채널
    # ============================================================

    # --- FITNESS (Round 2) ---
    "madfit95@gmail.com": {
        "category": "fitness",
        "niche": "Real-time at-home workouts for all fitness levels",
        "segment_original": "CA at-home workout creator (MadFit, 11.3M)",
        "industry": "Fitness Creator (B2C, mass at-home workout)",
        "angle_to_take": "MadFit (11.3M, CA) ships REAL-TIME workout-along videos — a format viewers literally do alongside the screen. Frame a branded MadFit app: real-time class player + Apple Watch heart-rate sync + streak tracker that rewards finishing the full session — turns YT followers into a recurring app subscription with retention data she can monetize.",
    },
    "pamela@biancoberlin.com": {
        "category": "fitness",
        "niche": "Free real-time workouts + 12 paid workout plans (Pam app already live)",
        "segment_original": "DE workout creator with own app (Pamela Reif, 10.7M)",
        "industry": "Fitness Creator + App (B2C, agency-managed)",
        "angle_to_take": "Pamela Reif (10.7M, DE) already has pam-app.de on Wix — visibly templated UI. Frame an upgrade: native iOS/Android app with offline downloads + Apple Health write + cohort challenges — a v2 that drops the Wix dependency and gives her engineering ownership over her largest asset.",
    },
    "mgmt@growwithjo.com": {
        "category": "fitness",
        "niche": "Beginner-friendly home workouts for women (Grow With Jo community)",
        "segment_original": "US women's beginner-fitness creator (growwithjo, 8.7M)",
        "industry": "Fitness Creator + Community (B2C)",
        "angle_to_take": "growwithjo (8.7M, US) runs the community on Circle + Stripe — a stack patched together. Frame a branded growwithjo app: community feed + workout calendar + transformation gallery + payments in one — replaces the Circle+Stripe+YT-comments split with a single member surface tuned to the beginner-women audience.",
    },
    "root@hasfit.com": {
        "category": "fitness",
        "niche": "1,000+ on-demand home workouts + senior-specific programs (Coach Kozak)",
        "segment_original": "US fitness brand with existing app (HASfit, 2.25M)",
        "industry": "Fitness Brand + App (B2C, broad-age audience)",
        "angle_to_take": "HASfit (2.25M) already has a Top Fitness App with 1B+ workouts done. Frame a focused v2 vertical: senior-specific app with low-impact tracks + family caregiver share + condition-tagged routines (post-surgery, arthritis) — splits the senior audience off into a premium SKU instead of stuck inside a generic fitness app.",
    },
    "margaret@margaretelizabeth.co": {
        "category": "fitness",
        "niche": "500-hour Certified Pilates Instructor (RA-driven origin story, online since 2020)",
        "segment_original": "US online Pilates instructor (Margaret Elizabeth, 114K)",
        "industry": "Pilates Coach (B2C)",
        "angle_to_take": "Margaret (114K, US) has a Squarespace site — a content site, not a member app. Frame a branded app: Pilates flows library + RA-friendly modifier tags + 1:1 private session booking — turns her credentialed niche (auto-immune-aware Pilates) into a paid subscription product the generic fitness apps don't serve.",
    },
    "kaylie@theglowmethod.co": {
        "category": "fitness",
        "niche": "Vinyasa + Pilates + Yoga Sculpt + Barre — own Glow Method app + retreats",
        "segment_original": "US Pilates/Sculpt/Barre creator with own app (The Glow Method, 112K)",
        "industry": "Pilates / Sculpt Coach + App (B2C)",
        "angle_to_take": "The Glow Method (112K) already has an app + retreats — they get the model. Frame a v2 with retreat add-on integration: app subscriber sees retreat dates + can buy attendance inside the app + post-retreat replay tracks gated to attendees — joins online and in-person revenue into one funnel.",
    },
    "keelpilates@gmail.com": {
        "category": "fitness",
        "niche": "Certified mat Pilates instructor (challenging at-home sessions)",
        "segment_original": "CA mat Pilates creator (Keel Pilates, 47.2K)",
        "industry": "Pilates Coach (B2C)",
        "angle_to_take": "Keel Pilates (47.2K, CA) sits in the at-home mat-Pilates niche — accessible, no equipment. Frame a branded starter app: difficulty-progression program tracks + no-equipment filter + form-cue audio overlay — a low-friction first product that converts free YT viewers into a $9/mo subscription without needing a flagship cohort.",
    },
    "zhoe@moveactive.co": {
        "category": "fitness",
        "niche": "APPI-certified Pilates Instructor + Physiotherapist (Mat + Reformer)",
        "segment_original": "AU Pilates+PT creator (MOVE WITH ISSY PILATES, 18.5K)",
        "industry": "Pilates / Physio Coach (B2C, AU)",
        "angle_to_take": "Issy (18.5K, AU) is dual-credentialed (Pilates + Physiotherapist) — a rare authority hook. Frame a branded app: injury-aware Pilates tracks + post-physio-recovery programs + symptom-based pose finder — a clinical-grade Pilates app that distinguishes from the dozens of generic ones.",
    },

    # --- MINDSET (Round 2) ---
    "michael_sealey@hotmail.com": {
        "category": "mindset",
        "niche": "Sleep hypnosis + hypnotherapy + guided meditation (positive-hypnosis approach)",
        "segment_original": "Long-running hypnosis creator (Michael Sealey, 2.06M)",
        "industry": "Hypnotherapy / Meditation Creator (B2C)",
        "angle_to_take": "Michael Sealey (2.06M) runs one of the largest sleep-hypnosis libraries on YT. Frame a branded Sealey app: full library off-YT + sleep-cycle alarm trigger + new-session unlock for subscribers — moves loyal listeners off YT (where ads break the immersion) into a paid sleep-tuned audio app.",
    },
    "thehonestguys@gmx.co.uk": {
        "category": "mindset",
        "niche": "Sleep meditation + fantasy visualizations + relaxation stories (effortless approach)",
        "segment_original": "GB sleep-meditation duo (The Honest Guys, 1.28M)",
        "industry": "Meditation / Sleep-Story Creator (B2C)",
        "angle_to_take": "The Honest Guys (1.28M, GB) sells products on Squarespace — heavy template feel. Frame a branded app: themed visualization library + bedtime trigger from Apple Health/Calendar + signature-voice consistency — a premium audio app that mirrors Calm's UX but loyal to a single creator's library at a lower price point.",
    },
    "connectandcre8@gmail.com": {
        "category": "mindset",
        "niche": "Manifestation + mindset + In2Bliss meditation app (alignment-energy framing)",
        "segment_original": "AU meditation + manifestation creator with app (Rising Higher, 1.04M)",
        "industry": "Meditation / Manifestation Creator + App",
        "angle_to_take": "Rising Higher (1.04M, AU) already runs In2Bliss — they understand the model. Frame a v2 angle: manifestation-track gamification + daily intention prompts + community circle for paid tier — adds engagement loops that a typical meditation app misses.",
    },
    "michellessanctuary@gmail.com": {
        "category": "mindset",
        "niche": "Cozy bedtime sleep stories + brief guided sleep meditations (signature female voice since 2015)",
        "segment_original": "US sleep-story channel (Michelle's Sanctuary, 115K)",
        "industry": "Sleep-Story / Meditation Creator (B2C)",
        "angle_to_take": "Michelle's Sanctuary (115K, US) is in a fast-growing sleep-story niche. Frame a branded app: ad-free story library + sleep-timer with fade-out + new story drops every Friday for subscribers — a focused niche app that competes with Get Sleepy/Calm-stories for a fraction of the price.",
    },

    # --- YOGA (Round 2) ---
    "maris@yogauploadplus.com": {
        "category": "yoga",
        "niche": "Vinyasa Flow + Power Yoga + Wrist-Free options (skillful + nurturing approach)",
        "segment_original": "US online yoga teacher (YOGA UPLOAD, 116K)",
        "industry": "Yoga Teacher (B2C)",
        "angle_to_take": "Maris (116K, US) already runs yogauploadplus.com on Mailchimp + Stripe — split tools. Frame a branded app that consolidates the funnel: program library + Mailchimp-replacing in-app drips + Stripe inside the app for subscriptions — one stack instead of three, with native push notifications she doesn't currently get.",
    },
    "tanatrzebinski@gmail.com": {
        "category": "yoga",
        "niche": "Power yoga + slow vinyasa + condition-targeted classes (anxiety, weight loss, energy)",
        "segment_original": "ZA yoga + Pilates creator (Tana Yoga, 111K)",
        "industry": "Yoga Teacher (B2C)",
        "angle_to_take": "Tana (111K, ZA) tags content by problem (anxiety, weight loss, flexibility). Frame a branded app: problem-indexed pose finder + outcome-based program tracks (e.g. \"Anxiety Reset 14-day\") + before/after self-rating — a tool the algorithmic YT browse can't replicate.",
    },
    "matt@yinyogawithmatt.com": {
        "category": "yoga",
        "niche": "Yin Yoga authority — physical/mental/emotional balance, athlete + Hollywood + military audience",
        "segment_original": "US Yin Yoga niche teacher (Yin Yoga with Matt, 14.2K)",
        "industry": "Yoga Teacher (B2C, niche)",
        "angle_to_take": "Matt (14.2K, US) already sells a membership on yinyogawithmatt.com (WordPress). Frame a branded app: Yin-only sequence library + long-hold pose timer + recovery-focused programs for athletes — moves a small loyal audience from a WordPress paywall into a polished native app they pay more for.",
    },

    # --- NUTRITION (Round 2) ---
    "mitahar@gmail.com": {
        "category": "nutrition",
        "niche": "India's leading public health advocate + globally followed nutritionist (1.7M+ books sold)",
        "segment_original": "IN top-tier nutritionist + author (Rujuta Diwekar, 1.14M)",
        "industry": "Nutritionist / Author (B2C, IN tier-1)",
        "angle_to_take": "Rujuta Diwekar (1.14M, IN) sells books at scale — 1.75M copies. Frame a branded app: book-companion content + IN-regional meal plans by season + daily food-rules audio (her signature short tips) — converts book buyers into a recurring subscription she can scale globally.",
    },
    "josh@mealprepmanual.com": {
        "category": "nutrition",
        "niche": "Meal-prep recipes with calorie + macro estimates calculated for the user",
        "segment_original": "US meal-prep creator (Josh Cortis, 839K)",
        "industry": "Nutrition / Meal-Prep Creator (B2C)",
        "angle_to_take": "Josh (839K, US) already runs mealprepmanual.com on Stripe + WordPress. Frame a branded app: macro-tagged recipe library + grocery list export + week-of meal-prep planner — replaces a content site with a planning tool that lifts subscription LTV vs one-off recipe-page traffic.",
    },
    "rj@remingtonjamesfitness.com": {
        "category": "nutrition",
        "niche": "Healthy recipes + fitness content + Anabolic Cookbook (Payhip)",
        "segment_original": "Recipe + cookbook creator (Remington James, 733K)",
        "industry": "Nutrition / Recipe Creator (B2C)",
        "angle_to_take": "Remington (733K) sells the Anabolic Cookbook on Payhip — basic checkout. Frame a branded app companion: cookbook-recipe interactive index + macro adjustment by goal + bonus weekly recipes for subscribers — turns a one-time cookbook buyer into a recurring app subscription.",
    },
    "eatmorelosemore7@gmail.com": {
        "category": "nutrition",
        "niche": "Sustainable fat loss + postpartum recovery + balanced-meal nutrition education",
        "segment_original": "IN nutrition educator (Eat more Lose more, 351K)",
        "industry": "Nutrition Educator (B2C, IN market)",
        "angle_to_take": "Eat more Lose more (351K, IN) covers postpartum recovery — a high-pay-willingness niche. Frame a branded app: trimester-aware postpartum diet tracks + macro education modules + new-mom community circle — the Indian-context postpartum nutrition app the global apps don't localize.",
    },
    "drdevpune@gmail.com": {
        "category": "nutrition",
        "niche": "Doctor / weight-loss educator with India-wide health awareness focus",
        "segment_original": "IN doctor + weight-loss educator (Dr. Dev, 96.2K)",
        "industry": "Doctor + Weight-Loss Coach (B2C, IN market)",
        "angle_to_take": "Dr. Dev (96.2K, IN) leads with credentials but content is short / awareness-style. Frame a branded app: structured 30-day weight-loss program + IN-meal templates + clinical-style symptom check-ins — a paid product that gives the channel a clear funnel beyond YT awareness.",
    },
    "khyatirupani@balancenutrition.in": {
        "category": "nutrition",
        "niche": "Personalized diets for PCOS, thyroid, fatty liver, diabetes, gut issues — 75K+ clients in 94+ countries",
        "segment_original": "IN clinical-condition nutrition practice (Balance Nutrition, 58.3K)",
        "industry": "Nutrition Practice (B2B2C, condition-specialized)",
        "angle_to_take": "Balance Nutrition (58.3K, IN) already runs a 75K-client practice across 94 countries. Frame a branded app: condition-specific diet tracks (PCOS, thyroid, fatty liver) + dietitian chat handoff + lab-result symptom logger — productizes a service business into a subscription that scales beyond 1:1 capacity.",
    },
    "shinuvlogs2022@gmail.com": {
        "category": "nutrition",
        "niche": "Certified nutritionist specialized in low-carb nutrition",
        "segment_original": "Low-carb nutrition channel (Shinuvlogs, 13.5K)",
        "industry": "Nutritionist (B2C, low-carb niche)",
        "angle_to_take": "Shinu (13.5K) sits in a focused low-carb niche. Frame a branded app: low-carb meal plans + carb-counter calculator + ketosis-tracking education — small audience but a clear vertical that the broad keto apps don't humanize with one creator's voice.",
    },

    # --- DROP (Round 2) ---
    "gpk-usersupport@google.com":         {"category": "drop", "niche": "", "segment_original": "", "industry": "", "angle_to_take": ""},  # Chloe Ting — Google Play role email, false positive
    "network@emvn.co":                    {"category": "drop", "niche": "", "segment_original": "", "industry": "", "angle_to_take": ""},  # Mind Motivation Coaching — copyright re-uploads
    "seminars@crossfit.com":              {"category": "drop", "niche": "", "segment_original": "", "industry": "", "angle_to_take": ""},  # CrossFit org — large brand
    "transcripts@crooked.com":            {"category": "drop", "niche": "", "segment_original": "", "industry": "", "angle_to_take": ""},  # Get Sleepy — host network email, false positive
    "shop@mayhemnation.com":              {"category": "drop", "niche": "", "segment_original": "", "industry": "", "angle_to_take": ""},  # CrossFit Mayhem — e-commerce role
    "siteerrors@audible.com":             {"category": "drop", "niche": "", "segment_original": "", "industry": "", "angle_to_take": ""},  # Papi MindsetCoach — Audible role email, false positive
    "helloboy1979@gmail.com":             {"category": "drop", "niche": "", "segment_original": "", "industry": "", "angle_to_take": ""},  # Dr Manjunath — accelerated learning, off-topic
    "customercare@align-pilates.com":     {"category": "drop", "niche": "", "segment_original": "", "industry": "", "angle_to_take": ""},  # Align-Pilates — equipment brand
    "stefan.jarmolowicz@upfitness.com":   {"category": "drop", "niche": "", "segment_original": "", "industry": "", "angle_to_take": ""},  # UltimatePerformance — large PT chain
}
