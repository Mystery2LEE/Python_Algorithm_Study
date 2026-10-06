def solution(n, computers):
    # 네트워크의 개수를 세는 변수
    count = 0
    # 방문 여부를 기록하는 리스트
    visited = [0]*(n)

    # 깊이 우선 탐색(DFS) 함수 정의
    def DFS(e):
        # 현재 노드 e와 연결된 모든 노드를 방문
        for k in range(n):
            # 현재 노드 e와 연결되어 있고, 아직 방문하지 않은 노드 k를 찾으면 DFS 재귀 호출
            if computers[e][k] == 1:
                # 현재 노드 k가 아직 방문하지 않은 경우, 방문 처리 후 DFS 재귀 호출
                if visited[k] == 0:
                    visited[k] = 1
                    DFS(k)
    # 모든 노드를 순회하며 DFS 호출
    for g in range(n):
        # 현재 노드 g가 아직 방문하지 않은 경우, DFS 호출 후 네트워크 개수 증가
        if visited[g] == 0:
            visited[g] = 1
            DFS(g)
            count += 1
    # 최종적으로 네트워크의 개수 반환
    return count