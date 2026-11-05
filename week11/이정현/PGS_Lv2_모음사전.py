def solution(word):
    alpha = ['A', 'E', 'I', 'O', 'U']
    dict = set()
    for w1 in alpha:
        dict.add(w1)
        for w2 in alpha:
            dict.add(w1+w2)
            for w3 in alpha:
                dict.add(w1+w2+w3)
                for w4 in alpha:
                    dict.add(w1+w2+w3+w4)
                    for w5 in alpha:
                        dict.add(w1+w2+w3+w4+w5)
                        
    dict = list(dict)
    answer = sorted(dict).index(word) + 1
    return answer