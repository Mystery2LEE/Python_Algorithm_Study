for tc in range(1, 11):
    N = int(input())
    line = input().strip()
    
    postfix = []
    operator_stack = []
    
    priority = {
        '+': 1,
        '*': 2
    }
    
    for ch in line:
        if ch.isdigit():
            postfix.append(ch)
        elif ch == '(':
            operator_stack.append(ch)
        elif ch == ')':
            while operator_stack[-1] != '(':
                postfix.append(operator_stack.pop())

            operator_stack.pop()
        else:
            while (
                operator_stack
                and operator_stack[-1] != '('
                and priority[operator_stack[-1]] >= priority[ch]
            ):
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
            
            if ch == '+':
                calc_stack.append(a + b)
            elif ch == '*':
                calc_stack.append(a * b)
                
    answer = calc_stack.pop()
    
    print(f'#{tc}', answer)