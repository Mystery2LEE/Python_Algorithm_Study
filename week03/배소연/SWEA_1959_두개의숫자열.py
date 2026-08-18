T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    if N > M:
        A, B = B, A
        N, M = M, N
    
    max_val = 0
    
    for i in range(0, M - N + 1):
        calc = 0
        
        for j in range(N):
            calc += A[j] * B[j+i]
        
        max_val = max(max_val, calc)
    
    print(f'#{tc} {max_val}')