"""
푸시된 풀이 파일 하나를 읽어 Notion '문제 풀이 기록' DB에 기록한다.

경로 규칙:  week01/이정현/BOJ_1000_A와B.py
            └주차┘ └풀이자┘ └플랫폼┘└번호┘└문제명┘

파일 상단 docstring에서 메타데이터를 읽는다. 없으면 비워둔 채로 기록.

사용:  python scripts/notion_sync.py week01/이정현/BOJ_1000_A와B.py
"""

import os
import re
import sys
from datetime import date

import requests

NOTION_TOKEN = os.environ["NOTION_TOKEN"]
DATABASE_ID = os.environ["NOTION_DATABASE_ID"]
REPO = os.environ.get("REPO", "")
SHA = os.environ.get("SHA", "main")

API = "https://api.notion.com/v1"
HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json",
}

PLATFORM_MAP = {
    "SWEA": "SWEA",
    "PGS": "프로그래머스",
    "PROGRAMMERS": "프로그래머스",
    "BOJ": "백준",
    "LC": "LeetCode",
    "LEETCODE": "LeetCode",
}

VALID_DIFFICULTY = {"Lv1", "Lv2", "Lv3", "Lv4+"}
VALID_TYPES = {
    "구현", "완전탐색", "DFS/BFS", "이분탐색", "그리디",
    "DP", "그래프", "자료구조", "정렬", "문자열", "수학",
}


# ---------------------------------------------------------------- 파싱

def parse_path(path):
    """week01/이정현/BOJ_1000_A와B.py -> dict"""
    parts = path.split("/")
    if len(parts) < 3:
        raise ValueError(f"경로 규칙에 맞지 않음: {path}")

    week_dir, solver, filename = parts[0], parts[1], parts[-1]

    m = re.match(r"week(\d+)", week_dir, re.IGNORECASE)
    week = f"{int(m.group(1))}주차" if m else None

    stem = re.sub(r"\.py$", "", filename)
    bits = stem.split("_", 2)

    platform = PLATFORM_MAP.get(bits[0].upper(), "기타") if bits else "기타"
    number = bits[1] if len(bits) > 1 else ""
    title = bits[2].replace("_", " ") if len(bits) > 2 else stem

    display = f"[{platform}] {number} {title}".strip()
    return {
        "주차": week,
        "풀이자": solver,
        "플랫폼": platform,
        "문제명": display,
    }


def parse_header(path):
    """파일 상단 docstring에서 메타데이터를 뽑는다."""
    with open(path, encoding="utf-8") as fp:
        text = fp.read(4000)

    m = re.search(r'"""(.*?)"""', text, re.DOTALL)
    if not m:
        return {}

    meta = {}
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        key = key.strip().replace(" ", "")
        value = value.strip()
        if value:
            meta[key] = value
    return meta


# ---------------------------------------------------------------- 속성 조립

def build_properties(path, info, meta):
    code_url = f"https://github.com/{REPO}/blob/{SHA}/{path}" if REPO else None

    props = {
        "문제명": {"title": [{"text": {"content": info["문제명"]}}]},
        "플랫폼": {"select": {"name": info["플랫폼"]}},
        "풀이일": {"date": {"start": date.today().isoformat()}},
        "상태": {"status": {"name": "완료"}},
    }

    if info["주차"]:
        props["주차"] = {"select": {"name": info["주차"]}}
    if info["풀이자"]:
        props["풀이자"] = {"select": {"name": info["풀이자"]}}
    if code_url:
        props["코드 링크"] = {"url": code_url}

    if link := meta.get("링크"):
        props["문제 링크"] = {"url": link}

    if (lv := meta.get("난이도")) in VALID_DIFFICULTY:
        props["난이도"] = {"select": {"name": lv}}

    if raw_types := meta.get("유형"):
        tags = [t.strip() for t in re.split(r"[,/·]| ", raw_types) if t.strip()]
        tags = [t for t in tags if t in VALID_TYPES]
        # 'DFS/BFS'는 위 split에서 쪼개지므로 별도 복원
        if "DFS" in raw_types or "BFS" in raw_types:
            tags.append("DFS/BFS")
        if tags:
            props["유형"] = {"multi_select": [{"name": t} for t in dict.fromkeys(tags)]}

    if big_o := meta.get("시간복잡도"):
        props["시간복잡도"] = {"rich_text": [{"text": {"content": big_o}}]}

    if retro := meta.get("회고"):
        props["한 줄 회고"] = {"rich_text": [{"text": {"content": retro[:1900]}}]}

    if spent := meta.get("소요시간"):
        digits = re.sub(r"\D", "", spent)
        if digits:
            props["소요 시간(분)"] = {"number": int(digits)}

    if review := meta.get("복습필요"):
        props["복습 필요"] = {"checkbox": review.upper() in {"Y", "YES", "O", "TRUE", "예"}}

    return props


# ---------------------------------------------------------------- Notion 호출

def find_existing(title, solver):
    """같은 사람이 같은 문제를 이미 올렸는지 확인 (중복 방지)."""
    payload = {
        "filter": {
            "and": [
                {"property": "문제명", "title": {"equals": title}},
                {"property": "풀이자", "select": {"equals": solver}},
            ]
        },
        "page_size": 1,
    }
    res = requests.post(
        f"{API}/databases/{DATABASE_ID}/query", headers=HEADERS, json=payload, timeout=30
    )
    res.raise_for_status()
    results = res.json().get("results", [])
    return results[0]["id"] if results else None


def upsert(props, title, solver):
    page_id = find_existing(title, solver)

    if page_id:
        res = requests.patch(
            f"{API}/pages/{page_id}", headers=HEADERS, json={"properties": props}, timeout=30
        )
        action = "갱신"
    else:
        body = {"parent": {"database_id": DATABASE_ID}, "properties": props}
        res = requests.post(f"{API}/pages", headers=HEADERS, json=body, timeout=30)
        action = "생성"

    if res.status_code >= 400:
        print(f"  ✗ 실패 ({res.status_code}): {res.text[:300]}")
        res.raise_for_status()

    print(f"  ✓ {action} 완료")


# ---------------------------------------------------------------- 진입점

def main():
    if len(sys.argv) < 2:
        print("파일 경로를 인자로 넘겨주세요.")
        sys.exit(1)

    path = sys.argv[1]
    print(f"→ {path}")

    try:
        info = parse_path(path)
    except ValueError as exc:
        print(f"  · 건너뜀: {exc}")
        return

    meta = parse_header(path)
    props = build_properties(path, info, meta)
    upsert(props, info["문제명"], info["풀이자"])


if __name__ == "__main__":
    main()
