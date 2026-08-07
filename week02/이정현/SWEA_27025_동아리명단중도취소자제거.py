T = int(input())

# 노드 클래스 선언
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

for test_case in range(1, T + 1):
    print(f"#{test_case}",end=" ")
    # 입력
    n = int(input())
    arr = list(input().split())


    head = None
    # 연결 리스트 내 노드에 입력받은 값 입력
    for a in arr:
        if head is None:
            node = Node(a)
            head = node
        else:
            node.next = Node(a)
            node = node.next

    # 입력2
    result_n = int(input())
    cancel = list(input().split())

    # 취소 리스트 내에 있는 값이 노드 어디에 있는지 찾고 해당 노드 연결선을 끊음
    for c in cancel:
        node = head
        prev = None
        while node.data != c:
            prev = node
            node = node.next

        if node == head:
            head = node.next
        else:
            next_node = node.next
            node = prev
            node.next = next_node

    # 노드 순서를 1번으로 바꿈
    node = head
    # 노드에 아무 것도 없으면 'enpty' 출력 있으면 차례대로 출력
    if not node:
        print("empty", end="")
    else:
        while node:
            print(node.data, end=" ")
            node = node.next
    print()