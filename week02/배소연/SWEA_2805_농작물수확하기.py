T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    farm = [list(map(int, input().strip())) for _ in range(N)]
    
    mid = N // 2
    profit = 0
    
    for r in range(N):
        distance = abs(r - mid)
        
        start = distance
        end = N - distance
        
        profit += sum(farm[r][start:end])
    
    print(f'#{tc} {profit}')