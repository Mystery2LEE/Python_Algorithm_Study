T = int(input())
for tc in range(1, T+1):
    string = input().strip() # strip 안해서 틀림....
    stack = []
    for s in string:
        if stack and stack[-1] == s:
            stack.pop()
            continue
        stack.append(s)
    print(f'#{tc} {len(stack)}')