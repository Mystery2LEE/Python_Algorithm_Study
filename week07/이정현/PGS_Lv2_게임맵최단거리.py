from collections import deque

def solution(maps):
    # 방문 확인 함수
    visited = [[0]*len(maps[0]) for _ in range(len(maps))] 
    # 최단 거리 탐색
    def bfs(r, c, maps):
        # 방향 변수
        dir = [(0,1), (0,-1), (1,0), (-1,0)]
        # 현재 갈 수 있는 경우의 수 담는 큐
        load = deque()
        # 출발점 및 최초 거리
        load.append((r, c, 1))
        # 출발점 방문 처리
        visited[0][0] = 1
        
        # 갈 수 있는 경우가 있을 때 까지
        while load:
            # 경우의 수 하나 pop
            d_r, d_c, d_count = load.popleft()
            # 4방향 탐색
            for d in range(4):
                n_r = d_r + dir[d][0]
                n_c = d_c + dir[d][1]
                # 만약 위치가 0보다 작고 행, 열 길이보다 길면 스킵
                if n_r < 0 or n_r >= len(maps) or n_c < 0 or n_c >= len(maps[0]):
                    continue
                # 방문했던 길이면 스킵
                if visited[n_r][n_c] == 1:
                    continue
                # 막힌 길이면 스킵
                if maps[n_r][n_c] == 0:
                    continue
                # 단계 증가
                n_count = d_count + 1
                # 방문 처리
                visited[n_r][n_c] = 1
                # 만약 도착점이면 최소 거리 리턴
                if n_r == len(maps) - 1 and n_c == len(maps[0]) - 1:
                    return n_count
                # 새로운 갈 수 있는 위치 저장    
                load.append((n_r, n_c, n_count))
        # 모두 탐색했는데 못찾으면 -1 리턴
        return -1
    
    return bfs(0, 0, maps)
            
            
        
        