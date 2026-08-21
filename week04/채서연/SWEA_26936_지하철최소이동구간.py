from collections import deque

t = int(input())
for tc in range(1,t+1):
    # V: 역 개수, E: 선로 구간의 개수
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        # 각 선로 구간이 있는 두 역의 번호
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    # S: 출발 역 번호, G: 목적지 역 번호
    S, G = map(int,input().split())

    # 출발역에서 i번 역까지 가는데 필요한 최소 선로 구간 수
    distance = [-1] * (V+1)
    queue = deque()
    queue.append(S)
    distance[S] = 0

    while queue:
        # 현재 노드를 인접 노드로 업데이트
        cur = queue.popleft()
        # 목적지 도착
        if cur == G:
            break

        # 현재 노드의 인접 노드 중에서
        for next in graph[cur]:
            # 아직 방문하지 않은 노드
            if distance[next] == -1:
                # 현재 노드까지의 거리 + 1
                distance[next] = distance[cur] + 1
                queue.append(next)


    dist = distance[G]
    if dist == -1:
        dist = 0
    print(f'#{tc} {dist}')