T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    mask = (1 << N) - 1

    if M & mask == mask:
        answer = "ON"
    else:
        answer = "OFF"