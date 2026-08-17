T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    result = 0
    # 도윤이랑 세아 각각 카드 담을 배열 초기화...
    dy = [0] * 10
    sa = [0] * 10
    isWin = False
    for i in range(12):
        # 도윤
        if i % 2 == 0:
            # 들어오는 카드 인덱스에 +1
            dy[cards[i]] += 1
            # 배열 max가 3이거나 연속된 3개 카드에 0이 없으면 win
            for j in range(8):
                if 0 not in dy[j:j+3]:
                    result = 1
                    isWin = True
                    break
            if isWin:
                break
            if max(dy) == 3:
                result = 1
                break            
            
        # 세아
        else:
            sa[cards[i]] += 1
            
            for j in range(8):
                if 0 not in sa[j:j+3]:
                    result = 2
                    isWin = True
                    break
            if isWin:
                break
            if max(sa) == 3:
                result = 2
                break
            
    
    print(f'#{tc} {result}')