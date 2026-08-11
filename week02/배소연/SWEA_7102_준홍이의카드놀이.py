T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    cardset_a = [i for i in range(1, N + 1)]
    cardset_b = [i for i in range(1, M + 1)]
    result = [0] * (N + M + 1)
    
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            result[i + j] += 1
            
    max_count = max(result)
    print(f'#{tc}', end=' ')
            
    for idx in range(len(result)):
        if result[idx] == max_count:
            print(idx, end=' ')
    
    print()