# root 찾기
def find(root, A):
    if root[A] != A:
        root[A] = find(root, root[A])
    return root[A]

# 합치기
def union(root, A, B):
    a = find(root, A)
    b = find(root, B)
    if a == b:
        return False
    if a < b:
        root[b] = a
    else:
        root[a] = b
    return True

t = int(input())
for tc in range(1, t+1):
    # N: 직원 수, M: 신청서 수
    N, M = map(int, input().split())
    # 초기에는 모든 노드의 루트가 자기 자신
    arr = list(map(int, input().split()))
    count = N
    root = [i for i in range(N+1)]
    
    # find에서 각 노드의 root를 업데이트한다고 생각해서 len(set(root))-1로 개수 셌는데 틀림
    # 합쳐질 때마다 count-1하는 방법으로..
    for i in range(0, 2*M, 2):
        if union(root, arr[i], arr[i+1]):
            count -= 1
        
    print(f'#{tc} {count}' )
