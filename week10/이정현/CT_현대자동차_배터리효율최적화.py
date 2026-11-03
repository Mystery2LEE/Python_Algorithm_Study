N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# Please write your code here.
D = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# 1단계: 모든 펜토미노 배치 생성
seen = set()

def grow(cells, mask):
    if mask in seen: return
    seen.add(mask)
    if len(cells) == 5: return
    
    for (r, c) in cells:
        for dr, dc in D:
            nr = r + dr
            nc = c + dc
            if not (0 <= nr < N and 0 <= nc < M):
                continue
            k = nr*M+nc
            if (1 << k) & mask:
                continue
            grow(cells + [(nr,nc)], mask | (1 << k))

for i in range(N):
    for j in range(M):
        grow([(i, j)], 1 << (i * M + j))

# 5칸짜리만 골라 (mask, 칸 합) 저장
pieces = []
for mask in seen:
    if bin(mask).count('1') == 5:
        s = sum(grid[k // M][k % M] for k in range(N * M) if mask & (1 << k))
        pieces.append((mask, s))  

# 2단계: 정확히 2칸 겹치는 쌍 중 최댓값
ans = float('-inf')
for a in range(len(pieces)):
    ma, sa = pieces[a]
    for b in range(a + 1, len(pieces)):
        mb, sb = pieces[b]
        if bin(ma & mb).count('1') == 2:
            ans = max(ans, sa + sb)

print(ans)