T = int(input())

for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    dp = [[0]*(k+1) for _ in range(n+1)]
    item = [[] for _ in range(n+1)]
    for i in range(1, n+1):
        v, c = map(int, input().split())
        item[i].append(v)
        item[i].append(c)

    for j in range(k+1):
        for i in range(1, n+1):
            if j >= item[i][0]:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - item[i][0]] + item[i][1])
            else:
                dp[i][j] = dp[i - 1][j]

    print(f"#{test_case} {dp[n][k]}")