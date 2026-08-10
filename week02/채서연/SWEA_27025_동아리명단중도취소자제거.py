class Node:
    def __init__(self, value=0):
        self.value = value
        self.next = None

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    id = list(map(int, input().split()))
    k = int(input())
    cid = list(map(int, input().split()))
    
    # 타겟 노드 바로 전 노드
    prev = None
    # 타겟 노드 바로 다음 노드
    next = None
    prev.next = next
    
    
    print(f'#{tc} ')