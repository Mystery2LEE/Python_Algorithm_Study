T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    max_r = 0
    max_c = 0
    c1 = 0
    c2 = 0

    arr_rotated = [list(row) for row in zip(*arr[::-1])]
    for i in range(100):
        max_r_temp = 0
        max_c_temp = 0
        c1 += arr[i][i]
        c2 += arr[i][100 - 1 - i]
        for j in range(100):
            max_r_temp += arr[i][j]
            max_c_temp += arr_rotated[i][j]
        if max_r_temp > max_r:
            max_r = max_r_temp
        if max_c_temp > max_c:
            max_c = max_c_temp

    max_num = max(max_r, max_c, c1, c2)
    print(f"#{test_case} {max_num}")