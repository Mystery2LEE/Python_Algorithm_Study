for tc in range(1, 11):
    N = int(input()) #문자열 계산식의 길이
    line = input().strip()
    
    postfix = []
    operator_stack = []
    
    for ch in line:
        if ch.isdigit():
            postfix.append(ch)
        else:
            if operator_stack:
                postfix.append(operator_stack.pop())
            operator_stack.append(ch)
            
    while operator_stack:
        postfix.append(operator_stack.pop())
    
    
    calc_stack = []
    
    for ch in postfix:
        if ch.isdigit():
            calc_stack.append(int(ch))
        else:
            b = calc_stack.pop()
            a = calc_stack.pop()
            
            calc_stack.append(a + b)

    answer = calc_stack.pop()
    
    print(f'#{tc}', answer)