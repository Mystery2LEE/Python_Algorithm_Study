T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    max_num = 0
    for i in range(n - 1):
        if max_num >= n - i - 1:
            break

        count = 0
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                count += 1
        if count > max_num:
            max_num = count

    print(f"#{test_case} {max_num}")