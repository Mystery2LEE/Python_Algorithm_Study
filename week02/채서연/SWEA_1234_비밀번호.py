for tc in range(1, 11):
    n, pwd = input().split()
    stack = []
    for p in pwd:
        if stack and stack[-1] == p:
            stack.pop()
        else:
            stack.append(p)
    result = ''.join(stack)        
            
    print(f'#{tc} {result}')