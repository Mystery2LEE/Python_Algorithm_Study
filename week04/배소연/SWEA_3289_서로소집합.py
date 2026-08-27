def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


def union(a, b):
    root_a = find(a)
    root_b = find(b)
    
    if root_a == root_b:
        return
    
    if rank[root_a] < rank[root_b]:
        parent[root_a] = root_b
    elif rank[root_a] > rank[root_b]:
        parent[root_b] = root_a
    else:
        parent[root_b] = root_a
        rank[root_a] += 1
        

T = int(input())

for tc in range(1, T + 1):
    # m: 연산의 개수
    n, m = map(int, input().split())
    parent = list(range(n + 1))
    rank = bytearray(n + 1)
    
    answer = []
    
    for _ in range(m):
        command, a, b = map(int, input().split())
        
        if command == 0:
            union(a, b)
        else:
            if find(a) == find(b):
                answer.append('1')
            else:
                answer.append('0')
            
    print(f'#{tc} {"".join(answer)}')