def solution(k, tangerine):
    dict = {}
    for t in tangerine:
        if not t in dict:
            dict[t] = 1
        else:
            dict[t] += 1
            
    d = sorted(dict.items(), key=lambda x: x[1], reverse = True)
    
    answer = 0
    
    for _, count in d:
        k -= count
        answer += 1
        if k <= 0:
            break
            
    return answer