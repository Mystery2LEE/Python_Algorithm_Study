# 최소힙
def insert(heap, x):
    heap.append(x)
    idx = len(heap) - 1
    while idx > 0:
        parent = (idx-1)//2
        if heap[parent] > heap[idx]:
            heap[parent], heap[idx] = heap[idx], heap[parent]
            idx = parent
        else:
            break
        
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    heap = []
    result = 0
    for x in num_list:
        insert(heap, x)

    # 합 구하기
    idx = (len(heap) - 2)//2
    while idx >= 0:  
        result += heap[idx]
        idx = (idx-1)//2
    print(f'#{tc} {result}')