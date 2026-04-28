# 2026-04-28 작성 — 내일 (2026-04-29) sweep 작업 계획

## 배경

오늘까지 4 카테고리 풀:

| 카테고리 | 현재 row | 약점 |
|---|---|---|
| mindset | 63 | yoga 압도적, breathwork (Wim Hof / Pranayama / Buteyko) 거의 없음, mindset/stress 코치 없음 |
| meditation | 31 | Stage B 1 page 만 돔 (~4500 quota 잔여 미사용) — 깊이 부족 |
| fitness | 168 | PT/HIIT/strength 위주, mobility / kettlebell / calisthenics 사실상 없음 |
| nutrition | 72 | RD/dietitian 일반, sports / gut / fasting 코치 부족 |

오늘 quota 잔량 ~960 — 자정 PT reset 까지 sweep 추가 보류. 내일 reset 후 ~10,000 quota 확보.

## 내일 작업 — A + B 두 갈래

### A. meditation 깊이 확장 + mindset breathwork/coach 보강
- meditation Stage B 를 PAGES=3 으로 deeper paginate (오늘 1 page 만 돈 10 keyword + 4 신규 = 14 keyword)
- mindset 의 빈약한 sub-niche 6 keyword × 2 page

### B. fitness/nutrition sub-niche 신규 surface
- fitness 6 keyword × 2 page (mobility / kettlebell / calisthenics / powerlifting / women's strength / recovery)
- nutrition 6 keyword × 2 page (sports / gut / fasting / hormonal / functional / metabolic)

D (sound healing / functional medicine / breathwork retreat) 는 이번 사이클 제외 — 다음 달 재고.

## Quota 예산 (~9,350 / 10,000 일일 한도, 버퍼 ~6.5%)

| 카테고리 | keyword × page | search.list | channels.list | freshness 필터 | 소계 |
|---|---|---|---|---|---|
| meditation | 14 × 3 | 4,200 | ~600 | ~250 | **5,050** |
| mindset (breathwork/coach) | 6 × 2 | 1,200 | ~150 | ~80 | **1,430** |
| fitness (sub-niche) | 6 × 2 | 1,200 | ~150 | ~90 | **1,440** |
| nutrition (sub-niche) | 6 × 2 | 1,200 | ~150 | ~80 | **1,430** |
| **합계** | | | | | **~9,350** |

타이트하지만 한도 안. quotaExceeded 시 v3 의 cleanly stop 패턴 그대로.

## Freshness 필터 (6 개월 무활동 채널 제외)

내일 sweep 의 추가 요구사항. 마지막 업로드가 6 개월 (180 일) 보다 오래된 채널은 surface 안 함.

**임계값**: today − 180d = **2025-10-28** (today 2026-04-28 기준).

### 구현
- `channels.list` 의 `part` 에 `contentDetails` 추가 (quota 영향 0 — 호출당 1 unit 그대로)
- 각 채널에서 `contentDetails.relatedPlaylists.uploads` (uploads 플레이리스트 ID) 추출
- MIN_SUBS / 국가 필터 통과한 채널에 대해서만:
  - `playlistItems.list(playlistId=uploads_id, part="snippet", maxResults=1)` 호출 (채널당 +1 quota)
  - `items[0].snippet.publishedAt` 가 cutoff 보다 새것이면 통과, 아니면 drop
  - items 가 비어있으면 (퍼블릭 영상 없음) → drop

### 컬럼 저장 안 함 (필터 전용)
`last_upload_at` 은 19-col schema 에 추가 안 함 — 필터링에만 사용하고 버림. 차후 재취득 가능.

### 적용 범위
**내일 sweep (`data/2026-04-29/`) 만 적용**. 기존 334 row (`data/total/`) 는 freshness 백필 안 함 — 이번 사이클 안전선.

### 예상 효과
- 일반적으로 3~5% 채널이 6 개월 무활동으로 drop (sweep 마다 다름)
- 추가 quota 비용: ~500 (전체 4 카테고리 합)

## 키워드 정의

### meditation (14)
오늘 1 page 만 돈 10 keyword 를 PAGES=3 으로 재실행 + 4 신규 추가:

```python
"meditation": [
    # Mindfulness practice
    ("guided meditation teacher", None),
    ("mindfulness meditation teacher", None),
    ("online meditation course", None),
    ("meditation for beginners channel", None),       # 신규
    ("daily meditation practice teacher", None),
    # Buddhist / Vipassana / Zen
    ("vipassana meditation teacher", None),
    ("insight meditation teacher", None),
    ("zen meditation teacher", None),
    ("buddhist meditation teacher", None),            # 신규
    # MBSR / clinical
    ("MBSR teacher online", None),
    ("mindfulness based stress reduction", None),    # 신규
    # Sleep / relaxation
    ("yoga nidra teacher", None),                    # 신규 — 일부 mindset 분류 가능
    ("sleep meditation channel", None),
    # Transcendental / mantra
    ("transcendental meditation teacher", None),
],
```

오늘 04-28 sweep 데이터 (`data/2026-04-28/meditation.csv`) 와 cross-date dedup 으로 자동 필터.

### mindset (6) — breathwork + coach 보강
현재 mindset 63 row 는 yoga 풀이 압도적. breathwork 와 mindset/stress 코치는 거의 없음.

```python
"mindset": [
    # Breathwork
    ("wim hof breathwork instructor", None),
    ("pranayama breathing technique teacher", None),
    ("holotropic breathwork facilitator", None),
    # Mindset coach
    ("mindset coach motivation", None),
    ("confidence coach personal development", None),
    ("stress management coach online", None),
],
```

### fitness (6) — 안 잡힌 sub-niche
현재 fitness 168 은 PT/HIIT/strength 위주. mobility / kettlebell / calisthenics 거의 없음.

```python
"fitness": [
    ("mobility coach posture training", None),
    ("kettlebell training coach", None),
    ("calisthenics street workout coach", None),
    ("powerlifting coach online", None),
    ("women's strength training coach", None),
    ("recovery rehabilitation fitness coach", None),
],
```

### nutrition (6) — 안 잡힌 sub-niche
현재 nutrition 72 는 RD/dietitian 일반. sports nutrition / gut health / fasting 거의 없음.

```python
"nutrition": [
    ("sports nutrition coach online", None),
    ("gut health nutritionist", None),
    ("intermittent fasting coach", None),
    ("women's hormonal health nutrition", None),
    ("functional nutrition coach", None),
    ("metabolic health coach", None),
],
```

## 작업 순서 (내일 실행할 단계)

### 1. `scripts/discover_2026-04-29.py` 신규
`scripts/discover_2026-04-28.py` 복제 + 변경:
- `DATED_NEW = ROOT / "data" / "2026-04-29"`
- `DATED_OLD_DIRS = [04-24, 04-25, 04-27, 04-28]` (cross-date dedup)
- `RUN_ORDER = ["meditation", "mindset", "fitness", "nutrition"]` (4 카테고리 동시 sweep)
- `KEYWORDS` = 위 4 카테고리 dict 로 교체
- `PAGES_PER_KEYWORD` 카테고리별 다르게:
  ```python
  PAGES_PER_KEYWORD = {"meditation": 3, "mindset": 2, "fitness": 2, "nutrition": 2}
  ```
- 설정 동일: `MIN_SUBS=1000`, `EXCLUDE_COUNTRIES={KR,JP}`
- **신규**: `FRESHNESS_DAYS = 180` (6 개월 freshness 임계값)
- **신규**: `channels.list` 의 `part` 에 `contentDetails` 추가
- **신규**: `is_recently_active(channel, threshold_date)` 헬퍼 — uploads 플레이리스트의 첫 video publishedAt 체크 (`playlistItems.list(playlistId=uploads_id, part="snippet", maxResults=1)`)
- **신규**: discover 로그에 `dropped (stale, last upload <YYYY-MM-DD)` 카운터 출력
- robots.txt + UA 로테이션 + delay_range (CLAUDE.md load-bearing)

### 2. discover 실행
```bash
uv run python scripts/discover_2026-04-29.py
```
산출물 (4 enriched CSV):
- `data/2026-04-29/meditation.csv` + `meditation_enriched.csv`
- `data/2026-04-29/mindset.csv` + `mindset_enriched.csv`
- `data/2026-04-29/fitness.csv` + `fitness_enriched.csv`
- `data/2026-04-29/nutrition.csv` + `nutrition_enriched.csv`

예상 양:
- meditation: +30~50 row
- mindset: +15~25 row
- fitness: +30~40 row
- nutrition: +20~30 row

### 3. `scripts/mapping_2026-04-29.py` 신규 (Claude 가 conversation 안에서 작성)
4 카테고리 row 별로 통합 dict 매핑 — email → {category, niche, segment_original, industry, angle_to_take}.
- discover 결과를 Claude 가 한 row 씩 검토 (description + segment_original + raw_context)
- 명백한 drop (paper-craft, off-topic, fan reaction, MD/clinical) 표시
- 카테고리 boundary 룰 (dominant signal):
  - "yoga teacher" 자칭 → mindset
  - "meditation teacher" / "sleep meditation" 자칭 → meditation
  - 멀티 모달 (yoga + meditation + breathwork) → 첫 명시 키워드 우선

### 4. AppBillChat-tone niche/seg/industry/angle 작성 가이드
- **breathwork instructor (Wim Hof certified 등)**: branded breathwork session player + cohort 운영 + biometric (cold exposure log) integration
- **mindset/stress coach**: weekly group call schedule + cohort progress board + journaling prompt + accountability streak
- **mobility/recovery PT**: protocol library (per body part) + assessment surface + before/after video diff
- **kettlebell/calisthenics specialist**: progression ladder (level 1→8) + form check submit/review + certification track
- **powerlifting / women's strength**: training cycle (block periodization) + PR tracker + plate calculator + meet prep timeline
- **sports nutritionist**: athlete intake form + macro calculator + race-day timing module
- **gut health / fasting / hormonal**: protocol-based program (8주 / 12주) + symptom tracker + lab result intake
- **functional / metabolic nutrition**: assessment quiz + biomarker dashboard + supplement protocol library

### 5. `scripts/apply_mappings_2026-04-29.py` 신규
`scripts/apply_mappings_2026-04-28.py` 복제, 다음 변경:
- `DATED = ROOT / "data" / "2026-04-29"`
- `CATEGORIES = ["meditation", "mindset", "fitness", "nutrition"]`
- `_more` / `_v3` suffix 자동 merge 로직 유지

### 6. `scripts/verify_2026-04-29.py` 신규
`scripts/verify_2026-04-28.py` 복제 + 변경:
- `OLD_DIRS` 확장 (04-24 ~ 04-28 포함)
- `CATS = ["meditation", "mindset", "fitness", "nutrition"]`

### 7. `scripts/build_total.py` 수정
`SOURCES_19COL` 에 4 enriched CSV 추가:
```python
SOURCES_19COL = [
    # ... 기존 6 ...
    DATA / "2026-04-29" / "meditation_enriched.csv",
    DATA / "2026-04-29" / "mindset_enriched.csv",
    DATA / "2026-04-29" / "fitness_enriched.csv",
    DATA / "2026-04-29" / "nutrition_enriched.csv",
]
```

`mapping_2026-04-29.py` 도 import (legacy_mapping 패턴):
```python
mapping_0429_mod = SCRIPTS / "mapping_2026-04-29.py"
mapping_0429 = _load_module(mapping_0429_mod).MAPPING if mapping_0429_mod.exists() else {}

# ... 기존 두 mapping source 와 함께 ...
for src_path, mapping in [
    (SOURCE_LEGACY, legacy_map),
    (SOURCE_MINDFUL, mindful_map),
    (SOURCE_MEDITATION_0428, meditation_0428_map),
    # 04-29 의 4 enriched CSV 는 SOURCES_19COL 로 들어가서 category_split_mapping 으로 처리
    # (or mapping_2026-04-29 가 통합 dict 라면 여기에 추가)
]:
```

설계 선택지 (둘 중 하나):
- **(a)** `mapping_2026-04-29.py` 를 단순 dict (email → category) 로 만들고 `category_split_mapping.py` 와 동급으로 — `niche/angle` 은 `_enriched.csv` 에 이미 있어야 함 → discover/enrich 단계 에서 채워야 함 (현재 discover 는 이 컬럼 비움)
- **(b)** `mapping_2026-04-29.py` 를 통합 dict (email → {category, niche, ...}) 로 만들고 build_total 의 `insert_with_mapping` 호출 — Stage A/B 의 `legacy_mapping` 패턴 따름 (권장)

**(b) 권장** — 일관성 + niche/angle 작성 위치 명확.

### 8. 재실행
```bash
uv run python scripts/build_total.py
uv run python scripts/verify_total.py
uv run pytest -q
```

## 핵심 파일

### 신규 (내일 만듦)
- `scripts/discover_2026-04-29.py` — 4 카테고리 sweep
- `data/2026-04-29/{meditation,mindset,fitness,nutrition}.csv` + `_enriched.csv` — sweep 산출물
- `scripts/mapping_2026-04-29.py` — Claude 작성 (통합 dict, 권장 (b))
- `scripts/apply_mappings_2026-04-29.py` — mapping 적용
- `scripts/verify_2026-04-29.py` — sweep 검증

### 수정 (내일)
- `scripts/build_total.py` — `SOURCES_19COL` 확장 + mapping import 추가

### 변경 없음
- 기존 8 source + Stage A/B 산출물 (`_legacy_enriched.csv`, `_mindful_enriched.csv`, `meditation_2026-04-28` 관련)
- `data/total/` — 4 CSV 모두 row 증가 (regression 없이 ADD-only)

## 워크플로우 (내일 그대로 실행)

```bash
# === Tomorrow (after PT midnight quota reset) ===

# 1. Multi-category discover sweep
uv run python scripts/discover_2026-04-29.py
# → 4 enriched CSV in data/2026-04-29/, ~8,850 quota used

# 2. Claude writes scripts/mapping_2026-04-29.py in conversation
#    (email → {category, niche, segment_original, industry, angle_to_take})

# 3. Apply mappings + verify
uv run python scripts/apply_mappings_2026-04-29.py
uv run python scripts/verify_2026-04-29.py

# 4. Rebuild totals
uv run python scripts/build_total.py
uv run python scripts/verify_total.py
uv run pytest -q
```

## 리스크 / 노트

- **quota 분배의 안전선** — 4 카테고리 동시 sweep 이면 한 카테고리 quotaExceeded 시 그 카테고리만 cleanly stop 후 다음으로. 카테고리 분리 실행 (4 번 따로) 도 옵션 — 더 보수적이지만 시간 비용 증가.
- **cross-category dedup** — 한 채널이 mindset + meditation 둘 다 surface 가능 (예: yoga nidra). discover 단계 dedup 은 (channel_id) 단위라 자동 처리. mapping 단계에서 Claude 가 dominant signal 로 1 카테고리 선택.
- **cross-date dedup** — 04-28 의 21 meditation row 와 중복 가능. discover 의 `DATED_OLD_DIRS` 에 04-28 포함 → 자동 필터.
- **breathwork keyword 의 false positive** — "wim hof" 검색은 supplement 광고, fan reaction 영상도 surface. mapping 단계 검수.
- **fasting keyword 의 의료 영역 침범** — "intermittent fasting coach" 는 medical influencer (MD) 도 surface. AppBillChat fit 약함 → drop 검토.
- **mindset coach 의 broad** — "mindset coach motivation" 은 generic motivational speaker 까지 surface. AppBillChat fit (구체적 method/program 운영) 기준으로 mapping 단계 검수.
- **paper-craft / journal noise** — 위 키워드 list 는 명상/breathwork 명시 키워드만 → 0422/mindful 의 false positive 재발 위험 낮음.

## 검증 체크리스트

1. `data/2026-04-29/{4 카테고리}_enriched.csv` 모두 생성 + 19-col schema (last_upload_at 컬럼 없음 확인 — 필터 전용)
2. JP/KR row 0
3. cross-date 채널 중복 0 (04-24 ~ 04-28 와 비교)
4. country 분포 합리적 (US/IN/GB/CA/AU 위주)
5. mapping 100% 작성 (mindset/meditation/fitness/nutrition/drop 중 하나)
6. niche/angle_to_take 100% 채워짐 (drop 제외)
7. core invariant: 모든 email 의 raw_context literal 매치
8. `data/total/` 4 CSV 모두 row 증가, 기존 row 보존 (regression 없음)
9. **freshness 필터 동작 확인**: discover 로그에 `dropped (stale, last upload <2025-10-28)` 카운터 출력. 통상 surface 채널의 3~5% drop
10. `uv run pytest -q` 25 통과

## 예상 최종 상태 (내일 sweep 후)

| 카테고리 | 현재 | sweep 추가 | 예상 |
|---|---|---|---|
| mindset | 63 | +15~25 | 80~88 |
| meditation | 31 | +30~50 | 60~80 |
| fitness | 168 | +30~40 | 198~208 |
| nutrition | 72 | +20~30 | 92~102 |
| **total** | **334** | **+95~145** | **~430~480** |

## 보류 / 차후 사이클

- **D 옵션** (sound healing / functional medicine / breathwork retreat) — 이번 달 제외. AppBillChat fit 가 method-teaching coach 로 좁혀진다면 다음 사이클 (2026-05-XX) 에 별도 카테고리 또는 mindset/meditation 의 sub-niche 로 재고.
- **0-quota 재크롤** (218 missing-website row Playwright 재크롤) — 신규 sweep 후 빈약 row 잔존 시 추가 작업.
- **`influencer_enriched.csv` 의 비-wellness vertical** (twitch 196 / Lifestyle 88 / finance 36 / Music Prod 31 / Pet Trainer 14 = 365 row) — 4 카테고리 무관, 별도 outreach 풀로 활용 가능하나 이번 작업 범위 외.
