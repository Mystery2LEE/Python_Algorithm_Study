T = int(input())

for test_case in range(1, T + 1):
    n, sixteen = map(str, input().split())
    result = []
    # 16진수 문자열을 2진수로 변환
    for s in sixteen:
        # 16진수 문자열을 10진수로 변환
        s = int(s, 16)
        # 10진수를 2진수로 변환하여 result에 추가
        for i in range(3, -1, -1):
            if s >= (1 << i):
                # 10진수에서 2진수로 변환한 값이 1이면 result에 1을 추가하고, s에서 2^i를 빼줌
                s = s - (1 << i)
                result.append(1)
            else:
                result.append(0)

    print(f"#{test_case}", ''.join(map(str, result)))

