from collections import deque

N, M, V = map(int, input().split())
graph = {}

for _ in range(M):
    k, v = map(int, input().split())
    if k not in graph:
        graph[k] = [v]
    else:
        graph[k].append(v)
    if v not in graph:
        graph[v] = [k]
    else:
        graph[v].append(k)

for d in graph:
    graph[d].sort()

def BFS(s):
    visited = [0] * (N+1)
    count = 0
    result = [s]
    visited[s] = 1
    queue = deque()
    queue.append((s, count, result))
    while queue:
        q, qc, qr = queue.popleft()
        if q not in graph:
            continue
        for v in graph[q]:
            if visited[v] != 0:
                continue
            visited[v] = 1
            qr.append(v)
            queue.append((v, qc+1, qr))
            result = qr
    return result

visited = [0] * (N+1)
visited[V] = 1
d_result = [V]
def DFS(s, visited, result):
    if s not in graph:
        return result
    for g in graph[s]:
        if visited[g] != 0:
            continue
        visited[g] = 1
        result.append(g)
        DFS(g, visited, result)
    return result

print(*DFS(V, visited, d_result))
print(*BFS(V))
