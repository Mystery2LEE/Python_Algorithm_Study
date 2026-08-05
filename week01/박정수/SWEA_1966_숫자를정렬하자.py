def quickSort(arr, start, end):
    if start >= end :
        return
    
    mid = arr[(start + end) // 2]
    left = start
    right = end 
    
    while left <= right:
        while arr[left] < mid :
            left += 1
        while arr[right] > mid :
            right -= 1

        if left <= right:
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp
            left += 1
            right -= 1

    quickSort(arr, start, left - 1)
    quickSort(arr, left, end)

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))

    quickSort(arr, 0, N-1)

    print(f"#{test_case} {' '.join(map(str, arr))}")