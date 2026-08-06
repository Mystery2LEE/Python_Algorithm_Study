T = int(input())

for test_case in range(1, T + 1):
    n, x = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr_rotated = [list(row) for row in zip(*arr[::-1])]

    can = 0
    for i in range(n):
        r_is_can = True
        c_is_can = True
        count = 1
        for j in range(n):
            a = arr[i][j]
            b = arr_rotated[i][j]
            if j > 0:
                if arr[i][j-1] == a:
                    count += 1
                else:
                    if count < x or 1 < abs(arr[i][j-1] - a):
                        r_is_can = False
                        break
                    else:
                        count = 1

                if arr_rotated[i][j - 1] == a:
                    count += 1
                else:
                    if count < x or 1 < abs(arr_rotated[i][j - 1] - a):
                        c_is_can = False
                        break
                    else:
                        count = 1
        if r_is_can:
            can += 1
        if c_is_can:
            can += 1

    print(f"#{test_case} {can}")
