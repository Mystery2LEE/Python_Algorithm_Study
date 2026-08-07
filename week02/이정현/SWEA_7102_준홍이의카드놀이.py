T = int(input())

for test_case in range(1, T + 1):
    # 카드 수 입력
    n, m = map(int, input().split())
    # 둘 중 작은 수 구별
    num = min(n, m)
    # 결과 값을 담을 리스트
    result = []
    # 두 수 중 작은 값에 1을 더한 수 부터 작은 값 + |n-m| + 1 한 값까지가 가장 확률 높은 수
    for i in range(num+1, num+(abs(n-m)+2)):
        result.append(i)

    print(f"#{test_case}", ' '.join(map(str, result)))
