def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []
    for i in range(n):
        # prices[stack[-1]]: 이전시점 prices[i]:현재시점
        # 현재 가격이 이전 시점보다 떨어지는 시간..들 계산해서 answer 갱신
        while stack and prices[stack[-1]] > prices[i]:
            idx = stack.pop()
            answer[idx] = i - idx
            
        # 아직 가격이 떨어지지 않은 인덱스
        stack.append(i)
        
    while stack:
        idx = stack.pop()
        answer[idx] = n - 1 - idx
    
    return answer
