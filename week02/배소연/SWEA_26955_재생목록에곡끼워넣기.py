T = int(input())

for tc in range(1, T + 1):
    # N: 처음 놓인 곡의 개수
    # M: 끼워 넣을 횟수
    # L: 조회할 자리 번호
    N, M, L = map(int, input().split())
    song_number = list(map(int, input().split())) # 처음 목록에 놓인 N개의 곡 번호
    
    for _ in range(M):
        # p: 끼워 넣을 자리
        # v: 그 자리에 들어갈 곡 번호
        p, v = map(int, input().split())
        song_number.insert(p, v)
    
    print(f'#{tc} {song_number[L]}')