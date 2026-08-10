from collections import deque

T = int(input())

for tc in range(1, T + 1):
    print(f'#{tc}', end=' ')
    
    M = int(input()) # 처리할 연산의 개수
    codes = list(map(int, input().split()))
    
    result = deque()
    number = 1
    
    for code in codes:
        if code == 1:
            result.append(number)
            number += 1
        elif code == 2:
            if result:
                print(result.popleft(), end=' ')
                
    print()