T = int(input())

for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))

    max_num = 0
    for num in arr:
        if num > max_num:
            max_num = num

    print(f"#{test_case} {max_num}")