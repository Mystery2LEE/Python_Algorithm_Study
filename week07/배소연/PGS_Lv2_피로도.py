from itertools import permutations


def solution(k, dungeons):  # k: 현재 피로도, dungeons:최소필요피로도/소모피로도
    answer = 0

    for order in permutations(dungeons):
        energy = k
        count = 0

        for need, spend in order:
            if energy >= need:
                energy -= spend
                count += 1

        answer = max(answer, count)

    return answer
