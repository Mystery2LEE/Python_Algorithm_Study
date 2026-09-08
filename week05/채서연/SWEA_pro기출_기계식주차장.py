class RESULT_E:
    def __init__(self,success,locname):
        self.success = success
        self.locname = locname

class RESULT_S:
    def __init__(self,cnt,carlist):
        self.cnt = cnt
        self.carlist = carlist # [str] * 5
zone = []
slot = []
towing_record = []
n = m = time = 0
def init(N : int,M : int,L : int) -> None:
    # N:구역 개수 M:각 구역의 슬롯 개수 L:차량을 주차장에 주차할 수 있는 최대 기간
    global zone,slot,n,m,time
    zone = [[0]*M for _ in range(N)]#주차된 차 번호와 입차 시각을 저장,처음에는 주차된 차가 없으니까 0으로 초기화
    slot = [M] * N  #각 구역에 남은 자리 개수 저장,처음에는 비어있으니까 M
    n = N
    m = M
    time = L

#출차/서치하는 시각에 견인되어야 하는 차가 있는지 확인
def towing(mTime):
    global towing_record
    for z in range(n):
        for car in zone[z]:
            if car != 0 and car[1] + time <= mTime:
                towing_record.append(car)

                idx = zone[z].index(car)
                zone[z][idx] = 0
                slot[z] += 1
def enter(mTime : int,mCarNo : str) -> RESULT_E:
    towing(mTime)

    #견인된 차량 번호가 주어질 경우 주차 성공 여부와 상관없이 견인 기록 삭제
    for tcar in towing_record:
        if tcar[0] == mCarNo:
            towing_record.remove(tcar)

    #빈 슬롯 없을 때 ->주차 실패
    max_slot = max(slot)
    if max_slot == 0:
        return RESULT_E(0,"")

    #우선순위#빈 슬롯 많고 가장 앞 구역,숫자 번호 작은 슬롯#빈 슬롯이 가장 많은 N
    max_slot_idx = slot.index(max_slot)
    for s in range(m):
        if zone[max_slot_idx][s] == 0:
            zone[max_slot_idx][s] = (mCarNo,mTime)  #차량 번호,입차 시각
            slot[max_slot_idx] -= 1 #주차 구역 슬롯 하나 줄이기
            return RESULT_E(1,chr(65+max_slot_idx)+f'{s:03d}')



def pullout(mTime : int,mCarNo : str) -> int:
    towing(mTime)
    # mTime에 차량 번호가 mCarNo인 차량을 출차
    for z in range(n):
        for car in zone[z]:
            if car != 0 and car[0] == mCarNo:
                idx = zone[z].index(car)
                result = mTime-car[1]
                zone[z][idx] = 0
                slot[z] += 1
                return result
    for tcar in towing_record:
        if tcar[0] == mCarNo:
            result = (time + (mTime-(time+tcar[1])) * 5) * (-1)
            towing_record.remove(tcar)
            return result
    return-1
def search(mTime : int,mStr : str) -> RESULT_S:
    towing(mTime)
    result_zone = []
    result_towing = []
    result = [''] * 5# mTime에 주차된 차량 또는 견인된 차량 중 차량 번호 뒷 4자리가 mStr과 일치하는 차량 우선 순위 순으로 최대 5대 검색
    for z in zone:
        for car in z:
            if car != 0 and car[0][3:7] == mStr:
                result_zone.append(car[0])
                result_zone = sorted(result_zone)
    if len(result_zone) > 5:
        result[0:5] = result_zone[0:5]
    else:
        for tcar in towing_record:
            if tcar[0][3:7] == mStr:
                result_towing.append(tcar[0])
                result_towing = sorted(result_towing)
        if len(result_zone) + len(result_towing) < 5:
            result[0:len(result_zone) + len(result_towing)] = result_zone + result_towing
        else:
            result[0:5] = result_zone + result_towing[0:5-len(result_zone)]

    cnt = 5-result.count('')
    #print(result)
    return RESULT_S(cnt,result)