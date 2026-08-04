T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().strip())) for _ in range(N)]

    mid = N // 2
    total = 0

    for i in range(N):
        for j in range(N):
            #맨해튼 거리로 가자 
            if abs(mid - i) + abs(mid - j) <= mid :
                total += arr[i][j]
            
    print(f"#{test_case} {total}")