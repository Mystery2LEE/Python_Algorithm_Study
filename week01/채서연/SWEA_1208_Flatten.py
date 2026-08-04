for t in range(1, 11):
    dump = int(input())
    arr = list(map(int,input().split()))
    
    for _ in range(dump):
        if max(arr) == min(arr):
            print(f'#{t} 0')
            break
        min_idx = arr.index(min(arr))
        max_idx = arr.index(max(arr))
        arr[min_idx] += 1
        arr[max_idx] -= 1
        
    print(f'#{t} {max(arr)-min(arr)}')