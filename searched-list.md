 처음 US/CA/AU/NZ 타겟으로 제안했던 라이프스타일 서브 카테고리 7개입니다:                                                                
                                                                                                                                                        
  1. 일반 vlog / 데일리 루틴 — daily vlog, morning routine, day in my life                                                                                
  2. 홈/인테리어/미니멀리즘 — home decor, apartment tour, minimalist lifestyle                                                                          
  3. 생산성/자기계발 — productivity tips, study with me, self improvement                                                                                 
  4. 웰니스/셀프케어 — wellness routine, self care routine, healthy lifestyle                                                                             
  5. 패션/스타일 — outfit ideas, capsule wardrobe                                                                                                         
  6. 여행 라이프스타일 — travel vlog, solo travel                                                                                                         
  7. 홈쿠킹/푸드 라이프스타일 — what i eat in a day, easy recipes                                                                                         
                                                                                                                                                          
  그리고 그 뒤에 앱빌챗 서비스 컨텍스트(7일 앱 제작) 공유하시면서 "라이프스타일 vlog/홈데코는 오히려 타겟 어긋난다 — 구독자가 앱 구매자가 아니라 콘텐츠   
  소비자" 라고 피드백 드리고, 창업자/코치/크리에이터 소유권자 카테고리(인디해커, 온라인 코치, 강의 판매자, 커뮤니티 운영자, 영양사 등) 로 선회했었죠.     
                                                                                                                                                          
  그 흐름에서 지금 영양사/다이어트 코치 니치를 실행하시는 겁니다.   

—----------------------------------

  1. Type Beat 프로듀서 — free type beat, drake type beat                                                                                                 
  2. 샘플팩/드럼킷 판매자 — free drum kit, sample pack review                                                                                             
  3. 믹싱/마스터링 튜토리얼 — mixing hip hop vocals, mastering tutorial                                                                                   
  4. DAW 전용 교육 — FL Studio tutorial, Ableton Live tutorial, Logic Pro X tutorial                                                                      
  5. 플러그인/VST 리뷰 — best VST plugins, Serum tutorial                                                                                                 
  6. 스튜디오 기어 리뷰 — best midi keyboard, audio interface review                                                                                      
  7. 음악 이론 for 프로듀서 — music theory for producers, chord progressions for beats                                                                    
  8. 사이드 장르 비트메이커 — Lo-fi / Drill / Afrobeat / R&B / Phonk                                                                                      
  9. 래퍼/보컬리스트 (제외 추천) 

