T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    # dp = [0] * (K + 1)
    # dp[0] = 1
    
    # for num in A:
    #     for total in range(K, num - 1, -1):
    #         dp[total] += dp[total - num]
    
    # print(f'#{tc} {dp[K]}')
    
    def dfs(idx, total):
        if total > K:
            return 0
        
        if idx == N:
            if total == K:
                return 1
            return 0
        
        selected = dfs(idx + 1, total + A[idx])
        non_selected = dfs(idx + 1, total)
        
        return selected + non_selected
        
    answer = dfs(0, 0)
    
    print(f'#{tc} {answer}')