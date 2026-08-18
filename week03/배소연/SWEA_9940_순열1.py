T = int(input())

for tc in range(1, T + 1):
    N = int(input()) # 주어지는 정수의 개수
    num_arr = list(map(int, input().split())) # 수열의 원소
    is_ok = True
    
    if len(set(num_arr)) == N:
        
        for num in num_arr:
            if 0 <= num <= N:
                is_ok = True
            else:
                is_ok = False
    else:
        is_ok = False
        
        
    if is_ok:
        print(f'#{tc} Yes')
    else:
        print(f'#{tc} No')