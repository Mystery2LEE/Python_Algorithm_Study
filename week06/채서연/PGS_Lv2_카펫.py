def solution(brown, yellow):
    total = brown + yellow
    c = int(total ** (1/2))
    r = 0
    while True:
        if total % c == 0:
            r = total // c
            if (r-2)*(c-2) == yellow:
                break
        c -= 1
    answer = [r, c]
    return answer