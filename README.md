# Influencer Finder

인플루언서 이메일 마케팅을 위한 **실제 연락 이메일** 수집 CLI.
YouTube / Instagram / TikTok 공개 바이오와 링크 인 바이오 페이지에서
문자열을 그대로 추출해 DB에 적재합니다.

## 왜 이 프로젝트인가

일반 LLM(Claude.ai, ChatGPT, Gemini)에 "인플루언서 이메일 알려줘"라고 물으면
**그럴듯한 이메일을 지어냅니다**. 실제 발송하면 대부분 반송됩니다.

이 도구는 다릅니다:

- **AI는 이메일을 만들지 않습니다.** 추출·파싱·검증만 합니다.
- DB에 저장되는 모든 이메일은 다음 정보를 함께 기록합니다:
  - `source_url` — 어떤 페이지 URL에서 추출했는지
  - `raw_context` — 이메일이 등장한 주변 100자 원문
  - `extraction_method` — `regex_direct` / `mailto_href` / `deobfuscated`
- 따라서 **사용자가 수동으로 출처를 검증**할 수 있습니다.

## 동작 원리

```
┌──────────────────────────────────────────────────────────────────────┐
│  1. YouTube Data API v3 (무료·공식)                                  │
│     키워드로 채널 검색 → description + 커스텀 URL + 구독자 수 수집    │
└──────────────────────────────────────────────────────────────────────┘
                                  ↓
┌──────────────────────────────────────────────────────────────────────┐
│  2. 바이오에서 이메일 + 외부 링크 정규식 추출                         │
│     - 표준 email, (at)/(dot) 난독화, 한국어 "골뱅이/점/엣/닷"         │
│     - instagram.com/<h>, tiktok.com/@<h>, linktr.ee/<s>, 개인 도메인  │
└──────────────────────────────────────────────────────────────────────┘
                                  ↓
┌──────────────────────────────────────────────────────────────────────┐
│  3. 링크 인 바이오 + 개인 사이트 크롤 (Playwright, headless)          │
│     - 요청 간 2-5초 랜덤 딜레이, UA 회전, robots.txt 존중             │
│     - 페이지 텍스트 + mailto: href 모두 수집                          │
└──────────────────────────────────────────────────────────────────────┘
                                  ↓
┌──────────────────────────────────────────────────────────────────────┐
│  4. 검증: Syntax → MX 레코드 → Role-based 태깅                        │
│     (SMTP 직접 검증은 IP 블랙리스트 위험으로 제외)                    │
└──────────────────────────────────────────────────────────────────────┘
                                  ↓
┌──────────────────────────────────────────────────────────────────────┐
│  5. CSV 내보내기 (Mailchimp/Brevo/ConvertKit 호환)                    │
└──────────────────────────────────────────────────────────────────────┘
```

## 설치

