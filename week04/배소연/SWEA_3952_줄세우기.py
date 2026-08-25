from collections import deque

T = int(input())

for tc in range(1, T + 1):
    # N: 학생의 수
    # M: 순서의 개수
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    
    indegree = [0] * (N + 1)
    
    for _ in range(M):
        a, b = map(int, input().split())
        
        graph[a].append(b)
        indegree[b] += 1
        
    queue = deque()
    for student in range(1, N + 1):
        if indegree[student] == 0:
            queue.append(student)
            
    answer = []
    while queue:
        current = queue.popleft()
        answer.append(current)
        
        for next_student in graph[current]:
            indegree[next_student] -= 1
            
            if indegree[next_student] == 0:
                queue.append(next_student)
        
    print(f'#{tc}', *answer)