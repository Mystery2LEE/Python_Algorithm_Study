def solution(brown, yellow):
    answer = []
    total = brown + yellow

    for brown_h in range(3, int(total**0.5) + 1):
        if total % brown_h == 0:
            brown_w = total // brown_h

            if brown_w < brown_h:
                break

            if yellow == (brown_w - 2) * (brown_h - 2):
                answer.append(brown_w)
                answer.append(brown_h)

    return answer
