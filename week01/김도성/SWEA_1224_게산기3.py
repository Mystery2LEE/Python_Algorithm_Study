# 다시한번 복습 필요

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    arr = list(input())


    stack = [0]
    sub_stack = [0]
    for a in arr:
        if a.isdigit():
            stack.append(a)
        else:
            if a == '+':
                if sub_stack[-1] == '+':
                    stack.append(a)
                elif sub_stack[-1] == '*':
                    b = sub_stack.pop()
                    while b == '*':
                        stack.append(b)
                        b = sub_stack.pop()
                    if b == '+':
                        stack.append(b)
                    else:
                        sub_stack.append(b)
                    sub_stack.append(a)
                else:
                    sub_stack.append(a)
            elif a == '*':
                if sub_stack[-1] == '+':
                    sub_stack.append(a)
                elif sub_stack[-1] == '*':
                    stack.append(a)
                else:
                    sub_stack.append(a)
            elif a == '(':
                n -= 1
                sub_stack.append(a)
            elif a == ')':
                n -= 1
                b = sub_stack.pop()
                while b != '(':
                    stack.append(b)
                    b = sub_stack.pop()
    while sub_stack[-1] != 0:
        stack.append(sub_stack.pop())
    stack.pop(0)
    
    cal_stack = []
    for i in range(n):
        if stack[i].isdigit():
            cal_stack.append(stack[i])
        else:
            if stack[i] == '+':
                a = int(cal_stack.pop())
                b = int(cal_stack.pop())
                cal_stack.append(a+b)
            elif stack[i] == '*':
                a = int(cal_stack.pop())
                b = int(cal_stack.pop())
                cal_stack.append(a*b)


    print(f'#{test_case} {cal_stack[0]}')
