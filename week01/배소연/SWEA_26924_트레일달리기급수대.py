T = int(input())

for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    water_spot = list(map(int, input().split()))

    current = 0
    answer = 0

    while current + K < N:
        next_spot = 0

        for position in range(current + K, current, -1):
            if position in water_spot:
                next_spot = position
                break

        if next_spot == 0:
            answer = 0
            break

        current = next_spot
        answer += 1

    print(f'#{tc} {answer}')