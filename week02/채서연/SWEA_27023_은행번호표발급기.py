t = int(input())
for tc in range(1, t+1):
    print(f'#{tc}', end=' ')
    m = int(input())
    arr = list(map(int,input().split()))
    queue = []
    count = 1
    for i in arr:
        if i == 1:
            queue.append(count)
            count += 1
        else:
            if queue:
                print(queue.pop(0), end=' ')
            else:
                print('empty', end=' ')
        
    print()