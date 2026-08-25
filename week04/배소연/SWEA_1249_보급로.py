import heapq

T = int(input())
INF = float('inf')

for tc in range(1, T + 1):
    N = int(input()) # 지도의 크기 N * N
    road = [list(map(int, input().strip())) for _ in range(N)]
    
    distance = [[INF] * N for _ in range(N)]
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    distance[0][0] = 0
    heap = [(0, 0, 0)] #(현재까지의 비용, 행, 열)

    while heap:
        cost, r, c = heapq.heappop(heap)
        
        if cost > distance[r][c]:
            continue
        
        if r == N - 1 and c == N - 1:
            break
        
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            
            if 0 <= nr < N and 0 <= nc < N:
                new_cost = cost + road[nr][nc]
                
                if new_cost < distance[nr][nc]:
                    distance[nr][nc] = new_cost
                    heapq.heappush(
                        heap,
                        (new_cost, nr, nc)
                    )    
    
    print(f'#{tc} {distance[N-1][N-1]}')