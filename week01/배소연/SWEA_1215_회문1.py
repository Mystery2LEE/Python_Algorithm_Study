for tc in range(1, 11):
    length = int(input())
    arr = [list(input().strip()) for _ in range(8)]
    
    count = 0
    
    for i in range(8):
        for j in range(8-length+1):
            word = arr[i][j:j+length]

            if word == word[::-1]:
                count += 1
            
            word = ''
            for k in range(length):
                word += arr[j+k][i]

            if word == word[::-1]:
                count += 1

    print(f'#{tc} {count}')