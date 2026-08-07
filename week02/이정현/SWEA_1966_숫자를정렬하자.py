T = int(input())

# 노드 클래스 선언
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


for test_case in range(1, T + 1):
    print(f"#{test_case}", end=" ")
    # 입력 숫자 개수
    n = int(input())
    # 숫자열 입력
    arr = list(map(int, input().split()))

    head = None
    tail = None
    # 이전 연결 리스트 조회 시 사용할 변수
    prev = None
    # 숫자열을 순환
    for a in arr:
        # 숫자를 데이터로 가진 노드 생성
        node = Node(a)
        # 첫번째 숫자일 때 노드 생성후 head, tail 지정
        if head is None:
            head = tail = node

        else:
            # 입력값이 head보다 작을 때 맨 앞에 리스트 넣기
            if a <= head.data:
                node.next = head
                head = node
            # 입력값이 tail보다 클 때 맨 뒤에 넣기
            elif a >= tail.data:
                tail.next = node
                tail = node
            # 사이 값이면 리스트를 순회하면서 리스트 내 값이 숫자보다 크면 숫자를 리스트 앞에 끼워넣기
            else:
                h = head
                while h:
                    if h.data < node.data:
                        prev = h
                        h = h.next
                    else:
                        node.next = h
                        prev.next = node
                        break

    node = head
    while node:
        print(node.data, end=" ")
        node = node.next
    print()
