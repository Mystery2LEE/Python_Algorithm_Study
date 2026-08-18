T = int(input())

for tc in range(1, T + 1):
    # N: 구역의 수
    # M: 인접 관계의 수
    # K: 색의 수
    N, M, K = map(int, input().split())
    graph = [[] for _ in range(N)]
    
    for _ in range(M):
        a, b = map(int, input().split())
        
        a -= 1
        b -= 1
        
        graph[a].append(b)
        graph[b].append(a)
        
    order = sorted(range(N), key=lambda x:len(graph[x]), reverse=True)
        
    colors = [-1] * N
    count = 0
    
    def dfs(depth):
        global count
        
        if depth == N:
            count += 1
            return
        
        area = order[depth]
        
        for color in range(K):
            possible = True
            
            for neighbor in graph[area]:
                if colors[neighbor] == color:
                    possible = False
                    break
                
            if not possible:
                continue
            
            colors[area]  = color
            dfs(depth + 1)
            colors[area] = -1
            
    dfs(0)
    print(f'#{tc} {count}')