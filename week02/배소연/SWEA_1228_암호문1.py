class LinkNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


def make_linked_list(arr):
    head = LinkNode(arr[0])
    curr = head

    for item in arr[1:]:
        new_node = LinkNode(item)

        curr.next = new_node
        new_node.prev = curr

        curr = new_node        

    return head

def insert_nodes(head, x, nums):
    if x == 0:
        first = None
        curr = None

        for num in nums:
            new_node = LinkNode(num)

            if first is None:
                first = new_node
                curr = new_node
            else:
                curr.next = new_node
                new_node.prev = curr

                curr = new_node

        curr.next = head
        head.prev = curr

        return first

    curr = head
    for _ in range(x - 1):
        curr = curr.next

    next_node = curr.next
    for num in nums:
        new_node = LinkNode(num)

        curr.next = new_node
        new_node.prev = curr

        curr = new_node

    curr.next = next_node
    if next_node is not None:
        next_node.prev = curr

    return head


for tc in range(1, 11):
    N = int(input()) #원본 암호문의 길이
    arr = list(map(int, input().split())) #원본 암호문

    crypto_list = make_linked_list(arr)

    command_num = int(input()) #명령어의 개수
    commands = input().split() #명령어, x, y, s

    idx = 0

    for _ in range(command_num):
        command = commands[idx]
        x = int(commands[idx + 1])
        y = int(commands[idx + 2])

        s = list(map(
            int,
            commands[idx + 3:idx + 3 + y]
        ))

        crypto_list = insert_nodes(crypto_list, x, s)

        idx += 3 + y

    print(f'#{tc}', end=' ')

    curr = crypto_list
    for _ in range(10):
        print(curr.val, end=' ')
        curr = curr.next

    print()