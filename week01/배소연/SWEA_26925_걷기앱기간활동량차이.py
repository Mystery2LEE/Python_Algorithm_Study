T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    per_a_day = list(map(int, input().split()))
    period = []

    for i in range(0, N-M+1):
        total = 0

        for j in range(i, i+M):
            total += per_a_day[j]

        period.append(total)

    print(f'#{tc} {max(period) - min(period)}')