def init(tree, start, end):
    if start > end :
        return 0
    if tree[start] != 0 :
        return tree[start]
    else :
        tree[start] = init(tree, start * 2, end) + init(tree,start * 2 + 1, end)
        return tree[start]
    
T = int(input())

for test_case in range(1, T + 1):
    N, M, L = map(int, input().split())

    tree = [0] * (N + 1)

    for _ in range(M):
        idx, score = map(int, input().split())
        tree[idx] = score

    init(tree, 1, N)
    print(f'#{test_case} {tree[L]}')
