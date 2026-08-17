T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    # dp[i]: 현재까지의 숫자 중 일부를 골라 합이 i가 되는 경우의 수
    dp = [0] * (K + 1)
    # 합이 0이 되는 경우 -> 아무 숫자도 선택하지 않는 것을 하나의 경우로 생각
    dp[0] = 1

    for x in A:
        for i in range(K, x - 1, -1):
            dp[i] += dp[i - x]

    print(f'#{tc} {dp[K]}')