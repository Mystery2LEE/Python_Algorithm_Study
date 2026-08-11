from collections import deque

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split()) #N: 바구니 자리의 수, M: 바구니의 개수
    Ci = list(map(int, input().split()))

    roaster = deque()

    for i in range(N):
        roaster.append((i + 1, Ci[i]))

    next_idx = N

    while len(roaster) > 1:
        num, moisture = roaster.popleft()
        moisture //= 2

        if moisture == 0:
            if next_idx < M:
                roaster.append((next_idx + 1, Ci[next_idx]))
                next_idx += 1

        else:
            roaster.append((num, moisture))

    last_bucket = roaster[0][0]

    print(f'#{tc} {last_bucket}')