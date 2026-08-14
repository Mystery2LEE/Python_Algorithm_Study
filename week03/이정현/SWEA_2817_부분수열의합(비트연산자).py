T = int(input())

for test_case in range(1, T + 1):
    # 입력값 받기
    n, k = map(int, input().split())
    # n개의 수를 리스트로 받기
    arr = list(map(int, input().split()))
    count = 0
    # 부분집합의 합이 k가 되는 경우의 수를 구하기 위해 2^n개의 부분집합을 생성
    for i in range(1 << n):
        num = 0
        # 각 부분집합의 합을 구하기 위해 비트 연산을 사용하여 부분집합에 포함된 수를 더함
        for j in range(n):
            # i의 j번째 비트가 1이면 arr[j]를 더함
            if i & (1 << j):
                num += arr[j]
        if num == k:
            count += 1

    print(f"#{test_case} {count}")