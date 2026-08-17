T = int(input())
for tc in range(1, T+1):
    # N: 구역 개수, M: 인접 구역 개수, K: 색상 개수
    N, M, K = map(int, input().split())
    
    # 인접 구역 저장
    graph = [[] for _ in range(N)]    
    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        
        graph[a].append(b)
        graph[b].append(a)
        
    # 각 구역의 색    
    color = [0] * N   
    
    def backtrack(depth):
        global result
        
        # 종료 조건 -> 모든 구역에 색칠함
        if depth == N:
            result += 1
            return
        
        for c in range(1, K+1):
            is_same = False
            
            for x in graph[depth]:
                if color[x] == c:
                    is_same = True
                    break
            # 인접한 구역이 같은 색이면 현재 색 사용하지 않음
            if is_same:
                continue
            
            color[depth] = c
            backtrack(depth + 1) # 다음 구역으로 이동
            color[depth] = 0 
        
    result = 0   
    backtrack(0)    
    
    print(f'#{tc} {result}')