T = int(input())

for test_case in range(1, T + 1):
    N,M,L = map(int, input().split())

    arr = list(map(int, input().split()))

    for i in range(M):
        p, v = map(int, input().split())

        arr.insert(p, v)

    print(f'#{test_case} {arr[L]}')