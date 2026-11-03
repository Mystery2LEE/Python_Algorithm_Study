from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    sum1 = sum(q1)
    sum2 = sum(q2)
    
    total = sum1 + sum2
    
    if total % 2 != 0:
        return -1
    
    target = total // 2
    limit = 4 * len(queue1)
    
    for count in range(limit + 1):
        if sum1 == target:
            return count
        
        if sum1 > target:
            num = q1.popleft()
            q2.append(num)
            sum1 -= num
        else:
            num = q2.popleft()
            q1.append(num)
            sum1 += num
    
    return -1