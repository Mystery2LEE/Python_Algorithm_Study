"""
푸시된 풀이 파일을 읽어 Notion '문제 풀이 기록' DB에 기록한다.

경로 규칙:  week01/이정현/BOJ_1000_A와B.py
            └주차┘ └풀이자┘ └플랫폼┘└번호┘└문제명┘

파일 상단 docstring에서 메타데이터를 읽는다. 없으면 비워둔 채로 기록.

DB는 NOTION_DATABASE_ID로 지정하거나, 비워두면 이름으로 자동 탐색한다.

사용:
    python scripts/notion_sync.py --from-file changed_files.txt
    python scripts/notion_sync.py --diagnose        # 접근 가능한 DB 목록 출력
"""

import os
import re
import sys
from datetime import date

import requests

TOKEN = os.environ.get("NOTION_TOKEN", "").strip()
RAW_DB_ID = os.environ.get("NOTION_DATABASE_ID", "").strip().replace("-", "")
DB_NAME_HINT = os.environ.get("NOTION_DATABASE_NAME", "문제 풀이 기록").strip()
REPO = os.environ.get("REPO", "")
SHA = os.environ.get("SHA", "main")

API = "https://api.notion.com/v1"
V_OLD = "2022-06-28"   # databases 엔드포인트
V_NEW = "2025-09-03"   # data_sources 엔드포인트

if not TOKEN:
    print("=" * 64)
    print("❌ GitHub Secret NOTION_TOKEN 이 비어 있습니다.")
    print("   레포 → Settings → Secrets and variables → Actions")
    print("=" * 64)
    sys.exit(1)


def call(method, path, version=V_OLD, **kwargs):
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Notion-Version": version,
        "Content-Type": "application/json",
    }
    return requests.request(method, f"{API}{path}", headers=headers, timeout=30, **kwargs)


# ---------------------------------------------------------------- DB 탐색

def whoami():
    """토큰이 어느 워크스페이스 / 어떤 인테그레이션의 것인지 출력."""
    res = call("GET", "/users/me", V_OLD)
    if not res.ok:
        print(f"❌ 토큰 확인 실패 ({res.status_code})")
        print(f"   {res.text[:300]}")
        if res.status_code == 401:
            print("   → NOTION_TOKEN 값이 잘못되었습니다. 복사할 때 공백이 섞였는지 확인하세요.")
        return None

    me = res.json()
    bot = me.get("bot", {})
    ws = bot.get("workspace_name") or "(알 수 없음)"
    name = me.get("name") or "(이름 없음)"

    print("=" * 64)
    print(f"🔑 토큰 주인   : {name}")
    print(f"🏢 워크스페이스 : {ws}")
    print("=" * 64)
    return ws


def list_accessible():
    """인테그레이션이 접근 가능한 DB / 데이터 소스를 모두 나열한다."""
    found = []

    res = call("POST", "/search", V_OLD,
               json={"filter": {"value": "database", "property": "object"}, "page_size": 100})
    if res.ok:
        for obj in res.json().get("results", []):
            title = "".join(t.get("plain_text", "") for t in obj.get("title", [])) or "(제목 없음)"
            found.append(("database", obj["id"].replace("-", ""), title))

    res = call("POST", "/search", V_NEW,
               json={"filter": {"value": "data_source", "property": "object"}, "page_size": 100})
    if res.ok:
        for obj in res.json().get("results", []):
            title = "".join(t.get("plain_text", "") for t in obj.get("title", [])) or "(제목 없음)"
            found.append(("data_source", obj["id"].replace("-", ""), title))

    return found


def list_pages():
    """접근 가능한 일반 페이지도 확인 (연결 자체가 붙었는지 판단용)."""
    res = call("POST", "/search", V_OLD,
               json={"filter": {"value": "page", "property": "object"}, "page_size": 20})
    if not res.ok:
        return []
    out = []
    for obj in res.json().get("results", []):
        props = obj.get("properties", {})
        title = "(제목 없음)"
        for prop in props.values():
            if prop.get("type") == "title":
                title = "".join(t.get("plain_text", "") for t in prop.get("title", [])) or title
                break
        out.append(title)
    return out


def print_accessible(found):
    print("-" * 64)
    if not found:
        print("접근 가능한 DB: 없음")
        pages = list_pages()
        if pages:
            print("다만 아래 페이지에는 접근됩니다:")
            for title in pages:
                print(f"  · {title}")
            print("→ 페이지 연결은 되어 있으나 DB가 그 하위에 없습니다.")
            print("  DB가 들어있는 상위 페이지에 연결을 추가하세요.")
        else:
            print("접근 가능한 페이지도 없음 → 연결이 전혀 안 붙어 있습니다.")
            print("→ 위에 표시된 워크스페이스에서 BASE CAMP 페이지를 열고")
            print("  ··· → 연결 → 연결 추가 → 인테그레이션 선택")
    else:
        print("접근 가능한 대상:")
        for kind, oid, title in found:
            print(f"  [{kind:11}] {oid}  {title}")
    print("-" * 64)


