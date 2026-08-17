T = int(input().strip())

def checkTree(tree, last) : 
    parent = tree[last//2]
    child = tree[last]
    if parent > child :
        temp = parent
        tree[last // 2] = child
        tree[last] = temp
        checkTree(tree, last//2)

    return tree
for test_case in range(1, T + 1) :
    N = int(input().strip())
    arr = list(map(int, input().split()))

    tree = [0] * (N + 1)
    for idx , node in enumerate(arr) :
        tree[idx + 1] = node 
        tree = checkTree(tree, idx+1)

    result = 0
    while N // 2 > 0 :
        result += tree[N//2]
        N //= 2 
    print(f'#{test_case} {result}')