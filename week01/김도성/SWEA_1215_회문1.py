T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n = int(input())
    
    arr_list = []
    for _ in range(8):
        arr = list(input())
        arr_list.append(arr)
   	
    row_count = 0
    for i in range(8):
        for j in range(8-n + 1):
            arr = []
            for k in range(n):
                arr.append(arr_list[i][j+k])
            if arr == arr[::-1]:
                row_count += 1
                
    col_count = 0
    for i in range(8-n + 1):
        for j in range(8):
            arr = []
            for k in range(n):
                arr.append(arr_list[i+k][j])
            if arr == arr[::-1]:
                col_count += 1
                
    print(f'#{test_case} {row_count + col_count}')