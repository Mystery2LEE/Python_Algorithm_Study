from collections import deque

def solution(maps):
    def bfs(x, y, s):
        D = [(1,0),(-1,0),(0,1),(0,-1)]
        visited = [[0] * len(maps[0]) for _ in range(len(maps))]
        queue = deque()
        queue.append((x, y, 1))
        visited[x][y] = 1
        while queue:
            qr, qc, count = queue.popleft()
            for r,c in D:
                nr = qr + r
                nc = qc + c
                if not (0 <= nr < len(maps) and 0 <= nc < len(maps[0])):
                    continue
                if visited[nr][nc] != 0:
                    continue
                if maps[nr][nc] == 'X':
                    continue
                if maps[nr][nc] == s:
                    return nr, nc, count
                visited[nr][nc] = 1
                queue.append((nr, nc, count+1))
        return 0, 0, -1
    
    sr, sc = 0, 0
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                sr, sc = i, j
                break
                
    lr, lc, lcount = bfs(sr, sc, 'L')
    if lcount == -1:
        return -1
    er, ec, ecount = bfs(lr, lc, 'E')
    if ecount == -1:
        return -1
    answer = lcount + ecount
        
    return answer