class LinkNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next= None

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    head, tail = None, None
    
    for _ in range(N):
        c, num_id = map(int, input().split())
        new_node = LinkNode(num_id)
        
        if head is None:
            head = new_node
            tail = new_node
        
        elif c == 1: # 줄의 맨 앞
            new_node.next = head
            head.prev = new_node
            head = new_node
            
        elif c == 2: # 줄의 맨 뒤
            new_node.prev = tail
            tail.next = new_node
            tail = new_node
    
    print(f'#{tc}', end=' ')
    
    current = head
    while current is not None:
        print(current.val, end=' ')
        current = current.next
        
    print()