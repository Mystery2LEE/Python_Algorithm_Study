#  길찾는 함수
def found(x, left_next, right_next, visited):
    # 방문한 노드라면 return
    if visited[x]:
        return
    # 방문하지 않은 노드라면 방문 처리
    else:
        visited[x] = True
    a = 0
    # 왼쪽, 오른쪽 노드 탐색
    for next_node in (left_next[x], right_next[x]):
        # 방문하지 않은 노드라면 탐색
        if next_node != 0:
            # 99번 노드에 도달하면 return 1
            if next_node == 99:
                return 1
            # 방문하지 않은 노드라면 재귀적으로 탐색
            a = found(next_node, left_next, right_next, visited)
        
        if a == 1:
            return 1
    return 0

T = 10

for test_case in range(1, T + 1):
    t, n = map(int, input().split())
    arr = list(map(int, input().split()))
    left_next = [0] * 100
    right_next = [0] * 100
    visited = [False] * 100
    for i in range(n):
        # 왼쪽, 오른쪽 노드 연결
        if left_next[arr[2*i]] == 0:
            left_next[arr[2*i]] = arr[2*i+1]
        else:
            right_next[arr[2 * i]] = arr[2 * i + 1]

    result = found(0, left_next, right_next, visited)
    print(f"#{t} {result}")