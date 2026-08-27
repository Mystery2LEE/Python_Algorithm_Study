for _ in range(1, 11):
    tc, N = map(int, input().split())
    arr = list(map(int, input().split()))    
    m1 = [-1] * 100
    m2 = [-1] * 100
    
    for i in range(0, N*2, 2):
        if m1[arr[i]] == -1:
            m1[arr[i]] = arr[i+1]
        else:
            m2[arr[i]] = arr[i+1]
    
    def dfs(v):
        if v == 99:
            return 1
        
        # 길이 존재할 때 도착지가 99면 return 1
        if m1[v] != -1:
            if dfs(m1[v]):
                return 1
        
        if m2[v] != -1:
            if dfs(m2[v]):
                return 1
            
        return 0
    
    print(f'#{tc} {dfs(0)}')