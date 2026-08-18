T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    
    cols = [False] * N
    diag1 = [False] * (2 * N - 1)
    diag2 = [False] * (2 * N - 1)
    
    count = 0
    
    def dfs(row):
        global count
        
        if row == N:
            count += 1
            return
        
        for col in range(N):
            d1 = row - col + N - 1
            d2 = row + col
            
            if cols[col] or diag1[d1] or diag2[d2]:
                continue
            
            cols[col] = True
            diag1[d1] = True
            diag2[d2] = True
            
            dfs(row + 1)

            cols[col] = False
            diag1[d1] = False
            diag2[d2] = False
    
    dfs(0)
    print(f'#{tc} {count}')