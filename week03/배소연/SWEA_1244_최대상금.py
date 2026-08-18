T = int(input())

for tc in range(1, T + 1):
    info, change = input().split()
    arr = list(info)
    change = int(change)
    
    N = len(arr)
    visited = [set() for _ in range(change + 1)]
    
    max_value = 0

    def dfs(depth):
        global max_value
        current = ''.join(arr)
        
        if current in visited[depth]:
            return
        
        visited[depth].add(current)
        
        if depth == change:
            max_value = max(max_value, int(current))
            return
        
        for i in range(N - 1):
            for j in range(i + 1, N):
                arr[i], arr[j] = arr[j], arr[i]
                dfs(depth + 1)
                arr[i], arr[j] = arr[j], arr[i]
                
    dfs(0)
    print(f'#{tc} {max_value}')