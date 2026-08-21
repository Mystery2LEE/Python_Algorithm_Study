t = int(input())
for tc in range(1, t+1):
    print(f'#{tc}')
    N = int(input().strip())
    result = []
    for x in [50000, 10000, 5000, 1000, 500, 100, 50, 10]:
        result.append(N//x)
        N %= x
    print(*result)