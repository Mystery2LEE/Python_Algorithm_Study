T = int(input())

for test_case in range(1, T + 1):
    arr = input().replace(" ", "").strip()

    stack = []
    correct = 1
    is_str = False

    for a in arr:
        if is_str:
            if a == '"' or a == "'":
                is_str = False
        else:
            if a == '"' or a == "'":
                is_str = True
                continue

            if a in "({":
                stack.append(a)

            elif a == ")":
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    correct = 0
                    break

            elif a == "}":
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    correct = 0
                    break

    if stack:
        correct = 0

    print(f"#{test_case} {correct}")