for _ in range(10):
    tc = int(input())
    N, M = map(int, input().split())

    answer = 1
    for _ in range(M):
        answer *= N
    
    print(f'#{tc} {answer}')