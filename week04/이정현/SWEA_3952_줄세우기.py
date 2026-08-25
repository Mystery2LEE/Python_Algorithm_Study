from collections import deque
T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    # 진입 차수를 저장할 리스트와 그래프를 초기화
    degree = [0] * (n+1)
    # 그래프를 인접 리스트로 표현
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        # 진입 차수를 증가시키고 그래프에 간선을 추가
        degree[b] += 1
        graph[a].append(b)

    q = deque([])
    result = []

    for i in range(1, n+1):
        if degree[i] == 0:
            # 진입 차수가 0인 노드를 큐에 추가
            q.append(i)

    while q:
        # 큐에서 노드를 꺼내고 결과 리스트에 추가
        a = q.popleft()
        result.append(a)
        # 해당 노드와 연결된 노드들의 진입 차수를 감소시키고, 진입 차수가 0이 된 노드를 큐에 추가
        for g in graph[a]:
            degree[g] -= 1
            if degree[g] == 0:
                q.append(g)

    print(f"#{test_case}", " ".join(map(str, result)))