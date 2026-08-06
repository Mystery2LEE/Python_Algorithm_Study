from collections import deque

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    print(f"#{test_case}", end=" ")
    # 숫자를 입력
    m = int(input())
    # 번호표 입력
    arr = list(map(int, input().split()))
    # qeue 생성
    data = deque()
    # 번호표 초기 번호
    num = 1

    for a in arr:
        # 호출 숫자가 1이면 번호표를 qeue에 push하고 num += 1
        if a == 1:
            data.append(num)
            num += 1
        # 호출 숫자가 2면 qeue에서 맨 왼쪽 것을 빼고 출력
        else:
            print(data.popleft(), end=" ")
    # 한 싸이클이 끝나면 줄바꾸기
    print()