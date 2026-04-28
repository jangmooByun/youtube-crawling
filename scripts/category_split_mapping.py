"""Per-row category mapping for sources #1~#6 (297 rows).

Maps email → one of: mindset | meditation | fitness | nutrition | drop

Rules (set by user):
  - mindset    = yoga (asana/vinyasa/hatha/kundalini/Rishikesh) + breathwork
                 + mindset coach (life coach / manifestation / mental health)
  - meditation = meditation only (mindfulness / Vipassana / Zen / MBSR / 정좌)
  - fitness    = PT / strength / hypertrophy / powerlifting / bodybuilding /
                 CrossFit / Pilates / bodyweight / calisthenics / dance fitness
                 / HIIT / functional / running / sport-specific S&C
  - nutrition  = dietitian / nutritionist / RD / macro / meal planning /
                 keto / diet coach / weight management (medical) / Ayurveda diet
  - drop       = OFF-TOPIC (gaming/scam/ministry/cross-vertical) +
                 JP/KR (excluded countries) +
                 non-creator entities (donations org / esports / immigration)

Multi-modal priority: dominant signal in segment_original.
yoga + meditation/breathwork → mindset (yoga primary).
fitness + nutrition → segment_original first keyword wins.
"""

MAPPING: dict[str, str] = {

    # =========================================================
    # S1 — data/2026-04-24/fitness_enriched.csv (15 rows)
    # =========================================================
    "kiransagar@shredfix.com": "fitness",
    "kontakt@coachlatif.com": "fitness",
    "rich@theviralistgroup.com": "fitness",
    "rosemarycp24@gmail.com": "nutrition",
    "jennclayton@yahoo.com": "nutrition",
    "email@typeform.com": "fitness",
    "opbisht@gmail.com": "fitness",
    "wellnessdrmeghan@gmail.com": "nutrition",
    "kaushikbose222@gmail.com": "fitness",
    "asaptheworkout@gmail.com": "fitness",
    "spandanamorem95@gmail.com": "mindset",
    "fitnessbyraviverma@gmail.com": "fitness",
    "transcripts@crooked.com": "fitness",
    "kwnfit@gmail.com": "fitness",
    "strengthcoachjazz@gmail.com": "fitness",

    # =========================================================
    # S2 — data/2026-04-24/nutrition_enriched.csv (18 rows)
    # =========================================================
    "coachrogueyt@gmail.com": "drop",
    # rosemarycp24@gmail.com  → already in S1 (same email, dedup)
    "shelly@skinnylouisiana.com": "nutrition",
    "nicole@nicoleferrierfitness.com": "nutrition",
    "orders@nationalnutrition.ca": "nutrition",
    "neenarseth@gmail.com": "nutrition",
    "eatwell@elainedietitian.com": "nutrition",
    "career@finesseinstitute.in": "nutrition",
    "seb@influencernexus.com": "nutrition",
    "nsaffo@nk-fitness.com": "nutrition",
    "prachi.nutritionist@gmail.com": "nutrition",
    "dieticiangarima@gmail.com": "nutrition",
    "dietadvisory@gmail.com": "nutrition",
    "askus@inchealthy.com": "nutrition",
    "meghanlkozlowski@gmail.com": "nutrition",
    "office@slaviclabs.com": "nutrition",
    "robert@dietfreelife.com": "nutrition",
    "hello@stephanielong.ca": "nutrition",

    # =========================================================
    # S3 — data/2026-04-25/fitness_enriched_0425.csv (50 rows)
    # =========================================================
    "team@armaanmalik.in": "fitness",
    "maazikram224@gmail.com": "fitness",
    "hellofittuber@gmail.com": "nutrition",
    "contato@exercicioemcasa.com.br": "fitness",
    "santoshkumarkumarenglis@gmail.com": "fitness",
    "zumbaclass.fitness@gmail.com": "fitness",
    "joannasohofficial@gmail.com": "fitness",
    "collab@thegravgear.com": "fitness",
    "coachmartinphysed@gmail.com": "fitness",
    "alexandrosthenics@gmail.com": "fitness",
    "mormahima9@gmail.com": "mindset",
    "movewithagnes@gmail.com": "fitness",
    "Melania.Antuchas@gmail.com": "fitness",
    "https://www.youtube.com/@khushibajwayoga": "drop",  # email column contains URL — broken extraction; valid khushibajwayoga@gmail.com row exists in S5_27F
    "norihiroabe@dekitore.jp": "drop",  # JP excluded
    "info@integrityattitudehustle.com": "fitness",
    "strongman19990706@gmail.com": "fitness",
    "egsports0104@gmail.com": "drop",  # KR excluded
    "hyperthenic.group@gmail.com": "fitness",
    "info@danielptfitness.com": "fitness",
    "onkarchughyoga@gmail.com": "mindset",
    "info@kettlebellkings.com": "fitness",
    "GWARTEM@GMAIL.COM": "fitness",
    "teamfoodsefitness@gmail.com": "nutrition",
    "info@bharatha.org": "mindset",
    "fryderyk.fruzynski@hotmail.com": "fitness",
    "holisticmovementpilates@gmail.com": "fitness",
    "https://www.youtube.com/@agetore9244": "drop",  # JP excluded
    "paultwymancoaching@gmail.com": "fitness",
    "https://www.youtube.com/@cavemantraining": "drop",  # email column contains URL — broken extraction
    "samueljordanfitness@gmail.com": "fitness",
    "borntoruncoach@gmail.com": "fitness",
    "https://www.youtube.com/@naddyfitness4141": "drop",  # JP excluded
    "Ruggedlifestyle93@gmail.com": "fitness",
    "tutorialsthatworks@gmail.com": "fitness",
    "calisthenixpro@gmail.com": "fitness",
    "info@danubecalisthenics.com": "fitness",
    "bk27718@gmail.com": "fitness",
    "maddiemilton.social@gmail.com": "fitness",
    "t_van_spanje@hotmail.com": "fitness",
    "homeworkout011@gmail.com": "fitness",
    "jermaster65@gmail.com": "fitness",
    "masterarjun94@gmail.com": "mindset",
    "service@strengthcoachnetwork.com": "fitness",
    "orders@prokettlebell.com": "fitness",
    "info@kbstronger.com": "fitness",
    "marcos@entrenadorwellness.com": "fitness",
    "bhoriabunty@gmail.com": "mindset",
    "support@kettlebelltransformation.co": "fitness",
    "support@joinladder.com": "fitness",  # multi-modality (strength + yoga + breathwork) — strength first

    # =========================================================
    # S4 — data/2026-04-25/nutrition_enriched_0425.csv (55 rows)
    # =========================================================
    "avnish239@gmail.com": "fitness",
    "rohitkhatribiz07@gmail.com": "nutrition",
    "rajivdixitjiofficial@gmail.com": "drop",  # posthumous orator archive
    "ankitbaiyanpuria@gmail.com": "fitness",
    "rajveerfitness@gmail.com": "fitness",
    "gunjanshouts@gmail.com": "fitness",
    "drshikhasingh24@gmail.com": "nutrition",
    "rc7674@gmail.com": "nutrition",
    "kyliesakaida@select.co": "nutrition",
    "healthfithindi@gmail.com": "nutrition",
    "foodfitnessfun.official@gmail.com": "nutrition",
    "bhumim3172@gmail.com": "drop",  # cross-vertical (home org + decor + recipes + yoga + weight-loss)
    "fullcurvenet@gmail.com": "fitness",
    "diettubeindia@gmail.com": "nutrition",
    "simpletipsanweshaofficial@gmail.com": "nutrition",
    "savikarbhardwaj@gmail.com": "nutrition",
    "info.heenahealth@gmail.com": "nutrition",
    "mrbfitbusiness@gmail.com": "nutrition",
    "emmie@modernmediaservices.com": "nutrition",
    "chadtag4404@gmail.com": "drop",  # IN regional lifestyle (off-topic)
    "nls@naturallifestyle.in": "drop",  # non-profit donations org
    "holisticwisdom134@gmail.com": "nutrition",
    "brian@thegainzbox.com": "nutrition",
    "drprashant_more@yahoo.com": "nutrition",
    "info@bodyfittv.in": "fitness",
    "online.weightlosstv@gmail.com": "nutrition",
    "rimislunchbox29@gmail.com": "nutrition",
    "tulasivkumar@gmail.com": "fitness",
    "dietitiansheena@gmail.com": "nutrition",
    "agendamento@nutricionistaesportiva.com": "nutrition",
    "tara@wholebodyliving.com": "nutrition",
    "ewl.adoretrust@gmail.com": "nutrition",
    "adm.nutrasports@gmail.com": "nutrition",
    "rakeshbsharma1981@gmail.com": "nutrition",
    "theblessedfam555@gmail.com": "nutrition",
    "Enquiry@macroglobalmoga.net": "drop",  # IELTS / immigration mis-categorized
    "clearcrinzy@gmail.com": "mindset",  # anxiety-recovery storytelling
    "info@thedietchannel.in": "nutrition",
    "info@marialuceyrd.com": "nutrition",
    "artemisatapia@gmail.com": "nutrition",
    "hypernestdigitalmedia@gmail.com": "nutrition",
    "inquiries@chicago-dietitian.com": "nutrition",
    "acbduarte@gmail.com": "nutrition",
    "contact@revivreparlassiette.fr": "nutrition",
    "hello.nutriketo@gmail.com": "nutrition",
    "care@amura.ai": "nutrition",
    "nutriallanfernandes@gmail.com": "nutrition",
    "assessoria@drafernandagranja.com.br": "nutrition",
    "info@themillennialnutritionist.com": "nutrition",
    "kyleegumm@gmail.com": "nutrition",
    "info@morethanjustveggies.com": "nutrition",
    "lauren@tastingtothrive.com": "nutrition",
    "irinaseewoo@gmail.com": "nutrition",
    "Natalie@NatalieJGrasso.com": "nutrition",
    "loboglobalsl@gmail.com": "nutrition",

    # =========================================================
    # S5 — data/2026-04-27/fitness_enriched.csv (104 rows)
    # =========================================================
    "mediarelations@athleanx.com": "fitness",
    "xenia@xglow-mgmt.com": "fitness",
    "walkathome@streaming-subscription.com": "fitness",
    "contact@willtennyson.ca": "fitness",
    "management@heatherrobertson.com": "fitness",
    "pregnancyandpostpartumtv@outloudtalent.com": "fitness",
    "danceyog2019@gmail.com": "fitness",
    "banosahida1@gmail.com": "mindset",
    "partnerships@midasmedia.ca": "fitness",
    "paul@teamonwardtalent.com": "fitness",
    "richburg.jessica@gmail.com": "mindset",
    "support@omstars.com": "mindset",
    "Connor@28thave.com": "fitness",
    "ccchhtt23@gmail.com": "fitness",
    "management@scottburnhard.com": "fitness",
    "support@jennacollinsfitness.com": "fitness",
    "support@jessicasmith.fitness": "fitness",
    "zthtraining@doubletapcontent.com": "fitness",
    "meetsrim@satsang-foundation.org": "mindset",  # Sri M Kriya Yoga retreats
    "collab@yoursalbany.com": "fitness",  # Pilates+Yoga+Prenatal — pilates first
    "mukeshgahlot.management@gmail.com": "fitness",
    "khushibajwayoga@gmail.com": "mindset",
    "sabahkadriofficial@gmail.com": "fitness",
    "sk8973729@gmail.com": "mindset",  # yoga + meditation + breathwork — yoga primary
    "saipoojayoga@gmail.com": "mindset",
    "kirra@strongsistersunited.com": "fitness",
    "alonefitness93@gmail.com": "fitness",
    "honeybusiness35@gmail.com": "fitness",
    "rk1000896@gmail.com": "mindset",
    "trainers@marklauren.com": "fitness",
    "support@joinggstudio.com": "fitness",
    "-prem40216@gmail.com": "mindset",
    "love.yogavision@gmail.com": "mindset",
    "team@msworkouts.com": "fitness",
    "hello@yogawithzelinda.com": "mindset",
    "mdsaiedali12@gmail.com": "fitness",
    "info@akramyoga.co.uk": "mindset",
    "info@solinfitness.com": "fitness",
    "info@rachelyoga.com": "mindset",
    "info@bodhischoolofyoga.com": "mindset",
    "tauheedkhan0698@gmail.com": "fitness",
    "hello@camiyogair.com": "mindset",
    "support@onlineyogateaching.com": "mindset",
    "morganchurch8050@gmail.com": "fitness",
    "support@jenniferraye.com": "mindset",
    "premanandyoga@gmail.com": "mindset",
    "bzwang43@gmail.com": "fitness",
    "feliciawalkeryoga@web.de": "mindset",
    "hello@lorettaloveslifting.com": "fitness",
    "info@yogavidyaschool.com": "mindset",
    "results@bodybyyoga.training": "mindset",
    "gojudo81@gmail.com": "fitness",
    "misskajal2025@gmail.com": "mindset",
    "info@flex-calisthenics.com": "fitness",
    "jessiraewellness@gmail.com": "mindset",
    "aermotionhelp@gmail.com": "fitness",
    "ayurvedaecosystem@gmail.com": "nutrition",  # AYUSH ayurveda diet/medical education
    "hello@elementpilatesyoga.com": "fitness",  # Pilates first in name
    "ondemand@speirpilates.com": "fitness",
    "strengthskl20@gmail.com": "fitness",
    "info@bendablebody.com": "fitness",
    "raghvendrapatel96@gmail.com": "fitness",
    "yogicali85@gmail.com": "fitness",  # Calisthenics + yoga + bodyweight — calisthenics first
    "ps.jooga@gmail.com": "mindset",  # Face Yoga
    "dhanaescueladeyoga@hotmail.com": "mindset",
    "info@pilatesbysophie.be": "fitness",
    "info@tiwariyoga.com": "mindset",  # yoga + meditation + breathwork + Ayurveda — yoga primary
    "info@atmayoga.it": "mindset",
    "admin@manayoga.ca": "mindset",
    "kontakt@pilatesstudioonline.pl": "fitness",
    "info@rainbowyogatraining.com": "mindset",
    "iris@sculptwithiris.com": "fitness",
    "info@crossyoga.org": "mindset",
    "info@pilatesliebe.de": "fitness",
    "narberth@elliehermanpilates.com": "fitness",
    "info@sallyparkesyoga.com": "mindset",
    "adrianne@thousandfoldlotus.com": "fitness",
    "Poojajha24thjan@gmail.com": "mindset",  # motivation + meditation + yoga — yoga primary
    "coljorgensen13@gmail.com": "fitness",  # pain-care movement (Pilates/Yoga/Somatics) — pilates+somatics
    "vladcalisthenicsman@gmail.com": "fitness",
    "reikilates@gmail.com": "fitness",  # Reiki+Pilates fusion — pilates dominant
    "Info@NataliaPilates.co.uk": "fitness",
    "edwardssophie@live.co.uk": "fitness",
    "lifestyle@yogapadova.it": "mindset",
    "rishikeshyogkendra1@gmail.com": "mindset",
    "info@theblackpranayoga.com": "mindset",
    "laura@lauragreenyoga.co.uk": "mindset",
    "harmanrooprai122@gmail.com": "fitness",
    "medtwalritu@gmail.com": "fitness",
    "info@yoga-yin.com": "mindset",
    "info@sarahbyoga.net": "mindset",
    "info@gr8flex.com": "fitness",
    "info@chriswongfitness.com": "fitness",
    "hello@studio20.me": "mindset",
    "contact@practicewithjodie.com": "mindset",
    "arjunsingh826448@gmail.com": "fitness",
    "filler@godaddy.com": "fitness",
    "coaching.liza@gmail.com": "fitness",
    "theoceanyoga.info@gmail.com": "mindset",
    "akshayrathodfitnesscoach@gmail.com": "fitness",
    "anugraha6613@gmail.com": "mindset",
    "seeu@ufitupilates.com": "fitness",
    "info@beyogi.com": "mindset",
    "info@antarayoga.nl": "mindset",

    # =========================================================
    # S6 — data/2026-04-28/fitness_enriched.csv (55 rows)
    # =========================================================
    "Browney@Delkatalents.com": "fitness",
    "graystillplays@gmail.com": "drop",  # gaming
    "wendigoon@manatalentgroup.com": "drop",  # true-crime
    "press@thepauselife.com": "nutrition",  # menopause MD + author
    "rehab@dublinsportsinjuryclinic.com": "fitness",  # PT clinic
    "contact@jacks-team.com": "nutrition",  # anti-inflammation diet primary
    "support@dr-gains.com": "fitness",
    "Joncandito.canditotraining@gmail.com": "fitness",
    "geodude412@yahoo.com": "fitness",
    "kevin@kevthetrainer.co": "fitness",
    "leon60954@gmail.com": "fitness",
    "ashokmartin007@gmail.com": "drop",  # Christian ministry
    "yt.basementbodybuilding@gmail.com": "fitness",
    "severin@posemethod.com": "fitness",
    "Charlie@charliejohnsonfitness.com": "fitness",
    "Fitnessmn@Yahoo.com": "fitness",
    "kangradeepak501@gmail.com": "fitness",
    "jamesli09business@gmail.com": "fitness",
    "support@socialbluebook.com": "fitness",
    "arydropp@gmail.com": "drop",  # training-music brand (not a coach)
    "educontent@crossfit.com": "fitness",
    "crossfitkrypton@gmail.com": "fitness",
    "halimtsiang@gmail.com": "fitness",
    "pomoc@sylwiadus.com.pl": "mindset",  # face yoga
    "info@movestrongfit.com": "fitness",
    "bharatfitnessinstitute@gmail.com": "fitness",
    "support@ganbarumethod.com": "fitness",
    "R4P.ORG@GMAIL.COM": "fitness",  # equipment brand (consistent w/ kettlebell brands)
    "kingwoodstrength@gmail.com": "fitness",
    "info@marcusveysey.com": "drop",  # Tarot/spiritual
    "anonymousmankindproject@gmail.com": "drop",  # PT + conspiracy mixed
    "sanjaycool4200@gmail.com": "fitness",
    "castleinprogress@gmail.com": "fitness",
    "thirst.training@gmail.com": "fitness",
    "martha@youronlinetenniscoach.com": "fitness",
    "info@contehsports.com": "fitness",
    "rsullivan@suf.fitness": "fitness",
    "Chris@CompetitiveBreed.com": "fitness",
    "support@playbookapp.io": "fitness",
    "thamketejas497@gmail.com": "fitness",
    "MarkMacqueenCoaching@yahoo.co.uk": "fitness",
    "info@crossfitsantiago.com": "fitness",
    "Coachrohitsharma@gmail.com": "fitness",
    "Fit4Expedition@gmail.com": "fitness",
    "Info@fitlifeathletics.com": "fitness",
    "vatsalkanirkar@gmail.com": "fitness",
    "Gio@Giovannitraining.com": "fitness",
    "BuiltByUnit@gmail.com": "fitness",
    "CoachHollyMitchell@gmail.com": "fitness",
    "OffGridStrength@gmail.com": "fitness",
    "conjugateiron@yahoo.com": "fitness",
    "protectyaneckfitness@gmail.com": "fitness",
    "info@crossfitboran.com": "fitness",
    "hello@w10.fit": "fitness",
    "info@onlineinc.biz": "drop",  # MLM/scam
}
