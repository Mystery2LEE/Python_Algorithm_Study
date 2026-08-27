T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int, input().split())

    flag = []
    for _ in range(n):
        line = list(input())
        flag.append(line)

    count_min = 99999999
    for white_end in range(1, n - 1):
        for blue_end in range(white_end + 1, n):
            count = 0
            for i in range(white_end):
                for j in range(m):
                    if flag[i][j] != 'W':
                        count += 1
            for i in range(white_end, blue_end):
                for j in range(m):
                    if flag[i][j] != 'B':
                        count += 1
            for i in range(blue_end, n):
                for j in range(m):
                    if flag[i][j] != 'R':
                        count += 1
            if count_min > count:
                count_min = count
        

    print(f'#{test_case} {count_min}')




            