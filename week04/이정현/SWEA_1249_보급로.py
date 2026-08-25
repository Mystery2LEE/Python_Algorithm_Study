import heapq

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    dist = [[float('inf')] * n for _ in range(n)]
    hall = [[int(i) for i in input()] for _ in range(n)]
    directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    heap = []
    heapq.heappush(heap, (0, 0, 0))

    while heap:
        cost, r, c = heapq.heappop(heap)
        if cost > dist[r][c]:
            continue
        for d in range(4):
            nr = r + directions[d][0]
            nc = c + directions[d][1]

            if nr < 0 or nr >= n or nc < 0 or nc >= n:
                continue

            new_cost = cost + hall[nr][nc]
            if new_cost < dist[nr][nc]:
                dist[nr][nc] = new_cost
                heapq.heappush(heap, (new_cost, nr, nc))

    print(f"#{test_case} {dist[n-1][n-1]}")