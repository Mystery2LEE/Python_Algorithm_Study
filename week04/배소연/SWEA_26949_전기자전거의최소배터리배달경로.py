import heapq

T = int(input())

for tc in range(1, T + 1):
    N = int(input()) # 정사각형 격자의 한 변의 칸 수
    graph = []
    
    for _ in range(N):
        graph.append(list(map(int, input().split())))
        
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    INF = float('inf')
    distance = [
        [INF] * N
        for _ in range(N)
    ]
    
    distance[0][0] = 0
    pq = [(0, 0, 0)]
    
    while pq:
        current_cost, r, c = heapq.heappop(pq)
        
        if current_cost > distance[r][c]:
            continue
        
        if r == N - 1 and c == N - 1:
            break
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            
            if 0 <= nr < N and 0 <= nc < N:
                move_cost = 1 + max(
                    0,
                    graph[nr][nc] - graph[r][c]
                )
                
                new_cost = current_cost + move_cost
                
                if new_cost < distance[nr][nc]:
                    distance[nr][nc] = new_cost
                    
                    heapq.heappush(
                        pq,
                        (new_cost, nr, nc)
                    )
                    
    print(f'#{tc} {distance[N-1][N-1]}')