def solve():
    N, L = map(int, input().split())
    burgers = []

    for _ in range(N):
        taste, calorie = map(int, input().split())
        burgers.append((taste, calorie))

    max_taste = 0

    def dfs(idx, taste_sum, calorie_sum):
        nonlocal max_taste

        if calorie_sum > L:
            return

        max_taste = max(max_taste, taste_sum)

        if idx == N:
            return

        taste, calorie = burgers[idx]

        # 현재 재료 선택
        dfs(
            idx + 1,
            taste_sum + taste,
            calorie_sum + calorie
        )

        # 현재 재료 선택하지 않음
        dfs(
            idx + 1,
            taste_sum,
            calorie_sum
        )

    dfs(0, 0, 0)

    return max_taste


T = int(input())

for tc in range(1, T + 1):
    answer = solve()
    print(f'#{tc} {answer}')