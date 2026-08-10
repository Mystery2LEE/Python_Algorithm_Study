class Node:
    def __init__(self, value=0):
        self.value = value # data
        self.next = None  

t = int(input())
for tc in range(1, t + 1):
    print(f'#{tc} ', end='')
    n = int(input())
    head = None
    tail = None
    for i in range(n):
        # c: 그 사람이 설 위치, data: 번호
        c, data = map(int, input().split())
        new_node = Node(data)
    
        if head == None: 
            head = new_node
            tail = new_node
            continue
        if c == 1: # 맨 앞에 삽입
            new_node.next = head
            head = new_node
        elif c == 2: # 맨 뒤에 삽입
            tail.next = new_node
            tail = new_node
            
    # 노드 출력
    node = head
    while node:
        print(node.value, end=' ')
        node = node.next
    print()
        