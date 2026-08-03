for t in range(1, 11):
    n, s = input().split()
    result = []
    for x in s:
        if len(result) == 0:
            result.append(x)
            continue
            
        if result[-1] == x:
            result.pop()
        else:
            result.append(x)
    result = ''.join(result)
    print(f'#{t} {result}')