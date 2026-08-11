for tc in range(1, 11):
    N, numbers = input().split()
    N = int(N)

    stack = []

    for num in numbers:
        if stack and stack[-1] == num:
            stack.pop()
        else:
            stack.append(num)

    password = ''.join(stack)

    print(f'#{tc} {password}')