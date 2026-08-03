T = int(input())

for test_case in range(1, T + 1):
    k, n, m = map(int, input().split())
    water = list(map(int, input().split()))

    arr = [0 for _ in range(n+1)]
    for c in water:
        arr[c] = 1

    current = 0
    count = 0
    while current+k < n:
        check = True
        temp = 0
        
        for i in range(current+1, current+k+1):
            if arr[i] == 1:
                check = False
                temp = i
                
        current = temp
        count += 1
        if check:
            count = 0
            break

    print(f"#{test_case} {count}")