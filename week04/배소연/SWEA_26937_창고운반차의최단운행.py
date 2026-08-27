from collections import deque

T = int(input())

for tc in range(1, T + 1):
    N = int(input()) # 창고의 한 변의 칸 수
    graph = [] # 창고 바닥의 상태
    
    start_r, start_c = 0, 0
    for r in range(N):
        row = list(map(int, input().strip()))
        graph.append(row)
        
        for c in range(N):
            if row[c] == 2:
                start_r = r
                start_c = c
        
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    distance = [
        [-1] * N
        for _ in range(N)
    ]
    
    queue = deque()
    queue.append((start_r, start_c))
    
    distance[start_r][start_c] = 0
    answer = 0
    
    while queue:
        r, c = queue.popleft()
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            
            if 0 <= nr < N and 0 <= nc < N:
                if graph[nr][nc] != 1 and distance[nr][nc] == -1:
                    distance[nr][nc] = distance[r][c] + 1
                    
                    if graph[nr][nc] == 3:
                        answer = distance[nr][nc] - 1
                        queue.clear()
                        break
                    
                    queue.append((nr, nc))
                    
    print(f'#{tc} {answer}')