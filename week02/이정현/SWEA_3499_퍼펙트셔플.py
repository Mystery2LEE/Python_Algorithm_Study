from collections import deque

T = int(input())

for test_case in range(1, T + 1):
    # 카드 개수 입력
    n = int(input())
    # 최초 카드 순서 리스트
    start = deque((input().split()))
    # 첫번째 카드 순서 리스트
    card1 = deque()
    # 두번째 카드 순서 리스트
    card2 = deque()
    # 최종 결과를 담을 리스트
    result = []
    # n//2 만큼 최초 카드 순서리스트 맨 왼쪽부터 빼서 card1 리스트에 넣음
    # 카드 개수가 홀수면 card1리스트에 1개를 더 넣음
    if n % 2 == 1:
        for i in range(n//2+1):
                card1.append(start.popleft())
    else:
        for i in range(n//2):
                card1.append(start.popleft())

    # card2 리스트에 넣음
    for i in range(n//2):
            card2.append(start.popleft())

    # card2에 값이 있을때까지 번갈아 가면서 결과 리스트에 push
    while card2:
        result.append(card1.popleft())
        result.append(card2.popleft())
    # 홀수인 경우 card1에 값이 남아있으므로 빼서 결과 리스트에 넣음
    if card1:
        result.append(card1.popleft())
    
    print(f"#{test_case}", ' '.join(map(str, result)))
