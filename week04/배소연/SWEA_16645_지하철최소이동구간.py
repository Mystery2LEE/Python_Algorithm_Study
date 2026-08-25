from collections import deque

T = int(input())

def bfs(start, goal):
    queue = deque([start])
    
    distance = [-1] * (V + 1)
    distance[start] = 0
    
    while queue:
        current = queue.popleft()
        
        if current == goal:
            return distance[current]
        
        for next_station in graph[current]:
            if distance[next_station] == -1:
                distance[next_station] = distance[current] + 1
                queue.append(next_station)
                
    return 0
            

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    
    for _ in range(E):
        a, b = map(int, input().split())
        
        graph[a].append(b)
        graph[b].append(a)
        
    S, G = map(int, input().split())
    
    answer = bfs(S, G)
    
    print(f'#{tc} {answer}')