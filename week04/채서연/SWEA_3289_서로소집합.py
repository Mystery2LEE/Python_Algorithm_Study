def find(root, x):
    if root[x] != x:
        root[x] = find(root,root[x])
    return root[x]

def union(root, a, b):
    a = find(root, a)
    b = find(root, b)
    if a < b:
        root[b] = a
    else:
        root[a] = b

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    root = [i for i in range(n+1)]
    result = ''
    for _ in range(m):
        cmd, a, b = map(int, input().split())
        # 합치기
        if cmd == 0:
            union(root, a, b)
            
        # 같집합인지 확인
        elif cmd == 1:
            if find(root, a) == find(root, b):
                result += '1'
            else:
                result += '0'
    
    print(f'#{tc} {''.join(result)}')