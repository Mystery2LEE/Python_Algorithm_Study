from collections import deque

T = int(input())

for test_case in range(1, T + 1):
    # 문자열 길이, 회전 횟수 입력
    n, m = map(int, input().split())
    # 문자열 큐로 입력
    arr = deque(list(input().split()))

    # 회전 수 만큼 FIFO를 시행
    for i in range(m):
        arr.append(arr.popleft())

    # 맨 왼쪽에 있는 것 출력
    print(f"#{test_case} {arr.popleft()}")