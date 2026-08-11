from collections import deque

for _ in range(10):
    T = int(input())
    data = list(map(int, input().split()))
    
    queue = deque(data)
    count = 1
    
    while queue[-1] > 0:
        if count > 5:
            count = 1
        
        num = queue.popleft()
        queue.append(num - count)
        
        if queue[-1] <= 0:
            queue[-1] = 0
        
        count += 1
        
    print(f'#{T}', *queue)