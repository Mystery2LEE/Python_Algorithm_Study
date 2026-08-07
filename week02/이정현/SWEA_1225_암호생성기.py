from collections import deque

T = 10

for test_case in range(1, T + 1):
    # 정수값 입력
    tc = int(input())
    # 문자열 큐로 입력
    arr = deque(list(map(int, input().split())))
    # 뺄 값
    cycle = 0
    while arr[-1] > 0:
        # 싸이클 마다 1씩 올리다가 5를 넘으면 1로 초기화
        cycle = (cycle % 5 + 1)
        # 맨 앞에거 빼서 cycle을 빼고 다시 push
        l = arr.popleft()
        l -= cycle
        arr.append(l)
    if arr[-1] < 0:
        arr.pop()
        arr.append(0)


    print(f"#{tc}", ' '.join(map(str, arr)))