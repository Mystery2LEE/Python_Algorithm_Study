import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        # 원소가 2개보다 작으면 갱신할 수 없음
        if len(scoville) < 2:
            return -1
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        if a < K:
            heapq.heappush(scoville, a+b*2)
            answer += 1

    
    return answer