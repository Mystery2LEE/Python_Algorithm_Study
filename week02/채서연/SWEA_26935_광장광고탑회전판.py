T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    view = list(map(int, input().split()))

    for _ in range(m % n):
        data = view.pop(0)
        view.append(data)

    print(f'#{tc} {view[0]}')
    