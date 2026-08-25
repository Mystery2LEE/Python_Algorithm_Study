from typing import List
from collections import deque

class RESULT:
    def __init__(self, mHeights : List[List[int]]):
        self.heights = mHeights

def bfs(x, y, gid):
    queue = deque([])
    queue.append((y, x))
    group[y][x] = gid
    dy_dx = [(1, 0), (-1, 0), (0, -1), (0, 1)]

    while queue:
        qy, qx = queue.popleft()
        for d in range(4):
            ny = (qy + dy_dx[d][0]) % size
            nx = (qx + dy_dx[d][1]) % size
            if height[ny][nx] > 0 and group[ny][nx] == -1:
                queue.append((ny, nx))
                group[ny][nx] = gid


def init(N : int, M : int, mIceBlock : List[List[int]], mIceGroup : List[List[int]]) -> None:
    global height, group, direction, size

    size = N

    height = [[mIceBlock[y][x] for x in range(N)] for y in range(N)]

    group = [[-1] * N for _ in range(N)]
    direction = [0] * M

    for gid, (x, y, d) in enumerate(mIceGroup):
        direction[gid] = d

        if group[y][x] != -1:
            continue

        bfs(x, y, gid)
    pass

def oneYearLater() -> RESULT:
    melt()
    area, volume, pos_y, pos_x = calc_stats()
    move()
    merge(area, volume, pos_y, pos_x)

    res_heights = [[height[y][x] for x in range(size)] for y in range(size)]
    return RESULT(res_heights)

def melt():
    global height, group, direction

    delta = [[0] * size for _ in range(size)]
    dy_dx = [(1, 0), (-1, 0), (0, -1), (0, 1)]

    for y in range(size):
        for x in range(size):
            if height[y][x] == 0:
                continue
            for d in range(4):
                ny = (y + dy_dx[d][0]) % size
                nx = (x + dy_dx[d][1]) % size
                if height[ny][nx] == 0:
                    delta[y][x] = 1
                    break

    for y in range(size):
        for x in range(size):
            height[y][x] -= delta[y][x]
            if height[y][x] == 0:
                group[y][x] = -1
            pass

    old_direction = direction[:]
    new_group = [[-1] * size for _ in range(size)]
    new_direction = []

    for y in range(size):
        for x in range(size):
            if height[y][x] > 0 and new_group[y][x] == -1:
                old_gid = group[y][x]
                new_gid = len(new_direction)
                new_direction.append(old_direction[old_gid])
                queue = deque([])
                queue.append((y, x))
                new_group[y][x] = new_gid

                while queue:
                    qy, qx = queue.popleft()
                    for d in range(4):
                        ny = (qy + dy_dx[d][0]) % size
                        nx = (qx + dy_dx[d][1]) % size
                        if height[ny][nx] > 0 and new_group[ny][nx] == -1:
                            queue.append((ny, nx))
                            new_group[ny][nx] = new_gid

    group = new_group
    direction = new_direction

def calc_stats():
    num_groups = len(direction)

    area = [0] * num_groups
    volume = [0] * num_groups
    pos_y = [None] * num_groups
    pos_x = [None] * num_groups

    for y in range(size):
        for x in range(size):
            gid = group[y][x]
            if gid == -1:
                continue

            area[gid] += 1
            volume[gid] += height[y][x]

            if pos_y[gid] is None or y < pos_y[gid]:
                pos_y[gid] = y
                pos_x[gid] = x
            elif y == pos_y[gid]:
                if x < pos_x[gid]:
                    pos_x[gid] = x

    return area, volume, pos_y, pos_x

def move():
    global height, group

    arrivals = [[[] for _ in range(size)] for _ in range(size)]

    dy_dx = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for y in range(size):
        for x in range(size):
            gid = group[y][x]
            if gid == -1:
                continue

            d = direction[gid]
            ny = (y + dy_dx[d][0]) % size
            nx = (x + dy_dx[d][1]) % size
            arrivals[ny][nx].append((height[y][x], gid))

    new_height = [[0] * size for _ in range(size)]
    new_group = [[-1] * size for _ in range(size)]

    for y in range(size):
        for x in range(size):
            if not arrivals[y][x]:
                continue
            max_h = 0
            winner_gid = -1
            for h, gid in arrivals[y][x]:
                if h > max_h:
                    max_h = h
                    winner_gid = gid

            new_height[y][x] = max_h
            new_group[y][x] = winner_gid

    height = new_height
    group = new_group

def merge(area, volume, pos_y, pos_x):
    global group, direction

    new_group = [[-1] * size for _ in range(size)]
    new_direction = []

    dy_dx = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for y in range(size):
        for x in range(size):
            if height[y][x] == 0 or new_group[y][x] != -1:
                continue

            new_gid = len(new_direction)
            queue = deque([(y, x)])
            new_group[y][x] = new_gid
            old_gids_in_group = set()
            old_gids_in_group.add(group[y][x])

            while queue:
                qy, qx = queue.popleft()
                for d in range(4):
                    ny = (qy + dy_dx[d][0]) % size
                    nx = (qx + dy_dx[d][1]) % size
                    if height[ny][nx] > 0 and new_group[ny][nx] == -1:
                        queue.append((ny, nx))
                        new_group[ny][nx] = new_gid
                        old_gids_in_group.add(group[ny][nx])

            winner_gid = -1
            for gid in old_gids_in_group:
                if winner_gid == -1 or is_better(gid, winner_gid, volume, area, pos_y, pos_x):
                    winner_gid = gid

            new_direction.append(direction[winner_gid])

    group = new_group
    direction = new_direction

def is_better(gid_a, gid_b, volume, area, pos_y, pos_x):
    if volume[gid_a] != volume[gid_b]:
        return volume[gid_a] > volume[gid_b]
    if area[gid_a] != area[gid_b]:
        return area[gid_a] < area[gid_b]
    if pos_y[gid_a] != pos_y[gid_b]:
        return pos_y[gid_a] < pos_y[gid_b]
    return pos_x[gid_a] < pos_x[gid_b]