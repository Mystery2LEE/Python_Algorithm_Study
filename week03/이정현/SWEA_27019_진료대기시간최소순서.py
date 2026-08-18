T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    arr = sorted(list(map(int, input().split())))

    result = 0
    # 이전 값들의 합을 구해서 더해주기
    for i in range(1, len(arr)):
        result += sum(arr[:i])
    print(f"#{test_case} {result}")