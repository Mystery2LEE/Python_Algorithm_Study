T = 10

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


for test_case in range(1, T + 1):
    print(f"#{test_case}", end=" ")
    n = int(input())
    arr = list(input().split())

    head = None
    prev = None

    for a in arr:
        if head is None:
            curr = Node(a)
            head = curr

        else:
            curr.next = Node(a)
            prev = curr
            curr = curr.next

    control_n = int(input())
    control_list = [c.strip().split() for c in list(input().split('I')) if c != '']

    for i in range(control_n):
        node_num = int(control_list[i][0])
        num_count = int(control_list[i][1])
        curr = head

        for _ in range(node_num):
            prev = curr
            curr = curr.next

        for j in range(num_count):
            node = Node(control_list[i][2+j])
            node.next = curr
            prev.next = node

    node = head
    for _ in range(10):
        print(node.data, end=" ")
        node = node.next
    print()