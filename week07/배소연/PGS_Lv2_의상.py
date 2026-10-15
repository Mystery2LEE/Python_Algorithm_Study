import collections


def solution(clothes):
    counter = collections.Counter(kind for name, kind in clothes)
    answer = 1

    for count in counter.values():
        answer *= count + 1

    return answer - 1
