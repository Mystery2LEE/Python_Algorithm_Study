def solution(triangle):
    # 삼각형의 위 부터 탐색
    for i in range(1, len(triangle)):
        # 삼각형 가로 탐색
        for j in range(len(triangle[i])):
            # 만약 맨 왼쪽이면 위 노드의 맨 왼쪽 더하기
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            # 맨 오른쪽이면 위 노드의 맨 오른쪽 더하기
            elif j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i-1][j-1]
            # 중간이면 왼쪽 오른쪽거 비교해서 큰 거 더하기
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
    # 마지막 줄에서 가장 큰 수 리턴
    return max(triangle[-1])