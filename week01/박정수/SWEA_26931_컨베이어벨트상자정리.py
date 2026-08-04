T = int(input())
for test_case in range(1, T + 1):
    s = input()
    stack = []

    for i in range(len(s)):
        c = s[i]
        if not stack :
            stack.append(c)
            continue

        if c == stack[-1]:
            stack.pop()
        else :
            stack.append(c)
    
    print(f"#{test_case} {len(stack)}")