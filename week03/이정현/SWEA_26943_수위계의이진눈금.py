T = int(input())

for test_case in range(1, T + 1):
    n = float(input())
    num = 0
    result = []
    can = False
    for i in range(1,13):
        # 1/2^i를 더해가며 n과 비교
        num += 1 / (1 << i)
        # 1/2^i를 더한 값이 n보다 작거나 같으면 1을, 크면 0을 result에 추가
        if num <= n:
            result.append(1)
        # 1/2^i를 더한 값이 n보다 크면 0을 result에 추가하고, num에서 1/2^i를 빼줌
        else:
            num -= 1 / (1 << i)
            result.append(0)
        if num == n:
            can = True
            break
    if can:
        print(f"#{test_case}", "".join(map(str, result)))
    else:
        print(f"#{test_case}", "overflow")
