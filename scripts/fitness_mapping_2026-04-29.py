"""Per-row mapping for data/2026-04-29/fitness_enriched.csv (16 rows).

Combined-dict format (same as legacy_mapping / mindful_mapping):
  email → {category, niche, segment_original, industry, angle_to_take}

Surfaced via the 6-keyword × 2-page fitness sub-niche sweep on 2026-04-29
(quota ~1,440, 39 stale-drops by 6-month freshness filter). Targets mobility
/ kettlebell / calisthenics / powerlifting / women's strength / recovery.
Category routing: fitness 15 / drop 1.
"""

MAPPING: dict[str, dict[str, str]] = {

    # gushcloud is a talent-agency relay address but Caroline Jordan is a real
    # fitness creator with her own carolinejordanfitness.com — agency-managed
    # is still a valid creator outreach.
    "Carolinejordan@gushcloud.com": {
        "category": "fitness",
        "niche": "US certified Health & Fitness Coach — movement-as-medicine framing, lifestyle change + healthy mindset (Caroline Jordan, 781K, agency-managed via Gushcloud)",
        "segment_original": "US Fitness + Mindset Lifestyle Coach (agency-managed)",
        "industry": "Fitness Creator (B2C, talent-agency relay)",
        "angle_to_take": "Caroline Jordan (781K, US) — certified health + fitness coach with a 'movement as medicine' positioning, agency-managed via Gushcloud. Frame a branded Caroline Jordan Fitness app with workout library by intent (energy / stress / recovery) + lifestyle-program cohort + brand-collab inquiry surface — replaces the FB / IG split + agency-only intake with a creator-controlled member tier.",
    },

    "dejan.stipic@365fit.ae": {
        "category": "fitness",
        "niche": "DE-based pro calisthenics athlete + coach — calisthenics / weighted calisthenics / bodyweight training, 25-yr training experience (Stipke, 265K)",
        "segment_original": "DE Pro Calisthenics Athlete + Coach",
        "industry": "Calisthenics Coach (B2C + program)",
        "angle_to_take": "Stipke / Dejan Stipic (265K, DE) — pro calisthenics athlete with 25 yrs training + championship background. Frame a branded Stipke app with progression ladder (street workout level 1→8) + form-check submit/review + weighted-calisthenics program — fits the structured progression his content is organized around.",
    },

    "info@integrityattitudehustle.com": {
        "category": "fitness",
        "niche": "US (Boston) functional-training coach — IAH Training brand, online coaching + functional training app + branded shop (Adriell Mayes, 215K)",
        "segment_original": "US Boston Functional / Online Training Coach",
        "industry": "Online PT + Branded Apparel (B2C)",
        "angle_to_take": "Adriell Mayes / IAH Training (215K, US) — Boston functional-training coach running online coaching + functional training app + apparel shop. Frame a branded IAH app with online coaching client surface + program library + apparel-store tab — collapses the integrityattitudehustle.com + LMNT-affiliate + Vivobarefoot-affiliate stack into a creator-tier app.",
    },

    # Foundation Training already runs FTstreaming.com — a 1000+ video subscription
    # platform. Method is fully productized. mediarelations@ implies B2B media inbox.
    "mediarelations@foundationtraining.com": {
        "category": "drop",
        "niche": "US Foundation Training method (Dr. Eric Goodman) — already runs FTstreaming.com subscription with 1000+ guided videos (Foundation Training, 177K)",
        "segment_original": "US Method-Brand with Own Subscription Platform",
        "industry": "n/a (drop — already has own platform + B2B media inbox)",
        "angle_to_take": "Foundation Training (177K, US) is a method brand that already runs FTstreaming.com (1000+ guided videos, weekly drops). The harvested email is also a media-relations B2B inbox, not a coach. Drop on both grounds.",
    },

    "contact@posturetonic.com": {
        "category": "fitness",
        "niche": "AU Clinical Pilates (APPI) + Remedial Massage diploma — Pilates / sculpt workouts focused on posture + elegant strength (Posture Tonic by Jacinta Brown, 168K)",
        "segment_original": "AU Pilates + Posture-Sculpt Coach",
        "industry": "Pilates Coach (B2C + brand collabs)",
        "angle_to_take": "Posture Tonic (168K, AU) — APPI Clinical Pilates instructor with weekly posture / sculpt workouts + Sunday schedule drops. Frame a branded Posture Tonic app with weekly-schedule calendar + workout library by body part + member-tier replacement of the YouTube channel-membership + Melbourne-office sponsorship intake.",
    },

    "info@danielptfitness.com": {
        "category": "fitness",
        "niche": "DE personal trainer + coach (15+ yrs) — kettlebell + dumbbell + bodyweight + resistance bands, 3 new HomeGym videos / week on subscription (DanielPT Fitness, 164K)",
        "segment_original": "DE Online PT + HomeGym Subscription",
        "industry": "Online PT + Subscription (B2C)",
        "angle_to_take": "DanielPT Fitness (164K, DE) — already runs danielptfitness.com/homegym subscription with 3 new coached workouts / week. Frame a branded DanielPT app to upgrade the WordPress-style subscription into a native experience with workout-streak + program calendar + 1-on-1 coaching booking — keeps the existing /homegym revenue model with a better delivery surface.",
    },

    "ulusoychannel@gmail.com": {
        "category": "fitness",
        "niche": "TR personal trainer + coach — sercanulusoy.com program with refund / freeze policies (Sercan Ulusoy, 112K)",
        "segment_original": "TR Online PT (Turkish-language)",
        "industry": "Online PT (B2C, Turkish-language)",
        "angle_to_take": "Sercan Ulusoy (112K, TR) — Turkish-language online PT with structured refund / freeze policies. Frame a branded app with Turkish-language workout player + free-evaluation intake + refund-/freeze-self-service surface — replaces the .com page that currently handles intake + policy via long-form text. (Note: TR-base; English outreach copy with Turkish-language localization plan.)",
    },

    "flexformbyshan@gmail.com": {
        "category": "fitness",
        "niche": "AU pro aerialist + flexibility / handstand coach — weekly online flex training (hip / hamstrings / back / shoulders), 10+ yrs teaching (FLEXFORM by Shan, 41.7K)",
        "segment_original": "AU Flexibility / Handstand Coach (online classes)",
        "industry": "Flexibility / Handstand Coach (B2C + classes)",
        "angle_to_take": "FLEXFORM by Shan (41.7K) — Australian pro aerialist + flexibility / handstand coach with weekly online classes. Frame a branded FLEXFORM app with weekly-class booking + flexibility progression by body part (hip / hamstrings / shoulders) + handstand skill tree + member tier — replaces the IG-only intake with a structured class surface.",
    },

    "stayfit@arogyaphysio.com": {
        "category": "fitness",
        "niche": "IN (Assam) physiotherapist (BPT, MPT Neurology) — pain management / physio exercises / lifestyle change for general public (Arogya Physiotherapy & Rehab Centre, 30.9K)",
        "segment_original": "IN Physiotherapy + Pain-Management Channel",
        "industry": "Physio / Rehab Coach (B2C + clinic)",
        "angle_to_take": "Arogya Physiotherapy (30.9K, IN) — clinic-based physiotherapist (Dr. Aruna, BPT, MPT Neurology) sharing pain-management + physio exercises. Frame a branded Arogya Physio app with pain-protocol library by body part + telehealth 1-on-1 booking + lifestyle-tracker — bridges the physical-clinic visit with a structured at-home protocol surface.",
    },

    "conceptnxc@gmail.com": {
        "category": "fitness",
        "niche": "FR HIIT NXC method since 2010 — street workout / calisthenics / circuit / bodyweight + formation + coaching + station design (NXC Workout, 9.19K)",
        "segment_original": "FR HIIT + Calisthenics Method (NXC, multi-coach)",
        "industry": "HIIT / Calisthenics Method (B2C + formation)",
        "angle_to_take": "NXC Workout (9.19K, FR) — Filip + Eric run a 14-yr-old HIIT / calisthenics method (NXC) covering training + formation + station design. Frame a branded NXC app with method-cert progression (formation modules) + workout-library by surface (street / circuit / bodyweight) + station-design consult inquiry — gives the multi-pillar method a single member surface vs the current SAS-style B2B sales motion.",
    },

    "samoelworkout@gmail.com": {
        "category": "fitness",
        "niche": "US personal trainer / athlete / content creator — gym + calisthenics + street workout, weighted-calisthenics performance focus (Samoel Workout, 3.14K)",
        "segment_original": "US PT + Calisthenics Performance Creator",
        "industry": "Online PT + Calisthenics (B2C, early-stage)",
        "angle_to_take": "Samoel Workout (3.14K, US) — early-stage PT + calisthenics performance creator. Frame a branded Samoel app with weighted-calisthenics progression ladder + advanced-bodyweight skill tree + 1-on-1 coaching intake — replaces the email-only contact with a structured creator surface as the channel grows.",
    },

    "magdalenakognetx@gmail.com": {
        "category": "fitness",
        "niche": "CA CanFitPro PT + former bikini competitor (yoga TTC in progress) — strength + mobility + calisthenics follow-along workouts, full-body functional movement (Magdalena Kognetx, 2.21K)",
        "segment_original": "CA Strength + Mobility + Calisthenics Coach",
        "industry": "Online PT (B2C + community)",
        "angle_to_take": "Magdalena Kognetx (2.21K, CA) — CanFitPro PT running follow-along strength + mobility + calisthenics workouts with an accountability-community framing. Frame a branded MagsMoves app with weekly schedule + accountability-streak + cohort program + brand-collab tab — replaces the IG / business-email-only intake she runs today.",
    },

    "Jmont_fit@yahoo.com": {
        "category": "fitness",
        "niche": "US bodybuilding / physique coach — 4 / 8 / 12-week programs + individualized plans + biweekly FaceTime check-ins, mens physique + classic physique competitor (Joe Monteverdi, 2.14K)",
        "segment_original": "US Bodybuilding / Physique Coach (program-based)",
        "industry": "Online PT (B2C, program-based)",
        "angle_to_take": "Joe Monteverdi (2.14K, US) — bodybuilding / physique coach with 4 / 8 / 12-week programs + biweekly FaceTime check-ins. Frame a branded JMont app with program-cohort tracker + intake-questionnaire intake + grocery-list module + check-in scheduler — replaces the FaceTime + IG ad-hoc workflow with a structured program surface.",
    },

    "support@kettlebelltransformation.co": {
        "category": "fitness",
        "niche": "Kettlebell Transformation System + Kettlebell Academy — done-for-you kettlebell programming for busy professionals, 400+ men coached (The Kettlebell Guys, 2.06K)",
        "segment_original": "Kettlebell Transformation System (paid program)",
        "industry": "Kettlebell Program (B2C, high-ticket)",
        "angle_to_take": "The Kettlebell Guys (2.06K) — Kettlebell Academy + KT System with $3.4K-equivalent kettlebell programming for busy professionals. Frame a branded Kettlebell Academy app with 2.5-yr progressive programming surface + form-check submit/review + driven-men cohort + KT-System onboarding — collapses the thekettlebellacademy.com + go.kettlebelltransformation.co + UTM-heavy funnel into one program-member app.",
    },

    "son5mike@gmail.com": {
        "category": "fitness",
        "niche": "IL Girevoy Sport (kettlebell sport) coach — beginner → advanced tutorials + technique breakdown + training protocols + workout routines (Coach Michael Son, 1.54K)",
        "segment_original": "IL Girevoy Sport (Kettlebell Sport) Coach",
        "industry": "Kettlebell Sport Coach (B2C + cohort)",
        "angle_to_take": "Girevoy Sport Education / Coach Michael Son (1.54K, IL) — Girevoy (kettlebell sport) coach with structured tutorials + protocols + routines. Frame a branded Girevoy Education app with technique-breakdown library + protocol calendar + competition-prep cohort + workout-pacing tool — fits the sport-prep specificity his content is built around.",
    },

    "info@fitfxtraining.ca": {
        "category": "fitness",
        "niche": "Registered Kinesiologist + Personal Trainer — exercise-prescription model for posture / pain / performance, #exerciseismedicine framing (Francesca / FitFx Training, 1.08K)",
        "segment_original": "CA Kinesiologist + PT (Exercise-Prescription Model)",
        "industry": "Kinesiology-Backed PT (B2C + email funnel)",
        "angle_to_take": "FitFx Training / Francesca R.Kin (1.08K, CA) — Registered Kinesiologist + PT framing exercise as a prescription for posture / pain / performance. Frame a branded FitFx app with intake-questionnaire → exercise-prescription assignment + lower-back-pain protocol library + Mailchimp-replacement email gating — collapses the mailchi.mp + email-only flow into a kinesiology-tiered member surface.",
    },
}
