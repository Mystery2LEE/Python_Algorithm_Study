T = int(input())

for test_case in range(1, T + 1):
    # 각 배열의 길이 입력
    m, n = map(int, input().split())
    # 각 배열 입력
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # 최대값
    max_num = 0
    # 큰 값과 작은값 구별
    long = max(m, n)
    short = min(m, n)
    # 각길이를 뺀 값으로 작은 값을 움직여 곱해 최대값을 추출
    for i in range(long-short+1):
        num = 0
        for j in range(short):
            if short == n:
                num += B[j] * A[j + i]
            else:
                num += A[j] * B[j+i]
        if num > max_num:
            max_num = num

    print(f"#{test_case} {max_num}")