# 너무 비효율적으로 품
# 다시 풀어볼것


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n = int(input())

    
    arr = [[0]*n for _ in range(n)]

    i = 0
    j = 0
    count = 0
    for k in range(1, n * n + 1):
        print(i, j)
        print(count)
        if i < 0 or i > n-1 or j < 0 or j > n-1:
            if count % 4 == 0:
                j -= 1
            elif count % 4 == 1:
                i -= 1
            elif count % 4 == 2:
                j += 1
            elif count % 4 == 3:
                i += 1
            count += 1
            if count % 4 == 0:
                j += 1
            elif count % 4 == 1:
                i += 1
            elif count % 4 == 2:
                j -= 1
            elif count % 4 == 3:
                i -= 1
        elif arr[i][j] != 0:
            if count % 4 == 0:
                j -= 1
            elif count % 4 == 1:
                i -= 1
            elif count % 4 == 2:
                j += 1
            elif count % 4 == 3:
                i += 1
            count += 1
            if count % 4 == 0:
                j += 1
            elif count % 4 == 1:
                i += 1
            elif count % 4 == 2:
                j -= 1
            elif count % 4 == 3:
                i -= 1
        print(i, j)
        arr[i][j] = k 
        print(arr[i][j])
        if count % 4 == 0:
            j += 1
        elif count % 4 == 1:
            i += 1
        elif count % 4 == 2:
            j -= 1
        elif count % 4 == 3:
            i -= 1

    
            
        
    print(f'#{test_case}')
    for row in arr:
        print(*row)