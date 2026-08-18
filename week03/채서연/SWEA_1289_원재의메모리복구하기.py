T = int(input())
for tc in range(1, T+1):
    origin = list(map(int,input()))
    count = 0
    L = len(origin)
    initial = [0]*L

    for i in range(L):
        if origin[i] != initial[i]:
            if origin[i] == 0:
                initial[i:] = [0]*(L-i)
            else:
                initial[i:] = [1]*(L-i)
            count += 1


    print(f'#{tc} {count}')
