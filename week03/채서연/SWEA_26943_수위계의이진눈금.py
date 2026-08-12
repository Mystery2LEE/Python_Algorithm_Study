T = int(input())
for tc in range(1, T+1):
    n = float(input())
    result = ''
    for i in range(13):
        if i == 12:
            result = 'overflow'
            break
        n *= 2
        result += str(int(n))
        n -= int(n)
        if n == 0:
            break

    print(f'#{tc} {result}')