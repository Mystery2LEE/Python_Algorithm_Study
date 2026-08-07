T = 10

# 노드 클래스 선언
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


for test_case in range(1, T + 1):
    print(f"#{test_case}", end=" ")
    # 기존 암호 개수 및 암호 입력
    n = int(input())
    arr = list(input().split())

    # 맨앞 노드
    head = None

    # 입력 받은 문자열을 연결 리스트로 변환
    for a in arr:
        if head is None:
            curr = Node(a)
            head = curr

        else:
            curr.next = Node(a)
            curr = curr.next

    # 맨 앞에 값을 넣기위해 더미데이터 생성
    dumy = Node(None)
    dumy.next = head
    head = dumy

    # 수정하는 암호 개수
    control_n = int(input())
    # 암호 변경 명령문 입력
    control_list = [c.strip().split() for c in list(input().split('I')) if c != '']

    # 명령문 1, 2번째 값을 통해 기존 암호문의 어느 위치에 몇개의 값을 넣을 지 입력
    for i in range(control_n):
        node_num = int(control_list[i][0])
        num_count = int(control_list[i][1])
        curr = head

        # 입력 받은 암호 위치만큼 이동
        for _ in range(node_num):
            curr = curr.next

        # 그 위치 뒤에 변경을 위한 암호문 삽입
        for j in range(num_count):
            node = Node(control_list[i][2+j])
            node.next = curr.next
            curr.next = node
            curr = curr.next

    # 더비데이터 제거
    head = head.next
    node = head

    # 10개만 출력
    for _ in range(10):
        print(node.data, end=" ")
        node = node.next
    print()