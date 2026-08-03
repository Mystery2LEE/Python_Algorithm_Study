from numpy import number


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = [[0] * N for _ in range(N)]

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    r, c = 0, 0
    direction = 0

    for n in range(1, N * N + 1):
        arr[r][c] = n

        nr = r + dr[direction]
        nc = c + dc[direction]

        if (
            nr < 0 or nr >= N
            or nc < 0 or nc >= N
            or arr[nr][nc] != 0
        ):
            direction = (direction + 1) % 4

            nr = r + dr[direction]
            nc = c + dc[direction]


        r, c = nr, nc

    print(f'#{tc}')
    for row in arr:
        print(*row)