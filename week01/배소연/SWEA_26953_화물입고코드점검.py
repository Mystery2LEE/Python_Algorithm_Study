T = int(input())

for tc in range(1, T+1):
    interested = list(input().strip())
    recorded = list(input().strip())

    N = len(interested)
    counting = [0] * N

    for i, ch in enumerate(interested):
        for record in recorded:
            if record == ch:
                counting[i] += 1

    answer = max(counting)

    print(f'#{tc} {answer}')