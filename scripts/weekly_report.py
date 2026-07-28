"""
주간 리포트 생성기.

지난 7일간(월~일) '문제 풀이 기록' DB를 집계해서
'주간 리포트' DB에 요약 한 페이지를 추가한다.

GitHub Actions에서 매주 일요일 밤 자동 실행되며, 수동 실행도 가능하다.

필요 환경변수:
  NOTION_TOKEN            - 인테그레이션 토큰
  NOTION_DATABASE_ID      - 문제 풀이 기록 DB (없으면 이름으로 탐색)
  NOTION_REPORT_DB_ID     - 주간 리포트 DB (없으면 이름으로 탐색)
"""

import os
import sys
from collections import Counter
from datetime import date, datetime, timedelta, timezone

import requests

TOKEN = os.environ.get("NOTION_TOKEN", "").strip()
SRC_DB_ID = os.environ.get("NOTION_DATABASE_ID", "").strip().replace("-", "")
REPORT_DB_ID = os.environ.get("NOTION_REPORT_DB_ID", "").strip().replace("-", "")

API = "https://api.notion.com/v1"
V = "2022-06-28"
KST = timezone(timedelta(hours=9))

MEMBERS = ["이정현", "배소연", "채서연", "양대건", "박정수"]

if not TOKEN:
    print("❌ NOTION_TOKEN 이 없습니다.")
    sys.exit(1)


def call(method, path, **kwargs):
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Notion-Version": V,
        "Content-Type": "application/json",
    }
    return requests.request(method, f"{API}{path}", headers=headers, timeout=30, **kwargs)


def find_db(name_hint):
    """이름으로 DB 검색."""
    res = call("POST", "/search",
               json={"filter": {"value": "database", "property": "object"},
                     "query": name_hint, "page_size": 20})
    if not res.ok:
        return None
    for obj in res.json().get("results", []):
        title = "".join(t.get("plain_text", "") for t in obj.get("title", []))
        if name_hint in title:
            return obj["id"].replace("-", "")
    return None


def query_all(db_id, date_filter=None):
    """DB의 모든 페이지를 페이지네이션으로 수집."""
    rows, cursor = [], None
    while True:
        body = {"page_size": 100}
        if cursor:
            body["start_cursor"] = cursor
        if date_filter:
            body["filter"] = date_filter
        res = call("POST", f"/databases/{db_id}/query", json=body)
        if not res.ok:
            print(f"  조회 실패 ({res.status_code}): {res.text[:200]}")
            return rows
        data = res.json()
        rows.extend(data.get("results", []))
        if not data.get("has_more"):
            break
        cursor = data["next_cursor"]
    return rows


def prop_text(page, name):
    p = page["properties"].get(name, {})
    t = p.get("type")
    if t == "select":
        return p["select"]["name"] if p["select"] else None
    if t == "multi_select":
        return [o["name"] for o in p["multi_select"]]
    if t == "checkbox":
        return p["checkbox"]
    if t == "title":
        return "".join(x["plain_text"] for x in p["title"])
    if t == "date":
        return p["date"]["start"] if p["date"] else None
    return None


def week_bounds():
    """지난 주 월요일 00:00 ~ 이번 주 월요일 00:00 (KST)."""
    now = datetime.now(KST)
    # 이번 주 월요일
    this_monday = (now - timedelta(days=now.weekday())).replace(
        hour=0, minute=0, second=0, microsecond=0)
    last_monday = this_monday - timedelta(days=7)
    return last_monday, this_monday


