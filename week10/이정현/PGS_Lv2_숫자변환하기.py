def solution(x, y, n):
    nums = [y]
    answer = 0
    while x not in nums:
        is_big = True
        answer += 1
        tmp = set()
        for ns in nums:
            if ns % 2 == 0:
                if x <= (ns//2):
                    tmp.add(ns // 2)
                    is_big = False
            if ns % 3 == 0:
                if x <= (ns//3):
                    tmp.add(ns // 3)
                    is_big = False
            if x <= ns - n:
                tmp.add(ns - n)
                is_big = False
        nums = tmp
        if is_big:
            return -1
    return answer