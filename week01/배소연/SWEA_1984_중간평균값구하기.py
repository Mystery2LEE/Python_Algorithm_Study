T = int(input())
 
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    arr.sort()
    average = round(sum(arr[1:-1]) / 8)
     
    print(f'#{tc} {average}')