def main():
    src = SRC_DB_ID or find_db("문제 풀이 기록")
    report = REPORT_DB_ID or find_db("주간 리포트")

    if not src:
        print("❌ 문제 풀이 기록 DB를 찾지 못했습니다. 인테그레이션 연결을 확인하세요.")
        sys.exit(1)
    if not report:
        print("❌ 주간 리포트 DB를 찾지 못했습니다.")
        sys.exit(1)

    start, end = week_bounds()
    print(f"집계 기간: {start.date()} ~ {(end - timedelta(days=1)).date()}")

    date_filter = {
        "and": [
            {"property": "풀이일", "date": {"on_or_after": start.date().isoformat()}},
            {"property": "풀이일", "date": {"before": end.date().isoformat()}},
        ]
    }
    rows = query_all(src, date_filter)

    total = len(rows)
    by_member = Counter()
    type_counter = Counter()
    review_count = 0

    for r in rows:
        solver = prop_text(r, "풀이자")
        if solver:
            by_member[solver] += 1
        for tp in (prop_text(r, "유형") or []):
            type_counter[tp] += 1
        if prop_text(r, "복습 필요"):
            review_count += 1

    submitted = [m for m in MEMBERS if by_member.get(m, 0) > 0]
    not_submitted = [m for m in MEMBERS if by_member.get(m, 0) == 0]

    if by_member:
        top_member, top_count = by_member.most_common(1)[0]
        top_str = f"{top_member} ({top_count}문제)"
    else:
        top_str = "제출 없음"

    type_str = " · ".join(f"{t} {c}" for t, c in type_counter.most_common()) or "없음"
    member_str = " / ".join(f"{m} {by_member.get(m, 0)}" for m in MEMBERS)

    label = f"{start.date().isoformat()} 주간 리포트"
    now_str = datetime.now(KST).strftime("%Y-%m-%d %H:%M KST")

    print(f"  총 제출: {total} / 제출 인원: {len(submitted)} / 복습 필요: {review_count}")
    print(f"  대원별: {member_str}")
    print(f"  미제출: {not_submitted or '없음'}")

    # 본문 콜아웃 구성
    children = [
        {"object": "block", "type": "callout",
         "callout": {"icon": {"emoji": "📊"},
                     "rich_text": [{"type": "text", "text": {"content":
                        f"총 {total}문제 · 제출 {len(submitted)}명 · 복습 필요 {review_count}문제"}}]}},
        {"object": "block", "type": "heading_3",
         "heading_3": {"rich_text": [{"type": "text", "text": {"content": "🧑‍🤝‍🧑 대원별 제출"}}]}},
        {"object": "block", "type": "paragraph",
         "paragraph": {"rich_text": [{"type": "text", "text": {"content": member_str}}]}},
        {"object": "block", "type": "heading_3",
         "heading_3": {"rich_text": [{"type": "text", "text": {"content": "🏷️ 유형 분포"}}]}},
        {"object": "block", "type": "paragraph",
         "paragraph": {"rich_text": [{"type": "text", "text": {"content": type_str}}]}},
    ]

    if not_submitted:
        children.append({"object": "block", "type": "callout",
            "callout": {"icon": {"emoji": "⚠️"}, "color": "red_background",
                        "rich_text": [{"type": "text", "text": {"content":
                            "미제출: " + ", ".join(not_submitted)}}]}})
    else:
        children.append({"object": "block", "type": "callout",
            "callout": {"icon": {"emoji": "🎉"}, "color": "green_background",
                        "rich_text": [{"type": "text", "text": {"content":
                            "전원 제출 완료!"}}]}})

    props = {
        "리포트": {"title": [{"text": {"content": label}}]},
        "주차 시작": {"date": {"start": start.date().isoformat()}},
        "총 제출": {"number": total},
        "제출 인원": {"number": len(submitted)},
        "복습 필요": {"number": review_count},
        "1위 대원": {"rich_text": [{"text": {"content": top_str}}]},
        "유형 분포": {"rich_text": [{"text": {"content": type_str[:1900]}}]},
        "미제출 인원": {"rich_text": [{"text": {"content": ", ".join(not_submitted) or "없음"}}]},
        "생성 시각": {"rich_text": [{"text": {"content": now_str}}]},
    }

    res = call("POST", "/pages", json={
        "parent": {"database_id": report},
        "icon": {"emoji": "📊"},
        "properties": props,
        "children": children,
    })

    if res.ok:
        print(f"✓ 리포트 생성 완료: {label}")
    else:
        print(f"✗ 리포트 생성 실패 ({res.status_code}): {res.text[:300]}")
        sys.exit(1)


if __name__ == "__main__":
    main()
