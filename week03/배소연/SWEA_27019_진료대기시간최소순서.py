T = int(input())

for tc in range(1, T + 1):
    N = int(input()) #환자의 수
    t_arr = list(map(int, input().split())) #N명의 진료시간
    t_arr.sort()
    
    wait_time = 0
    for i in range(N):
        wait_time += t_arr[i] * (N - i - 1)
        
    print(f'#{tc} {wait_time}')