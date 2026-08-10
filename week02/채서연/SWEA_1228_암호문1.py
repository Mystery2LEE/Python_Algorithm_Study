class Node:
    def __init__(self, value=0):
        self.value = value
        self.next = None

for tc in range(1, 11):
    n = int(input())
    pwd = input().split()
    m =int(input())
    cm = input().split()

    head_node = None
    curr_node = None
    # 원본 암호문
    for p in pwd:
        new_node = Node(p)  
        if head_node == None:
            head_node = new_node
        if curr_node != None:
            curr_node.next = new_node
        curr_node = new_node

    # 암호문 수정
    i = 0
    while i < len(cm):
        x = int(cm[i + 1])
        y = int(cm[i + 2])

        insert_data = cm[i + 3:i + 3 + y]

        curr = None

        if x == 0:
            # 맨 앞에 삽입
            for data in reversed(insert_data):
                new_node = Node(data)
                new_node.next = head_node
                head_node = new_node

        else:
            # x번째 노드 찾기
            curr = head_node

            for _ in range(x - 1):
                curr = curr.next

            # x번째 노드 뒤에 삽입
            for data in insert_data:
                new_node = Node(data)

                new_node.next = curr.next
                curr.next = new_node

                curr = new_node

        i += 3 + y

    result = []
    curr = head_node

    for _ in range(10):
        result.append(curr.value)
        curr = curr.next

    print(f"#{tc}", *result)