T = 10

for test_case in range(1, T + 1):

    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(n):

        arr[arr.index(max(arr))] -= 1
        arr[arr.index(min(arr))] += 1

    print(f"#{test_case} {max(arr) - min(arr)}")