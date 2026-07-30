T = 10

for test_case in range(1, T + 1):
    n = int(input())
    s_arr = [list(input().rstrip()) for _ in range(8)]
    s_arr_90 = [list(row) for row in zip(*s_arr[::-1])]

    count = 0
    for i in range(8):
        for j in range(8-n+1):
            target1 = s_arr[i][j:j+n]
            target2 = s_arr_90[i][j:j+n]

            if target1 == target1[::-1]:
                count += 1
            if target2 == target2[::-1]:
                count += 1

    print(f"#{test_case} {count}")