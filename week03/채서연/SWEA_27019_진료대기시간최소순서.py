T = int(input())
for tc in range(1, T+1):
    n = int(input())
    t_i = list(map(int, input().split()))
    t_i.sort()
    time = 0
    for i in range(n):
        time += t_i[i]*(n-i-1)

    print(f'#{tc} {time}')