T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    cfs = list(map(int, input().split()))
    
    front = M % N
    
    print(f'#{tc} {cfs[front]}')