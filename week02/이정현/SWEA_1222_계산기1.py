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

    # 최종 합 숫자
    num = 0

    # 문자열을 순환
    for a in arr:
        # 문자가 숫자인지 확인
        if a.isdigit():
            # 숫자면 후위표기식에 담음
            result.append(a)
        else:
            # 아니면 stack에 값이 있으면 pop해서 후위표기식에 담음
            if stack:
                result.append(stack.pop())
            stack.append(a)

    # 마지막이 숫자여서 연산자 하나가 stack에 남아있어서 pop 이후 후위표기식에 담음
    result.append(stack.pop())

    # 후위표기식에서 숫자는 스택에 쌓아 놓았다가 연산자가 나오면 뽑아서 더한다
    for r in result:
        if r.isdigit():
            stack.append(r)
        else:
            while stack:
                num += int(stack.pop())


    print("#{} {}".format(test_case, num))