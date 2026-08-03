T = 10

for test_case in range(1, T + 1):
    t = input()
    arr = [list(input().strip()) for _ in range(100)]
    arr_rotated = [list(row) for row in zip(*arr[::-1])]
    max_num = 0
    for i in range(100):
        for j in range(100):
            for k in range(101):
                if j + k <= 100 and k > max_num:
                    target1 = arr[i][j:j+k]
                    target2 = arr_rotated[i][j:j+k]
                    if target1 == target1[::-1]:
                        max_num = k
                    if target2 == target2[::-1]:
                        max_num = k

    print(f"#{t} {max_num}")