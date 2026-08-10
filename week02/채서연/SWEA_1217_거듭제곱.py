def f(n, m):
    if m == 1:
        return n
    else:
        return n * f(n, m-1)

for _ in range(10):
    tc = int(input())
    n, m = map(int, input().split())

    print(f'#{tc} {f(n, m)}')