from collections import deque

def solution(topping):
    to = deque(topping)
    answer = 0
    r_type = {}
    for t in topping:
        if t not in r_type:
            r_type[t] = 1
        else:
            r_type[t] += 1
    
    l_type = {}
    for t in topping:
        if t not in l_type:
            l_type[t] = 1
        r_type[t] -= 1
        if r_type[t] == 0:
            r_type.pop(t)
        if len(l_type) == len(r_type):
            answer += 1
    
    return answer