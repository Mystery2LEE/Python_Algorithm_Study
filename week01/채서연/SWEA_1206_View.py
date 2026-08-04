for t in range(1, 11):
    result = 0
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(2,n-2):
        if arr[i]>arr[i-1] and arr[i]>arr[i-2] and arr[i]>arr[i+1] and arr[i]>arr[i+2]:
            result+=arr[i]-max(arr[i-2],arr[i-1],arr[i+1], arr[i+2])
    
    print(f'#{t} {result}')