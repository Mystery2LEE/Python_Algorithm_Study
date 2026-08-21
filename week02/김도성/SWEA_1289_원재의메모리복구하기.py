T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    bit = list(map(int, input()))
    n = len(bit)

    arr = [0 for _ in range(n)]

    count = 0
    for i in range(n):
        if arr[i] != bit[i]:
            for j in range(i, n):
                arr[j] = bit[i]
            count += 1

    print(f'#{test_case} {count}')