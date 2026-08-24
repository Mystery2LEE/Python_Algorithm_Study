# 아니 1개가 자꾸 틀리는데 왜 틀리는지 모르겠음
# 안 해 씨앙....


t = int(input().strip())
for tc in range(1, t+1):
    result = 0
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    
    def binary_search(l, r, x, prev):
        while l <= r:
            m = (l + r) // 2

            if A[m] == x:
                return 1

            elif x < A[m]:
                if prev == -1:
                    return 0

                prev = -1
                r = m - 1

            elif x > A[m]:
                if prev == 1:
                    return 0

                prev = 1
                l = m + 1

        return 0
                
    
    for b in B:
        result += binary_search(0, N-1, b, 0)   
        
    print(f'#{tc} {result}')
    
    # def binary_search(l, r, x, prev):
    #     if l > r:
    #         return 0
    #     m = (l + r) // 2
        
    #     if x == A[m]:
    #         return 1
        
    #     # 왼쪽
    #     elif x < A[m]:
    #         # 직전에 왼쪽 방향 골랐음 -> 조건 불만족
    #         if prev == 'left':
    #             return 0
    #         return binary_search(l, m-1, x, 'left')
            
    #     # 오른쪽
    #     elif x > A[m]:
    #         if prev == 'right':
    #             return 0            
    #         return binary_search(m + 1, r, x, 'right')