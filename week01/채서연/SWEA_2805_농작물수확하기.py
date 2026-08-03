t = int(input())
for case in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    result = 0
    for i in range(n//2+1):
        if i != n//2:
            result += sum(arr[i][n//2-i:n//2+i+1]) + sum(arr[n-1-i][n//2-i:n//2+i+1])
        elif i == n//2:
            result += sum(arr[i])
    
    print(f'#{case} {result}')
    
