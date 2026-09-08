from typing import List


def init(N: int, mMap: List[List[int]]) -> None:
    global size, path, cell_to_idx, tw_interval, tw_cov_list, tw_cov_set

    size = N
    # [FIX 10] reset tower state for every test case
    tw_interval, tw_cov_list, tw_cov_set = [], [], []

    start = end = None
    for i in range(N):
        for j in range(N):
            v = mMap[i][j]
            if v == 2:
                start = (i, j)
            elif v == 3:
                end = (i, j)

    # [FIX 8a] path is unique, so walk it once here and store it as a list.
    #          runner position becomes a single path index, so move() disappears.
    path = [start]
    seen = {start}
    cur = start
    while cur != end:
        r, c = cur
        for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            # [FIX 8b] bounds check BEFORE array access; allow the goal cell (value 3)
            if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in seen and mMap[nr][nc] in (1, 3):
                cur = (nr, nc)
                seen.add(cur)
                path.append(cur)
                break
        else:
            break

    cell_to_idx = {cell: idx for idx, cell in enumerate(path)}


def addTower(mRow: int, mCol: int, mInterval: int) -> None:
    # [FIX 1] range is distance <= 3 (full diamond). "== 3" only caught the rim.
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

    # a tower covering no path cell can never fire, so drop it entirely
    if not cov:
        return

    cov.sort()
    tw_interval.append(mInterval)
    tw_cov_list.append(cov)
    tw_cov_set.append(set(cov))   # O(1) check for "keep last target"


def runSimulation(M: int, mInterval: int, mHP: int,
                  mRetTs: List[int], mRetHP: List[int]) -> None:
    L = len(path)
    end_idx = L - 1
    T = len(tw_interval)
    cov_list, cov_set, iv = tw_cov_list, tw_cov_set, tw_interval

    hp = [mHP] * M
    pos = [-1] * M          # runner -> path index. -1 means not on the map
    occ = [-1] * L          # path index -> runner id (at most one per cell)
    on_map = []             # runners on the map, ascending = closest to goal first
    tgt = [-1] * T          # each tower's last target

    # [FIX 3] reload as a schedule of "next turn this tower may fire",
    #         so a reloading tower never enters the loop and never picks a target
    max_t = mInterval * (M + L) + 64
    sched = [[] for _ in range(max_t + 32)]
    sched[1] = list(range(T))       # every tower is ready when the game starts

    spawned = 0
    finished = 0
    t = 0

    while finished < M:
        t += 1

        # ---------- pass 1: selection only, never touch HP here ----------
        # [FIX 6] simultaneous attack requires selection and damage to be separate passes
        shots = []
        for i in sched[t]:
            last = tgt[i]
            # [FIX 7a] keep the last target if it is ALIVE and still in range (rule 2-a).
            #          dead or escaped runners have pos = -1, so the check fails by itself
            if last >= 0 and pos[last] >= 0 and pos[last] in cov_set[i]:
                shots.append((i, last))
                continue

            # [FIX 5] priorities 2 and 3 as one tuple comparison: (remaining hp, spawn order)
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
                # [FIX 7b] no target found: last target is cleared, retry next turn (rule 3)
                sched[t + 1].append(i)

        # ---------- pass 2: apply all damage at once ----------
        if shots:
            for i, r in shots:
                hp[r] -= 1          # overkill is allowed even if hp already hit 0
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

        # ---------- move and spawn ----------
        # [FIX 2] spec order: attacks resolve first, movement and spawning come after
        if t % mInterval == 0:
            if on_map:
                arrived = False
                # front runners move first so the cell behind them frees up
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

            # [FIX 4] spawn counter is fully separated from the tower loop variable
            if spawned < M:
                pos[spawned] = 0
                occ[0] = spawned
                on_map.append(spawned)
                spawned += 1

        # [FIX 9] loop until all M runners are gone, not just the last one