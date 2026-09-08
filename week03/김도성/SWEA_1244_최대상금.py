T = int(input())

for tc in range(1, T + 1):
    n, c = map(int, input().split())

    n = list(map(int, str(n)))

    max_result = 0
    visited = set()

    def f_s(cha):
        global max_result

        state = (tuple(n), cha)

        if state in visited:
            return

        visited.add(state)

        m = len(n)
        result = 0

        if cha <= 0:
            result = int(''.join(map(str, n)))
            max_result = max(result, max_result)
            return

        for i in range(m-1):
            for j in range(i + 1, m):
                n[i], n[j] = n[j], n[i]
                f_s(cha - 1)
                n[i], n[j] = n[j], n[i]

    f_s(c)

    print(f'#{tc} {max_result}')