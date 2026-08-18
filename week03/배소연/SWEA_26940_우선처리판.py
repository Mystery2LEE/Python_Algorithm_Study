T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    wait_num = list(map(int, input().split()))
    
    heap = [0]
    for num in wait_num:
        heap.append(num)
        idx = len(heap) - 1
    
        while idx > 1:
            parent = idx // 2
            
            if heap[parent] > heap[idx]:
                heap[parent], heap[idx] = heap[idx], heap[parent]
                idx = parent
            else:
                break
            
    answer = 0
    idx = N
    
    while idx > 1:
        idx //= 2
        answer += heap[idx]

    print(f'#{tc} {answer}')