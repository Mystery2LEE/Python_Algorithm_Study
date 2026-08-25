# 아직 init은 지피티가 도와줘서 구현했는데 later는 init 참고해서 조금 더 생각해 볼게요.....


from typing import List

class RESULT:
    def __init__(self, mHeights : List[List[int]]):
        self.heights = mHeights

n = 0
ice = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def init(N : int, M : int, mIceBlock : List[List[int]], mIceGroup : List[List[int]]) -> None:
    global ice, n
    ice = []
    n = N
    # mIceBlock[][]: 각 좌표에 존재하는 얼음덩어리 높이
    # mIceGroup[][]: 각 빙하를 구성하고 있는 얼음덩어리 1개에 대한 X, Y 좌표 및 빙하의 이동 방향
    # 0 : ↑, 1: →, 2: ↓, 3: ←

    # 초기 빙하 찾기
    visited = [[False] * n for _ in range(n)]
    for x, y, d in mIceGroup:
        if visited[y][x]:
            continue
        # 빙하를 구성하는 얼음덩어리 담을 딕셔너리
        cells = {}
        # BFS
        queue = [(y, x)]
        visited[y][x] = True
        front = 0

        while front < len(queue):

            cy, cx = queue[front]
            front += 1
            # {(좌표):높이}
            cells[(cy, cx)] = mIceBlock[cy][cx]

            for direction in range(4):

                ny = (cy + dy[direction]) % n
                nx = (cx + dx[direction]) % n

                if visited[ny][nx]:
                    continue

                if mIceBlock[ny][nx] == 0:
                    continue

                visited[ny][nx] = True
                queue.append((ny, nx))

        ice.append({
            "cells": cells,
            "dir": d
        })


def oneYearLater() -> RESULT:
    # 1. 융해: 상하좌우 바다에 인접한 얼음 덩어리의 높이가 1씩 줄어든다,
    # 높이가 0이 될 경우 그 얼음덩어리는 사라진다. 융해에 의해 빙하는 2개 이상의 빙하로 나누어질 수 잇다.

    for y in range(n):
        for x in range(n):
            if ice[y][x] != 0:
                # 4방향 중 한면이라도 바다랑 인접하면 -1
                for d in range(4):
                    ny = y + dy[d]
                    nx = x + dx[d]
                    if ice[ny][nx] == 0:
                        ice[y][x] -= 1
                        break

    # 2. 이동: 빙하가 상하좌우 중 한 방향으로 1칸씩 이동한다, 초기에 이동하는 방향은 입력으로 주어진다.



    # 3. 병합: 다른 빙하가 서로 충돌하거나, 상하좌우로 인접할 경우 하나의 빙하가 된다. 이동 후 서로 다른 빙하를 구성하고 있는 얼음덩어리가 같은 좌표에 겹치거나 상하좌우로 인접할 수 있다
    # 겹칠 경우 두 얼음덩어리 중 높이가 높은 얼음덩어리만 그 좌표에 남는다
    # 병합된 빙하는 이동 방향이 바뀌며, 다음과 같이 각 빙하가 이동하기 전의 상태를 비교하여 병합 후의 이동방향을 결정한다.
        # 1. 부피가 큰 빙하의 이동 방향을 따른다
        # 2. 부피가 같을 경우 면적이 작은 빙하의 이동 방향을 따른다
        # 3. 면적이 같을 경우, 두 빙하의 위치 중 Y좌표가 작은 위치에 있는 빙하의 이동 방향을 따른다
        # 4. Y좌표가 같을 경우, 두 빙하의 위치 중 X좌표가 작은 위치에 있는 빙하의 이동 방향을 따른다



    # 마지막 빙하의 상태를 기준으로 1년이 지난 후 빙하의 상태를 반환한다.
    # 반환은 RESULT 구조체의 mheights 배열에 각 좌표의 얼음덩어리 “높이” 값을 저장

    res = RESULT([[0 for _ in range(100)] for _ in range(100)])
    return res