from collections import deque
N = int(input())
t = []
w = []

for _ in range(N):
    time, pos = input().split()
    t.append(int(time))
    w.append(pos)

answer = [-1] * N
q = [deque() for _ in range(4)]
for i in range(N):
    if w[i] == 'A':
        q[0].append((t[i], i))
    if w[i] == 'B':
        q[1].append((t[i], i))
    if w[i] == 'C':
        q[2].append((t[i], i))
    if w[i] == 'D':
        q[3].append((t[i], i))

# 현재 시간
curr_time = min(t)
# 남은 차량 수
remain = N
while remain > 0:
    # 현재 차선에 대기중인 차가 있는지
    waiting = [False] * 4

    # 차선의 첫번째 차의 도착 시간이 현재 시간보다 작거나 같으면 대기중
    for i in range(4):
        if q[i] and q[i][0][0] <= curr_time:
            waiting[i] = True

    # 대기 중인 차량이 없다면 다음 시간으로 이동
    if not any(waiting):
        # 각 차선의 첫번째 차 도착 시간 중 제일 빠른 시간
        next_times = [q[i][0][0] for i in range(4) if q[i]]
        if next_times:
            curr_time = min(next_times)
            continue

    # 모든 차선에 차량이 있다면 교착 상태
    if all(waiting):
        break

    # 통과 가능한 차량 찾기
    can_pass = []
    for i in range(4):
        right = (i + 3) % 4
        # 현재 차선의 차에서 오른쪽에 차가 없을 때 패스
        if waiting[i] and not waiting[right]:
            can_pass.append(i)

    # 5. 통과 가능한 차량 동시에 처리
    for i in can_pass:
        time, idx = q[i].popleft()
        answer[idx] = curr_time
        remain -= 1

    curr_time += 1

for a in answer:
    print(a)
