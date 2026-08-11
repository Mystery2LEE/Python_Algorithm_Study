T = int(input())

for test_case in range(1, T + 1):
    # 중위 순회 방식 값 입력
    def inoder(seat, N, flower, counter):
        # 위치가 N을 벗어나면 값을 스킵
        if seat > N:
            return counter
        # 왼쪽부터 값을 넣음
        counter = inoder(2*seat, N, flower, counter)
        # 위치에 오면 counter + 1
        counter += 1
        # 위치에 따라 counter 값을 배열에 넣음
        flower[seat] = counter
        # 왼쪽과 루트 탐색이 끝나면 오른쪽 값 삽입
        counter = inoder(2*seat+1, N, flower, counter)
        return counter

    # 숫자 입력
    n = int(input())
    counter = 0
    flower = [0 for _ in range(n+1)]

    inoder(1, n, flower, counter)

    print(f"#{test_case} {flower[1]} {flower[n//2]}")