def probe(kind, oid):
    """해당 대상에 실제로 쿼리가 되는지 확인."""
    if kind == "data_source":
        res = call("POST", f"/data_sources/{oid}/query", V_NEW, json={"page_size": 1})
    else:
        res = call("POST", f"/databases/{oid}/query", V_OLD, json={"page_size": 1})
    return res.ok


def resolve_target():
    """(kind, id) 반환. 실패 시 진단 출력 후 종료."""
    # 1) 지정된 ID를 두 방식으로 시도
    if RAW_DB_ID:
        for kind in ("data_source", "database"):
            if probe(kind, RAW_DB_ID):
                print(f"✔ 대상 확인: {kind} / {RAW_DB_ID}")
                return kind, RAW_DB_ID
        print(f"⚠ NOTION_DATABASE_ID({RAW_DB_ID})로 조회할 수 없습니다. 이름으로 재탐색합니다.")

    # 2) 이름으로 자동 탐색
    found = list_accessible()
    for kind, oid, title in found:
        if DB_NAME_HINT in title and probe(kind, oid):
            print(f"✔ 이름으로 찾음: {kind} / {oid}  ({title})")
            print(f"  → NOTION_DATABASE_ID 를 {oid} 로 바꿔두면 다음부터 빨라집니다.")
            return kind, oid

    print("❌ 사용할 수 있는 DB를 찾지 못했습니다.")
    whoami()
    print_accessible(found)
    sys.exit(1)


# ---------------------------------------------------------------- 파싱

PLATFORM_MAP = {
    "SWEA": "SWEA", "PGS": "프로그래머스", "PROGRAMMERS": "프로그래머스",
    "BOJ": "백준", "LC": "LeetCode", "LEETCODE": "LeetCode",
}
VALID_DIFFICULTY = {"D1", "D2", "D3", "D4", "D5", "D6+"}
# D4 이상이면 자동으로 복습 대상으로 표시 (어려운 문제는 다시 풀 가치가 있음)
AUTO_REVIEW_DIFFICULTY = {"D4", "D5", "D6+"}
VALID_TYPES = {"구현", "완전탐색", "DFS/BFS", "이분탐색", "그리디",
               "DP", "그래프", "자료구조", "정렬", "문자열", "수학"}


def unquote_git_path(path):
    """git이 비ASCII 경로를 "week01/\\354\\235\\264..." 로 감싸 출력하는 경우를 되돌린다."""
    path = path.strip()
    if len(path) >= 2 and path.startswith('"') and path.endswith('"'):
        inner = path[1:-1]
        try:
            return bytes(inner, "utf-8").decode("unicode_escape").encode("latin-1").decode("utf-8")
        except (UnicodeDecodeError, UnicodeEncodeError):
            return inner
    return path


def parse_path(path):
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

    return {
        "주차": week,
        "풀이자": solver,
        "플랫폼": platform,
        "문제명": f"[{platform}] {number} {title}".strip(),
    }


def parse_header(path):
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
        key, value = key.strip().replace(" ", ""), value.strip()
        if value:
            meta[key] = value
    return meta


def normalize_difficulty(raw):
    """'d3', 'Lv3', 'D3' 등을 표준 'D3'로. SWEA D체계로 통일."""
    if not raw:
        return None
    s = raw.strip().upper().replace(" ", "")
    # Lv 표기가 들어오면 D로 매핑 (과거 습관 방어)
    s = s.replace("LV", "D").replace("LEVEL", "D")
    if s in VALID_DIFFICULTY:
        return s
    # 'D4+' 같은 변형 흡수
    if s in {"D6", "D7", "D8", "D9", "D6+", "D7+"}:
        return "D6+"
    return None


