"""Per-row angle_to_take for lead CSVs in my-data/ + data/nutrition_all.csv.

Each angle is crafted from the row's raw_context / detected_tech / source_url
(max 2 sentences). Role-based or sparse rows fall back to a 'cost saving'
framing. Output: <source>_enriched.csv next to each input.
"""

from __future__ import annotations

import csv
from pathlib import Path


ANGLES: dict[str, dict[str, str]] = {
    "productivity_all.csv": {
        "celinecatm@gmail.com": (
            "Lead with questions around study-buddy retention, cohort accountability, and turning passive \"study with me\" viewers into a paying study community. "
            "Position the app as a branded focus environment with live study rooms, timers, and a private cohort feed—more intimate than broadcasting on YouTube."
        ),
        "hello@missiondrive.com": (
            "Lead with questions around Notion-template ceilings on YearZero/Framer, mentorship bottlenecks, and scaling his Life-OS method into a product. "
            "Position the app as a branded Life-OS companion with progress tracking, habit modules, and a private mentor community—beyond what a static Notion template delivers."
        ),
        "bobbycyr@videotron.ca": (
            "Lead with questions around piano-student progression, daily-practice retention, and the limits of a Squarespace course page. "
            "Position the app as a branded practice companion with lesson tracking, practice reminders, and a student community—stronger than a static resource hub."
        ),
    },

    "fitness_all.csv": {
        "movewithagnes@gmail.com": (
            "Lead with questions around IISM-certified Pilates program delivery, paid-client retention, and turning her 467k audience into a branded member base. "
            "Position the app as a professional client companion with workout libraries, progress logs, and 1:1 check-ins—premium over generic fitness YouTube."
        ),
        "lottie@lottiemurphy.com": (
            "Lead with questions around lottiemurphypilates.com subscription LTV, Framer/Stripe checkout friction, and paid-Pilates member retention. "
            "Position the app as a branded studio companion with classes, progress tracking, and push reminders—tighter than browser-based Framer."
        ),
        "hello@lottiemurphy.com": (
            "Role-based contact for her Framer+Stripe studio site; frame the conversation as a branded member app upgrade. "
            "Cost-saving angle: consolidate Framer + Stripe + email funnel into one branded Pilates environment."
        ),
        "info@yoqi.com": (
            "Lead with questions around Qigong session scheduling, paid-retreat funnel, and retention on her Squarespace site. "
            "Position the app as a branded practice space with a guided-session player, event calendar, and community—beyond a static contact form."
        ),
        "yogaworldtx@gmail.com": (
            "Lead with questions around Patreon-tier retention, exclusive-class delivery, and converting free YouTube viewers into paid members. "
            "Position the app as a branded YOGATX class environment with a class library, challenges, and member-only streams—stronger than Patreon's generic feed."
        ),
        "pr@patreon.com": (
            "Role-based Patreon press contact for brand-asset requests; not the creator directly. "
            "If used, frame as PR/brand context; reserve the cost-saving + owned-app pitch for the creator's personal address."
        ),
        "collab@yoursalbany.com": (
            "Lead with questions around at-home-workout retention, DMV-area community, and the collab pipeline she already flags in bio. "
            "Position the app as a branded Bright & Salted Yoga companion with routines, progress logs, and a fan community—consolidating her IG/TikTok/Pinterest sprawl."
        ),
        "melania.antuchas@gmail.com": (
            "Lead with questions around FOREVER FIT BLUEPRINT sales and the habit gap after ebook purchase. "
            "Position the app as a branded blueprint-execution companion with daily workouts, progress tracking, and accountability—closing the loop between ebook and result."
        ),
        "preeti@yogbela.com": (
            "Lead with questions around tutorial-viewer retention, class-like experience at scale, and monetizing her 278k yoga audience beyond YouTube. "
            "Position the app as a branded YogBela studio with progressive class tracks and practice reminders—more structured than loose tutorials."
        ),
        "office@greenblau.com": (
            "Lead with questions around her shor.by link-in-bio consolidation, body-positive community retention, and Stripe subscription LTV across WordPress/Intercom. "
            "Position the app as a branded inclusive-yoga space unifying her scattered tech stack—cost saving and brand-coherent."
        ),
        "hello@joellefixson.com": (
            "Lead with questions around ConvertKit list-to-customer funnel, DE-market localization, and student retention after gift-card redemption. "
            "Position the app as a branded Yoga With Joelle companion with classes, reminders, and progress tracking—beyond email drips."
        ),
        "kirra@strongsistersunited.com": (
            "Lead with questions around 1:1 strength-coaching capacity, gym-confidence tracking, and the nutrition add-on she mentions. "
            "Position the app as a branded Strong Sisters companion with programs, check-ins, and community—premium over DM-based coaching."
        ),
        "holisticmovementpilates@gmail.com": (
            "Lead with questions around self-paced Pilates retention, IG DM inquiry volume, and converting followers to paying clients. "
            "Position the app as a branded at-your-own-pace Pilates space with classes, reminders, and journals—reducing DM coaching overhead."
        ),
        "bigsis.biz.global@gmail.com": (
            "Lead with questions around \"BigSis\" fan-identity, community branding, and converting IG followers to paid members. "
            "Position the app as a branded BigSis sisterhood with workouts, challenges, and a private community—owning the brand beyond YouTube."
        ),
        "pilatesplatform44@gmail.com": (
            "Lead with questions around her newly launched community structure and board-Pilates workout progression. "
            "Position the app as a branded board-Pilates space with workouts, community feed, and member check-ins—stronger than scattered Discord/WhatsApp."
        ),
        "hello@nancysidhu.com": (
            "Lead with questions around class consistency, student retention, and building brand equity beyond YouTube. "
            "Cost-saving angle: one branded Nancy-yoga app replacing email funnel + social channels for paying students."
        ),
        "rachel@rnaagency.com": (
            "She already has an app at rapilates.com (Shopify+Typeform). Lead with questions around current-app retention, Shopify subscription friction, and conversion of guided-workout viewers. "
            "Position a rebuild/upgrade as a cleaner branded Pilates environment—cost saving over patchwork Shopify/Typeform."
        ),
        "help@skool.com": (
            "Role-based Skool help address — not the creator. Her community runs on Skool+Stripe. "
            "Position a fully branded member app with workouts, Stripe checkout, and push reminders as an alternative—cost saving and brand control vs. Skool's shared infra."
        ),
        "myleedance@daum.net": (
            "Lead with questions around K-market home-fitness retention, IG/TikTok overlap, and phone-based business intake (031-5176-9929). "
            "Position the app as a branded MYLEEFit environment with dance workouts and fan community—localized and owned."
        ),
        "support@onlineyogateaching.com": (
            "Role-based support address for her Wix site. "
            "Position a branded yoga-teaching app as an upgrade with progression tracking, student portal, and community—cost saving and professional feel vs. Wix template."
        ),
        "morganchurch8050@gmail.com": (
            "Third-party agent (morganchurch) handles her paid promo — not direct creator. "
            "Frame as brand-partnership conversation through agent; cost-saving angle for Courteney's owned retention product if creator direct is reached later."
        ),
        "katy@sculptpilates.co.uk": (
            "Lead with questions around Sculpt Pilates virtual-studio retention, Wix-site limits, and class-scheduling overhead. "
            "Position the app as a branded studio companion with class library, booking, and progress tracking—cleaner than Wix subscription flows."
        ),
        "strengthteacher@gmail.com": (
            "Lead with questions around Stan Store product mix, Discord-community retention, and scaling strength coaching. "
            "Position the app as a branded all-in-one environment replacing Stan + Discord—cleaner and cost-saving over stacked SaaS."
        ),
        "homeworkout011@gmail.com": (
            "Lead with questions around home-workout content monetization in IN and audience beyond YouTube ads. "
            "Cost-saving angle: branded home-workout companion with routines and product recommendations as primary monetization lever."
        ),
        "asaptheworkout@gmail.com": (
            "Lead with questions around ASAP program licensing, coach-to-athlete video delivery, and the Ted Lambrinides brand reach. "
            "Position the app as a branded ASAP performance environment with program library and athlete progress tracking—a professional upgrade over video-email workflow."
        ),
        "erin@ecfitstrength.com": (
            "Lead with questions around Mailchimp list-to-customer funnel and paid-client retention. "
            "Position the app as a branded ECFIT companion with programs, progress tracking, and push reminders—more engaging than email broadcasts."
        ),
    },

    "mindful_all.csv": {
        "pr@patreon.com": (
            "Role-based Patreon press contact for brand-asset requests; not the creator. "
            "Frame as PR/media angle only; reserve the owned-app pitch for personal creator contact."
        ),
        "pam@thepaperoutpost.com": (
            "Lead with questions around junk-journal course sales, craft-community retention, and Stripe subscription LTV on thepaperoutpost.com. "
            "Position the app as a branded junk-journaling community with tutorials, daily prompts, and member swaps—stronger than site + Stripe combo."
        ),
        "hello@rosalieesilva.com": (
            "Lead with questions around Insight Timer distribution vs. owned-brand value, ConvertKit audience monetization, and retention on her Wix site. "
            "Position the app as a branded Hypnayoga practice space so the daily habit happens in her brand, not Insight Timer's."
        ),
        "carriewalker321@gmail.com": (
            "Lead with questions around her \"journaling army\" fan-group identity and conversion from YouTube to paying journalers. "
            "Position the app as a branded journaling-army HQ with prompts, challenges, and community—owning the brand beyond YouTube."
        ),
        "wellness@kristynroseyoga.ca": (
            "Lead with questions around retreat/training funnel, Patreon-to-paid-student conversion, and the sprawl across Patreon/Shopify/Wix/WordPress. "
            "Position the app as a consolidated branded Yoga Nidra environment—cost saving and brand simplification across four tools."
        ),
        "kristynroseyoga@gmail.com": (
            "Same creator as wellness@ contact. Reinforce the multi-platform sprawl angle (Patreon/Shopify/Wix/WordPress). "
            "Cost-saving angle: one branded Kristyn-Rose hub absorbing all four platforms into a single stack."
        ),
        "info@jackkornfield.com": (
            "Lead with questions around the \"All Access Pass\" member experience, WordPress-site retention, and podcast-to-app conversion. "
            "Position the app as a branded teaching environment with dharma talks, guided meditations, and gated member access—cleaner than WordPress gating."
        ),
        "junkjournaljoy@gmail.com": (
            "Lead with questions around IT-market craft community retention and turning YouTube/Linktree traffic into a paid circle. "
            "Position the app as a branded journaling community with tutorials and daily prompts—cost saving over Linktree-scattered flow."
        ),
        "hborison@sbcglobal.net": (
            "Individual Earth Care coordinator contact at Insight Meditation Center — non-profit sangha. "
            "Cost-saving angle: branded IMC app unifying 10+ program-coordinator inboxes and Zoom logistics across WordPress/Mailchimp."
        ),
        "earthcare.dharma@gmail.com": (
            "Earth Care group at Insight Meditation Center — non-profit sangha with WordPress + Mailchimp stack. "
            "Frame a branded sangha app consolidating Earth Care + other programs into one environment—cost saving on coordinator overhead."
        ),
        "imc.volunteerdirector@gmail.com": (
            "Volunteer director at Insight Meditation Center — non-profit with many program coordinators. "
            "Position a branded IMC app as the volunteer-coordination layer replacing scattered Zoom links + admin emails—cost saving for volunteer ops."
        ),
        "asianimc2020@gmail.com": (
            "Asian/Pacific Islander sangha coordinator at Insight Meditation Center. "
            "Position a branded IMC app with dedicated sub-sangha spaces (AAPI, BIPOC, queer, family)—cost saving over one-coordinator-per-inbox model."
        ),
        "imc.familyprogram@gmail.com": (
            "Family Program coordinator at Insight Meditation Center. "
            "Position a branded IMC app with family-program calendar, Zoom integration, and RSVP—cost saving over phone/email RSVP coordination."
        ),
        "eightfoldpath@insightmeditationcenter.org": (
            "Eightfold Path course contact at Insight Meditation Center — structured course with mentor and Zoom retreat. "
            "Position a branded IMC course app with student progression, mentor notes, and retreat check-in—cost saving over email-driven mentoring."
        ),
        "imcsg22@gmail.com": (
            "Sitting-group coordinator at Insight Meditation Center — pre-registration via email. "
            "Cost-saving angle: branded IMC app with self-serve sitting-group RSVP and Zoom-link issuance—removing manual coordinator work."
        ),
        "melodybaumgartner@gmail.com": (
            "Individual teacher contact at Insight Meditation Center series. "
            "Position a branded IMC app so series contact info + registration lives in the app, not in a per-teacher inbox—cost saving as primary."
        ),
        "imcqueersangha@gmail.com": (
            "Queer sangha coordinator at Insight Meditation Center — LGBTQIA2S+ community with email-list signup. "
            "Position a branded IMC app with dedicated queer-sangha space + email-list management—cost saving over manual list curation."
        ),
        "contact@insightmeditationcenter.org": (
            "Main role-based contact for Insight Meditation Center — non-profit Redwood City, CA. "
            "Cost-saving angle: one branded IMC app absorbs 10+ role inboxes, WordPress, and Mailchimp into a single sangha environment."
        ),
        "tealandtattered@gmail.com": (
            "Lead with questions around Calendly coaching capacity and Patreon-tier retention for paying journalers. "
            "Position the app as a branded journaling + 1:1 coaching hub with built-in booking and member content—cost saving over Calendly + Patreon stack."
        ),
        "meditationwithsk@gmail.com": (
            "Lead with questions around brand-sponsorship mix and scaling her IN audience to paid students. "
            "Position the app as a branded meditation companion with guided sessions and sponsor slots—diversifying revenue beyond one-off collabs."
        ),
        "wednesdaynightconversations@gmail.com": (
            "Lead with questions around converting \"Wednesday Night\" viewers into paying weekly attendees. "
            "Position the app as a branded weekly-practice environment with live-session replay, journal prompts, and community—cost saving over YouTube-only."
        ),
        "ktsjournal.contact@gmail.com": (
            "Lead with questions around journal-aesthetics monetization and converting casual viewers to a paid community. "
            "Cost-saving angle: branded journaling-inspiration app with prompts, member journals, and merch integration as primary monetization."
        ),
        "filler@godaddy.com": (
            "GoDaddy placeholder email — her midlmeditation.com site is partly scaffolded with filler auth. "
            "Position the app as a branded MIDL practice environment with course/community/auth built-in—cost saving over rebuilding from scratch on GoDaddy."
        ),
        "contact@laitattis.com.au": (
            "AU sleep-hypnosis niche with role-based site contact. "
            "Position the app as a branded sleep-hypnosis companion with nightly sessions and habit tracking—cost saving and niche-specific retention tool."
        ),
    },

    "finance_all.csv": {
        "alba.nicoleee@gmail.com": (
            "Lead with questions around PH-market personal-finance education and converting her 485k audience into paying subscribers. "
            "Position the app as a branded PH-first finance companion with budget tools, challenges, and community—cost saving and localized."
        ),
        "professorg.invest@gmail.com": (
            "Lead with questions around Private Financial Coaching capacity, thoughtleaders.io agency workflow, and sponsor-booking conversion. "
            "Position the app as a branded coaching + content hub with 1:1 booking, course library, and member community—cost saving over agency-led funnel."
        ),
        "investingsimplified@thoughtleaders.io": (
            "ThoughtLeaders agency address for Professor G; frame as brand-partnership channel. "
            "Creator-direct cost-saving app angle applies via his personal ProfessorG.invest@ address."
        ),
        "taekim@creatorsagency.co": (
            "Creators Agency address for Tae Kim — brand-partnership channel. "
            "Frame a branded Financial Tortoise app as a direct-to-audience product—cost saving over purely agency-led monetization."
        ),
        "tae@financialtortoise.com": (
            "Direct creator email for Financial Tortoise LLC. "
            "Position the app as a branded Financial Tortoise environment with budget tools, courses, and community—owned funnel over agency-mediated partnerships."
        ),
        "accordingtonicole2022@gmail.com": (
            "Lead with questions around the Sunday-10AM content rhythm and turning predictable viewers into paid subscribers. "
            "Position the app as a branded weekly-drop environment with member-only videos, budget challenges, and community—cost saving over YouTube-dependence."
        ),
        "tobynewbatt@icloud.com": (
            "Partnership-only posture — lead partnership conversation around a branded UK-finance app for his 188k audience. "
            "Position as a co-branded finance companion focused on UK investing—cost saving over brand-sponsored YouTube drops."
        ),
        "williamsaustin329@gmail.com": (
            "Lead with questions around Friday content cadence and audience-to-product funnel for \"intentional decisions\" framing. "
            "Position the app as a branded finance-decisions companion with budget/goal tools—cost saving over ad-dependent revenue."
        ),
        "debtfreemillennials@creatorsagency.co": (
            "Creators Agency address for Debt Free Millennials. "
            "Frame partnership around a branded DFM debt-payoff app — budget tracking, payoff milestones, community — complementary to agency-led brand deals."
        ),
        "askafundmanager@gmail.com": (
            "Lead with questions around buyside-expertise monetization and Q&A engagement (\"Email Questions to...\"). "
            "Position the app as a branded Q&A + analysis environment with paid advisory tier, research feed, and member forum—cost saving over scattered email Q&A."
        ),
        "financewithwali@gmail.com": (
            "Lead with questions around AE/MENA finance-education audience and Patreon-tier retention. "
            "Position the app as a branded Wali Khan finance companion with courses, budget tools, and member community—cost saving via Patreon migration."
        ),
        "wali@walikhan.co": (
            "Direct WordPress + Patreon sprawl. "
            "Cost-saving angle: consolidated branded Wali Khan environment absorbing Patreon + WordPress + social into one stack."
        ),
        "pr@patreon.com": (
            "Role-based Patreon press contact (appears here via Wali Khan's Patreon). "
            "Frame as PR/media angle only; reserve owned-app pitch for creator-direct addresses."
        ),
        "gobudgetgirl@gmail.com": (
            "Lead with questions around Budget Club retention and conversion from YouTube viewers to paid club members. "
            "Position the app as a branded Budget Girl club with budget tools, challenges, and community—cost saving over bit.ly redirect + external hosting."
        ),
        "jc@thefrugalrich.com": (
            "Lead with questions around partnership-driven revenue and paid-membership potential in the frugal-rich audience. "
            "Position the app as a branded personal-finance + self-development companion with budget tools and habit tracker—cost saving over YouTube-only."
        ),
        "miamcgrath@sixteenth.com": (
            "Sixteenth agency address for Mia McGrath. "
            "Frame a branded \"Frugal Chic\" app for her young-professional wealth-builder audience—20s budget tools + investment challenges—complementary to agency brand deals."
        ),
        "pipslittlemomma@gmail.com": (
            "Lead with questions around BuyMeACoffee-based support model and homestead-community retention. "
            "Position the app as a branded frugal-homestead environment with wealth tracker, homesteading challenges, and community—cost saving over coffee-jar tipping."
        ),
        "practicalpf@gmail.com": (
            "Lead with questions around collaboration-driven content and audience-to-product path. "
            "Position the app as a branded practical-finance companion—cost saving over ad-only model."
        ),
        "info@principlespersonalfinance.co.uk": (
            "UK finance educator, role-based info@; disclaimers around financial-planning advice. "
            "Position the app as a UK-compliant financial-education environment with budget tools, modules, and disclaimer-friendly advisory tier—cost saving as primary."
        ),
        "corrections@businessinsider.com": (
            "Business Insider corporate corrections address — not direct creator. "
            "Pursue as media-partnership conversation; cost-saving creator-app angle doesn't apply here."
        ),
        "bizdev@businessinsider.com": (
            "Business Insider business-development address. "
            "Frame as ad-inventory / brand-partnership conversation; creator-app angle doesn't fit."
        ),
        "inbounds@businessinsider.com": (
            "Business Insider generic inbounds address. "
            "Default to brand-partnership context; creator-app cost-saving angle not a fit."
        ),
        "fixes@businessinsider.com": (
            "Business Insider tech/bugs address — inappropriate for outreach. "
            "Skip or escalate to BI biz-dev channel only."
        ),
        "personal.finance.opinions@gmail.com": (
            "Lead with questions around PK-market finance basics audience and sponsorship/collab mix. "
            "Position the app as a branded PK-first budget/investing app—cost saving via localized product."
        ),
        "chinweotutoezekiel@gmail.com": (
            "Lead with questions around NG audience pain (saving/budgeting/investing) and viewer-to-student conversion. "
            "Position the app as a branded NG-first finance companion with local budgeting habits—cost saving via localization."
        ),
        "lispmanfinance@gmail.com": (
            "Lead with questions around his comedy-finance hybrid retention and audience monetization. "
            "Position the app as a branded Lispman finance-tips environment with short-form coaching and budget tools—cost saving over pure ad revenue."
        ),
        "collabwithchandu@gmail.com": (
            "Lead with questions around collab-driven content and building IN audience loyalty. "
            "Position the app as a branded Chandu finance companion—cost saving over collab-only monetization."
        ),
        "sreuben121@gmail.com": (
            "Lead with questions around NG finance-education audience and collab vs. owned-product strategy. "
            "Position the app as a branded MoneyLine companion with NG-specific budgeting—cost saving via localization."
        ),
        "lovinglifeonless@yahoo.com": (
            "Lead with questions around Amazon-affiliate revenue ceiling and building a direct-product stream. "
            "Position the app as a branded frugal-living companion with budget tools and content library—cost saving over affiliate-only."
        ),
        "frederickmnl@gmail.com": (
            "Lead with questions around Calendly meeting conversion and retirement-planning client pipeline. "
            "Position the app as a branded financial-planning client portal with booking, client docs, and follow-through—cost saving over Calendly + YouTube scatter."
        ),
        "pinoypersonalfinance.business@gmail.com": (
            "Lead with questions around PH-diaspora audience in CA and business-inquiry-only posture. "
            "Position the app as a branded Pinoy-PH finance companion with Tagalog/Taglish content—cost saving via localization."
        ),
        "ellendrottar50@gmail.com": (
            "Lead with questions around abundance-mindset content + her art/jewelry side-brand. "
            "Position the app as a branded abundant-life companion integrating content, art store, and financial habits—cost saving across multi-brand."
        ),
        "sgarciacreations@gmail.com": (
            "Lead with questions around OT-day-job audience overlap and her student-loan payoff journey. "
            "Position the app as a branded debt-payoff diary with budget tools and milestones—cost saving over YouTube-only."
        ),
        "info@paydowndebtsolutions.com": (
            "Role-based coaching-business email. Lead with questions around 1-on-1 capacity and \"Pay Down method\" scale. "
            "Position the app as a branded Pay-Down method app with guided program, tracker, and community—cost saving over 1-on-1 calls."
        ),
        "mpantique@yahoo.com": (
            "Lead with questions around mature-audience retention and content cadence. "
            "Cost-saving angle: branded thrifty-living companion with tips, challenges, and community as primary."
        ),
        "yvonnehudduma@gmail.com": (
            "Lead with questions around withkoji link-in-bio monetization and money-saving audience retention. "
            "Position the app as a branded saving-tips environment consolidating her Koji links—cost saving and brand control."
        ),
        "livingonalowincome@outlook.com": (
            "Lead with questions around BuyMeACoffee tip-jar support and low-income UK budgeting community. "
            "Position the app as a branded low-income-UK companion with budget tools and meal-plan content—cost saving over tip-jar dependence."
        ),
    },

    "nutrition_all.csv": {
        "kiransagar@shredfix.com": (
            "Lead with questions around his \"Esthetic Transformation\" worldwide online-coaching program and client-gallery funnel (Wix site). "
            "Position the app as a branded ShredFix client companion with transformation logs, meal plans, and 1:1 check-ins—cost saving over Wix + WhatsApp."
        ),
        "shredfixteam@gmail.com": (
            "Team email for appointment booking (+91-9019169276 phone intake). "
            "Frame a branded client-intake + appointment portal replacing phone-and-Wix workflow—cost saving on admin overhead."
        ),
        "rosemarycp24@gmail.com": (
            "Lead with questions around recipe-content monetization and fitness-advice cross-sell. "
            "Position the app as a branded Rose-nutrition companion with recipes, workouts, and styling tips—cost saving over YouTube-only."
        ),
        "orders@nationalnutrition.ca": (
            "Retailer orders address for National Nutrition (CA health-products store). "
            "Frame as B2B2C branded shopping-companion app for retail customers—cost saving on scattered role-inbox coordination."
        ),
        "cnpa@nationalnutrition.ca": (
            "National Nutrition CNPA (Certified Natural Health Products Advisor) channel. "
            "Position a branded shopping + advisor-consult app unifying multiple role inboxes—cost saving as primary."
        ),
        "francais@nationalnutrition.ca": (
            "National Nutrition FR-language customer inbox. "
            "Frame a branded multilingual shopping-companion app with FR/EN toggle—cost saving on per-language inbox fragmentation."
        ),
        "hr@nationalnutrition.ca": (
            "HR inbox for National Nutrition — internal, not a customer-pitch target. "
            "Cost-saving angle only if pursuing a corporate-team app; otherwise skip."
        ),
        "darren@nationalnutrition.ca": (
            "Named personal contact inside National Nutrition. "
            "Frame as warm internal-champion conversation around a branded customer-shopping app—cost saving over Mailchimp + scattered inboxes."
        ),
        "neenarseth@gmail.com": (
            "Lead with questions around her paid-diet-plan order volume and WhatsApp-based client management (+91 9811762690). "
            "Position the app as a branded diet-plan delivery + WhatsApp-replacement with meal plans, reminders, and progress—cost saving over WhatsApp logistics."
        ),
        "career@finesseinstitute.in": (
            "Institute with multi-domain career/enrollment inboxes (IN). "
            "Frame a branded course-delivery + student-community app replacing scattered enrollment inboxes—cost saving on admin overhead."
        ),
        "career.finesseinstitute@gmail.com": (
            "Alternate Finesse Institute enrollment inbox. "
            "Same angle: branded course + student-community app consolidating both inboxes—cost saving as primary."
        ),
        "office@slaviclabs.com": (
            "Slavic Labs brand with Klaviyo/Shopify/WordPress sprawl (PL dietcoach). "
            "Position the app as a consolidated branded Sroka-Dietcoach companion absorbing email/shop/content—cost saving across three-tool stack."
        ),
        "seb@influencernexus.com": (
            "InfluencerNexus agency address for Danielle the Dietitian. "
            "Frame partnership around a branded online course + group nutrition program app—complementary to agency brand deals."
        ),
        "robert@dietfreelife.com": (
            "Diet Free Life author with Calendly/Kajabi/Linktree/WordPress stack. "
            "Position the app as a branded Diet-Free-Life environment consolidating booking/course/link-in-bio/site—cost saving across four tools."
        ),
        "info@dietfreelife.com": (
            "Role-based Diet Free Life contact — same four-tool stack (Calendly/Kajabi/Linktree/WordPress). "
            "Cost-saving angle: single branded app absorbing all four into one stack."
        ),
        "hello@stephanielong.ca": (
            "Nutrition-business coach with ConvertKit/Kajabi/Squarespace stack (CA). "
            "Position the app as a branded nutrition-coach companion replacing the three-tool sprawl—cost saving and brand-coherent."
        ),
    },
}


