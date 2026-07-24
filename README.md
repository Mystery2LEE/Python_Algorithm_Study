# 🏔️ BASE CAMP — Python Algorithm Study

Python 알고리즘 스터디 공통 레포. **push하면 Notion 문제 풀이 기록 DB에 자동으로 기록됩니다.**

대원: 이정현(리드) · 배소연 · 채서연 · 양대건 · 박정수

---

## 📁 폴더 규칙

```
week01/
  이정현/
    BOJ_1000_A와B.py
    SWEA_1954_달팽이숫자.py
  배소연/
    BOJ_1000_A와B.py
week02/
  ...
```

**파일명:** `{플랫폼}_{문제번호}_{문제이름}.py`

| 접두사 | 플랫폼 |
|---|---|
| `SWEA_` | SWEA |
| `PGS_` | 프로그래머스 |
| `BOJ_` | 백준 |
| `LC_` | LeetCode |

경로에서 **주차 / 풀이자 / 플랫폼 / 문제명**이 자동으로 뽑힙니다. 폴더 이름은 Notion DB의 `풀이자` 옵션과 **정확히 같아야** 매칭됩니다.

---

## 📝 파일 상단 주석 규칙

파일 맨 위 docstring에 아래 항목을 쓰면 Notion 속성이 같이 채워집니다. 전부 선택 사항이고, 없으면 그냥 비워진 채로 기록됩니다.

```python
"""
링크: https://www.acmicpc.net/problem/1000
난이도: Lv1
유형: 구현, 수학
시간복잡도: O(1)
소요시간: 35분
복습필요: Y
회고: 이분탐색 경계 조건에서 두 번 틀림. lo/hi 갱신 방향 헷갈림.
"""
```

| 항목 | Notion 속성 | 형식 |
|---|---|---|
| `링크` | 문제 링크 | URL |
| `난이도` | 난이도 | `Lv1` / `Lv2` / `Lv3` / `Lv4+` |
| `유형` | 유형 | 쉼표 구분 (구현, 완전탐색, DFS/BFS, 이분탐색, 그리디, DP, 그래프, 자료구조, 정렬, 문자열, 수학) |
| `시간복잡도` | 시간복잡도 | 자유 텍스트 |
| `소요시간` | 소요 시간(분) | 숫자 (단위 붙여도 됨) |
| `복습필요` | 복습 필요 | `Y` / `N` |
| `회고` | 한 줄 회고 | 자유 텍스트 |

> 💡 **`복습필요: Y`** 로 두면 Notion의 **🔁 다시 풀 문제** 뷰에 자동으로 모입니다. 모임 전엔 그 뷰만 보면 됩니다.

`상태`는 완료, `풀이일`은 push한 날짜, `코드 링크`는 GitHub 파일 링크로 자동 입력됩니다.
같은 사람이 같은 문제를 다시 push하면 새 행이 생기지 않고 **기존 행이 갱신**됩니다.

---

## ⚙️ 최초 1회 세팅 (리드 클라이머만)

### 1. Notion 인테그레이션 만들기

1. https://www.notion.so/my-integrations → **New integration**
2. 이름은 아무거나 (예: `algo-study-bot`), 워크스페이스 선택 후 생성
3. **Internal Integration Secret** 복사 (`ntn_...` 로 시작)

### 2. DB에 인테그레이션 초대

Notion에서 **✅ 문제 풀이 기록** DB 페이지 열기 → 우측 상단 `···` → **연결** → 방금 만든 인테그레이션 추가

> ⚠️ 이거 안 하면 토큰이 있어도 404가 납니다.

### 3. DB ID 확인

DB를 전체 페이지로 열고 주소창에서 복사:

```
https://www.notion.so/<workspace>/784ab227e2784b7093f61c7f769304be?v=...
                                  └────────── 이 32자리가 DB ID ──────────┘
```

### 4. GitHub Secrets 등록

레포 → **Settings** → **Secrets and variables** → **Actions** → **New repository secret**

| 이름 | 값 |
|---|---|
| `NOTION_TOKEN` | 1번에서 복사한 `ntn_...` |
| `NOTION_DATABASE_ID` | 3번에서 복사한 32자리 |

### 5. 끝

`week01/이정현/BOJ_1000_A와B.py` 같은 파일을 push하면 Actions 탭에서 실행되고, Notion에 행이 생깁니다.
실패하면 Actions 로그에 응답 본문이 그대로 찍히니 거기서 원인 확인하세요.

---

## 🔧 로컬에서 테스트

```bash
pip install requests
export NOTION_TOKEN="ntn_..."
export NOTION_DATABASE_ID="784ab227..."
export REPO="Mystery2LEE/Python_Algorithm_Study"
export SHA="main"

python scripts/notion_sync.py week01/이정현/BOJ_1000_A와B.py
```

---

## 🌱 브랜치 전략

기본은 `main` 직접 push로 충분합니다. 코드 리뷰를 PR로 돌리고 싶어지면 그때 브랜치를 파세요.
자동 기록은 `main` / `master` push 기준으로 동작합니다.
