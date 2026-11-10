def solution(want, number, discount):
    items = {}
    answer = 0
    for i in range(len(discount)):
        if discount[i] not in items:
            items[discount[i]] = 1
        else:
            items[discount[i]] += 1
        if i > 9:
            items[discount[i-10]] -= 1
    
        if i >= 9:
            is_true = True
            for w in range(len(want)):
                if want[w] not in items:
                    is_true = False
                    break
                if items[want[w]] < number[w]:
                    is_true = False
                    break
            if is_true:
                answer += 1
                
    return answer