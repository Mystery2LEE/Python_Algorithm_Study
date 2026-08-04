for t in range(1, 11):
    length = int(input())
    string = input()
    result = []
    stack =[]
    
    # 후위식으로 변환
    for s in string:
        # 숫자는 바로 result에 넣기
        if s.isdigit():
            result.append(s)
        # 연산자
        elif s == '(':
            stack.append(s)
        elif s == ')':
            # 닫는 괄호 나올 때까지 pop해서 result에 추가
            while True:
                item = stack.pop()
                if item == '(':
                    break
                result.append(item)
        else:
            # 스택에 요소가 존재하고 ...
            while stack and stack[-1] != '(':
                # 현재 연산자보다 스택 연산자의 우선순위가 높으면 pop
                if (s == '+' and stack[-1] in '*/+') or (s == '*' and stack[-1] == '*'):
                    result.append(stack.pop())
                else:
                    break
            stack.append(s)
            
    while stack:
        result.append(stack.pop())

    # 계산
    calc_stack = []

    for s in result:
        # 숫자
        if s.isdigit():
            calc_stack.append(int(s))
        # 연산자
        else:
            b = calc_stack.pop()
            a = calc_stack.pop()
            if s == '+':
                calc_stack.append(a + b)
            elif s == '*':
                calc_stack.append(a * b)

    answer = calc_stack.pop()
    
    print(f'#{t} {answer}')
