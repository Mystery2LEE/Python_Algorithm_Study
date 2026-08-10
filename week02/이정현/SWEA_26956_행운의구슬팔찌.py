T = int(input())

for test_case in range(1, T + 1):
    # 구슬 횟수, 넘어갈 크기 등 입력
    n, m, k = map(int, input().split())
    # 최초 구슬 띠 입력
    origin = list(map(int, input().split()))
    # 구슬 위치
    start = 0

    for _ in range(k):
        # 넘어가는 크기 만큼 구슬 위치 이동
        start = start + m
        # 만약 띠를 넘어가면 모듈로를 사용
        if start >= len(origin):
            start = start % len(origin)
        # 띠가 0이면 맨뒤에 구슬을 끼워넣음
        if start == 0:
            origin.extend([origin[0] + origin[-1]])
            start = len(origin) - 1
        # 해당 구슬 위치에 구슬을 끼워넣음
        else:
            origin[start:start] = [origin[start-1] + origin[start]]

    print(f"#{test_case}", " ".join(map(str, origin[::-1][:10])))