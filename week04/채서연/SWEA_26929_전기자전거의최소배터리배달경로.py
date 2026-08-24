t = int(input().strip())
for tc in range(1, t+1):
    result = 0
    N = int(input().strip())
    graph = [list(map(int, input().split())) for _ in range(N)]
    
    
    print(f'#{tc} {result}')