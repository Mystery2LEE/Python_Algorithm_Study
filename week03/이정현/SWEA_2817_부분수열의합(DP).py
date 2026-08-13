T = int(input())

for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    # 부분집합의 합이 k가 되는 경우의 수를 구하기 위해 dp 배열을 생성
    dp = [0] * (k+1)
    # dp[0]은 1로 초기화 (합이 0이 되는 경우는 공집합 하나)
    dp[0] = 1
    # 각 수를 하나씩 확인하며 dp 배열을 갱신
    for a in arr:
        # 부분집합의 합이 k가 되는 경우의 수를 구하기 위해 dp 배열을 갱신
        for i in range(k, a-1, -1):
            # dp[i]는 dp[i]와 dp[i-a]를 더한 값으로 갱신 (dp[i-a]는 a를 포함한 경우의 수)
            dp[i] += dp[i - a]
            
    count = dp[k]
    print(f"#{test_case} {count}")