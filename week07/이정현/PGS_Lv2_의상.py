def solution(clothes):
    cdict = {}
    for c, t in clothes:
        if t not in cdict:
            cdict[t] = []
        cdict[t].append(c)
        
    num = 1
    for c in cdict:
        num *= len(cdict[c]) + 1
        
    return num - 1