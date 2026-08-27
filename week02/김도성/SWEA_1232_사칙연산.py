# gpt도움으로 풀었음
# 다시 한번 풀어볼것

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())

    tree = [None] * (n+1)
    for _ in range(n):
        arr = input().split()
        index = int(arr.pop(0))
        if len(arr) == 3:
            arr[1] = int(arr[1])
            arr[2] = int(arr[2])
            tree[index] = arr
        else:
            tree[index] = int(arr[0])

    def calculate(index):
        if isinstance(tree[index], int):
            return tree[index]

        left = tree[index][1]
        right = tree[index][2]

        left_value = calculate(left)
        right_value = calculate(right)

        cal = tree[index][0]

        if cal == '+':
            return left_value + right_value
        elif cal == '-':
            return left_value - right_value
        elif cal == '*':
            return left_value * right_value
        elif cal == '/':
            return left_value / right_value

    result = calculate(1)


    print(f'#{test_case} {int(result)}')

