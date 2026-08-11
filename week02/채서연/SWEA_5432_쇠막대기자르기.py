T = int(input())
for tc in range(1, T + 1):
    # 레이저 표시인 괄호는 L로 변경해서 저장
    str = input().replace('()', 'L')
    result = 0
    stack = []
    for s in str:
        if s == "(":
            stack.append(s)
        elif s == 'L':
            result += len(stack)
        # 
        elif s== ')':
            if stack and stack[-1] == '(':
                stack.pop()
                result += 1


    print(f'#{tc} {result}')