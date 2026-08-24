from collections import deque

T = int(input())
for tc in range(1, T+1):
    # N: 학생 수, M: 순서의 개수(간선 개수)
    N, M = map(int, input().split())
    # 모든 노드에 대한 진입 차수 0으로 초기화
    indegree = [0]*(N+1)
    # 각 노드에 연결된 간선 관리할 그래프
    graph = [[] for _ in range(N+1)]
    
    queue = deque()
    result = []
    
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        # a->b 연결, b진입차수 1씩 증가
        indegree[b] += 1
    
    # 1. 진입차수가 0인 노드 찾기
    for i in range(1, N+1):
        if indegree[i] == 0:
            queue.append(i)
        
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 원소를 꺼내 해당 노드에서 나가는 간선을 그래프에서 제거
        item = queue.popleft()
        result.append(item)
        for x in graph[item]:
            # 간선 제거 -> 진입차수 1 줄음 -> 0이면 큐에 삽입
            indegree[x] -= 1
            if indegree[x] == 0:
                queue.append(x)
        # 새롭게 진입차수가 0이 된 노드를 큐에 삽입
        
    
    
    print(f'#{tc}', *result)