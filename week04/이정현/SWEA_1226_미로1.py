# 미로 탐색 함수
def dfs(y, x, arr, visited, directions):
    # 방문 기록을 남기는 변수
    visited[y][x] = True
    # 4방향을 탐색하며 갈 수 있는 방향을 찾는다
    for d in range(4):
        ny = y + directions[d][0]
        nx = x + directions[d][1]
        if ny < 0 or ny >= n or nx < 0 or nx >= n:
            continue
        if visited[ny][nx] or arr[ny][nx] == 1:
            continue
        # 값이 3이면 리턴 1
        if arr[ny][nx] == 3:
            return 1
        # dfs가 1이면 1을 출력
        if dfs(ny, nx, arr, visited, directions) == 1:
            return 1

    return 0


T = 10
n = 16

for test_case in range(1, T + 1):
    t = int(input())
    directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    arr = [[int(i) for i in input()] for _ in range(n)]
    visited = [[False] * 16 for _ in range(16)]
    s_y = 0
    s_x = 0

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                s_y = i
                s_x = j

    result = dfs(s_y, s_x, arr, visited, directions)
    print(f"#{t} {result}")