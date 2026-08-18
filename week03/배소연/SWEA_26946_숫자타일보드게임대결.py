def check(hand):
    for i in range(10):
        if hand[i] >= 3:
            return True
    
    for i in range(8):
        if hand[i] > 0 and hand[i + 1] > 0 and hand[i + 2] > 0:
            return True
    
    return False

T = int(input())

for tc in range(1, T + 1):
    cards = list(map(int, input().split()))
    
    doyun = [0] * 10
    seah = [0] * 10
    
    winner = 0
    
    for i in range(12):
        card = cards[i]
        
        if i % 2 == 0:
            doyun[card] += 1
            
            if check(doyun):
                winner = 1
                break
        else:
            seah[card] += 1
            
            if check(seah):
                winner = 2
                break
            
    print(f'#{tc} {winner}')