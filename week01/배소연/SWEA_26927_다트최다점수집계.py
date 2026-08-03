T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    scores = list(map(int, input().strip()))
    dart = [0] * 10

    for score in scores:
        dart[score] += 1

    freq = max(dart)
    for i, score in enumerate(dart):
        if score == freq:
            freq_score = i

    print(f'#{tc} {freq_score} {freq}')