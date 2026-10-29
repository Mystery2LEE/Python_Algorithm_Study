from collections import deque

def solution(queue1, queue2):
    count = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    q1_sum = sum(q1)
    q2_sum = sum(q2)
    if (q1_sum + q2_sum) % 2 == 1:
        return -1
    half = (q1_sum + q2_sum) // 2
    while q1_sum != q2_sum:
        while q2 and q2_sum > half:
            l = q2.popleft()
            q1.append(l)
            q2_sum -= l
            q1_sum += l
            count += 1
        while q1 and q1_sum > half:
            l = q1.popleft()
            q2.append(l)
            q1_sum -= l
            q2_sum += l
            count += 1  
        if count > 4*len(queue1):
            return -1
    return count