# 트리 노드 클래스
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
# 부하 직원 노드 개수 세기
def count(node):
    # 노드에 값이 없으면 0을 리턴
    if node is None:
        return 0
    cnt = 0
    # 스택에 노드를 쌓음
    stack = [node]
    while stack:
        # 스택 내에 값이 있으면 pop
        cur = stack.pop()
        cnt += 1
        # 부하 직원이 있으면 스택에 쌓기
        if cur.left:
            stack.append(cur.left)
        if cur.right:
            stack.append(cur.right)
    return cnt

T = int(input())

for test_case in range(1, T + 1):
    m, n = map(int, input().split())
    arr = list(map(int, input().split()))
    # 노드를 연결할 딕셔너리
    nodes = {}
    # 출현 횟수를 셀 딕셔너리
    appear_count = {}
    for i in range(m):
        h = arr[2*i]
        c = arr[2*i+1]
        # 처음 나왔다면 딕셔너리에 노드 추가
        if h not in nodes:
            nodes[h] = Node(h)
        # 처음 나왔다면 appear_count 딕셔너리에 추가
        if h not in appear_count:
            appear_count[h] = 0
        # c가 0이 아니고 c가 노드에 없다면 생성
        if c != 0 and c not in nodes:
            nodes[c] = Node(c)
        # 출현 횟수가 0이면 left에 추가
        if appear_count[h] == 0:
            nodes[h].left = None if c == 0 else nodes[c]
        else:
        # 아니면 right에 추가
            nodes[h].right = None if c == 0 else nodes[c]
        # 출현 횟수 증가
        appear_count[h] += 1

    print(f"#{test_case} {count(nodes[n])}")