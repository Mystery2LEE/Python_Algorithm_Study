T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    arr_list = []
    for _ in range(n):
        arr = list(str(input()))
        arr_list.append(arr)

    count = 0
    for i in range(n):
        print(count)
        if i < n//2:
            for j in range(n // 2 - i, n // 2 + 1 + i):
                count += int(arr_list[i][j])
        elif i  == n//2:
            for j in range(n):
                count += int(arr_list[i][j])
        else:
            for j in range(n // 2 - (n - 1 - i), n // 2 + 1 + (n - 1 - i)):
                count += int(arr_list[i][j])

    print(f'#{test_case} {count}')