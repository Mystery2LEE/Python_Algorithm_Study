T = int(input())
for tc in range(1, T+1):
    n, m, l = map(int, input().split())  
    arr = list(map(int, input().split()))
   
    for _ in range(m):
        p, v = map(int,input().split())
        arr.insert(p, v)
    print(f'#{tc} {arr[l]}')
    