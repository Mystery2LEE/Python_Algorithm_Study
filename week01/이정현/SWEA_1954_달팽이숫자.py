T = int(input())

for test_case in range(1, T + 1):
    print(f"#{test_case}")
    n = int(input())

    arr = [[0 for _ in range(n)] for _ in range(n)]
    dc = [0, 1, 0, -1]
    dr = [1, 0, -1, 0]

    i = 0
    j = 0
    d = 0
    for v in range(1, n*n+1):
        arr[i][j] = v

        if 0 > i + dc[d] or i + dc[d] >= n or 0 > j + dr[d] or  j + dr[d] >= n or arr[i + dc[d]][j + dr[d]] != 0:
            d = (d+1) % 4

        i = i+dc[d]
        j = j+dr[d]

    for k in range(n):
        print(" ".join(map(str, arr[k])))