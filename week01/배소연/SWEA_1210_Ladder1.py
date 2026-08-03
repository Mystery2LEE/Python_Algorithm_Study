for _ in range(10):
    tc = int(input())

    ladder = [
        list(map(int, input().split()))
        for _ in range(100)
    ]

    r = 99
    c = ladder[99].index(2)

    while r > 0:
        if c > 0 and ladder[r][c - 1] == 1:
            while c > 0 and ladder[r][c - 1] == 1:
                c -= 1
            r -= 1

        elif c < 99 and ladder[r][c + 1] == 1:
            while c < 99 and ladder[r][c + 1] == 1:
                c += 1
            r -= 1

        else:
            r -= 1

    print(f'#{tc} {c}')