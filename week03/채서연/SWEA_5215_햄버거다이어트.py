
T = int(input())
for tc in range(1, T+1):
    N, L = map(int, input().split())
    s = []
    k = []
    
    def dfs(i, score, kcal):
        global max_score
        if kcal > L:
            return
        if score > max_score:
            max_score = score
        if i == N:
            return
        dfs(i+1, score + s[i], kcal + k[i]) # 현재 재료 선택
        dfs(i+1, score, kcal) # 현재 재료 미선택
        
    for _ in range(N):
        score, kcal = map(int, input().split())
        s.append(score)
        k.append(kcal)
    
    max_score = 0
    dfs(0, 0, 0)
    
    print(f'#{tc} {max_score}')