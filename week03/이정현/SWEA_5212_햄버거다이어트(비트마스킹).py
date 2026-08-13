T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    # n개의 햄버거 재료의 맛 점수와 칼로리를 리스트로 받기
    Q = []
    K = []
    for _ in range(n):
        # 입력값 받기
        q, k = map(int, input().split())
        Q.append(q)
        K.append(k)

    best_burger = 0
    # 부분집합이 2^n개이므로 0부터 2^n-1까지 반복
    for i in range(1 << n):
        k_sum = 0
        q_sum = 0
        # 각 부분집합의 합을 구하기 위해 비트 연산을 사용하여 부분집합에 포함된 수를 더함
        for j in range(n):
            # i의 j번째 비트가 1이면 K[j]와 Q[j]를 더함
            if i & (1 << j):
                k_sum += K[j]
                q_sum += Q[j]
        # 부분집합의 칼로리 합이 제한 칼로리 m 이하이면 맛 점수 합을 비교하여 최대값 갱신
        if k_sum <= m:
            if q_sum > best_burger:
                best_burger = q_sum

    print(f"#{test_case} {best_burger}")