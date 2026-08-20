from collections import deque
# BFS를 사용하여 최단 거리 계산
def bfs(s, g):
    visited = [False] * (len(graph) + 1)
    # dist 배열 초기화
    dist[s] = 0
    # 큐를 사용하여 BFS 수행
    queue = deque([s])
    visited[s] = True

    while queue:
        node = queue.popleft()
        if node == g:
            break

        for next_node in graph[node]:
            if not visited[next_node]:
                # 방문하지 않은 노드라면 방문 처리하고, dist 배열에 최단 거리 갱신
                visited[next_node] = True
                # dist 배열에 최단 거리 갱신
                dist[next_node] = dist[node] + 1
                queue.append(next_node)

T = int(input())

for test_case in range(1, T + 1):
    V, E = map(int, input().split())

    dist = [-1] * (V + 1)
    graph = {}

    for i in range(1, V + 1):
        graph[i] = []

    for _ in range(E):
        k, v = map(int, input().split())
        graph[k].append(v)
        graph[v].append(k)

    s, g = map(int, input().split())

    bfs(s, g)
    # dist[g]가 -1이면, s에서 g로 가는 경로가 없다는 의미이므로, dist[g]를 0으로 설정
    if dist[g] == -1:
        dist[g] = 0

    print(f"#{test_case} {dist[g]}")