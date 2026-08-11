t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    # 1번부터 M번까지 각 바구니의 처음 수분량
    c = list(map(int, input().split()))
    
    drum = []
    for i in range(n):
        drum.append((i+1, c[i]))
    idx = n
    while len(drum) > 1:
        drum[0] = (drum[0][0],drum[0][1]//2)
        # 갱신된 드럼의 첫번째 바구니
        item = drum.pop(0)
        # 0이면 새 바구니 추가
        if item[1] == 0:            
            if idx < m:
                drum.append((idx+1, c[idx]))
                idx += 1
        else:
            drum.append(item)
    print(f'#{tc} {drum[0][0]}')