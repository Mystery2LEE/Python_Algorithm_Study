T = int(input())

for test_case in range(1, T + 1):
    # 곡의 개수, 편집 횟수, 자리 번호 입력
    n, m, l = map(int, input().split())
    # 곡 ID 입력
    origin = list(input().split())

    for _ in range(m):
        # 명령어 입력
        control = list(input().split())
        # I 일때 x 위치에 y값 삽입
        if control[0] == 'I':
            x = int(control[1])
            y = int(control[2])
            origin[x:x] = [y]
        # D일 때 x위치 삭제
        elif control[0] == 'D':
            x = int(control[1])
            del origin[x]
        # C일 때 x위치 삭제후 y 삽입
        elif control[0] == 'C':
            x = int(control[1])
            y = int(control[2])
            del origin[x]
            origin[x:x] = [y]
    # origin의 길이가 l보다 길 때 값 출력 작을 때 -1 출력
    if len(origin) > l:
        print(f"#{test_case} {origin[l]}")
    else:
        print(f"#{test_case} -1")