def build_properties(path, info, meta):
    # 상태: 기본은 완료. 주석에 '상태: 시도중' 이면 진행 중으로.
    status = "완료"
    if (st := meta.get("상태", "")).replace(" ", "") in {"시도중", "진행중", "풀이중", "WIP"}:
        status = "진행 중"

    props = {
        "문제명": {"title": [{"text": {"content": info["문제명"]}}]},
        "플랫폼": {"select": {"name": info["플랫폼"]}},
        "풀이일": {"date": {"start": date.today().isoformat()}},
        "상태": {"status": {"name": status}},
    }
    if info["주차"]:
        props["주차"] = {"select": {"name": info["주차"]}}
    if info["풀이자"]:
        props["풀이자"] = {"select": {"name": info["풀이자"]}}
    if REPO:
        props["코드 링크"] = {"url": f"https://github.com/{REPO}/blob/{SHA}/{path}"}
    if link := meta.get("링크"):
        props["문제 링크"] = {"url": link}

    difficulty = normalize_difficulty(meta.get("난이도"))
    if difficulty:
        props["난이도"] = {"select": {"name": difficulty}}

    if raw := meta.get("유형"):
        tags = [t.strip() for t in re.split(r"[,·]|\s", raw) if t.strip()]
        tags = [t for t in tags if t in VALID_TYPES]
        if "DFS" in raw or "BFS" in raw:
            tags.append("DFS/BFS")
        if tags:
            props["유형"] = {"multi_select": [{"name": t} for t in dict.fromkeys(tags)]}
    if big_o := meta.get("시간복잡도"):
        props["시간복잡도"] = {"rich_text": [{"text": {"content": big_o}}]}
    if retro := meta.get("회고"):
        props["한 줄 회고"] = {"rich_text": [{"text": {"content": retro[:1900]}}]}
    if spent := meta.get("소요시간"):
        if digits := re.sub(r"\D", "", spent):
            props["소요 시간(분)"] = {"number": int(digits)}

    # 복습 필요: ① 명시적으로 Y 적었거나  ② 난이도가 D4 이상이면 자동 체크
    review_explicit = meta.get("복습필요", "").upper() in {"Y", "YES", "O", "TRUE", "예"}
    review_auto = difficulty in AUTO_REVIEW_DIFFICULTY
    if "복습필요" in meta or review_auto:
        props["복습 필요"] = {"checkbox": review_explicit or review_auto}

    return props


# ---------------------------------------------------------------- 기록

def explain(res):
    print(f"    {res.text[:400]}")
    if res.status_code == 401:
        print("    → NOTION_TOKEN 오류. 앞뒤 공백이나 워크스페이스를 확인하세요.")
    elif res.status_code == 404:
        print("    → 인테그레이션이 해당 DB에 연결되어 있지 않습니다.")
    elif res.status_code == 400:
        print("    → 속성 이름/타입 불일치. 위 message를 확인하세요.")


def upsert(kind, oid, props, title, solver):
    query_filter = {
        "and": [
            {"property": "문제명", "title": {"equals": title}},
            {"property": "풀이자", "select": {"equals": solver}},
        ]
    }
    if kind == "data_source":
        res = call("POST", f"/data_sources/{oid}/query", V_NEW,
                   json={"filter": query_filter, "page_size": 1})
        parent = {"type": "data_source_id", "data_source_id": oid}
        version = V_NEW
    else:
        res = call("POST", f"/databases/{oid}/query", V_OLD,
                   json={"filter": query_filter, "page_size": 1})
        parent = {"database_id": oid}
        version = V_OLD

    if not res.ok:
        print(f"  ✗ 조회 실패 ({res.status_code})")
        explain(res)
        return False

    results = res.json().get("results", [])
    if results:
        res = call("PATCH", f"/pages/{results[0]['id']}", version, json={"properties": props})
        action = "갱신"
    else:
        res = call("POST", "/pages", version, json={"parent": parent, "properties": props})
        action = "생성"

    if not res.ok:
        print(f"  ✗ {action} 실패 ({res.status_code})")
        explain(res)
        return False

    print(f"  ✓ {action} 완료")
    return True


def sync_one(kind, oid, path):
    print(f"→ {path}")
    if not os.path.isfile(path):
        print("  · 건너뜀: 파일 없음")
        return True
    try:
        info = parse_path(path)
    except ValueError as exc:
        print(f"  · 건너뜀: {exc}")
        return True
    props = build_properties(path, info, parse_header(path))
    return upsert(kind, oid, props, info["문제명"], info["풀이자"])


def main():
    args = sys.argv[1:]

    if args and args[0] == "--diagnose":
        whoami()
        print_accessible(list_accessible())
        return

    if not args:
        print("사용법: notion_sync.py --from-file <목록> | <경로...> | --diagnose")
        sys.exit(1)

    if args[0] == "--from-file":
        with open(args[1], encoding="utf-8") as fp:
            paths = [unquote_git_path(l) for l in fp if l.strip()]
    else:
        paths = [unquote_git_path(a) for a in args]

    if not paths:
        print("동기화할 파일이 없습니다.")
        return

    kind, oid = resolve_target()

    failed = 0
    for path in paths:
        if not sync_one(kind, oid, path):
            failed += 1

    print(f"\n총 {len(paths)}건 중 {len(paths) - failed}건 성공, {failed}건 실패")
    if failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
