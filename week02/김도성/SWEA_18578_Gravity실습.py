T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())

    box_list = list(map(int, input().split()))

    box_max = max(box_list)

    n_list = [[0 for _ in range(box_max)] for _ in range(n)]

    for i in range(n):
        for j in range(box_list[i]):
            n_list[i][j] = 1

    max_count = 0
    for i in range(n-1, -1, -1):
        for j in range(box_max):
            count = 0
            for k in range(n - i):
                if i + k - 1 < 0:
                    break
                if n_list[i + k][j] == 0 and n_list[i + k - 1][j] == 1:
                    if i + k >= n:
                        break
                    n_list[i + k][j] = 1
                    n_list[i + k - 1][j] = 0
                    count += 1
            if max_count < count:
                max_count = count

    print(f'#{test_case} {max_count}')

    