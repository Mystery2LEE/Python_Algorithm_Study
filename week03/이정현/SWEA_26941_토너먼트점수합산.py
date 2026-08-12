T = int(input())

for test_case in range(1, T + 1):
    n, m, l = map(int, input().split())
    # match 리스트를 0으로 초기화
    match = [0 for _ in range(n+1)]
    # m개의 경기 결과를 입력받아 match 리스트에 합산
    for _ in range(m):
        p, v = map(int, input().split())
        match[p] += v

    # match 리스트를 bottom-up 방식으로 합산
    for i in range(n, 0, -1):
        match[i//2] += match[i]

    print(f"#{test_case} {match[l]}")