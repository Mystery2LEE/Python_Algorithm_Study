T = int(input())

for tc in range(1, T + 1):
    S = input().strip()
    
    stack = []
    quote = None
    valid = True
    
    pair = {
        ')' : '(',
        '}' : '{'
    }
    
    for ch in S:
        if quote is not None:
            if ch == quote:
                quote = None
        
            continue
        
        if ch == "'" or ch == '"':
            quote = ch
            
        elif ch in '({':
            stack.append(ch)
            
        elif ch in ')}':
            if not stack or stack[-1] != pair[ch]:
                valid = False
                break
            
            stack.pop()
            
    if stack:
        valid = False

    
    print(f'#{tc} {1 if valid else 0}')