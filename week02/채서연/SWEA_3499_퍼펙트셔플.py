t = int(input())
for tc in range(1, t+1):
    n = int(input())
    deck = input().split()
    result = []
    
    if n % 2 == 0:
        for i in range(0, n//2):  
            result.append(deck[i])
            result.append(deck[(n//2)+i])
    else:
        for i in range(0, n//2+1):  
            result.append(deck[i])
            if i+1+n//2 < n:
                result.append(deck[i+1+n//2])
            
    print(f'#{tc}',*result)