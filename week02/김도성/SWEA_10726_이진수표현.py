T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int, input().split())

    arr = []
    while m > 0:
        result = m // 2
        remainder = m % 2
        arr.append(remainder)
        m = result


    bit = 'ON'
    if len(arr) < n:
        bit = 'OFF'
    else:
        for i in range(n):
            if arr[i] == 0:
                bit = 'OFF'


    print(f'#{test_case} {bit}')