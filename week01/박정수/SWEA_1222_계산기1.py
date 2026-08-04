# T = int(input())
T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    S = input()

    backOrder = []
    stack = []
    for i in range(N):
        c = S[i]
        if c.isdigit():
            backOrder.append(c)
        else :
            if stack :
                backOrder.append(stack.pop())
                stack.append(c)
            else :
                stack.append(c)

    while stack :
        backOrder.append(stack.pop())

    for i in range(N) :
        c = backOrder[i]
        if not c.isdigit() :
            num1 = int(stack.pop())
            num2 = int(stack.pop())
            stack.append(num1+num2)
        else :
            stack.append(c)

    print(f"#{test_case} {stack.pop()}")