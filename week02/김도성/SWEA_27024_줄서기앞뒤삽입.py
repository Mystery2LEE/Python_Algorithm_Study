T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    arr = []

    for _ in range(N):
        c, idx = map(int, input().split())
        if c == 1:
            arr.insert(0, idx)
        else:
            arr.append(idx)


    print(f'#{tc} ', end='')

    for a in arr:
        print(a, end=' ')

    print()