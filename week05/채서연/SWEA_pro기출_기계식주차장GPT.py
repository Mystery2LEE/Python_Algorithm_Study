import heapq


class RESULT_E:
    def __init__(self, success, locname):
        self.success = success
        self.locname = locname


class RESULT_S:
    def __init__(self, cnt, carlist):
        self.cnt = cnt
        self.carlist = carlist


# ----------------------------------
# 전역 변수
# ----------------------------------

N = M = L = 0

# 각 구역의 빈 슬롯
# free_slots[z] = min heap
free_slots = []

# (-빈자리수, zone)
zone_heap = []

# 차량 현재 상태
# parked:
# cars[car] = ('P', enter_time, zone, slot)
#
# towing:
# cars[car] = ('T', enter_time, tow_time)
cars = {}

# 견인 예정 차량
# (tow_time, car_no)
tow_heap = []

# 검색용
# suffix -> heap
parked_search = {}
towed_search = {}

def init(N_, M_, L_):
    global N, M, L
    global free_slots, zone_heap
    global cars, tow_heap
    global parked_search, towed_search

    N = N_
    M = M_
    L = L_

    cars = {}
    tow_heap = []

    free_slots = []
    zone_heap = []

    parked_search = {}
    towed_search = {}

    for z in range(N):
        # 각 구역의 빈 슬롯
        free_slots.append(list(range(M)))
        heapq.heapify(free_slots[z])

        # 빈 슬롯 M개
        heapq.heappush(zone_heap, (-M, z))
        
def towing(mTime):
    global zone_heap

    while tow_heap and tow_heap[0][0] <= mTime:

        tow_time, car_no = heapq.heappop(tow_heap)

        # 현재 상태 확인
        info = cars.get(car_no)

        # 이미 출차했거나 재입차했다면
        # 이 견인 이벤트는 무효
        if info is None:
            continue

        if info[0] != 'P':
            continue

        _, enter_time, z, s = info

        # 실제 견인 예정 시각과 다르면 오래된 이벤트
        if enter_time + L != tow_time:
            continue

        # -------------------------
        # 실제 견인
        # -------------------------

        cars[car_no] = ('T', enter_time, tow_time)

        # 슬롯 반환
        heapq.heappush(free_slots[z], s)

        # 해당 구역 빈자리 +1
        heapq.heappush(
            zone_heap,
            (-len(free_slots[z]), z)
        )

        # 견인 검색 heap
        suffix = car_no[3:]

        if suffix not in towed_search:
            towed_search[suffix] = []

        xx = int(car_no[:2])
        y = car_no[2]

        heapq.heappush(
            towed_search[suffix],
            (xx, y, car_no)
        )
        
def enter(mTime, mCarNo):
    # 먼저 현재 시각까지 견인될 차량 처리
    towing(mTime)

    # --------------------------------
    # 견인 기록 삭제
    # --------------------------------

    info = cars.get(mCarNo)

    if info is not None and info[0] == 'T':
        del cars[mCarNo]

    # --------------------------------
    # 빈자리가 가장 많은 구역 찾기
    # --------------------------------

    while zone_heap:

        neg_count, z = zone_heap[0]

        current_count = len(free_slots[z])

        # 오래된 heap 정보 제거
        if -neg_count != current_count:
            heapq.heappop(zone_heap)
            continue

        break

    # 주차장 만차
    if not zone_heap or len(free_slots[zone_heap[0][1]]) == 0:
        return RESULT_E(0, "")

    # --------------------------------
    # 구역 선택
    # --------------------------------

    _, z = heapq.heappop(zone_heap)

    # 가장 작은 빈 슬롯
    s = heapq.heappop(free_slots[z])

    # --------------------------------
    # 차량 정보 저장
    # --------------------------------

    cars[mCarNo] = ('P', mTime, z, s)

    # --------------------------------
    # 견인 예정 heap
    # --------------------------------

    heapq.heappush(
        tow_heap,
        (mTime + L, mCarNo)
    )

    # --------------------------------
    # 검색 heap
    # --------------------------------

    suffix = mCarNo[3:]

    if suffix not in parked_search:
        parked_search[suffix] = []

    xx = int(mCarNo[:2])
    y = mCarNo[2]

    heapq.heappush(
        parked_search[suffix],
        (xx, y, mCarNo)
    )

    # --------------------------------
    # 변경된 구역 상태 저장
    # --------------------------------

    heapq.heappush(
        zone_heap,
        (-len(free_slots[z]), z)
    )

    locname = chr(65 + z) + f'{s:03d}'

    return RESULT_E(1, locname)

def pullout(mTime, mCarNo):
    towing(mTime)

    info = cars.get(mCarNo)

    # 없는 차량
    if info is None:
        return -1

    # --------------------------------
    # 주차 중인 차량
    # --------------------------------

    if info[0] == 'P':

        _, enter_time, z, s = info

        result = mTime - enter_time

        # 차량 삭제
        del cars[mCarNo]

        # 슬롯 반환
        heapq.heappush(free_slots[z], s)

        # 구역 빈자리 정보 갱신
        heapq.heappush(
            zone_heap,
            (-len(free_slots[z]), z)
        )

        return result

    # --------------------------------
    # 견인된 차량
    # --------------------------------

    _, enter_time, tow_time = info

    towing_period = mTime - tow_time

    result = (L + towing_period * 5) * (-1)

    # 견인 기록 삭제
    del cars[mCarNo]

    return result

def get_valid(heap, expected_status, limit):
    result = []
    temp = []

    while heap and len(result) < limit:

        item = heapq.heappop(heap)

        xx, y, car_no = item

        info = cars.get(car_no)

        # 현재 상태가 원하는 상태가 아니면 버림
        if info is None or info[0] != expected_status:
            continue

        result.append(car_no)
        temp.append(item)

    # 사용한 정상 데이터는 다시 넣어줌
    for item in temp:
        heapq.heappush(heap, item)

    return result

def search(mTime, mStr):
    towing(mTime)

    result = []

    # -----------------------------
    # 주차 차량
    # -----------------------------

    heap = parked_search.get(mStr)

    if heap:
        parked = get_valid(heap, 'P', 5)
        result.extend(parked)

    # -----------------------------
    # 견인 차량
    # -----------------------------

    if len(result) < 5:

        heap = towed_search.get(mStr)

        if heap:
            towed = get_valid(
                heap,
                'T',
                5 - len(result)
            )

            result.extend(towed)

    # -----------------------------
    # 결과
    # -----------------------------

    result += [''] * (5 - len(result))

    return RESULT_S(
        len(result) - result.count(''),
        result
    )