T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    
    heap = [0]
    result = []
    
    for _ in range(N):
        line = list(map(int, input().split()))
        command = line[0]
        
        if command == 1:
            num = line[1]
            
            heap.append(num)
            idx = len(heap) - 1
            
            while idx > 1:
                parent = idx // 2
                
                if heap[parent] < heap[idx]:
                    heap[parent], heap[idx] = heap[idx], heap[parent]
                    idx = parent
                else:
                    break
            
        elif command == 2:
            if len(heap) == 1:
                result.append(-1)
                continue
            
            result.append(heap[1])
            heap[1] = heap[-1]
            heap.pop()
            
            idx = 1
            
            while True:
                left = idx * 2
                right = idx * 2 + 1
                
                if left >= len(heap):
                    break
                    
                bigger = left
                
                if right < len(heap) and heap[right] > heap[left]:
                    bigger = right
                    
                if heap[bigger] > heap[idx]:
                    heap[bigger], heap[idx] = heap[idx], heap[bigger]
                    idx = bigger
                else:
                    break
                
        
    print(f'#{tc}', *result)