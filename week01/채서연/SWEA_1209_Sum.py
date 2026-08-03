for _ in range(10):
    n = int(input())
    result = 0
    
    matrix = [list(map(int,input().split())) for _ in range(100)]
    
    sum_dia_left = 0
    sum_dia_right = 0
        
    for i in range(100):
        sum_row = 0
        sum_col = 0
        for j in range(100):        
            # row col 합
            sum_row += matrix[i][j]
            sum_col += matrix[j][i]
        if result < max(sum_row, sum_col):
            result = max(sum_row, sum_col)
            
        # 대각선 합
        sum_dia_right += matrix[i][99-i]
        sum_dia_left += matrix[i][i]
    if result < max(sum_dia_left, sum_dia_right):
        result = max(sum_dia_left, sum_dia_right)
        
    print(f'#{n} {result}')