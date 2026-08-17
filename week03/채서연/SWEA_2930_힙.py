# 최대힙

# 삽입
def insert(item):
    global heap
    heap.append(item)
    idx = len(heap) -1
    
    while idx > 0:
        parent = (idx - 1) // 2
        if heap[parent] < heap[idx]:
            heap[parent], heap[idx] = heap[idx], heap[parent]
            idx = parent
        else:
            break
#삭제
def delete(heap):
    heap_size = len(heap)
    if not heap:
        print(-1, end=' ')
    elif len(heap) <= 2:
        print(heap.pop(), end=' ')
    else:
        heap[0], heap[-1] = heap[-1], heap[0]
        print(heap.pop(), end=' ')
        parent = 0
        left = parent*2 + 1
        right = parent*2 + 2
        while True:
            if left < heap_size and heap[parent] < heap[left]:
                pass
            
        


T = int(input())
for tc in range(1, T+1):
    cmd = list(map(int,input().split()))
    heap = []
    # 삽입
    if cmd[0] == 1:
        insert(cmd[1])
        
    # 최댓값(루트) 출력 후 해당 키값 삭제
    else:
        delete(heap)
    print(f'#{tc}')
