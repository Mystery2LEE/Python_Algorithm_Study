# gpt도움으로 풀었음
# 다시 풀어볼 것


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    nums, n = map(int, input().split())

    nums = list(str(nums))

    visited = set()
    max_value = 0

    def dfs(count):
        global max_value

        state = (count, ''.join(nums))

        if state in visited:
            return

        visited.add(state)

        if count == n:
            value = int(''.join(nums))
            if max_value < value:
                max_value = value
            return

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]

                dfs(count + 1)

                nums[i], nums[j] = nums[j], nums[i]

    dfs(0)

    print(f'#{test_case} {max_value}')

