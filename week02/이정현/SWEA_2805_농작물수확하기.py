T = int(input())

for test_case in range(1, T + 1):
    # 밭의 크기 입력
    n = int(input())
    # 밭 입력
    field = [list(map(int, input().strip())) for _ in range(n)]
    # 총 가치
    value = 0
    # 2차원 배열에서 마름모 위치만 순환하면서 해당 값들을 더한다
    for i in range(n):
        num = abs(n//2-i)
        for j in range(num, n-num):
            value += field[i][j]

    print(f"#{test_case} {value}")