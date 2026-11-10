from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    num = 0
    through = []
    end = len(truck_weights)
    wait = deque(truck_weights)
    in_bridge = deque()
    while in_bridge or wait:
        if not in_bridge:
            t = wait.popleft()
            in_bridge.append([t, time])
            num += t
        else:
            i, it = in_bridge[0]
            if time - it == bridge_length:
                through.append(in_bridge.popleft())
                num -= i
            if wait and (num + wait[0] <= weight):
                t = wait.popleft()
                in_bridge.append([t, time])
                num += t
        time += 1
    
    return time