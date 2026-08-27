# 비트마스크
# 다시 한번 풀어볼것


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    count = 0
    for mask in range(1, 1<<n):
        sum_v = 0
        for i in range(n):
            if mask & (1<<i):
                sum_v += arr[i]
        if sum_v == k:
            count+=1
        

    print(f'#{test_case} {count}')
