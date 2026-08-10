for tc in range(1, 11):
    n= int(input())
    string = input()
    stack = []
    result = []

    for s in string:
        if s.isdigit():
            result.append(s)
        else:
            if stack:
                result.append(stack.pop())
                stack.append(s)
            else:
                stack.append(s)
    while stack:
        result.append(stack.pop())

    cal = []
    for x in result:
        if x.isdigit():
            cal.append(int(x))
        else:
            a = cal.pop()
            b = cal.pop()
            cal.append(a + b)
    
    answer = cal.pop()
    print(f'#{tc} {answer}')