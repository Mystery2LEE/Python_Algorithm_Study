# 노드 클래스
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
# 사칙연산 함수
def cal(node):
    # 노드의 value가 정수형일 때 value를 리턴
    if node.value.isdigit():
        return int(node.value)
    # 아닐때 value의 값에 따라 사칙연산을 실행하며 왼쪽 부터 중앙 오른쪽을 탐색해서 중위 순회
    else:
        if node.value == '+':
            return cal(node.left) + cal(node.right)
        elif node.value == '-':
            return cal(node.left) - cal(node.right)
        elif node.value == '*':
            return cal(node.left) * cal(node.right)
        elif node.value == '/':
            return cal(node.left) / cal(node.right)


T = 10

for test_case in range(1, T + 1):
    n = int(input())
    # 노드를 담을 딕셔너리
    nodes = {}

    for _ in range(n):
        arr = list(input().split())
        # 값이 기호이면
        if int(arr[0]) not in nodes:
            # 노드를 생성하고 value를 채워넣는다
            nodes[int(arr[0])] = Node(arr[1])
        # 값이 none이면 value에 값을 채워 넣는다
        if nodes[int(arr[0])].value is None:
            nodes[int(arr[0])].value = arr[1]
        # value가 기호일때
        if not arr[1].isdigit():
            # 왼쪽 오른쪽 자식 노드를 생성하고 None값을 넣는다 추후에 None값일 때 값을 채움
            if int(arr[2]) not in nodes:
                nodes[int(arr[2])] = Node(None)
            if int(arr[3]) not in nodes:
                nodes[int(arr[3])] = Node(None)

            nodes[int(arr[0])].left = nodes[int(arr[2])]
            nodes[int(arr[0])].right = nodes[int(arr[3])]

    print(f"#{test_case} {int(cal(nodes[1]))}")