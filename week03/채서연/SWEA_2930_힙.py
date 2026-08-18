# 최대힙

# 삽입
def insert(heap, item):
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
    if not heap:        
        return -1

    result = heap[0]
    heap[0] = heap[-1]
    heap.pop()
    
    if not heap:
        return result

    parent = 0
    while True:
        left = parent * 2 + 1
        right = parent * 2 + 2

        if left >= len(heap):
            break

        child = left

        if right < len(heap) and heap[right] > heap[left]:
            child = right

        if heap[parent] >= heap[child]:
            break

        heap[parent], heap[child] = heap[child], heap[parent]
        parent = child
    return result

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    heap = []
    result = []
    for _ in range(N):        
        cmd = list(map(int,input().split()))
        
        if cmd[0] == 1:
            insert(heap, cmd[1])
            
        else:
            result.append(delete(heap))
    print(f'#{tc}', *result)

# reuslt로 delete한 데이터 모아서 한번에 출력해야 시간초과 안 남