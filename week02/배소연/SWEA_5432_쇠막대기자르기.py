T = int(input())

for tc in range(1, T + 1):
    line = list(input().strip())
    
    open_count = 0
    pieces = 0
    
    for i in range(len(line)):
        if line[i] == '(':
            open_count += 1
        else:
            open_count -= 1
            
            if line[i-1] == '(':
                pieces += open_count
            else:
                pieces += 1
    
    print(f'#{tc} {pieces}')