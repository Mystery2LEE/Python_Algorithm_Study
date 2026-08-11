for tc in range(1, 11):
    n = int(input())
    string = input()
    result = []
    stack = []
    cal = []
    # 후위식 변환
    for s in string:
        if s.isdigit():
            result.append(s)
        else:
            if s == '(':
                stack.append(s)
            elif s == ')':
                while True:
                    item = stack.pop()
                    if item != '(':
                        result.append(item)
                    else:
                        break
            else:
                while stack and stack[-1] !='(':
                # 현재 연산자보다 스택 연산자의 우선순위가 높으면 pop
                    if (s == '+' and stack[-1] in '*/+') or (s == '*' and stack[-1] == '*'):
                        result.append(stack.pop())
                    else:
                        break
                # 여는 괄호일 때는 스택에 바로 넣기
                stack.append(s)

    while stack:
        result.append(stack.pop())

    # 계산
    for x in result:
        if x.isdigit():
            cal.append(int(x))
        else:
            a = cal.pop()
            b = cal.pop()
            if x == '+':
                cal.append(a + b)
            else:
                cal.append(a * b)
        
    answer = cal.pop()
    print(f'#{tc} {answer}')