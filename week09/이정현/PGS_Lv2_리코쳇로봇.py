from collections import deque

def solution(board):
    # 최단거리 탐색
    def BFS(r, c, visited):
        D = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = deque([])
        count = 0 # 이동한 횟수
        queue.append((r, c, count))
        while queue:
            qr, qc, qcount = queue.popleft()
            for dr, dc in D:
                nr = qr + dr
                nc = qc + dc
                # 미끄러지는 거
                while True:
                    # 넘어가거나 벽을 만나면 break
                    if  nr < 0 or nr >= len(board) or nc < 0 or nc >= len(board[0]) or board[nr][nc] == 'D':
                        nr -= dr
                        nc -= dc
                        break
                    nr += dr
                    nc += dc
                if visited[nr][nc] == 1:
                    continue
                if board[nr][nc] == 'G':
                        return qcount + 1
                visited[nr][nc] = 1
                queue.append((nr, nc, qcount+1))
        return -1
                    
    visited = [[0] * len(board[0]) for _ in range(len(board))]
    s, e = 0, 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                s, e = i, j
    visited[s][e] = 1
    answer = BFS(s, e, visited)
    return answer