from collections import deque

pair = {
    ')': '(',
    '}': '{',
    ']': '[',
    '>': '<'
}


for tc in range(1, 11):
    N = int(input()) # 테스트케이스의 길이
    line = list(input().strip()) # 테스트케이스
    
    stack = deque()
    valid = True
    
    for ch in line:
        if ch in '({[<':
            stack.append(ch)
        else:
            if not stack or stack[-1] != pair[ch]:
                valid = False
                break
            
            stack.pop()
            
    if stack:
        valid = False
        
    print(f'#{tc} {1 if valid else 0}')