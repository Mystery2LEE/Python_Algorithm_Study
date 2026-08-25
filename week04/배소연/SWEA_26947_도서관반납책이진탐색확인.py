# 테스트케이스 1개가 통과가 안됨

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    
    A = list(map(int, input().split())) # 원소 개수 N
    B = list(map(int, input().split())) # 원소 개수 M
    
    count = 0
    
    for target in B:
        l = 0
        r = N - 1
        
        prev = None
        possible = True
        
        while l <= r:
            m = (l + r) // 2
            
            if A[m] == target:
                break
                
            elif A[m] < target:
                if prev == 'R':
                    possible = False
                    break
                
                prev = 'R'
                l = m + 1
                
            elif A[m] > target:
                if prev == 'L':
                    possible = False
                    break
                
                prev = 'L'
                r = m - 1
                
        else:
            possible = False
            
        if possible:
            count += 1
                    
    print(f'#{tc} {count}')