from collections import deque

T = int(input())

for test_case in range(1, T + 1):
    # 로스팅 기기 크기, 바구니 총 개수 입력
    n, m = map(int, input().split())
    # 수분량 입력
    water = deque(list(map(int, input().split())))
    # 로스트 기기 큐
    roast = deque()
    # 순서 큐
    turn = deque()
    # 순서 큐에 새로운 값 추가 시 더해줄 변수
    k = 1
    
    # 수분량에서 n 크기 만큼 로스트 기기 큐에 넣어줌
    for i in range(n):
        roast.append(water.popleft())
        # 1~n 까지 순서를 순서 큐에 더해줌
        turn.append(i+1)
    
    # 로스트 기기에 값이 1개 남을 때까지 반복
    while len(roast) > 1:
        # 로스트 기기의 맨 앞 수분량을 빼서 2로 나눔
        r = roast.popleft() // 2
        # 바구니 순서를 같이 추출
        t = turn.popleft()
        # 2로 나눈 수분량이 0보다 크다면 다시 맨뒤로, 순서도 같이 맨 뒤로
        if r > 0:
            roast.append(r)
            turn.append(t)
        # 수분량이 0이면 수분량과 바구니 순서 제외
        else:
            # 수증기가 남아있다면
            if water:
                # 로스트기기에 추가
                roast.append(water.popleft())
                # 바구니 순서도 순서에 추가
                turn.append(n+k)
                # k를 이용해서 바구니 순서 값 증가
                k += 1

    print(f"#{test_case} {turn.pop()}")