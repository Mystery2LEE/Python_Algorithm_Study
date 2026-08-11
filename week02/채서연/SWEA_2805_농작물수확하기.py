T= int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int,input())) for _ in range(n)]
    
    # 가운데줄 먼저 계산
    result = sum(arr[n//2])

    for r in range(n//2):
        # 위
        result += sum(arr[r][n//2-r:n//2+1+r])
        # 아래
        result += sum(arr[n-1-r][n//2-r:n//2+r])

    print(f'#{tc} {result}')