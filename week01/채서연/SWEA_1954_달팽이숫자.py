# 너무 어려움 에.바. 라고 생각

# 인덱스를 활용해서 방향 전환
dr = [-1, 0, 1, 0] # 행 방향 전환, -1 -> 왼쪽으로 한칸 1 -> 오른쪽으로 한칸
dc = [0, 1, 0, -1] # 열 방향 전환 -1 -> 위로 한칸 1 -> 아래로 한칸

t = int(input())

for case in range(1, t+1):
    n = int(input())
    snail = [[0]*n for _ in range(n)]
    
    # 초기 위치 & 회전 방향 설정
    r, c = 0, 0
    dist = 0 # 0:우 1:하 2:좌 3:상
    
    for i in range(1, n*n+1):
        snail[r][c] = i
        r += dr[dist]
        c += dc[dist]
        
        # 범위를 벗어나거나 0이 아닌 다른 값이 이미 있다면 방향 변경
        # 인덱스를 원위치시켜야 함 -> dist 다시 빼주기
        # 방향 바꾸고 다시 움직일 수 있게 인덱스 업데이트
        if r < 0 or c < 0 or r >= n or c >= n or snail[r][c] != 0:
            # 인덱스 원위치
            r -= dr[dist]
            c -= dc[dist]
            dist = (dist + 1) % 4
            r += dr[dist]
            c += dc[dist]
            
        
    print(f'#{case}')
    for row in snail:
        print(*row)