class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# 자식 노드 개수 구하기
def child_cnt(node):
    count = 1
    # 자식 노드는 왼쪽부터 채워지니까 왼쪽이 비어있으면 오른쪽도 비어있음 -> 자식이 없다
    if node.left is None: 
        return count
    
    if node.left is not None:
        count += child_cnt(node.left)
    if node.right is not None:
        count += child_cnt(node.right)
    return count

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    node_list = []

    for i in range(E+1):
        node_list.append(Node(i))

    for i in range(0, E*2 , 2):
        if arr[i+1] == 0:
            continue
        # 인덱스랑 value랑 1 차이남
        p, c = arr[i]-1, arr[i+1]-1
        if node_list[p].left is None:
            node_list[p].left = node_list[c]
        elif node_list[p].right is None:
            node_list[p].right = node_list[c]


    node = node_list[N-1]
    print(f'#{tc} {child_cnt(node)}')