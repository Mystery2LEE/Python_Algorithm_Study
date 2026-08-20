T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n = int(input())
    
    arr_list = list(map(int, input().split()))
    
    def one_cycle(arr):
        for i in range(1,6):
            if arr[-1] <= 0:
                break
            v = arr.pop(0)
            v -= i
            if v <= 0:
                v = 0
            arr.append(v)
           
    while arr_list[-1] > 0:
        one_cycle(arr_list)
        
    
    print(f'#{test_case}', *arr_list)