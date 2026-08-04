T = int(input())

for test_case in range(1, T + 1):
    # 숫자의 수 입력
    n = int(input().strip())

    # 숫자를 입력 받을 배열
    stack = []

    # 숫자 수 만큼 값을 입력 받음
    for _ in range(n):
        # 스텍 내에 값이 있고 현재 입력 받는 값이 0이면 pop
        a = int(input().strip())
        if stack and a == 0:
            stack.pop()
        # 그렇지 않으면 리스트에 값을 추가
        else:
            stack.append(a)

    # sum을 이용해서 리스트 값을 더해 출력
    print(f"#{test_case} {sum(stack)}")