from collections import deque


def solution(maps):
    n, m = len(maps), len(maps[0])
    start_r, start_c = 0, 0

    dr = [-1, 0, 1, 0]
    dc = [0, -1, 0, 1]

    queue = deque([(start_r, start_c)])
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1

    while queue:
        r, c = queue.popleft()

        if r == n - 1 and c == m - 1:
            return visited[r][c]

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < n and 0 <= nc < m:
                if maps[nr][nc] == 1 and visited[nr][nc] == 0:
                    visited[nr][nc] = visited[r][c] + 1
                    queue.append((nr, nc))

    return -1
