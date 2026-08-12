T = int(input())

for tc in range(1, T + 1):
    # D: 다이얼의 개수
    # S: 목표로 하는 숫자의 합
    D, S = map(int, input().split())
    dp = [0] * (S + 1)
    dp[0] = 1
    
    for _ in range(D):
        next_dp = [0] * (S + 1)
        
        for current_sum in range(S + 1):
            if dp[current_sum] == 0:
                continue
            
            for num in range(10):
                new_sum = current_sum + num
                
                if new_sum > S:
                    break
                
                next_dp[new_sum] += dp[current_sum]   
                
        dp = next_dp
        
    print(f'#{tc} {dp[S]}') 