T = int(input())

for test_case in range(1, T + 1):
    # 그래프 가로 길이
    c = int(input())
    # 블록 개수 배열 입력
    arr = list(map(int, input().split()))
    # 최대 값
    max_num = 0
    # 배열 순환
    for i in range(c):
        # 각 열 위치에 따른 최대 중력 값
        num = c - 1 - i
        # 행 오른 쪽으로 순환하면 해당 값보다 크거나 같으면 중력 값 - 1
        for j in range(i+1, c):
            if arr[i] <= arr[j]:
                num -= 1
        # 최대값 판정
        if num > max_num:
            max_num = num

    print(f"#{test_case} {max_num}")