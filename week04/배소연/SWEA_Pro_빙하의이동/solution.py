# 너 무 어 려 워 (하다 말앗어요 with GPT)


from typing import List
from collections import deque


# =====================
# 1. 상수 / 데이터
# =====================
# 상, 우, 하, 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N = 0
heights = None
group_map = None
ices = None


class RESULT:
    def __init__(self, mHeights : List[List[int]]):
        self.heights = mHeights


class ICE:
    # 번호, 면적, 부피, 이동방향, 위치(y, x)
    def __init__(self, idx, area, volume, direction, loc):
        self.idx = idx
        self.area = area
        self.volume = volume
        self.direction = direction
        self.loc = loc


# =====================
# 2. 탐색
# =====================
def bfs(r, c, idx):
    queue = deque([(r, c)])
    group_map[r][c] = idx

    area = 0
    volume = 0
    loc = (r, c)

    while queue:
        cr, cc = queue.popleft()

        area += 1
        volume += heights[cr][cc]
        loc = min(loc, (cr, cc))

        for d in range(4):
            nr = (cr + dr[d]) % N
            nc = (cc + dc[d]) % N

            #  바다
            if heights[nr][nc] == 0:
                continue

            # 이미 어떤 빙하에 포함됨
            if group_map[nr][nc] != -1:
                continue

            group_map[nr][nc] = idx
            queue.append((nr, nc))

    return area, volume, loc


# =====================
# 3. 초기화
# =====================
# n: 바다 가로/세로 길이
# m: 빙하의 개수
# mIceBlock: 좌표의 얼음덩어리 높이 정보
# mIceGroup: 얼음덩어리의 X좌표, Y좌표, 빙하 이동 방향
def init(N_ : int, M : int, mIceBlock : List[List[int]], mIceGroup : List[List[int]]) -> None:
    global N, heights, group_map, ices

    N = N_
    heights = [row[:] for row in mIceBlock]
    group_map = [[-1] * N for _ in range(N)]
    ices = {}

    for group_id in range(M):
        x, y, direction = mIceGroup[group_id]
        area, volume, loc = bfs(y, x, group_id)

        ices[group_id] = ICE(
            group_id,
            area,
            volume,
            direction,
            loc
        )


# =====================
# 4. 1년 동안 발생하는 일
# =====================
# 바다와 닿은 얼음 높이 -1
def melt():
    global heights, group_map, ices

    old_group_map = group_map
    old_ices = ices

    new_heights = [row[:] for row in heights]

    for r in range(N):
        for c in range(N):
            if heights[r][c] == 0:
                continue

            for d in range(4):
                nr = (r + dr[d]) % 4
                nc = (c + dc[d]) % 4

                if heights[nr][nc] == 0:
                    new_heights[nr][nc] -= 1
                    break

    heights = new_heights

    # -------------------------
    # 융해 후 빙하 다시 구성
    # -------------------------
    # 녹으면서 하나의 빙하가 여러 개로
    # 나뉠 수 있기 때문
    group_map = [[-1] * N for _ in range(N)]
    ices = {}

    new_id = 0

    for r in range(N):
        for c in range(N):
            if heights[r][c] == 0:
                continue

            if group_map[r][c] != -1:
                continue

            old_id = old_group_map[r][c]
            area, volume, loc = bfs(r, c, new_id)

            direction = old_ices[old_id].direction
            ices[new_id] = ICE(
                new_id,
                area,
                volume,
                direction,
                loc
            )

            new_id += 1



# 모든 빙하를 동시에 한 칸 이동
# 같은 좌표에 얼음이 겹치면 높은 것만 남김
def move():
    global heights, group_map

    new_heights = [[0] * N for _ in range(N)]
    new_group_map = [[-1] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if heights[r][c] == 0:
                continue

            group_id = group_map[r][c]
            direction = ices[group_id].direction

            nr = (r + dr[direction]) % N
            nc = (c + dc[direction]) % N

            # --------------------------------
            # 높이 처리
            # 같은 위치에 겹치면 높은 얼음만 남음
            # --------------------------------
            new_heights[nr][nc] = max(
                new_heights[nr][nc],
                heights[nr][nc]
            )

            # --------------------------------
            # 어느 빙하가 이 위치로 왔는지 기록
            # --------------------------------
            if new_group_map[nr][nc] == -1:
                new_group_map[nr][nc] = group_id
            else:
                # 이미 다른 빙하가 이 칸으로 이동해왔다면
                # 병합 방향 결정 기준이 더 강한 빙하를 기록
                old_id = new_group_map[nr][nc]

                old_ice = ices[old_id]
                new_ice = ices[group_id]

                old_key = (
                    old.
                )


# 이동 완료 후
# 상하좌우로 연결된 빙하를 다시 하나로 묶음
# 새 이동 방향 결정
def merge():



# =====================
# 5. 채점기가 호출하는 함수
# =====================
def oneYearLater() -> RESULT:
    melt()
    move()
    merge()

    return RESULT(heights)