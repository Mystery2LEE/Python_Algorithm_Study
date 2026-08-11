# 함수 없이 Node 클래스에서 prev지정하고 원본 명단을 딕셔너리로 관리하는 게 좋다고 함....

class Node:
    def __init__(self, value=0):
        self.value = value
        self.next = None

# 삭제할 노드의 앞뒤 노드 찾기
def find(haed_node, pid):
    curr = head_node
    prev = None
    while True:
        if curr == head_node and curr.value == pid:
            return prev, curr.next
        elif curr.value == pid:
            return prev, curr.next
        else:
            prev = curr
            curr = curr.next

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    pid = list(map(int, input().split()))
    k = int(input())
    cid = list(map(int, input().split()))

    head_node = None
    curr_node = None

    # 취소 전 명단
    for p in pid:
        new_node = Node(p)
        if head_node == None:
            head_node = new_node
        if curr_node != None:
            curr_node.next = new_node
        curr_node = new_node

    # 타겟 노드 바로 전 노드
    prev = None
    # 타겟 노드 바로 다음 노드
    next = None

    # 취소자 제거
    for cp in cid:
        prev, next = find(head_node, cp)   
        if prev == None:
            head_node = next
        else:
            prev.next = next
    
    curr = head_node
    print(f'#{tc}', end=" ")
    if curr == None:
        print('empty', end=' ')
    else:
        while curr:
            print(curr.value, end=' ')
            curr = curr.next
    
    print()