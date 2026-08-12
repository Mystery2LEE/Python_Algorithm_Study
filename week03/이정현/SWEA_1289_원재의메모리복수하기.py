T = int(input())

for test_case in range(1, T + 1):
    # 최초 메모리 상태
    origin = list(input())
    # 메모리 길이
    length = len(origin)
    # 현재 메모리 상태
    curr = ['0' for _ in range(length)]

    count = 0
    for i in range(length):
        # 원래 메모리 상태와 현재 메모리 상태가 다르면
        if origin[i] != curr[i]:
            # 현재 메모리 상태를 원래 메모리 상태와 같게 바꿔주고, count 증가
            if curr[i] == '0':
                curr[i:length] = ['1' for _ in range(i, length)]
            else:
                curr[i:length] = ['0' for _ in range(i, length)]
            count += 1

    print(f"#{test_case} {count}")