"""Per-row LLM classification for data/2026-04-24/career.csv."""

MAPPING = {
    "ashokkumar4love@gmail.com": {
        "niche": "Overseas education & career guidance",
        "segment_original": "Study-Abroad & Career Guidance",
        "industry": "Careers / education / international mobility",
        "angle_to_take": (
            "Ask about how he handles student cohorts, document workflows for "
            "visa and overseas applications, and engagement with the 30K+ "
            "student community. Position the app as a branded overseas-career "
            "environment—document checklists, cohort Q&A, push reminders for "
            "application deadlines, and private mentorship sessions—replacing "
            "WhatsApp and email chaos with a premium platform worthy of an "
            "'India Best International Career Planner' credential."
        ),
    },
    "coachingforjobs@gmail.com": {
        "niche": "Stenography & shorthand career coaching",
        "segment_original": "Specialized Skills Career Coaching (Stenography)",
        "industry": "Careers / education / specialized skills",
        "angle_to_take": (
            "Start with questions about how stenography students practice "
            "between videos, how exam preparation stays structured, and how "
            "the Instagram plus Gmail touchpoints consolidate. Position the "
            "app as a branded skills-coaching environment with structured "
            "practice modules, progress tracking, and push reminders—premium "
            "positioning for a specialized career path that deserves more "
            "than YouTube plus DMs."
        ),
    },
    "therichardwalls@gmail.com": {
        "niche": "Career development & online learning community",
        "segment_original": "Career Development & Online Learning Coaching",
        "industry": "Careers / professional development",
        "angle_to_take": (
            "Lead with discovery around the Level Up Careers community on X "
            "and how followers actually progress from free YouTube into paid "
            "programs. Frame the app as a branded community hub—programs, "
            "live Q&A, push-based accountability—replacing scattered links "
            "across bit.ly, Twitter group, and LinkedIn with a premium "
            "retention surface he owns entirely."
        ),
    },
    "careerguidanceforeveryone@gmail.com": {
        "niche": "Business Analyst training & interview prep",
        "segment_original": "Business Analyst Interview & Training Coaching",
        "industry": "Careers / tech training",
        "angle_to_take": (
            "Ask about how resume consultations, BA tutorials, and interview "
            "prep flow together across WhatsApp and email. Position the app "
            "as a branded BA-training environment—structured tutorials by "
            "domain (healthcare, agile), interview question banks, resume "
            "review submissions, push reminders—replacing WhatsApp plus "
            "Gmail with a premium experience positioned for an international "
            "BA audience."
        ),
    },
    "assistant@enoeka.com": {
        "niche": "Business analysis career coaching",
        "segment_original": "Business Analysis & Income Acceleration Coaching",
        "industry": "Careers / tech training",
        "angle_to_take": (
            "Start with discovery around how her free class at "
            "BusinessAnalysisSchool converts into paid coaching, and how she "
            "delivers income-acceleration content at scale. Frame the app as "
            "a branded BA-career environment—free-training funnel, cohort "
            "programs, community Q&A, push-based accountability—more polished "
            "than LinkedIn DMs and retention-focused for a coaching business "
            "targeting $100k+ career moves."
        ),
    },
    "gsprimementorship@gmail.com": {
        "niche": "Chartered Accountant interview & mentorship",
        "segment_original": "Chartered Accountant Career Mentorship",
        "industry": "Careers / professional services / finance",
        "angle_to_take": (
            "Ask about how he manages the 30K+ alumni, Topmate bookings, and "
            "WhatsApp group interactions. Position the app as a branded CA-"
            "mentorship environment—1:1 session scheduling, alumni community, "
            "resume and cover-letter workflows, push reminders for interview "
            "deadlines—replacing Topmate plus WhatsApp with a premium "
            "platform that matches his Big-4 pedigree."
        ),
    },
    "newgradnursinginterviewcoach@gmail.com": {
        "niche": "New-grad nursing interview coaching",
        "segment_original": "Specialized Nursing Interview Coaching",
        "industry": "Careers / healthcare training",
        "angle_to_take": (
            "Lead with discovery around how mock-interview clients go from "
            "video to 1-on-1 coaching, and how the Clinical Memory Journal "
            "sells off her Wix page. Frame the app as a branded nursing-"
            "career environment—mock-interview scheduling, study journals, "
            "question banks, push reminders—replacing Wix plus email with a "
            "premium platform that matches her top-20-hospital credibility."
        ),
    },
    "gpk-usersupport@google.com": {
        "niche": "Hindi-language competitive exam career coaching",
        "segment_original": "Competitive Exam Career Coaching (Hindi)",
        "industry": "Careers / education / competitive exams",
        "angle_to_take": (
            "Start with questions about how 30K+ students track exam prep, "
            "course purchases via the current Career Coaching app, and the "
            "Discord community. Position the app as a branded exam-prep "
            "environment—course library, progress tracking per exam, push "
            "reminders for SSC/Bank/Railway dates, private community—premium "
            "positioning that stops students defaulting to free YouTube for "
            "serious competitive-exam prep."
        ),
    },
    "erika@pocketboard.co": {
        "niche": "Tech career & interview coaching",
        "segment_original": "Tech Industry Interview & Negotiation Coaching",
        "industry": "Careers / tech / recruiting",
        "angle_to_take": (
            "Lead with discovery around the patchwork she juggles—Calendly, "
            "Gumroad, Stripe, Substack—and how the First Round Ready course "
            "delivers across them. Frame the app as a branded tech-career "
            "environment—course delivery, 1:1 bookings, offer-negotiation "
            "resources, push-based accountability—more polished and retention-"
            "focused than four disconnected tools, and a premium surface "
            "worthy of an ex-Google hiring manager."
        ),
    },
    "sara@camilocareers.com": {
        "niche": "Certified resume writer & career coach",
        "segment_original": "Resume Writing & Recruiter-Side Career Coaching",
        "industry": "Careers / recruiting / professional development",
        "angle_to_take": (
            "Ask about how clients flow between Kajabi courses, the "
            "Squarespace site, and 1:1 coaching, and how resume reviews stay "
            "organized at scale. Position the app as a branded career-"
            "coaching environment—resume intake workflow, course modules, "
            "interview prep, push-based check-ins—replacing Kajabi plus "
            "Squarespace with a premium client experience from a 15-year "
            "ex-recruiter."
        ),
    },
    "ps9600955@gmail.com": {
        "niche": "Safety Officer & overseas career guidance",
        "segment_original": "Fire & Safety Career & Overseas Job Coaching",
        "industry": "Careers / specialized vocational",
        "angle_to_take": (
            "Start with questions about how he warns students away from "
            "fraud agents, delivers experience-based guidance, and stays "
            "ahead of fake-job scams. Frame the app as a branded safety-"
            "career environment—verified job updates, document checklists, "
            "interview prep, push alerts for visa/HSE deadlines—premium "
            "positioning for a trusted advisor who competes with fraud agents "
            "on trust, not reach."
        ),
    },
    "coachsammanika@gmail.com": {
        "niche": "Legal career mentorship for law students",
        "segment_original": "Legal Career & Mentorship Coaching",
        "industry": "Careers / legal / education",
        "angle_to_take": (
            "Lead with discovery around how NLU vs non-NLU students engage "
            "with YLCC, how the WhatsApp job/internship groups scale, and "
            "how she delivers 'unconventional legal career' content. Position "
            "the app as a branded legal-career environment—mentorship tiers, "
            "job/internship feed, resources library, push alerts—replacing "
            "WordPress plus WhatsApp with a premium members-only platform."
        ),
    },
    "navytransitioncoach@gmail.com": {
        "niche": "Military-to-civilian transition coaching",
        "segment_original": "Military Transition Career Coaching",
        "industry": "Careers / veterans / life transitions",
        "angle_to_take": (
            "Start with discovery around how service members find her between "
            "deployments, how the book plus mailing list plus WordPress plus "
            "Jotform flow actually connects, and what retention looks like "
            "post-transition. Frame the app as a branded military-transition "
            "environment—structured content, book integration, transition "
            "checklists, push reminders, private Q&A—premium positioning for "
            "service members who deserve more than a Jotform-plus-WordPress "
            "experience."
        ),
    },
    "dherajsahkgec@gmail.com": {
        "niche": "Entry-level career & mindset coaching",
        "segment_original": "Entry-Level Career & Mindset Coaching",
        "industry": "Careers / professional development",
        "angle_to_take": (
            "Ask about how students engage beyond YouTube, how job updates "
            "reach them reliably, and how 1-on-1 inquiries are managed "
            "today. Position the app as a branded career-mindset environment"
            "—resume templates, interview prep, job-update feeds, productivity "
            "frameworks, push-based accountability—replacing inbox chaos with "
            "a premium platform that matches the MNC-engineer credibility he "
            "brings."
        ),
    },
    "charlie@interviewcoach.me": {
        "niche": "Behavioural interview coaching (STAR method)",
        "segment_original": "Behavioural Interview Coaching",
        "industry": "Careers / interview preparation",
        "angle_to_take": (
            "Lead with questions around how candidates move from YouTube "
            "into 1:1 discovery calls, and how interview drilling stays "
            "structured between sessions. Frame the app as a branded "
            "interview-prep environment—STAR frameworks, behavioural question "
            "bank, mock-interview workflows, push-based practice reminders—"
            "more polished than a Calendly-only funnel and retention-focused "
            "for a program that lives on structured repetition."
        ),
    },
    "collabs@tarakermiet.com": {
        "niche": "Burnout + career coaching with 5Cs framework",
        "segment_original": "Burnout & Career Integration Coaching",
        "industry": "Wellness / careers / leadership development",
        "angle_to_take": (
            "Lead with discovery around the Beacons plus Stan Store plus "
            "Substack patchwork and how clients slow down to do reflective "
            "career work between sessions. Position the app as a branded "
            "burnout-and-career environment—5Cs frameworks, podcast, guided "
            "reflections, private Q&A, push-based check-ins—more premium "
            "than three disconnected tools and built for the thoughtful, "
            "slower pace her work requires."
        ),
    },
    "prakash_diamond1@yahoo.co.in": {
        "niche": "General life & career guidance",
        "segment_original": "General Career & Life Coaching",
        "industry": "Careers / general coaching",
        "angle_to_take": (
            "Start with questions about how he currently connects with "
            "followers beyond WhatsApp and Instagram DMs, and where "
            "structured coaching actually happens. Frame the app as a branded "
            "career-coaching environment—program delivery, 1:1 scheduling, "
            "structured content, push reminders—premium positioning that "
            "elevates his practice beyond a WhatsApp-number-in-the-bio "
            "presence."
        ),
    },
    "ernestcareercoach@gmail.com": {
        "niche": "Interview coaching for grads and professionals",
        "segment_original": "Interview Skills Coaching",
        "industry": "Careers / interview preparation",
        "angle_to_take": (
            "Ask how candidates move from YouTube to Stan Store to 1:1 "
            "coaching, and what retention looks like after the dream-job "
            "offer lands. Position the app as a branded interview-coach "
            "environment—structured lessons, question banks, 1:1 scheduling, "
            "push-based practice—more polished than Stan Store plus Gmail "
            "and retention-focused for an audience that graduates out fast "
            "without repeat buyers."
        ),
    },
    "educationindiakota@gmail.com": {
        "niche": "MBA admission & CAT preparation",
        "segment_original": "MBA Admission & CAT Preparation Coaching",
        "industry": "Careers / education / MBA",
        "angle_to_take": (
            "Start with discovery around how CAT aspirants engage between "
            "uploads, how he delivers insights from 400+ B-school visits, "
            "and what happens to admissions clients post-offer. Frame the "
            "app as a branded MBA-admissions environment—CAT blueprint, "
            "college comparison tool, interview prep, push reminders for "
            "deadlines—premium positioning for a channel branding itself "
            "'India's #1 MBA Admission Guidance.'"
        ),
    },
}
