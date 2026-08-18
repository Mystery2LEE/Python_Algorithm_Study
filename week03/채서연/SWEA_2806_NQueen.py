T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # graph[row] = col
    # graph[0] = 1 -> 0행 1열에 퀸을 놓았다는 말
    graph = [0]*N    
    
    def nqueen(V):
        global count
        if V == N:
            count+=1
            return
        else:
            # 현재 행에서 각 열에 퀸을 놓아봄
            for x in range(N):
                # 놓을 수 있는 위치면 
                if is_valid(V, x):
                    graph[V] = x
                    nqueen(V+1)

    def is_valid(row, col):
        for i in range(row):
            # abs(graph[i] - col) == row - i -> 대각선 검사
            if graph[i] == col or abs(graph[i] - col) == row - i:
                return False
        return True
        
        
    count = 0
    nqueen(0)
    print(f'#{tc} {count}')