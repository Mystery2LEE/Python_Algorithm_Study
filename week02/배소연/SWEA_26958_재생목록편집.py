T = int(input())

for tc in range(1, T + 1):
    # N: 처음 놓인 곡의 개수
    # M: 수행할 편집의 횟수
    # L: 답을 물어볼 자리 번호
    N, M, L = map(int, input().split())
    
    song_list = list(map(int, input().split())) # N개의 곡 ID
    
    for _ in range(M):
        line = input().split()
        command = line[0]
        
        if command == 'I':
            p = int(line[1])
            v = int(line[2])
            
            song_list.insert(p, v)
            
        elif command == 'D':
            p = int(line[1])
            
            del song_list[p]
        elif command == 'C':
            p = int(line[1])
            v = int(line[2])
            
            song_list[p] = v
                
    if L >= len(song_list):
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {song_list[L]}')