from typing import List


def init(N: int, mMap: List[List[int]]) -> None:
    global size, path, cell_to_idx, tw_interval, tw_cov_list, tw_cov_set

    size = N
    # [수정 10] 테스트케이스마다 타워 상태를 완전히 새로 만든다
    tw_interval, tw_cov_list, tw_cov_set = [], [], []

    start = end = None
    for i in range(N):
        for j in range(N):
            v = mMap[i][j]
            if v == 2:
                start = (i, j)
            elif v == 3:
                end = (i, j)

    # [수정 8a] 경로가 유일하므로 여기서 한 번만 훑어 리스트로 만든다.
    #           도망자 위치가 좌표가 아니라 경로 인덱스 정수 하나가 되어 move 함수가 사라진다
    path = [start]
    seen = {start}
    cur = start
    while cur != end:
        r, c = cur
        for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            # [수정 8b] 경계 검사를 배열 접근보다 먼저 한다. 도착지(값 3)도 통과시킨다
            if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in seen and mMap[nr][nc] in (1, 3):
                cur = (nr, nc)
                seen.add(cur)
                path.append(cur)
                break
        else:
            break

    cell_to_idx = {cell: idx for idx, cell in enumerate(path)}


def addTower(mRow: int, mCol: int, mInterval: int) -> None:
    # [수정 1] 사정거리는 거리 3 이하, 즉 마름모 전체다. 기존 == 3 은 테두리만 잡혔다
    cov = []
    for dr in range(-3, 4):
        nr = mRow + dr
        if nr < 0 or nr >= size:
            continue
        rem = 3 - abs(dr)
        for dc in range(-rem, rem + 1):
            nc = mCol + dc
            if nc < 0 or nc >= size:
                continue
            p = cell_to_idx.get((nr, nc))
            if p is not None:
                cov.append(p)

    # 사정거리 안에 길이 하나도 없는 타워는 영원히 못 쏘므로 아예 제외한다
    if not cov:
        return

    cov.sort()
    tw_interval.append(mInterval)
    tw_cov_list.append(cov)
    tw_cov_set.append(set(cov))   # 직전 타겟 유지 판정을 O(1)로 하기 위한 집합


def runSimulation(M: int, mInterval: int, mHP: int,
                  mRetTs: List[int], mRetHP: List[int]) -> None:
    L = len(path)
    end_idx = L - 1
    T = len(tw_interval)
    cov_list, cov_set, iv = tw_cov_list, tw_cov_set, tw_interval

    hp = [mHP] * M
    pos = [-1] * M          # 도망자의 경로 인덱스, -1 이면 맵에 없음
    occ = [-1] * L          # 경로 칸에 있는 도망자 번호, 한 칸에 최대 한 명
    on_map = []             # 맵 위 도망자 번호, 오름차순이 도착지에 가까운 순
    tgt = [-1] * T          # 타워의 직전 공격 대상

    # [수정 3] 재장전을 플래그가 아니라 다음에 쏠 수 있는 턴 스케줄로 관리한다.
    #          버킷에 없는 타워는 루프에 아예 안 들어오므로 대상 탐색도 하지 않는다
    max_t = mInterval * (M + L) + 64
    sched = [[] for _ in range(max_t + 32)]
    sched[1] = list(range(T))       # 게임 시작 시 모든 타워는 준비 완료 상태

    spawned = 0
    finished = 0
    t = 0

    while finished < M:
        t += 1

        # ---------- 1패스: 선정만 한다. 여기서는 체력을 절대 건드리지 않는다 ----------
        # [수정 6] 동시에 공격하려면 선정 패스와 데미지 적용 패스를 반드시 분리해야 한다
        shots = []
        for i in sched[t]:
            last = tgt[i]
            # [수정 7a] 직전 타겟이 살아 있고 사정거리 내면 그대로 유지한다(규칙 2-a).
            #           죽거나 탈출한 도망자는 pos 가 -1 이라 조건이 저절로 깨진다
            if last >= 0 and pos[last] >= 0 and pos[last] in cov_set[i]:
                shots.append((i, last))
                continue

            # [수정 5] 우선순위 2와 3을 남은 체력, 등장 순서 튜플 비교 한 번으로 처리한다
            best, best_key = -1, None
            for p in cov_list[i]:
                r = occ[p]
                if r >= 0:
                    key = (hp[r], r)
                    if best_key is None or key < best_key:
                        best_key, best = key, r

            tgt[i] = best
            if best >= 0:
                shots.append((i, best))
            else:
                # [수정 7b] 대상을 못 찾으면 직전 타겟이 없는 상태가 되고 다음 턴에 다시 찾는다(규칙 3)
                sched[t + 1].append(i)

        # ---------- 2패스: 여기서 데미지를 일괄 적용한다 ----------
        if shots:
            for i, r in shots:
                hp[r] -= 1          # 체력이 이미 0 이어도 그대로 깎는다, 오버킬 허용
                sched[t + iv[i]].append(i)

            died = False
            for i, r in shots:
                if hp[r] <= 0 and pos[r] >= 0:
                    mRetTs[r] = t
                    mRetHP[r] = 0
                    occ[pos[r]] = -1
                    pos[r] = -1
                    finished += 1
                    died = True
            if died:
                on_map = [r for r in on_map if pos[r] >= 0]

        # ---------- 이동과 스폰 ----------
        # [수정 2] 스펙 순서대로 공격이 모두 끝난 뒤에 이동과 스폰이 온다
        if t % mInterval == 0:
            if on_map:
                arrived = False
                # 앞선 도망자부터 옮겨야 뒤 도망자가 들어올 칸이 비워진다
                for r in on_map:
                    p = pos[r]
                    occ[p] = -1
                    np_ = p + 1
                    if np_ == end_idx:
                        mRetTs[r] = t
                        mRetHP[r] = hp[r]
                        pos[r] = -1
                        finished += 1
                        arrived = True
                    else:
                        pos[r] = np_
                        occ[np_] = r
                if arrived:
                    on_map = [r for r in on_map if pos[r] >= 0]

            # [수정 4] 스폰 카운터를 타워 루프 변수와 완전히 분리했다
            if spawned < M:
                pos[spawned] = 0
                occ[0] = spawned
                on_map.append(spawned)
                spawned += 1

        # [수정 9] 마지막 한 명만 보지 않고, 사라진 도망자 수가 M 이 될 때까지 반복한다