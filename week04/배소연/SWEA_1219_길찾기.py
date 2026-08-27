for _ in range(10):
    tc, roads = map(int, input().split())
    arr = list(map(int, input().split()))
    
    graph = [[] for _ in range(100)]
    
    for i in range(0, len(arr), 2):
        a = arr[i]
        b = arr[i + 1]
        
        graph[a].append(b)
        
    visited = [False] * 100
    stack = [0]
    answer = 0
    
    while stack:
        current = stack.pop()
        
        if current == 99:
            answer = 1
            break
        
        if visited[current]:
            continue
        
        visited[current] = True
        for next_node in graph[current]:
            if not visited[next_node]:
                stack.append(next_node)
                
    print(f'#{tc} {answer}')