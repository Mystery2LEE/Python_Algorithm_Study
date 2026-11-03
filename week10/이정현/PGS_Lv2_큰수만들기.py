from collections import deque

def solution(number, k):
    answer = []
    count = 0
    
    if len(number) <= k:
        return '0'
    
    for n in number:
        if not answer:
            answer.append(n)
        else:
            if k > 0:
                while answer and answer[-1] < n:
                    answer.pop()
                    k -= 1
                    if k == 0:
                        break
                    
                answer.append(n)
            else:
                answer.append(n)
                
    while k > 0:
        answer.pop()
        k -= 1
                
                
    return ''.join(map(str, answer))