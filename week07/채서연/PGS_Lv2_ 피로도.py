from itertools import permutations

def solution(k, dungeons):
    n = len(dungeons)
    answer = 0
    
    for arr in permutations(dungeons):
        remain = k
        num = 0
        for x, y in arr:
            if remain >= x:
                remain -= y
                num += 1
            else:
                break
        answer = max(answer, num)
        if answer == n:
            break

    return answer