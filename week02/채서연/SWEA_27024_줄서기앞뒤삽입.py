class Node:
    def __init__(self, value):
        self.value = value # id
        self.next = None # c


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    for _ in range(n):
        # c: 그 사람이 설 위치, id: 번호
        c, id = map(int, input().split())