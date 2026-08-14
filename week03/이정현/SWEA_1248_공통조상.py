# 노드 클래스 선언
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        # 부모 노드를 저장하기 위한 변수
        self.parent = None
# 공통 조상 찾기 함수
def find_root(node, l):
    if node is None:
        return l
    find_root(node.parent, l)
    l.append(node.value)
    return l
# 자식 노드 개수 세기 함수
def count_child(node):
    if node is None:
        return 0
    return count_child(node.left) + count_child(node.right) + 1

T = int(input())

for test_case in range(1, T + 1):
    v, e, n1, n2 = map(int, input().split())
    arr = list(map(int, input().split()))
    nodes = {}
    # 노드 생성 및 부모-자식 관계 설정
    for i in range(e):
        p = arr[2*i]
        c = arr[2*i+1]
        if p not in nodes:
            nodes[p] = Node(p)
        if c not in nodes:
            nodes[c] = Node(c)
        if nodes[p].left is None:
            nodes[p].left = nodes[c]
        else:
            nodes[p].right = nodes[c]
        nodes[c].parent = nodes[p]

    n1_p = []
    n2_p = []
    result = []
    count = 0
    # 공통 조상 찾기
    find_root(nodes[n1], n1_p)
    find_root(nodes[n2], n2_p)
    # 공통 조상 중 가장 가까운 조상 찾기
    for n in set(n1_p):
        if n in set(n2_p):
            result.append(n)
    # 가장 가까운 조상과 그 자식 노드 개수 출력
    near_root = result[-1]
    count = count_child(nodes[near_root])

    print(f"#{test_case} {near_root} {count}")