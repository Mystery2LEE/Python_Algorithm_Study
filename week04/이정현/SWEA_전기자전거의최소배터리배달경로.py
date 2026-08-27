import heapq

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dist = [[float('inf')] * n for _ in range(n)]
    dist[0][0] = 0
    directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    heap = []
    # 시작점 (0, 0)에서의 비용은 0으로 설정하고 우선순위 큐에 추가
    heapq.heappush(heap, (0, 0, 0))

    while heap:
        # 현재 위치에서의 비용과 좌표를 가져옴
        cost, r, c = heapq.heappop(heap)
        # 현재 위치에서의 비용이 이미 기록된 최소 비용보다 크면 무시
        if cost > dist[r][c]:
            continue
        # 현재 위치에서 상하좌우로 이동하며 비용을 계산
        for d in range(4):
            nr = r + directions[d][0]
            nc = c + directions[d][1]

            if nr < 0 or nr >= n or nc < 0 or nc >= n:
                continue
            # 이동 비용 계산: 현재 위치의 높이와 이동할 위치의 높이 차이에 따라 비용을 계산
            move_cost = 1 + max(0, arr[nr][nc] - arr[r][c])
            new_cost = cost + move_cost
            if new_cost < dist[nr][nc]:
                dist[nr][nc] = new_cost
                heapq.heappush(heap, (new_cost, nr, nc))

    print(f"#{test_case} {dist[n-1][n-1]}")



