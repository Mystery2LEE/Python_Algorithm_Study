for tc in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))

    answer = 0

    for i in range(2, N-2):
        near_max = max(
            buildings[i-2],
            buildings[i-1],
            buildings[i+1],
            buildings[i+2]
        )

        if buildings[i] > near_max:
            answer += buildings[i] - near_max

    print(f'#{tc} {answer}')