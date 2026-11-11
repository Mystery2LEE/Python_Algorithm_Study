def solution(maps):
    answer = []
    visited = [[0] * len(maps[0]) for _ in range(len(maps))]
    D = [(0,1),(0,-1),(1,0),(-1,0)]
    
    for r in range(len(maps)):
        for c in range(len(maps[0])):
            if maps[r][c] == 'X':
                visited[r][c] += 1
            else:
                if visited[r][c] > 0:
                    continue
                queue = [(r, c)]
                visited[r][c] += 1
                days = 0
                while queue:
                    qr, qc = queue.pop()
                    days += int(maps[qr][qc])
                    for dr, dc in D:
                        nr = qr + dr
                        nc = qc + dc
                        if not (0 <= nr < len(maps) and 0 <= nc < len(maps[0])):
                            continue
                        if visited[nr][nc] > 0:
                            continue
                        if maps[nr][nc] == 'X':
                            visited[nr][nc] += 1
                            continue
                        visited[nr][nc] += 1
                        queue.append((nr, nc))
                answer.append(days)
                        
        if not answer:
            answer.append(-1)
    return sorted(answer)