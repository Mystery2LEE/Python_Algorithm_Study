from collections import deque

def bfs(graph):
    queue = deque([(1, 1)])
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    graph[1][1] = 1
    
    while queue:
        r, c = queue.popleft()
        
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            
            if graph[nr][nc] == 3:
                return 1
            
            if graph[nr][nc] == 0:
                graph[nr][nc] = 1
                queue.append((nr, nc))
                
    return 0


for _ in range(1, 11):
    tc = int(input())
    graph = [list(map(int, input().strip())) for _ in range(16)]

    answer = bfs(graph)
    print(f'#{tc} {answer}')