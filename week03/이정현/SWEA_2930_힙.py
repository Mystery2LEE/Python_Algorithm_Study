import heapq

T = int(input())
# 결과값을 넣을 리스트
result = []

for test_case in range(1, T + 1):
    res = [f"#{test_case}"]
    n = int(input())
    heap = []
    for _ in range(n):
        cal = input().split()
        if cal[0] == '1':
            # 최대 힙을 구현하기 위해 입력 값에 -1을 곱해 heap에 push
            heapq.heappush(heap, -int(cal[1]))
        else:
            if heap:
                res.append(str(-heapq.heappop(heap)))
            else:
                res.append("-1")
    result.append(" ".join(res))
print("\n".join(result))