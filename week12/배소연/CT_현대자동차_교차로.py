from collections import deque

N = int(input())
t = []
w = []

for _ in range(N):
    time, pos = input().split()
    t.append(int(time))
    w.append(pos)


# A, B, C, D 차선별 큐 생성
queues = [deque() for _ in range(4)]

# 차량을 각 차선에 배치
for i in range(N):
    pos = ord(w[i]) - ord("A")
    queues[pos].append((t[i], i))

# 각 차량의 통과 시간 (-1은 통과하지 못함)
answer = [-1] * N
time = 0

while any(queues):
    # 현재 시각에 대기 중인 차량 확인
    waiting = [False] * 4

    for i in range(4):
        if queues[i] and queues[i][0][0] <= time:
            waiting[i] = True

    # 4개 차선 모두 차량이 있다면 교착 상태
    if all(waiting):
        break

    # 대기 차량이 없다면 다음 차량 도착 시간으로 이동
    if not any(waiting):
        time = min(q[0][0] for q in queues if q)
        continue

    # 이번 초에 통과 가능한 차선
    passing = []

    for i in range(4):
        right = (i - 1) % 4

        if waiting[i] and not waiting[right]:
            passing.append(i)

    # 통과 가능한 차량 처리
    for i in passing:
        arrival, idx = queues[i].popleft()
        answer[idx] = time

    time += 1

for a in answer:
    print(a)
