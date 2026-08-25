import heapq
t = int(input().strip())
for tc in range(1, t+1):
    N = int(input().strip())
    graph = [list(map(int, input())) for _ in range(N)]
    
    INF = float('inf')    
    dist = [[INF] * N for _ in range(N)]
    # [0][0]부터 [r][c]까지 가는 최소 비용 저장하는 행렬
    dist[0][0] = 0
    
    # 이동 경로 상하좌우
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    
    # (복구 시간, 행, 열)
    pq = [(0, 0, 0)]
    
    while pq:
        cost, r, c = heapq.heappop(pq)
        # 이미 더 적은 비용으로 방문한 적이 있으면 무시
        if cost > dist[r][c]:
            continue
        # 목적지 도착
        if r == N-1 and c == N-1:
            break
        # 상하좌우 한칸씩 이동
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            # 이전까지의 비용 + 현재 이동한 곳의 비용
            new_cost = dist[r][c] + graph[nr][nc]
            # 이미 저장된 경로보다 새로운 비용이 작을 경우 갱신하고 큐에 추가
            if new_cost < dist[nr][nc]:
                dist[nr][nc] = new_cost
                heapq.heappush(pq, (new_cost, nr, nc))            
    
    
    print(f'#{tc} {dist[N-1][N-1]}')