import heapq

t = int(input().strip())
for tc in range(1, t+1):
    N = int(input().strip())
    graph = [list(map(int, input().split())) for _ in range(N)]
    
    # [0][0]에서 [r][c]까지의 최소 배터리 소비량
    INF = float('inf')
    dist = [[INF] * N for _ in range(N)]
    
    # 시작 위치
    dist[0][0] = 0
    # 현재까지 배터리 소비량, 행, 열
    pq = [(0, 0, 0)]
    
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    
    while pq:
        cost, r, c = heapq.heappop(pq) # 현재
        
        # 이미 더 적은 비용으로 방문한 적이 있다면 무시
        if cost > dist[r][c]:
            continue
        
        if r == N-1 and c == N-1:
            break
        
        # 상하좌우 탐색
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            
            # 그래프 범위 벗어날 경우
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            
            # 이동 비용(배터리 소비량)
            move_cost = 1 + max(0, graph[nr][nc] - graph[r][c])
            new_cost = cost + move_cost # 기존 소비량 + 새로 이동한 소비량
            
            if new_cost < dist[nr][nc]:
                dist[nr][nc] = new_cost
                heapq.heappush(pq, (new_cost, nr, nc))
    
    print(f'#{tc} {dist[N-1][N-1]}')