Python 3.11+ 및 [uv](https://github.com/astral-sh/uv)를 사용합니다.

```bash
git clone <your-repo-or-copy-folder>
cd influencer

uv venv --python 3.11
uv pip install -e .
uv run playwright install chromium
```

## YouTube API 키 발급 (무료)

1. [Google Cloud Console](https://console.cloud.google.com/) 접속
2. 새 프로젝트 생성 → **API 및 서비스** → **라이브러리**
3. **YouTube Data API v3** 검색 후 활성화
4. **사용자 인증 정보** → **API 키 만들기**
5. `.env.example`을 `.env`로 복사 후 키 입력

```bash
cp .env.example .env
# .env 파일 열어서 YOUTUBE_API_KEY=AIza... 입력
```

일일 무료 쿼터 10,000 units → 채널 50~100개 검색 가능 (소규모 타겟에 충분).

## 사용법

### 단계별 실행

```bash
# 1. DB 초기화
uv run influencer init

# 2. YouTube에서 키워드로 채널 탐색
uv run influencer discover youtube --keyword "한국 뷰티 리뷰" --max 50 --min-subs 10000

# 3. 바이오에서 이메일 + 외부 링크 추출
uv run influencer extract

# 4. 외부 링크(linktr.ee, 개인 사이트) 크롤
uv run influencer crawl-links

# 5. 이메일 검증 (syntax + MX)
uv run influencer validate

# 6. 진행 상황 확인
uv run influencer stats

# 7. CSV로 내보내기 (실제 발송 가능한 개인 이메일만)
uv run influencer export --filter "has_mx=1 AND is_role_based=0" --out leads.csv
```

### 전체 파이프라인 한 번에

```bash
uv run influencer run-all \
  --keyword "k-beauty skincare" \
  --max 50 \
  --min-subs 10000 \
  --out leads.csv
```

### config.yaml로 니치 관리

`config.yaml`에서 니치별 키워드·필터를 정의할 수 있습니다. 크롤 딜레이·User-Agent
회전·contact 경로 목록도 여기서 조정됩니다.

## ⚠️ 환각 방지 검증 (반드시 수행)

AI 결과물이 실제인지 의심하는 게 이 도구의 존재 이유입니다. **첫 실행 후 반드시**:

```bash
uv run influencer export --out test_leads.csv
```

1. `test_leads.csv`에서 무작위 5개 행 샘플링.
2. 각 행의 `source_url`을 브라우저로 여세요.
3. `raw_context` 필드의 문자열이 그 페이지에 **그대로 존재**하는지 Ctrl+F로 확인.
4. 한 건이라도 원본에 없으면 추출 로직 버그 → GitHub issue로 제보하세요.

**예상 수확률 (20명 샘플 기준)**:

| 단계 | 이메일 확보 |
|---|---|
| YouTube 채널 설명 직접 기재 | 8~12건 (40~60%) |
| 링크 인 바이오 / 개인 사이트 크롤 | 추가 3~5건 |
| MX 레코드 통과율 | ~90% |
| 최종 발송 가능 | 12~17건 |

## 테스트

```bash
uv run pytest
```

14개의 유닛 테스트가 이메일 추출 규칙을 검증합니다 (한국어 난독화 패턴 포함).

## 법적 · 윤리적 체크리스트

수집 자체는 공개 데이터지만 **발송 시점**에 반드시 준수:

- **한국 정보통신망법**: 광고 이메일은 원칙적으로 opt-in 필요. 단, 채널 설명에
  `business inquiries` / `collab` / `brand partnerships` 명시된 이메일은 B2B
  비즈니스 문의로 간주되어 cold outreach 정당성이 상대적으로 강함.
  → `raw_context`에서 해당 맥락을 확인한 뒤 발송 여부 판단하세요.
- **GDPR** (EU): 정당한 이익 근거 명시 + 본문 내 즉시 opt-out.
- **CAN-SPAM** (미국): 실제 발신자 주소 + 정직한 제목 + opt-out 링크 + 물리 주소.
- **플랫폼 ToS**: Instagram/TikTok 직접 스크레이핑은 ToS 회색지대. 본 도구는
  기본 경로로 **YouTube 진입 + 바이오 링크 크롤**만 사용하여 위험을 최소화합니다.

## 구조

```
src/influencer_finder/
├── cli.py                  # typer CLI 엔트리포인트
├── pipeline.py             # 단계별 오케스트레이션
├── db.py                   # SQLite 스키마·쿼리
├── models.py               # Profile / Email / Source 모델
├── export.py               # CSV 내보내기
├── discovery/youtube.py    # YouTube Data API v3
├── extractors/
│   ├── email_regex.py      # 정규식 + 난독화 해제
│   ├── bio.py              # 외부 링크 감지
│   └── website.py          # Playwright 크롤러
└── validators/
    ├── syntax.py           # email-validator
    ├── mx.py               # dnspython
    └── role.py             # role-based 판별
```

## 범위 밖

- SMTP 직접 검증 (IP 블랙리스트 위험 → Hunter.io 유료로 전환 권장)
- 발송 시스템 (Mailchimp/Brevo 연동)
- 답장 추적 + CRM
- 가짜 팔로워 탐지
- 이미지 내 이메일 OCR
- 순수 IG/TikTok-only 인플루언서 해시태그 기반 seed discovery
