T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, l = map(int, input().split())

    tk_list = []
    for _ in range(n):
        arr = list(map(int, input().split()))
        tk_list.append(arr)

    sum_t_max = 0
    for mask in range(1, 1<<n):
        sum_t = 0
        sum_k = 0
        for i in range(n):
            if mask & (1<<i):
                sum_t += tk_list[i][0]
                sum_k += tk_list[i][1]
        if sum_k <= l:
            if sum_t > sum_t_max:
                sum_t_max = sum_t


    print(f'#{test_case} {sum_t_max}')