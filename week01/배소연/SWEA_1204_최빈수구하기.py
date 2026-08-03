T = int(input())

for _ in range(T):
    tc = int(input())

    scores = list(map(int, input().split()))
    score_range = [0] * 101

    for score in scores:
        score_range[score] += 1

    max_count = max(score_range)

    for score in range(100, -1, -1):
        if score_range[score] == max_count:
            answer = score
            break

    print(f'#{tc} {answer}')