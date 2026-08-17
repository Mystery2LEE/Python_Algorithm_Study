from collections import deque

T = int(input().strip())

for test_case in range(1, T + 1) :
    E ,N = map(int, input().split())
    
    arr = list(map(int, input().split()))

    employee = [[] for _ in range(E + 2)]
    for i in range(0, E * 2, 2):
        v1 = arr[i]
        v2 = arr[i + 1]

        employee[v1].append(v2)

    q = deque()
    result = 0

    q.append(N)
    while q :
        node = q.popleft()
        result += 1
        for child in employee[node] :
            q.append(child)
    print(f'#{test_case} {result}')