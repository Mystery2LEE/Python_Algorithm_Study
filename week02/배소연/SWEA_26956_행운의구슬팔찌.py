T = int(input())

for tc in range(1, T + 1):
    # N: 구슬의 개수
    # M: 세는 칸 수
    # K: 반복 횟수
    N, M, K = map(int, input().split())
    bizz = list(map(int, input().split()))
    
    idx = 0
    
    for _ in range(K):
        next_idx = (idx + M) % len(bizz)
        
        if next_idx == 0:
            new_num = bizz[-1] + bizz[0]
            bizz.append(new_num)
            idx = len(bizz) - 1
            
        else:
            new_num = bizz[next_idx - 1] + bizz[next_idx]
            bizz.insert(next_idx, new_num)
            idx = next_idx
    
    print(f'#{tc}', *bizz[-1:-11:-1])