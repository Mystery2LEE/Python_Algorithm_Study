T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    cards = input().split()
    mid = (N + 1) // 2
    
    part_a = cards[:mid]
    part_b = cards[mid:]
    
    new_arr = []
    
    for i in range(len(part_b)):
        new_arr.append(part_a[i])
        new_arr.append(part_b[i])

    if len(part_a) > len(part_b):
        new_arr.append(part_a[-1])
        
    print(f'#{tc}', end=' ')
    print(*new_arr)