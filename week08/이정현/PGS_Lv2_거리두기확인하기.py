from collections import deque

def solution(places):
    def dfs(places, r, c):
        D = [(1,0), (-1,0), (0,1), (0,-1)]
        visited = [[0]*5 for _ in range(5)]
        que = deque()
        count = 0
        que.append((r,c,count))
        visited[r][c] = 1
        while que:
            qr, qc, qcount = que.popleft()
            if qcount == 2:
                continue
            for dr, dc in D:
                nr = qr + dr
                nc = qc + dc
                if not (0 <= nr < 5 and 0 <= nc < 5):
                    continue
                if visited[nr][nc] > 0:
                    continue
                if places[nr][nc] == 'X':
                    continue
                if places[nr][nc] == 'P':
                    return False
                visited[nr][nc] = 1
                que.append((nr, nc, qcount+1))
        return True
                
    answer = []
    for p in places:
        is_not = False
        for i in range(5):
            for j in range(5):
                if p[i][j] == 'P':
                    if not dfs(p, i, j):
                        answer.append(0)
                        is_not = True
                if is_not:
                    break
            if is_not:
                break
        if is_not:
            continue
        answer.append(1)
                                  
    return answer