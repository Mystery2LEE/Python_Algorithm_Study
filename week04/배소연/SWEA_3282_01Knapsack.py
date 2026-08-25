T = int(input())

for tc in range(1, T + 1):
    # N: 물건의 개수
    # K: 가방의 부피
    N, K = map(int, input().split())
    dp = [0] * (K + 1)
    
    for _ in range(N):
        # V: 부피, C: 가치
        V, C = map(int, input().split())
        
        for k in range(K, V - 1, -1):
            dp[k] = max(dp[k], dp[k - V] + C)
            
    print(f'#{tc} {dp[K]}')