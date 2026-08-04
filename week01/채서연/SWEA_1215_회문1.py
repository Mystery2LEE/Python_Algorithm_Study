for t in range(1, 11):
    length = int(input())
    arr = [list(input()) for _ in range(8)]
    count = 0 
        
    # 행에 있는 회문 찾기
    for i in range(8):
        for j in range(8 - length + 1):
            row = []        
            for k in range(length):            
                row.append(arr[i][j+k])
            if row == row[::-1]:
                count += 1
                
    # 열에 있는 회문 찾기
    for j in range(8):
        for i in range(8 - length + 1):
            col = []        
            for k in range(length):            
                col.append(arr[i+k][j])
            if col == col[::-1]:
                count += 1
                
    print(f'#{t} {count}')