—----------------------------------

 # ===== A. 피트니스/홈트 (fitness.db) =====

  # 0. 정리
  rm -f fitness.db fitness_leads.csv fitness_all.csv

  # 1. DB 초기화
  uv run influencer init --db-path fitness.db

  # 2. 채널 발견 — 피트니스 × US/CA/AU/NZ (4 키워드 × 4 리전 = 16회)
  # US
  uv run influencer discover youtube -k "home workout" --max 50 --min-subs 10000 --max-subs 500000 --region US --language en --db fitness.db
  uv run influencer discover youtube -k "pilates at home" --max 50 --min-subs 10000 --max-subs 500000 --region US --language en --db fitness.db
  uv run influencer discover youtube -k "beginner yoga" --max 50 --min-subs 10000 --max-subs 500000 --region US --language en --db fitness.db
  uv run influencer discover youtube -k "strength training" --max 50 --min-subs 10000 --max-subs 500000 --region US --language en --db fitness.db

  # CA
  uv run influencer discover youtube -k "home workout" --max 50 --min-subs 5000 --max-subs 500000 --region CA --language en --db fitness.db
  uv run influencer discover youtube -k "pilates at home" --max 50 --min-subs 5000 --max-subs 500000 --region CA --language en --db fitness.db
  uv run influencer discover youtube -k "beginner yoga" --max 50 --min-subs 5000 --max-subs 500000 --region CA --language en --db fitness.db
  uv run influencer discover youtube -k "strength training" --max 50 --min-subs 5000 --max-subs 500000 --region CA --language en --db fitness.db

  # AU
  uv run influencer discover youtube -k "home workout" --max 50 --min-subs 3000 --max-subs 500000 --region AU --language en --db fitness.db
  uv run influencer discover youtube -k "pilates at home" --max 50 --min-subs 3000 --max-subs 500000 --region AU --language en --db fitness.db
  uv run influencer discover youtube -k "beginner yoga" --max 50 --min-subs 3000 --max-subs 500000 --region AU --language en --db fitness.db
  uv run influencer discover youtube -k "strength training" --max 50 --min-subs 3000 --max-subs 500000 --region AU --language en --db fitness.db

  # NZ
  uv run influencer discover youtube -k "home workout" --max 50 --min-subs 1000 --max-subs 500000 --region NZ --language en --db fitness.db
  uv run influencer discover youtube -k "pilates at home" --max 50 --min-subs 1000 --max-subs 500000 --region NZ --language en --db fitness.db
  uv run influencer discover youtube -k "beginner yoga" --max 50 --min-subs 1000 --max-subs 500000 --region NZ --language en --db fitness.db
  uv run influencer discover youtube -k "strength training" --max 50 --min-subs 1000 --max-subs 500000 --region NZ --language en --db fitness.db

  # 3. 중간 진행 확인
  uv run influencer stats --db fitness.db

  # 4. Bio 에서 이메일 + 외부 링크 추출
  uv run influencer extract --db fitness.db

  # 5. 외부 링크 크롤링 (SaaS 감지 포함)
  uv run influencer crawl-links --db fitness.db

  # 6. 이메일 검증
  uv run influencer validate --db fitness.db

  # 7. CSV 내보내기
  uv run influencer export --filter "has_mx=1 AND is_role_based=0 AND follower_count <= 500000" --out fitness_leads.csv --db fitness.db
  uv run influencer export --filter "has_mx=1 AND follower_count <= 500000" --out fitness_all.csv --db fitness.db

  # 8. 최종 통계
  uv run influencer stats --db fitness.db

  # ===== B. 저널링/마인드풀니스 (mindful.db) =====

  rm -f mindful.db mindful_leads.csv mindful_all.csv

  uv run influencer init --db-path mindful.db

  # US
  uv run influencer discover youtube -k "journaling for beginners" --max 50 --min-subs 10000 --max-subs 500000 --region US --language en --db mindful.db
  uv run influencer discover youtube -k "meditation for beginners" --max 50 --min-subs 10000 --max-subs 500000 --region US --language en --db mindful.db
  uv run influencer discover youtube -k "mindfulness practice" --max 50 --min-subs 10000 --max-subs 500000 --region US --language en --db mindful.db
  uv run influencer discover youtube -k "guided meditation" --max 50 --min-subs 10000 --max-subs 500000 --region US --language en --db mindful.db

  # CA
  uv run influencer discover youtube -k "journaling for beginners" --max 50 --min-subs 5000 --max-subs 500000 --region CA --language en --db mindful.db
  uv run influencer discover youtube -k "meditation for beginners" --max 50 --min-subs 5000 --max-subs 500000 --region CA --language en --db mindful.db
  uv run influencer discover youtube -k "mindfulness practice" --max 50 --min-subs 5000 --max-subs 500000 --region CA --language en --db mindful.db
  uv run influencer discover youtube -k "guided meditation" --max 50 --min-subs 5000 --max-subs 500000 --region CA --language en --db mindful.db

  # AU
  uv run influencer discover youtube -k "journaling for beginners" --max 50 --min-subs 3000 --max-subs 500000 --region AU --language en --db mindful.db
  uv run influencer discover youtube -k "meditation for beginners" --max 50 --min-subs 3000 --max-subs 500000 --region AU --language en --db mindful.db
  uv run influencer discover youtube -k "mindfulness practice" --max 50 --min-subs 3000 --max-subs 500000 --region AU --language en --db mindful.db
  uv run influencer discover youtube -k "guided meditation" --max 50 --min-subs 3000 --max-subs 500000 --region AU --language en --db mindful.db

  # NZ
  uv run influencer discover youtube -k "journaling for beginners" --max 50 --min-subs 1000 --max-subs 500000 --region NZ --language en --db mindful.db
  uv run influencer discover youtube -k "meditation for beginners" --max 50 --min-subs 1000 --max-subs 500000 --region NZ --language en --db mindful.db
  uv run influencer discover youtube -k "mindfulness practice" --max 50 --min-subs 1000 --max-subs 500000 --region NZ --language en --db mindful.db
  uv run influencer discover youtube -k "guided meditation" --max 50 --min-subs 1000 --max-subs 500000 --region NZ --language en --db mindful.db

  uv run influencer stats       --db mindful.db
  uv run influencer extract     --db mindful.db
  uv run influencer crawl-links --db mindful.db
  uv run influencer validate    --db mindful.db

  uv run influencer export --filter "has_mx=1 AND is_role_based=0 AND follower_count <= 500000" --out mindful_leads.csv --db mindful.db
  uv run influencer export --filter "has_mx=1 AND follower_count <= 500000" --out mindful_all.csv --db mindful.db

  uv run influencer stats --db mindful.db

  # ===== C. 파이낸셜/가계부 (finance.db) =====

  rm -f finance.db finance_leads.csv finance_all.csv

  uv run influencer init --db-path finance.db

  # US
  uv run influencer discover youtube -k "personal finance" --max 190 --min-subs 10000 --max-subs 500000 --region US --language en --db finance.db
  uv run influencer discover youtube -k "budgeting tips" --max 100 --min-subs 10000 --max-subs 500000 --region US --language en --db finance.db
  uv run influencer discover youtube -k "frugal living" --max 100 --min-subs 10000 --max-subs 500000 --region US --language en --db finance.db
  uv run influencer discover youtube -k "debt payoff" --max 100 --min-subs 10000 --max-subs 500000 --region US --language en --db finance.db

  # CA
  uv run influencer discover youtube -k "personal finance" --max 50 --min-subs 5000 --max-subs 500000 --region CA --language en --db finance.db
  uv run influencer discover youtube -k "budgeting tips" --max 50 --min-subs 5000 --max-subs 500000 --region CA --language en --db finance.db
  uv run influencer discover youtube -k "frugal living" --max 50 --min-subs 5000 --max-subs 500000 --region CA --language en --db finance.db
  uv run influencer discover youtube -k "debt payoff" --max 50 --min-subs 5000 --max-subs 500000 --region CA --language en --db finance.db

  # AU
  uv run influencer discover youtube -k "personal finance" --max 50 --min-subs 3000 --max-subs 500000 --region AU --language en --db finance.db
  uv run influencer discover youtube -k "budgeting tips" --max 50 --min-subs 3000 --max-subs 500000 --region AU --language en --db finance.db
  uv run influencer discover youtube -k "frugal living" --max 50 --min-subs 3000 --max-subs 500000 --region AU --language en --db finance.db
  uv run influencer discover youtube -k "debt payoff" --max 50 --min-subs 3000 --max-subs 500000 --region AU --language en --db finance.db

  # NZ
  uv run influencer discover youtube -k "personal finance" --max 50 --min-subs 1000 --max-subs 500000 --region NZ --language en --db finance.db
  uv run influencer discover youtube -k "budgeting tips" --max 50 --min-subs 1000 --max-subs 500000 --region NZ --language en --db finance.db
  uv run influencer discover youtube -k "frugal living" --max 50 --min-subs 1000 --max-subs 500000 --region NZ --language en --db finance.db
  uv run influencer discover youtube -k "debt payoff" --max 50 --min-subs 1000 --max-subs 500000 --region NZ --language en --db finance.db

  uv run influencer stats       --db finance.db
  uv run influencer extract     --db finance.db
  uv run influencer crawl-links --db finance.db
  uv run influencer validate    --db finance.db

  uv run influencer export --filter "has_mx=1 AND is_role_based=0 AND follower_count <= 500000" --out finance_leads.csv --db finance.db
  uv run influencer export --filter "has_mx=1 AND follower_count <= 500000" --out finance_all.csv --db finance.db

  uv run influencer stats --db finance.db

  # ===== D. 생산성/자기계발 (productivity.db) =====

  rm -f productivity.db productivity_leads.csv productivity_all.csv

  uv run influencer init --db-path productivity.db

  # US
  uv run influencer discover youtube -k "productivity tips" --max 50 --min-subs 10000 --max-subs 500000 --region US --language en --db productivity.db
  uv run influencer discover youtube -k "study with me" --max 50 --min-subs 10000 --max-subs 500000 --region US --language en --db productivity.db
  uv run influencer discover youtube -k "notion tutorial" --max 50 --min-subs 10000 --max-subs 500000 --region US --language en --db productivity.db
  uv run influencer discover youtube -k "time management" --max 50 --min-subs 10000 --max-subs 500000 --region US --language en --db productivity.db

  # CA
  uv run influencer discover youtube -k "productivity tips" --max 50 --min-subs 5000 --max-subs 500000 --region CA --language en --db productivity.db
  uv run influencer discover youtube -k "study with me" --max 50 --min-subs 5000 --max-subs 500000 --region CA --language en --db productivity.db
  uv run influencer discover youtube -k "notion tutorial" --max 50 --min-subs 5000 --max-subs 500000 --region CA --language en --db productivity.db
  uv run influencer discover youtube -k "time management" --max 50 --min-subs 5000 --max-subs 500000 --region CA --language en --db productivity.db

  # AU
  uv run influencer discover youtube -k "productivity tips" --max 50 --min-subs 3000 --max-subs 500000 --region AU --language en --db productivity.db
  uv run influencer discover youtube -k "study with me" --max 50 --min-subs 3000 --max-subs 500000 --region AU --language en --db productivity.db
  uv run influencer discover youtube -k "notion tutorial" --max 50 --min-subs 3000 --max-subs 500000 --region AU --language en --db productivity.db
  uv run influencer discover youtube -k "time management" --max 50 --min-subs 3000 --max-subs 500000 --region AU --language en --db productivity.db

  # NZ
  uv run influencer discover youtube -k "productivity tips" --max 50 --min-subs 1000 --max-subs 500000 --region NZ --language en --db productivity.db
  uv run influencer discover youtube -k "study with me" --max 50 --min-subs 1000 --max-subs 500000 --region NZ --language en --db productivity.db
  uv run influencer discover youtube -k "notion tutorial" --max 50 --min-subs 1000 --max-subs 500000 --region NZ --language en --db productivity.db
  uv run influencer discover youtube -k "time management" --max 50 --min-subs 1000 --max-subs 500000 --region NZ --language en --db productivity.db

  uv run influencer stats       --db productivity.db
  uv run influencer extract     --db productivity.db
  uv run influencer crawl-links --db productivity.db
  uv run influencer validate    --db productivity.db

  uv run influencer export --filter "has_mx=1 AND is_role_based=0 AND follower_count <= 500000" --out productivity_leads.csv --db productivity.db
  uv run influencer export --filter "has_mx=1 AND follower_count <= 500000" --out productivity_all.csv --db productivity.db

  uv run influencer stats --db productivity.db

  API 쿼터 (4 DB × 16 discover = 64 호출 ≈ 8,000 units) — 하루 10,000 무료 안에 들어오지만 빡빡하니 카테고리 1~2 개씩 나눠 돌리는 편 안전.
