T = 10

for test_case in range(1, T + 1):
    buildings = int(input())
    arr = list(map(int, input().split()))

    loyal_floor = 0
    for i in range(2, buildings-1):
        if arr[i] > arr[i-1] and arr[i] > arr[i-2] and arr[i] > arr[i+1] and arr[i] > arr[i+2]:
            n = max(arr[i-1],arr[i-2],arr[i+1],arr[i+2])
            loyal_floor += arr[i] - n
        
    print(f"{test_case} {loyal_floor}")