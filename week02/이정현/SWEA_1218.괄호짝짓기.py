T = 10

for test_case in range(1, T + 1):
    # 숫자 입력
    n = int(input())

    # 문자열 입력
    arr = list(input().strip())

    # 유효성 여부를 판단하는 변수
    c = 1

    # 값을 검증할 딕셔너리 생성
    check = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }

    # 값을 저장하며 검증할 리스트 생성
    stack = []

    # 문자열을 순회
    for a in arr:
        # 문자가 딕셔너리 내에 있는지 확인(열린 괄호 문자인지 확인)
        if a in check:
            # 맞으면 스택
            stack.append(a)
        else:
            # 아니면 (닫힌 문자), 마지막 문자를 가져옴
            s = stack[-1]
            # 마지막 문자가 입력 값과 쌍인지 확인
            if check[s] == a:
                # 맞으면 pop
                stack.pop()
            else:
                # 아니면 옳지 않은 문자열이여서 c = 0
                c = 0
                break
    # 만약 stack에 값이 남아 있으면 옳지 않은 문자열이니 c = 0
    if stack:
        c = 0

    print("#{} {}".format(test_case, c))
