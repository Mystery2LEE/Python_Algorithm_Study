T = int(input().strip())

for test_case in range(1, T+1):
    N, L = map(int , input().split())

    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    
    arr.sort(key=lambda x: x[1])
    dp = [0] * (L+1)

    for i in range(N):
        score =arr[i][0]
        calorie = arr[i][1]
        for j in range(L, calorie - 1, -1):
            if dp[j] < score + dp[j - calorie] :
                dp[j] = score + dp[j - calorie]

    result = max(dp)
    
    print(f'#{test_case} {result}')