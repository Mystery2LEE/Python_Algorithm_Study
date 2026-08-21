from collections import deque

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().strip())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                start = (i, j)
            elif arr[i][j] == 3:
                end = (i, j)

    queue = deque()
    # (행, 열, 이동한 거리) -> 큐에 삽입
    queue.append((start[0], start[1], 0))
    visited = [[False] * n for _ in range(n)]
    # 시작 노드 -> 방문(True)
    visited[start[0]][start[1]] = True

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    count = 0

    while queue:
        r, c, dist = queue.popleft()
        # 현재 방문한 노드가 도착 노드인 경우
        # BFS는 가장 가까운 노드부터 탐색하기 때문에 처음 도착한 거리가 최단거리다
        if (r, c) == end:
            count = dist -1
            break

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            # 인덱스 범위 안에 있고 아직 방문하지 않은 노드인 경우
            if 0 <= nr < n and 0 <= nc < n:                
                if not visited[nr][nc] and arr[nr][nc] != 1:
                    visited[nr][nc] = True
                    queue.append((nr, nc, dist+1))

    print(f'#{tc} {count}')