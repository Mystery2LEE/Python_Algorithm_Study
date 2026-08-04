T = int(input())

for test_case in range(1, T + 1):
    # 문자열 입력
    arr = list(input().strip())
    # 문자열을 담을 스택
    stack = []

    # 문자열을 스택에 다시 담으면서 상자 쌍 검증
    for c in arr:
        # 스택에 값이 존재하고 마지막 값이 같은면 pop으로 문자쌍 추출
        if stack and stack[-1] == c:
            stack.pop()
        # 문자쌍이 아니면 스택에 쌓음
        else:
            stack.append(c)

    # 문자열에 남은 글자 수 len을 이용해 출력
    print(f"#{test_case} {len(stack)}")