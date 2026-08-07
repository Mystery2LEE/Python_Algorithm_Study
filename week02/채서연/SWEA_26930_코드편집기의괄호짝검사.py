t = int(input())
for tc in range(1, t + 1):
    # 괄호가 올바르면 1, 아니면 0
    result = 0
    stack = []
    string = input()
    count = 0
    for s in string:
        count += 1
        # 여는 괄호 나왔을 때 일단 스택에 넣음
        if s == "(" or s == "{":
            stack.append(s)
    
        # 닫는 괄호 나왔을 때 스택 마지막 요소가 같은 타입의 여는 괄호면 pop, 아니면 break 
        elif s == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                break
        elif s == "}":
            if stack and stack[-1] == "{":
                stack.pop()
            else:
                break
        if len(string) == count and len(stack) == 0:
            result = 1
    print(f'#{tc} {result}')