T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n_a, n_b = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))

    if n_a > n_b:
        count_max = 0
        for i in range(n_a - n_b + 1):
            count = 0
            for j in range(n_b):
                count = count + a_list[i + j] * b_list[j]
            if count_max < count:
                count_max = count
    else:
        count_max = 0
        for i in range(n_b - n_a + 1):
            count = 0
            for j in range(n_a):
                count = count + a_list[j] * b_list[i + j]
            if count_max < count:
                count_max = count

    print(f'#{test_case} {count_max}')