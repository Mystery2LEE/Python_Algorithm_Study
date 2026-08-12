import heapq

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    # heaq를 통해 값을 입력
    heap = []
    # heap에 값을 푸쉬
    for a in arr:
        heapq.heappush(heap, a)
    # 마지막값 인덱스를 찾는다
    h = heap.index(heap[-1]) + 1
    num = 0
    # 루트 값 까지 순환하며 그 라인에 있는 값을 찾는다
    while h != 1:
        # 자식 노드 인덱스에 2로 나눈 몫이 부모 노드의 인덱스
        h = h // 2
        num += heap[h-1]

    print(f"#{test_case} {num}")