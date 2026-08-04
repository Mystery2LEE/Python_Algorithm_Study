for _ in range(10):
    n = int(input())
    arr = list(map(int, input().split()))
    
    while True:
        for i in range(1, 6):
            num = arr.pop(0) - i
            if num <= 0:
                arr.append(0)
                break
            arr.append(num)
        else:
            continue
        break
    
    print(f"#{n} {' '.join(map(str, arr))}")