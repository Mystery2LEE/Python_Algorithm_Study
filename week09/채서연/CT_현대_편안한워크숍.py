from collections import deque
N, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# Please write your code here.
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

# 델타 탐색으로 다음에 이돟할 곳이 grid 안에 있고 현재 위치의 값보다 클 때만 이동하게 하면 될 거 같은데...
# 등산로 길이가 k 이상이니까... 이동할 때마다 cnt 1씩 증가시키면서 k면 리턴..?
# cnt = 0
# for d in range(4):
#     nr, nc = r+dr[d], c+dc[d]
#     if 0 <= nr < N and 0 <= nc < N and grid[nr][nr] > grid[r][c]:
#         curr = max(curr, grid[nr][nc] - grid[r][c])
#         cnt += 1
#         if cnt == K:
#             answer = min(answer, curr)
#
######################################################################################################

# 이분탐색 + DP 

answer = -1

# 높이가 낮은 칸부터 정렬
# 우선순위: 높이 낮음 -> 행 오름차순
cells = []
for r in range(N):
    for c in range(N):
        cells.append((grid[r][c], r, c))

cells.sort()

# DP 구현
# limit: 한 번 이동할 때 허용되는 최대 높이. (left + right) / 2 값이 들어옴
def check(limit):
    # (r, c) 칸에서 끝나는, 조건을 만족하는 가장 긴 등산로의 길이
    dp = [[1] * N for _ in range(N)]
    # 낮은 높이부터 탐색
    for height, r, c in cells:
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]

            if 0 <= nr < N and 0 <= nc < N:
                # 이동한 칸은 이전에 지나온 칸이라고 생각 -> grid[nr][nc]이 값이 grid[r][c]이 값보다 작음
                diff = grid[r][c] - grid[nr][nc]

                if 0 < diff <= limit:
                    dp[r][c] = max(dp[r][c], dp[nr][nc] + 1)

        if dp[r][c] >= K:
            return True

    return False

# 이분탐색
left = 0
# grid 최댓갓 - 최솟값. 높이차가 right 보다 클 수 없음
right = max(max(row) for row in grid) - min(min(row) for row in grid)

while left <= right:
    mid = (left + right) // 2
    # 높이차가 mid 이하일 때 길이 K 이상의 등산로를 만들 수 있는지 확인
    # 만들 수 있으면 mid를 정답 후보로 두고 왼쪽 범위로 다시 탐색
    if check(mid):
        answer = mid
        right = mid - 1
    # 만들 수 없으면 오른쪽 범위로 다시 탐색
    else:
        left = mid + 1

print(answer)