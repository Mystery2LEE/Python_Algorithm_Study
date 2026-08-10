from collections import deque

T = int(input())

for tc in range(1, T + 1):
    boxes = input().strip()
    stack = deque()
    
    for i in range(len(boxes)):
        if stack and boxes[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(boxes[i])
    
    print(f'#{tc} {len(stack)}')