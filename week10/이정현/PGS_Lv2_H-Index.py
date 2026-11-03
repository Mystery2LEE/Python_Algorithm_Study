def solution(citations):
    n = len(citations)
    h = n
    citations.sort()
    for i in range(n):
        if h <= citations[i]:
            break
        h -= 1
    return h