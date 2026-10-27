N, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# 각 위치의 높이와 위치를 저장
cells = [(grid[r][c], r, c) for r in range(N) for c in range(N)]
# 오름차순으로 정렬 (파라메트릭 서치)
cells.sort()

d = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def find(D): # 최대 차이 <= D로 길이 K 이상 경로가 있는지 확인
    # 먼저 최소 1을 기입한 dp 배열 선언
    dp = [[1]*N for _ in range(N)]
    for (h, r, c) in cells: # 낮은 칸부터 서치
        for dr, dc in d:
            nr = r + dr
            nc = c + dc
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            if grid[nr][nc] >= grid[r][c]: # 이웃이 나보다 낮지 않으면 건너뜀
                continue
            if h -  grid[nr][nc] > D: # 높이 차이가 D를 넘으면 건너 뜀
                continue
            dp[r][c] = max(dp[r][c], dp[nr][nc] + 1) # 이웃까지의 최장 경로 + 지금 칸 1
        if dp[r][c] >= K: return True # 길이가 K 이상 경로를 찾으면 트루 리턴
    return False

lo, hi = 0, max(map(max, grid)) # 답의 범위 0 ~ 최대값
while lo < hi:
    mid = (lo + hi) // 2
    if find(mid): hi = mid
    else: lo = mid + 1

print(lo)