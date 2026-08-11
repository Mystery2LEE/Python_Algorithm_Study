T = int(input())
for tc in range(1, T+1):
    n ,m, k = map(int, input().split())
    arr = list(map(int, input().split()))   

    idx = 0 # 처음 작업 위치
    for _ in range(k):
        idx += m

        # 인덱스 범위 벗어날 때
        if idx >= len(arr):
            idx %= len(arr)
        
        if idx == 0:
            value = arr[-1] + arr[0]
            arr.append(value)
            # 인덱스 조정해야함!!!!!!!!!!!!! 
            idx = len(arr) - 1

        else:
            value = arr[idx-1] + arr[idx]

            arr.insert(idx, value)

    count = 0
    print(f'#{tc}', end=" ")
    for i in range(len(arr)-1, -1, -1):
        if count == 10:
            break
        print(arr[i], end=" ")
        count+=1
    print()