FILES = [
    ("/home/test1/ABC/Marketing/youtube-crawling/my-data/productivity_all.csv", "productivity_all.csv"),
    ("/home/test1/ABC/Marketing/youtube-crawling/my-data/fitness_all.csv", "fitness_all.csv"),
    ("/home/test1/ABC/Marketing/youtube-crawling/my-data/mindful_all.csv", "mindful_all.csv"),
    ("/home/test1/ABC/Marketing/youtube-crawling/my-data/finance_all.csv", "finance_all.csv"),
    ("/home/test1/ABC/Marketing/youtube-crawling/data/nutrition_all.csv", "nutrition_all.csv"),
]


def main() -> None:
    total_rows = 0
    missing_per_file: dict[str, list[str]] = {}

    for src_path, key in FILES:
        src = Path(src_path)
        dst = src.with_name(src.stem + "_enriched.csv")
        angles = ANGLES.get(key, {})
        missing: list[str] = []

        with src.open(encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            fieldnames = list(reader.fieldnames or []) + ["angle_to_take"]
            rows = list(reader)

        for row in rows:
            email = (row.get("email") or "").strip().lower()
            angle = angles.get(email) or angles.get(row.get("email") or "")
            if not angle:
                angle = "cost saving"
                missing.append(email)
            row["angle_to_take"] = angle

        with dst.open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

        total_rows += len(rows)
        missing_per_file[key] = missing
        print(f"{key}: wrote {len(rows)} rows → {dst.name}")

    print(f"\nTotal: {total_rows} rows")
    for k, missing in missing_per_file.items():
        if missing:
            print(f"  {k} missing angle (→ fallback): {missing}")


if __name__ == "__main__":
    main()
