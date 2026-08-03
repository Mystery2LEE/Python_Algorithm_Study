T = 10

for test_case in range(1, T + 1):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    y = 99
    x = 0

    for i in range(100):
        if arr[-1][i] == 2:
            x = i

    b_x = 0
    b_y = 0
    dc = [0, 0, -1]
    dr = [-1, 1, 0]
    while y != 0:
        for d in range(3):
            ny = dc[d] + y
            nx = dr[d] + x
            if 0 <= ny < 100 and 0 <= nx < 100 and not (nx == b_x and ny == b_y):
                if arr[ny][nx] == 1:
                    b_x = x
                    b_y = y
                    y = ny
                    x = nx
                    break

    print(f"#{test_case} {x}")