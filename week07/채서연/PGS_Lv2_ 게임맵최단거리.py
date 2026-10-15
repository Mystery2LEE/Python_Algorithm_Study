from collections import deque

def solution(maps):
    answer = -1
    # n이랑 m 구하기
    n = len(maps)
    m = len(maps[0])

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    # 현재까지 이동 거리 저장할 배열
    dist = [[0] * m for _ in range(n)]

    # 시작 위치 큐에 넣기
    q = deque()
    q.append((0, 0))
    dist[0][0] = 1

    while q:
        r, c = q.popleft()

        if r == n - 1 and c == m - 1:
            break

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < n and 0 <= nc < m:
                # maps가 0이면 벽, 1이면 벽이 없는 자리
                if maps[nr][nc] == 1 and dist[nr][nc] == 0:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))

    if dist[n-1][m-1] != 0:
        answer = dist[n-1][m-1]

    return answer