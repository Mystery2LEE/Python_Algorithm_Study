from collections import deque
def solution(targets):
    targets.sort(key=lambda x: x[1])
    target = deque(targets)
    s = target.popleft()
    count = 0
    while target:
        t = target.popleft()
        if s[1] > t[0]:
            continue
        else:
            s = t
            count += 1
    count += 1
    return count