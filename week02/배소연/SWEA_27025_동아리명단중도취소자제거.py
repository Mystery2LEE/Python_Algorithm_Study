class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


def make_linked_list(member_list):
    head = ListNode(member_list[0])
    current = head

    nodes = {member_list[0]: head}

    for member in member_list[1:]:
        new_node = ListNode(member)

        current.next = new_node
        new_node.prev = current

        current = new_node
        nodes[member] = new_node

    return head, nodes


def remove_node(head, node):
    if node.prev:
        node.prev.next = node.next
    else:
        head = node.next

    if node.next:
        node.next.prev = node.prev

    return head


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    member_list = list(map(int, input().split()))

    head, nodes = make_linked_list(member_list)

    K = int(input())
    canceled_member_list = list(map(int, input().split()))

    for member in canceled_member_list:
        node = nodes[member]
        head = remove_node(head, node)

    result = []
    current = head

    while current:
        result.append(str(current.val))
        current = current.next

    if result:
        print(f"#{tc} {' '.join(result)}")
    else:
        print(f"#{tc} empty")