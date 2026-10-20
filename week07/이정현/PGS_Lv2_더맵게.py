import heapq

def solution(scoville, K):
    # heap으로 리스트 변환
    heapq.heapify(scoville)
    # 최종 음식 혼합 횟수
    count = 0
    
    while True:
        # 가장 스코빌이 작은 값 pop
        s1 = heapq.heappop(scoville)
        # 가장 스코빌이 작은 값이 K보다 작을 때
        if s1 < K:
            # 만약 scovile에 남은 값이 없다면 -1 리턴
            if not scoville:
                return -1
            # 2번째로 스코빌이 작은 값 pop
            s2 = heapq.heappop(scoville)
            # 두 음식을 섞은 값 push
            heapq.heappush(scoville, s1 + (s2 * 2))
            # 횟수 증가
            count += 1
        # K보다 크다면 회수 리턴
        else:
            return count