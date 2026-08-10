T = int(input())

for test_case in range(1, T + 1):

    n, m, k = map(int, input().split())

    origin = list(map(int, input().split()))

    start = 0
    for _ in range(k):
        start = start + m
        if start >= len(origin):
            start = start % len(origin)

        if start == 0:
            origin.extend([origin[0] + origin[-1]])
            start = len(origin) - 1
        else:
            origin[start:start] = [origin[start-1] + origin[start]]

    print(f"#{test_case}", " ".join(map(str, origin[::-1][:10])))