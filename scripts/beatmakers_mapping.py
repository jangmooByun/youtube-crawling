"""Per-row niche / segment_original / industry / angle_to_take for
data/2026-04-24/beatmakers.csv (28 rows). Hand-crafted from each channel's
YouTube description, handle, follower count, and country. Same pattern as
nutrition_mapping.py / lifestyle_mapping.py.
"""

MAPPING = {
    "matt@humanmg.com": {
        "niche": "Absurdist how-to comedy content (HowToBasic)",
        "segment_original": "Comedy / Absurdist (mis-categorized)",
        "industry": "Entertainment / comedy",
        "angle_to_take": (
            "Human Management represents HowToBasic (17.8M, AU) — this is a comedy channel, NOT a beatmaker "
            "(mis-categorized from source discovery). Frame any outreach as brand-partnership / sponsored-"
            "content conversation; the producer-tool pitch does not apply."
        ),
    },
    "skip@leadingline.online": {
        "niche": "Gaming-tutorial / Minecraft-tips entertainment content",
        "segment_original": "Gaming Entertainment (mis-categorized)",
        "industry": "Gaming / entertainment",
        "angle_to_take": (
            "Leading Line Online represents Skip the Tutorial (10.4M, US) — this is a gaming-tutorial channel, "
            "NOT a beatmaker (mis-categorized). Frame as gaming-creator brand partnership; producer-tool pitch "
            "does not apply."
        ),
    },
    "customer_service@wondershare.com": {
        "niche": "Wondershare Filmora video-editor software brand",
        "segment_original": "Software Vendor (not a creator)",
        "industry": "Software / video editing",
        "angle_to_take": (
            "Role-based customer-service contact for Wondershare Filmora (913k). This is a software-vendor "
            "brand, not an individual creator. Frame as brand-partnership / affiliate conversation; skip the "
            "creator-app pitch."
        ),
    },
    "ryini@ryinibeats.com": {
        "niche": "Hip-hop rap/rock guitar beats & sample packs (LA, Berklee-trained)",
        "segment_original": "Hip-Hop Beatmaker + Guitar Producer",
        "industry": "Music / production",
        "angle_to_take": (
            "Ryini Beats (520k, LA) sells beats at ryinibeats.com and positions around rock/metal guitar "
            "samples into hip-hop. Lead with questions around beat-pack repeat buyers and guitar-sample "
            "catalog depth. Frame a branded Ryini app with beat vault, guitar-sample library, and a producer "
            "circle — tighter than website-only sales."
        ),
    },
    "management@trapmasters.io": {
        "niche": "FL Studio hip-hop remake breakdowns & tutorials",
        "segment_original": "FL Studio / Hip-Hop Tutorial Creator",
        "industry": "Music / education",
        "angle_to_take": (
            "Trapmasters Management represents Aiden Kenway (359k, AU) — FL Studio remake/tutorial content. "
            "Frame a branded Aiden app with structured FL Studio curriculum, project files, mentor Q&A, "
            "and a producer community — complementary to management's brand-deal pipeline."
        ),
    },
    "classroom@underdogmusicschool.com": {
        "niche": "Electronic-music school with Brussels classroom (Underdog)",
        "segment_original": "Electronic Music School",
        "industry": "Music / education",
        "angle_to_take": (
            "Underdog Electronic Music School (346k, BE) runs a Brussels classroom + courses at "
            "underdog.brussels. Role-based classroom@ inbox for Brussels-specific inquiries. Frame a branded "
            "Underdog app with cohort feed, assignment tracking, and mentor hours — replacing Zoom/email "
            "coordination for the Brussels classroom."
        ),
    },
    "rlybeats@rlybeats.com": {
        "niche": "Minimalist lo-fi hip-hop beats ('music go brrrr')",
        "segment_original": "Lo-fi Beatmaker",
        "industry": "Music / production",
        "angle_to_take": (
            "rly Beats (212k, CA) runs rlybeats.com with extremely minimal bio. Frame a branded rly app "
            "with beat catalog, type-beat drops, and a producer community — owned retention beyond website-only "
            "sales."
        ),
    },
    "studioplug.net@gmail.com": {
        "niche": "FL Studio tutorial content for beatmakers",
        "segment_original": "FL Studio Tutorial Creator",
        "industry": "Music / education",
        "angle_to_take": (
            "StudioPlug (161k, US) runs FL Studio tutorials + tips. Lead with questions around tutorial-to-"
            "student conversion. Frame a branded StudioPlug app with structured FL Studio course, project files, "
            "and a student community — more polished than loose YouTube tutorials."
        ),
    },
    "lollypopbeatz@gmail.com": {
        "niche": "London young-producer type-beats with secondary channel",
        "segment_original": "Type-Beat Producer (London)",
        "industry": "Music / production",
        "angle_to_take": (
            "Lollypopbeatz (145k, GB, 25yo London producer) runs type-beats + secondary channel + Miami Music "
            "Management. Frame a branded Lollypop app consolidating both channels with beat vault, type-beat "
            "subscription, and a producer community — complementary to management."
        ),
    },
    "faizan@wethemvmnt.com": {
        "niche": "Indian Hip-Hop collective (Sez on the Beat / MVMNT label & management)",
        "segment_original": "Hip-Hop Collective + Label",
        "industry": "Music / label & management",
        "angle_to_take": (
            "THE MVMNT / Sez on the Beat (122k, IN) is a hip-hop collective + record label + management "
            "vertical — co-founder contact. Frame a branded MVMNT app with roster releases, mentorship "
            "sessions, and a member feed — owned retention vs. scattered Soundcloud/IG posting."
        ),
    },
    "movecutclone@gmail.com": {
        "niche": "Sample-based boombap hip-hop + hardware/software experimentation",
        "segment_original": "Boombap Beatmaker + Gear Explorer",
        "industry": "Music / production",
        "angle_to_take": (
            "Accurate Beats (110k, SE) releases on Spotify/Bandcamp/Soundcloud and runs Move Cut Clone + "
            "tape drops. Frame a branded Accurate app with sampler-science tutorials, tape catalog, and "
            "a boombap community — consolidating Spotify + Bandcamp + Soundcloud + YouTube sprawl."
        ),
    },
    "shyybeats1@gmail.com": {
        "niche": "AU instrumentals-focused beatmaker (sparse bio)",
        "segment_original": "Instrumentals Beatmaker (AU)",
        "industry": "Music / production",
        "angle_to_take": (
            "SHYY BEATS (86.7k, AU) has minimal bio — IG-primary + gmail for inquiries. Frame a branded SHYY "
            "app with instrumental catalog, type-beat drops, and a producer community — owned retention beyond "
            "IG."
        ),
    },
    "teamred808@gmail.com": {
        "niche": "Hindi-language FL Studio tutorial creator (IN)",
        "segment_original": "FL Studio Tutorial (Hindi)",
        "industry": "Music / education",
        "angle_to_take": (
            "RedBlood Music Production (72k, IN Hindi) runs free Hindi FL Studio tutorials + commissioned "
            "music. Frame a branded RedBlood app with structured Hindi FL Studio course, commission intake, "
            "and a Hindi-producer community — replacing IG/FB/Twitter sprawl."
        ),
    },
    "jeetubeats@gmail.com": {
        "niche": "Hindi FL Studio course creator (Rajasthan, CA by training)",
        "segment_original": "Paid FL Studio Course Creator (Hindi)",
        "industry": "Music / education",
        "angle_to_take": (
            "Jeetu Beats (69.3k, IN) already sells a paid FL Studio course at jeetubeats.com and runs Telegram "
            "+ YouTube + website. Lead with questions around course-to-student retention and Telegram-channel "
            "overhead. Frame a branded Jeetu app consolidating course delivery, Telegram community, and "
            "website under one stack."
        ),
    },
    "badhabit.biz@gmail.com": {
        "niche": "LA platinum-producer/artist (Atlantic Records / Billboard-charted)",
        "segment_original": "Platinum Producer + Artist",
        "industry": "Music / artist + production",
        "angle_to_take": (
            "badhabit (65.8k, US LA) — 7x Platinum producer-artist with 500M+ streams, Zara Larsson/Ghali/"
            "Diplo/David Guetta credits. Frame a branded badhabit fan app with exclusive tracks, remix drops, "
            "tipping, and a producer-fan community — owned retention for a platinum-tier artist."
        ),
    },
    "contact.beatsbyai@gmail.com": {
        "niche": "AI-generated beats with streaming-platform distribution",
        "segment_original": "AI Beats Creator",
        "industry": "Music / production (AI)",
        "angle_to_take": (
            "Beats By AI (56.6k, US) runs AI-generated beats across streaming platforms. Sparse bio. Frame "
            "a branded Beats-By-AI app with AI-beat catalog, type-beat subscription, and a producer community "
            "— owned retention beyond streaming-platform splits."
        ),
    },
    "saksham.jha029@gmail.com": {
        "niche": "IN-origin young Revealed Recordings producer (progressive/future bass)",
        "segment_original": "EDM Producer (IN)",
        "industry": "Music / production",
        "angle_to_take": (
            "Saksham (45.4k, IN, 20yo) — first IN producer on Revealed Recordings, Martin Garrix collab. "
            "Frame a branded Saksham app with tutorial breakdowns, original-track drops, and a producer "
            "community — owned retention for an emerging EDM producer beyond platform deals."
        ),
    },
    "markmywords.beats@gmail.com": {
        "niche": "Boutique 'timeless music' beatmaker (sparse bio)",
        "segment_original": "Boutique Beatmaker (SE)",
        "industry": "Music / production",
        "angle_to_take": (
            "Markmywords Beats (44.3k, SE) has very minimal bio ('I make timeless music'). Frame a branded "
            "Markmywords app with beat catalog, type-beat subscription, and a producer community — owned "
            "retention beyond email-only inquiries."
        ),
    },
    "studioninekolkata@gmail.com": {
        "niche": "Kolkata music studio offering production courses (Indian/Bollywood/western)",
        "segment_original": "Music Production Academy (IN)",
        "industry": "Music / education",
        "angle_to_take": (
            "Studio 9 Music Production (40.1k, IN Kolkata) runs studio9musicproduction.com + courses covering "
            "Indian/Bollywood/western music + FL Studio trainer certification. Frame a branded Studio-9 app "
            "with structured curriculum, template/loop library, and student community — replacing website + "
            "YouTube split."
        ),
    },
    "ambitiouskid403@gmail.com": {
        "niche": "ZA-market amapiano beat tutorials on Caustic 3 + FL Studio Mobile",
        "segment_original": "Amapiano Beatmaker (ZA)",
        "industry": "Music / production",
        "angle_to_take": (
            "Ambitious Kid (27k, ZA) produces amapiano with Caustic 3 + FL Studio Mobile tutorials. Frame a "
            "branded Ambitious-Kid app with amapiano tutorial archive, pack drops, and a ZA-producer community "
            "— owned retention for a regional amapiano niche."
        ),
    },
    "engagemusicproduction@gmail.com": {
        "niche": "FL Studio-focused tutorials + VST plugin reviews (IN)",
        "segment_original": "FL Studio Tutorial Creator (IN)",
        "industry": "Music / education",
        "angle_to_take": (
            "Engage Music Production (21k, IN) runs FL Studio tutorials + VST reviews. Frame a branded Engage "
            "app with tutorial library, VST review archive, and a production community — more polished than "
            "loose YouTube tutorials."
        ),
    },
    "uranus040220@gmail.com": {
        "niche": "KR-market beatmaking tutorials + commission music services",
        "segment_original": "Tutorial Creator + Commissions (KR)",
        "industry": "Music / production & education",
        "angle_to_take": (
            "URANUS20 Tutorials (18.2k, KR) offers tutorials + paid commissions with SoundCloud portfolio. "
            "Frame a branded URANUS app with tutorial archive, commission intake, and a KR-producer community "
            "— replacing email-only commission flow."
        ),
    },
    "tipshindiflstudio@gmail.com": {
        "niche": "Hindi FL Studio tutorials + mixing & mastering content",
        "segment_original": "FL Studio Tutorial (Hindi)",
        "industry": "Music / education",
        "angle_to_take": (
            "FL Studio Tips Hindi / Harsshu (17.6k, IN Hindi) covers FL Studio + mixing/mastering + sound "
            "design + VST reviews. Frame a branded Hindi FL Studio app with structured course, beat-making "
            "tracks, and a Hindi-producer community — owned retention beyond IG."
        ),
    },
    "rmakesbeats@gmail.com": {
        "niche": "Sample-based soul/R&B-fueled beatmaker (Ryan, CA)",
        "segment_original": "Sample-Based Beatmaker",
        "industry": "Music / production",
        "angle_to_take": (
            "Ryan Makes Beats (14.5k, CA) runs RyanMakesBeats.com — sample-based producer with 60s/70s soul "
            "record-collecting angle. Frame a branded Ryan app with sample-demonstration archive, record-"
            "collection catalog, and a sample-based-producer community — owned retention beyond website-only."
        ),
    },
    "beatpro.in@gmail.com": {
        "niche": "Mumbai-based music-production academy (online + offline)",
        "segment_original": "Music Production Academy (Mumbai)",
        "industry": "Music / education",
        "angle_to_take": (
            "BeatPro Music Production (12.7k, IN Mumbai Andheri West) runs beatpro.in + onlinebeatpro.com "
            "with online + offline courses covering Bollywood/EDM. Frame a branded BeatPro app consolidating "
            "the two websites + YouTube with cohort tracking, curriculum, and student community."
        ),
    },
    "makenobeats@gmail.com": {
        "niche": "UK-based beatmaker with extremely minimal bio",
        "segment_original": "Boutique Beatmaker (UK)",
        "industry": "Music / production",
        "angle_to_take": (
            "MAKE NO BEATS (12.6k, GB) has near-empty bio — IG + gmail only. Frame a branded MAKE-NO-BEATS "
            "app with beat catalog, type-beat subscription, and a UK-producer community — owned retention "
            "beyond IG-only."
        ),
    },
    "morflstricks@yahoo.com": {
        "niche": "FL Studio knowledge-sharing (solo, since 2000s)",
        "segment_original": "FL Studio Veteran Creator",
        "industry": "Music / education",
        "angle_to_take": (
            "FL Studio Tricks / Matthias Fischer (7.65k, ES) is a solo FL-Studio veteran (producing since 1995) "
            "with no affiliation to Image Line. Frame a branded FL-Studio-Tricks app with deep-dive tutorials, "
            "Q&A intake, and a veteran-producer community — owned retention beyond Yahoo email-only."
        ),
    },
    "beatsmake6@gmail.com": {
        "niche": "Standalone-studio-hardware beatmaker with gear reviews & theory",
        "segment_original": "Hardware Beatmaker + Theory Educator",
        "industry": "Music / production & education",
        "angle_to_take": (
            "I Make Beats (5.68k, US) covers hardware beatmaking + gear reviews + music theory / chord "
            "progressions. Frame a branded I-Make-Beats app with hardware tutorial archive, gear catalog, "
            "theory lessons, and a producer community — owned retention beyond YouTube-only."
        ),
    },
}
