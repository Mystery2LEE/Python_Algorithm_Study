def binary_search_count(P, target):
    l = 1
    r = P
    count = 0

    while True:
        count += 1
        c = (l + r) // 2

        if c == target:
            return count
        elif c < target:
            l = c
        else:
            r = c


T = int(input())

for tc in range(1, T + 1):
    P, A, B = map(int, input().split())

    a_count = binary_search_count(P, A)
    b_count = binary_search_count(P, B)

    if a_count < b_count:
        result = 'A'
    elif a_count > b_count:
        result = 'B'
    else:
        result = '0'

    print(f'#{tc} {result}')