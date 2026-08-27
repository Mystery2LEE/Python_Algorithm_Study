T = int(input())

for tc in range(1, T + 1):
    # N: 물건의 개수, C: 상자 용량의 종류 수
    N, C = map(int, input().split())
    boxes = list(map(int, input().split()))
    
    dp = [0] * (N + 1)
    dp[0] = 1
    
    for box in boxes:
        for total in range(box, N + 1):
            dp[total] += dp[total - box]
            
    answer = dp[N]
    
    print(f'#{tc} {answer}')