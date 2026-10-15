import math
from collections import deque


def solution(progresses, speeds):
    answer = []
    days_left = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]
    days_deque = deque(days_left)

    while days_deque:
        max_day = days_deque.popleft()
        count = 1

        while days_deque and days_deque[0] <= max_day:
            days_deque.popleft()
            count += 1

        answer.append(count)

    return answer
