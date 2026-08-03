T = int(input())

for tc in range(1, T+1):
    N = int(input())
    book_shelf = list(map(int, input().split()))
    score = [0] * N

    for i in range(N):
        if book_shelf[i] == 0:
            continue

        for j in range(i, N):
            if (book_shelf[j] < book_shelf[i]):
                score[i] += 1

    print(f'#{tc} {max(score)}')