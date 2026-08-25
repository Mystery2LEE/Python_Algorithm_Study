for _ in range(1, 11):
    tc = int(input().strip())
    graph = [list(map(int, input())) for _ in range(16)]
    
    # 상하좌우 탐색
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visited = [[0]*16 for _ in range(16)]
    
    def dfs(x, y):
        # 도착점에 도달했으면 -> 1
        if graph[x][y] == 3:
            return 1
        # 
        visited[y][x] = 1

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < 16 and 0 <= ny < 16:
                if graph[ny][nx] != 1 and visited[ny][nx] == 0:
                    if dfs(nx, ny):
                        return 1
        return 0
    print(f'#{tc} {dfs(1,1)}')
    