T = int(input())

for test_case in range(1, T + 1):
    # 입력값 받기
    n, m = map(int, input().split())
    Q = []
    K = []
    # n개의 햄버거 재료의 맛 점수와 칼로리를 리스트로 받기
    for _ in range(n):
        q, k = map(int, input().split())
        Q.append(q)
        K.append(k)
    # 부분집합의 합이 제한 칼로리 m 이하인 경우의 맛 점수 합의 최대값을 구하기 위해 dp 배열을 생성
    dp = [0] * (m + 1)
    # 각 재료를 하나씩 확인하며 dp 배열을 갱신
    for i in range(n):
        # 각 재료의 칼로리와 맛 점수를 가져옴
        k = K[i]
        q = Q[i]
        # 부분집합의 합이 제한 칼로리 m 이하인 경우의 맛 점수 합의 최대값을 구하기 위해 dp 배열을 갱신
        for j in range(m, k-1, -1):
            # dp[j]는 dp[j]와 dp[j-k] + q를 비교하여 최대값으로 갱신 (dp[j-k]는 k를 포함한 경우의 수)
            dp[j] = max(dp[j], dp[j - k] + q)
    # 부분집합의 합이 제한 칼로리 m 이하인 경우의 맛 점수 합의 최대값을 구함
    best_berger = max(dp)

    print(f"#{test_case} {best_berger}")