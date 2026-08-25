# 부모 노드를 찾는 함수
def find(x):
    if parent[x] == x:
        return x
    p = find(parent[x])
    return p

# 두 노드를 합치는 함수
def union(x, y):
    parent[find(y)] = find(x)

T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    parent = [i for i in range(n+1)]
    idx = 0
    for i in range(m):
        x = arr[2*i]
        y = arr[2*i+1]
        if find(x) != find(y):
            union(x, y)

    # 서로 다른 부모 노드의 개수를 세기 위해 set 자료형을 사용
    s = set()
    
    for p in range(1, n+1):
        s.add(find(p))

    print(f"#{test_case} {len(s)}")
