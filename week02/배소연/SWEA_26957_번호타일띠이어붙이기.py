T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split()) #N: 한 띠의 타일 개수, M: 띠의 수
    grid = []
    
    for _ in range(M):
        arr = list(map(int, input().split()))
        grid.append(arr)
        
    answer = grid[0]

    for i in range(1, M):
        target = grid[i][0]
        
        insert_idx = len(answer)
        for idx in range(len(answer)):
            if answer[idx] > target:
                insert_idx = idx
                break
            
        answer = (
            answer[:insert_idx]
            + grid[i]
            + answer[insert_idx:]
        )
        
    print(f'#{tc}', *answer[-1:-11:-1])