from collections import deque

# BFS를 사용하여 최단 거리 계산
def bfs(x, y, grid, n):
    visited = [[False] * n for _ in range(n)]
    queue = deque([(y, x)])
    # dist 배열 초기화
    dist = [[-1] * n for _ in range(n)]
    dist[y][x] = 0
    # 큐를 사용하여 BFS 수행
    dy = [0, 0, 1, -1]
    dx = [-1, 1, 0, 0]
    # 방문 처리
    while queue:
        qy, qx = queue.popleft()
        # dist 배열에 최단 거리 갱신
        for d in range(4):
            ny = qy + dy[d]
            nx = qx + dx[d]
            # 범위를 벗어나거나, 이미 방문한 노드이거나, 벽인 경우에는 건너뛰도록 구현
            if 0 > ny or ny >= n or 0 > nx or nx >= n:
                continue
            if visited[ny][nx] is True:
                continue
            if grid[ny][nx] == '1':
                continue
            # 3을 만나면, dist 배열에 최단 거리 갱신 후, BFS 종료
            if grid[ny][nx] == '3':
                return dist[qy][qx]

            dist[ny][nx] = dist[qy][qx] + 1
            visited[ny][nx] = True
            queue.append((ny, nx))

    return 0

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    grid = [list(input()) for _ in range(n)]

    x, y = 0, 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == '2':
                x = j
                y = i

    result = bfs(x, y, grid, n)

    print(f"#{test_case} {result}")