N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

visited = [[False] * M for _ in range(N)]
#
selected = []
modules = {}

# 연결된 5칸으로 이루어진 모듈 생성

# c	현재까지 선택한 칸의 개수
# mask	선택한 칸의 위치를 비트로 표현한 정수
# total	현재까지 선택한 칸들의 점수 합계
def dfs(c, mask, total):
    # 5칸을 선택하면 모듈 하나 완성
    if c == 5:
        modules[mask] = total
        return

    # 현재까지 선택한 모든 칸에서 확장
    for i, j in selected:
        for d in range(4):
            nr = i + dr[d]
            nc = j + dc[d]

            # 격자 범위 검사
            if not (0 <= nr < N and 0 <= nc < M):
                continue

            # 이미 선택한 칸이면 건너뛰기
            if visited[nr][nc]:
                continue

            # 방문 처리
            visited[nr][nc] = True
            selected.append((nr, nc))

            # 다음 칸 탐색
            # nr * M + nc -> N = 2, M = 4, (1,2) 면 6
            # new_mask: DFS에서 지금까지 선택한 모든 칸의 위치를 비트(0과 1)로 기록한 값
            new_mask = mask | (1 << (nr * M + nc))
            dfs(c + 1, new_mask, total + grid[nr][nc])

            # 백트래킹
            selected.pop()
            visited[nr][nc] = False


# 모든 칸을 시작점으로 DFS 실행
for i in range(N):
    for j in range(M):
        visited[i][j] = True
        selected.append((i, j))

        mask = 1 << (i * M + j)
        dfs(1, mask, grid[i][j])

        selected.pop()
        visited[i][j] = False


# 생성한 모듈들을 리스트로 변환
items = list(modules.items())

answer = float('-inf')

# 모듈 2개 선택
for i in range(len(items)):
    mask1, sum1 = items[i]

    for j in range(i + 1, len(items)):
        mask2, sum2 = items[j]

        # 정확히 2칸이 겹치는지 확인
        overlap = (mask1 & mask2).bit_count()

        if overlap == 2:
            answer = max(answer, sum1 + sum2)

print(answer)