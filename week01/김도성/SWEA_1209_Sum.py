import sys
sys.stdin = open("input.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    test = int(input())
    
    arr_list = []
    for _ in range(100):
        arr = list(map(int, input().split()))
        arr_list.append(arr)
    
    count_max = 0
    
    cro_sum1 = 0
    cro_sum2 = 0
    for i in range(100):
        cro_sum1 += arr_list[i][i]
        cro_sum2 += arr_list[i][99-i]
        col_sum = 0
        row_sum = 0
        for j in range(100):
            col_sum += arr_list[j][i]
            row_sum += arr_list[i][j]
        if count_max < col_sum:
            count_max = col_sum
        if count_max < row_sum:
            count_max = row_sum
        if count_max < cro_sum1:
            count_max = cro_sum1
        if count_max < cro_sum2:
            count_max = cro_sum2
        
    print(f'#{test_case} {count_max}')