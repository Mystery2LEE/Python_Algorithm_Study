T = int(input())

for test_case in range(1, T + 1):
    # 괄호 문자열 입력
    arr = list(input().strip())

    # 레이저의 유무와 현재 쇠막대임을 구별하기 위한 배열
    stack = []

    # 조각 수
    piece = 0

    # 입력 받은 문자열 순회
    for i in range(len(arr)):
        # 스택에 값이 있고 마지막 문자가 ')'인지 검증
        if arr[i] == ')':
            # stack의 마지막 문자가 '('인지 검증
            if stack and stack[-1] == '(':
                # 끝에있는 '(' 문자 제거
                stack.pop()
                # arr[i-1]이 '('인지 검증하여 레이저인지 검증
                if arr[i-1] == '(':
                    # stack에 있는 '(' 개수만큼 조각 수를 더해주고 레이저는 쇠막대가 아니기에 더했던 1을 빼준다
                    piece += len(stack)-1

        # '('일 경우 stack에 쌓고 쇠막대 끝부분을 고려해서 + 1
        else:
            stack.append(arr[i])
            piece += 1
    # 이 문제에서는 f-string이 안되서 format 사용
    print(f"#{test_case} {piece}")