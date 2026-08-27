T = int(input())

def return_money(money):
    units = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    change = []
    
    for unit in units:
        change.append(money // unit)
        money %= unit
            
    return change


for tc in range(1, T + 1):
    N = int(input()) # 손님에게 거슬러줘야 할 금액
    
    change = return_money(N)
    
    print(f'#{tc}')
    print(*change)