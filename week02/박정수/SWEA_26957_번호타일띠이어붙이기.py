T = int(input())

for test_case in range(1, T + 1):
    N,M = map(int, input().split())

    arr = []

    for i in range(M):
        tail = list(map(int, input().split()))
        head = tail[0]
        #일단 여기까지는 ok 
        #흠 head에서 각 arr별 값을 비교.....
        idx = 0
        for i in range(len(arr)):
            if head < arr[i] :
                break
            else :
                idx += 1
    
        arr = arr[:idx] + tail + arr[idx:]
    print(f'#{test_case} {" ".join(map(str, arr[-1:-11:-1]))}')