# 🏔️ BASE CAMP — Python Algorithm Study

Python 알고리즘 스터디 공통 레포입니다.
**GitHub에 push하면 Notion `문제 풀이 기록` DB에 자동으로 기록됩니다.**

대원: 이정현(리드) · 배소연 · 채서연 · 김도성 · 박정수
플랫폼: SWEA (난이도 D1~D5)

---

## 🚀 코드 올리는 법 (3단계)

### 1. 파일을 규칙대로 만든다

```
week01/이정현/SWEA_1954_달팽이숫자.py
└주차┘ └내이름┘ └플랫폼_번호_문제이름┘
```

- **week01** → Notion `주차` = 1주차
- **내 이름 폴더** → Notion `풀이자`. 아래 이름과 **정확히** 일치해야 함
  `이정현` `배소연` `채서연` `김도성` `박정수` (띄어쓰기 금지)
- **파일명 접두사** → `SWEA_` `PGS_` `BOJ_` `LC_`

### 2. (선택) 파일 맨 위에 주석을 적는다

```python
"""
링크: https://swexpertacademy.com/...
난이도: D3
유형: DFS/BFS
시간복잡도: O(N*M)
소요시간: 35분
복습필요: Y
회고: visited 체크 타이밍에서 두 번 틀림
"""

import sys
...
```

전부 선택 사항이고, 없어도 기록은 됩니다.

### 3. push 한다

```bash
git pull                          # 먼저 최신 받기
git add .
git commit -m "week01 SWEA 1954 풀이"
git push
```

30초쯤 뒤 Notion에 카드가 생깁니다. 끝.

---

## 📝 주석 항목 표

| 항목 | Notion 속성 | 형식 |
|---|---|---|
| `링크` | 문제 링크 | URL |
| `난이도` | 난이도 | **D1 ~ D6+** (SWEA 기준) |
| `유형` | 유형 | 쉼표 구분 (아래 목록) |
| `시간복잡도` | 시간복잡도 | O(N) 등 자유 |
| `소요시간` | 소요 시간(분) | 숫자 ("35분" 가능) |
| `복습필요` | 복습 필요 | Y / N |
| `회고` | 한 줄 회고 | 막힌 지점 한 문장 |
| `상태` | 상태 | 생략=완료, `시도중`=진행 중 |

**유형 목록:** 구현 · 완전탐색 · DFS/BFS · 이분탐색 · 그리디 · DP · 그래프 · 자료구조 · 정렬 · 문자열 · 수학

---

## 🤖 자동으로 처리되는 것

push만 하면 아래는 알아서 채워집니다.

| 속성 | 자동 처리 |
|---|---|
| 상태 | **완료** 로 표시 (주석에 `상태: 시도중` 쓰면 진행 중) |
| 풀이일 | push한 날짜 |
| 코드 링크 | GitHub 파일 주소 |
| **복습 필요** | 난이도 **D4 이상이면 자동 체크** ⭐ |

> ⭐ **D4 이상은 복습필요를 안 적어도 자동으로 `🔁 다시 풀 문제`에 올라갑니다.**
> 어려운 문제는 무조건 다시 볼 가치가 있으니까요. D3 이하는 `복습필요: Y`를 직접 적어야 올라갑니다.

**같은 사람이 같은 문제를 다시 push하면** 새 행이 생기지 않고 기존 행이 갱신됩니다.
코드를 개선해서 다시 올려도 중복이 안 쌓입니다.

---

## 🔍 잘 됐는지 확인

레포 **Actions** 탭 → 초록 체크면 성공.
실패(빨강)하면 실행 기록 → `Sync to Notion` 단계를 펼치면 원인이 한글로 나옵니다.

| 증상 | 원인 |
|---|---|
| 카드가 안 생김 | 경로가 `week00/이름/` 형식인지 (week 소문자) |
| 풀이자 칸이 빔 | 폴더 이름 오타 |
| 플랫폼이 "기타" | 접두사 뒤 언더바 누락 |
| 난이도 안 채워짐 | `난이도: D3` 처럼 콜론 필요 |

---

## 📂 폴더 구조 예시

```
Python_Algorithm_Study/
├── week01/
│   ├── 이정현/
│   │   ├── SWEA_1954_달팽이숫자.py
│   │   └── SWEA_1208_Flatten.py
│   └── 배소연/
│       └── SWEA_1954_달팽이숫자.py
├── week02/
│   └── ...
├── scripts/          # 자동화 스크립트 (건드리지 마세요)
└── .github/          # GitHub Actions (건드리지 마세요)
```

---

## ⚙️ 관리자용 (리드만)

자동 기록은 GitHub Actions + Notion API로 동작합니다.
Secrets 2개(`NOTION_TOKEN`, `NOTION_DATABASE_ID`)가 레포 Settings에 등록되어 있어야 합니다.
문제가 생기면 Actions 로그 맨 위에 접근 가능한 DB 목록과 워크스페이스가 출력됩니다.

로컬 테스트:
```bash
pip install requests
export NOTION_TOKEN="ntn_..."
export NOTION_DATABASE_ID="53ec05749386838f8aa8817ff95aaaf6"
export REPO="Mystery2LEE/Python_Algorithm_Study"
export SHA="main"
python scripts/notion_sync.py --diagnose         # 접근 가능한 DB 확인
python scripts/notion_sync.py week01/이정현/SWEA_1954_달팽이숫자.py
```

---

## 📊 주간 리포트 (자동)

매주 **일요일 밤 22:00(KST)**, 지난 한 주(월~일)의 활동이 자동 집계되어
Notion **📊 주간 리포트** DB에 한 페이지씩 쌓입니다. 모임 준비 자료가 저절로 만들어집니다.

집계 내용: 총 제출 수 · 대원별 제출 수 · 유형 분포 · 복습 필요 개수 · **미제출 인원**

수동 실행: Actions 탭 → **Weekly Report** → Run workflow

### 관리자용 세팅 (1회)

`weekly_report.py`는 리포트 DB ID가 필요합니다. GitHub Secret 하나를 추가하세요.

| 이름 | 값 |
|---|---|
| `NOTION_REPORT_DB_ID` | `326d6949ba6f4885ad70f746b4b17d7e` |

(없어도 이름으로 자동 탐색하지만, 명시해두면 더 안정적입니다.)
