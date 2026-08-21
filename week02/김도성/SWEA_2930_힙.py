T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())

    heap = []
    result = []
    for _ in range(n):
        arr = list(map(int, input().split()))
        if arr[0] == 1:
            heap.append(arr[1])
            index = len(heap) - 1
            while index > 0:
                if heap[index] > heap[(index - 1) // 2]:
                    n = heap[(index - 1) // 2]
                    heap[(index - 1) // 2] = heap[index]
                    heap[index] = n 
                    index = (index - 1) // 2
                else:
                    break
        else:
            if len(heap) == 0:
                result.append(-1)
            else:
                r = heap[-1]
                heap[-1] = heap[0]
                heap[0] = r
                result.append(heap.pop())
                index = 0
                while True:
                    left = 2 * index + 1
                    right = 2 * index + 2
                    if left >= len(heap):
                        break
                    if right >= len(heap):
                        if heap[left] > heap[index]:
                            n = heap[left]
                            heap[left] = heap[index]
                            heap[index] = n 
                            index = left
                        break
                    if heap[left] > heap[right]:
                        if heap[left] > heap[index]:
                            n = heap[left]
                            heap[left] = heap[index]
                            heap[index] = n 
                            index = left
                        else:
                            break
                    else:
                        if heap[right] > heap[index]:
                            n = heap[right]
                            heap[right] = heap[index]
                            heap[index] = n 
                            index = right
                        else:
                            break

    print(f'#{test_case}', *result)
