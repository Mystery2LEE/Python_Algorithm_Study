# 루트를 찾는 함수
def find(x):
    if parents[x] == x:
        return x
    p = find(parents[x])
    # 부모 노드를 갱신하여 경로 압축
    parents[x] = p
    return p

# 두 노드를 합치는 함수
def union(x, y):
    parents[find(y)] = find(x)

T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    parents = [i for i in range(n+1)]
    result = []
    for _ in range(m):
        c, a, b = map(int, input().split())
        if c == 0:
            union(a, b)
        else:
            if find(a) == find(b):
                result.append(1)
            else:
                result.append(0)

    print(f"#{test_case}", ''.join(map(str, result)))