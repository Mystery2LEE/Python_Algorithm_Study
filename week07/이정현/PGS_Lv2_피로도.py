def solution(k, dungeons):
    # 방문 함수
    visited = [False] * len(dungeons)
    # 깊이 우선 탐색
    def DFS(visited, k, count):
        # 현재 count를 최대 점수로 기록
        max_num = count
        # 전체 탐색
        for i in range(len(dungeons)):
            # 만약 방문 했으면 넘긴다
            if visited[i]:
                continue
            # k가 최소 필요 체력보다 작으면 넘긴다
            if k < dungeons[i][0]:
                continue
            # 방문을 visited로 변경
            visited[i] = True
            # 해당 값 최대 count 반환
            n = DFS(visited, k - dungeons[i][1], count + 1)
            # n이 max_num보다 크면 갱신
            if n > max_num:
                max_num = n
            # 백트래킹
            visited[i] = False
        # 최대값 반환
        return max_num
    return DFS(visited, k, 0)