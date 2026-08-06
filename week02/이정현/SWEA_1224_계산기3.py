T = 10

for test_case in range(1, T + 1):
    # 배열 길이 입력
    n = int(input())

    # 문자열 입력
    arr = list(input().strip())

    # 후위표기식을 담을 리스트
    result = []

    # 연산자를 담을 리스트
    stack = []

    # 연산자 우선순위를 나타내는 딕셔너리
    check = {
        '*': 2,
        '+': 1
    }
    # 최종 합 숫자

    # 문자열을 순환
    for a in arr:
        # 문자가 숫자인지 확인
        if a.isdigit():
            # 숫자면 후위표기식에 담음
            result.append(a)
            # 열린 괄호면 스택에 담음
        elif a == '(':
            stack.append(a)
            # 닫힌 괄호면 열린 괄호가 나올때 까지 연산자 pop후 후위표기식에 담음
        elif a == ')':
            while stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()  # 연산자 스택에 남은 '(' 제거
        # 괄호를 제외한 문자는 두 연산자의 우선순위를 비교해서 입력하는 연산자의 우선순위가
        # stack[-1]의 연산자의 우선 순위보다 높으면 stack에 push하고 작으면 하나를 꺼내서 
        # 후위표기식에 push후 stack에 담음
        else:
            while stack and stack[-1] != '(' and check[stack[-1]] >= check[a]:
                result.append(stack.pop())
            stack.append(a)

    # 스택에 남아있는 연산자 pop 이후 후위표기식에 담음
    while stack:
        result.append(stack.pop())

    # 계산을 위한 스택 리스트
    eval_stack = []

    # 후위표기식에서 숫자는 스택에 쌓아 놓았다가 연산자가 나오면 2개의 숫자를 뽑아서 더한다
    for r in result:
        if r.isdigit():
            eval_stack.append(int(r))
        else:
            b = eval_stack.pop()
            a = eval_stack.pop()
            if r == '+':
                eval_stack.append(a + b)
            else:  # '*'
                eval_stack.append(a * b)
    num = eval_stack.pop()

    print("#{} {}".format(test_case, num))