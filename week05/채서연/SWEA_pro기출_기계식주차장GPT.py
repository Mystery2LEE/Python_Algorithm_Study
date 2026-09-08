from collections import deque
import heapq

t = int(input().strip())
for tc in range(1, t + 1):
    n, m = map(int, input().split())

    # 주차 공간의 단위당 요금 (1번 공간부터 저장)
    rates = [0] + [int(input().strip()) for _ in range(n)]

    # 차량의 무게 (1번 차량부터 저장)
    weights = [0] + [int(input().strip()) for _ in range(m)]

    # 빈 주차 공간을 관리하는 최소 힙 (가장 작은 번호의 주차 공간이 우선)
    empty_spots = [i for i in range(1, n + 1)]
    heapq.heapify(empty_spots)

    # 각 차량이 몇 번 주차 공간에 들어갔는지 기록
    parked_spot = [0] * (m + 1)

    waiting_queue = deque()
    total_fee = 0

    for _ in range(2 * m):
        car_num = int(input().strip())

        if car_num > 0:  # 입차
            if empty_spots:
                spot = heapq.heappop(empty_spots)
                parked_spot[car_num] = spot
                total_fee += weights[car_num] * rates[spot]
            else:
                waiting_queue.append(car_num)

        else:  # 출차
            target_car = -car_num
            spot = parked_spot[target_car]

            if waiting_queue:
                # 대기 중인 차량이 있다면 바로 그 자리에 주차
                next_car = waiting_queue.popleft()
                parked_spot[next_car] = spot
                total_fee += weights[next_car] * rates[spot]
            else:
                # 대기 차량이 없다면 주차 공간을 힙에 반환
                heapq.heappush(empty_spots, spot)

    print(f'#{tc} {total_fee}')
