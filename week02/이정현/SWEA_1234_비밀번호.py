T = 10

for test_case in range(1, T + 1):
    n, arr = input().split()
    n = int(n)
    arr = list(arr)
    stack = []

    for a in arr:
        if stack and stack[-1] == a:
            stack.pop()
        else:
            stack.append(a)

    print(f"#{test_case} {''.join(stack)}")