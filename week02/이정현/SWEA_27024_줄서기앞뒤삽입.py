T = int(input())
# 노드 생서
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

for test_case in range(1, T + 1):
    print(f"#{test_case}", end=" ")
    # 숫자 입력
    n = int(input())
    # 연결 리스트 헤드
    head = None
    # 연결 리스트 꼬리
    tail = None
    # c, id 입력
    for _ in range(n):
        c, i = map(int, input().split())
        # 처음 입력되는 값
        if head is None:
            head = tail = Node(i)
        else:
            # c가 1이면 노드를 생성후 헤드로 설정한 뒤에 전체 연결
            if c == 1:
                node = Node(i)
                node.next = head
                head = node
            # c가 2면 노드를 끝에 생성 후 추가
            else:
                tail.next = Node(i)
                tail = tail.next

    node = head
    # 노드안에 값이 있다면 출력
    while node:
        print(node.data, end=" ")
        node = node.next
    print()