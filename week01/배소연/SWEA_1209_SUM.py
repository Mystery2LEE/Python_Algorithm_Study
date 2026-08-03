for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    row_sum = []
    for i in range(100):
        total = 0
        
        for j in range(100):
            total += arr[i][j]

        row_sum.append(total)

    col_sum = []
    for i in range(100):
        total = 0

        for j in range(100):
            total += arr[j][i]

        col_sum.append(total)

    cross1, cross2 = 0, 0
    for i in range(100):
        cross1 += arr[i][i]
        cross2 += arr[i][99-i]

    row_max = max(row_sum)
    col_max = max(col_sum)
    cross_max = max(cross1, cross2)

    answer = max(row_max, col_max, cross_max)
    
    print(f'#{tc} {answer}')