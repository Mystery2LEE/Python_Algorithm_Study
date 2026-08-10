T = 10

for test_case in range(1, T + 1):
    # 문자열 길이 입력
    count = int(input())
    # 기존 암호문 입력
    origin = list(input().split())
    # 명령문 길이 입력
    control_count = int(input())
    # 명령문 개수 입력
    control = list(input().split())
    # 인덱스 변수
    start = 0
    # 명령문 개수 만큼 반복
    for _ in range(control_count):
        # I, D, A 명령문 구별
        cmd = control[start]
        if control[start] == 'I':
            # I 명령문에 맞게 다음 명령문 시작 인덱스 설정
            end = start + int(control[start + 2]) + 3
            # 해당 명령문 부분 발췌
            part_c = control[start + 3:end]
            # 기존 문자열에 새로운 문자열 삽입
            origin[int(control[start + 1]):int(control[start + 1])] = part_c

        elif control[start] == 'D':
            # D 명령문에 맞게 다음 명령문 시작 인덱스 설정
            end = start + 3
            # 해당 인덱스에 있는 문자열 삭제
            del origin[int(control[start+1]):int(control[start+1])+int(control[start+2])]

        elif control[start] == 'A':
            end = start + int(control[start + 1]) + 2
            part_c = control[start + 2:end]
            # 리스트 맨뒤에 붙임
            origin.extend(part_c)

        start = end

    print(f"#{test_case}", ' '.join(map(str, origin[:10])))
