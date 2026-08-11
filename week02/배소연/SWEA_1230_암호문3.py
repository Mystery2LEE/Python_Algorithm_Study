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
    
    tail = curr
    
    return head, tail


def insert_nodes(head, tail, x, nums):
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
        
        head = first
        
        return head, tail
    
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
    else:
        tail = curr
        
    return head, tail


def delete_nodes(head, tail, x, y):
    if x == 0:
        curr = head
        
        for _ in range(y):
            curr = curr.next
    
        head = curr
        
        if head is not None:
            head.prev = None
        else:
            tail = None
        
        return head, tail
    
    curr = head
    for _ in range(x - 1):
        curr = curr.next
    
    next_node = curr.next
    for _ in range(y):
        next_node = next_node.next
    
    curr.next = next_node
    if next_node is not None:
        next_node.prev = curr
    else:
        tail = curr
    
    return head, tail


def add_nodes(head, tail, nums):
    for num in nums:
        new_node = LinkNode(num)
        
        if tail is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            new_node.prev = tail
            tail = new_node

    return head, tail


for tc in range(1, 11):
    N = int(input()) #암호문 개수
    original_crypto = list(map(int, input().split())) #원본 암호문 뭉치
    
    head, tail = make_linked_list(original_crypto)
    
    commands_num = int(input()) #명령어 개수
    commands = input().split() #명령어, x, y, s
    
    idx = 0
    
    for _ in range(commands_num):
        command = commands[idx]
        
        if command == 'I':
            x = int(commands[idx + 1])
            y = int(commands[idx + 2])
            s = list(map(int, commands[idx + 3: idx + 3 + y]))
            
            idx += 3 + y
            head, tail = insert_nodes(head, tail, x, s)
            
        elif command == 'D':
            x = int(commands[idx + 1])
            y = int(commands[idx + 2])
            
            idx += 3
            head, tail = delete_nodes(head, tail, x, y)
            
        elif command == 'A':
            y = int(commands[idx + 1])
            s = list(map(int, commands[idx + 2: idx + 2 + y]))
            
            idx += 2 + y
            head, tail = add_nodes(head, tail, s)
            
    print(f'#{tc}', end=' ')
    
    curr = head
    for _ in range(10):
        if curr is None:
            break
        
        print(curr.val, end=' ')
        curr = curr.next
        
    print()