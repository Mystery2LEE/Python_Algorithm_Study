T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    max_num = 0
    min_num = 1000000

    for i in range(n-m+1):
        target = sum(arr[i:i+m])
        if max_num < target:
            max_num = target
        if min_num > target:
            min_num = target

    print(f"#{test_case} {max_num - min_num}")
