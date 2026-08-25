T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    
    parent = [i for i in range(N + 1)]
        
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(a, b):
        root_a = find(a)
        root_b = find(b)
        
        if root_a != root_b:
            parent[root_b] = root_a
            
    if M > 0:
        arr = list(map(int, input().split()))
        
        for i in range(0, 2 * M, 2):
            a = arr[i]
            b = arr[i + 1]
            
            union(a, b)
            
    count = 0
    
    for person in range(1, N + 1):
        if find(person) == person:
            count += 1
            
    print(f'#{tc} {count}')