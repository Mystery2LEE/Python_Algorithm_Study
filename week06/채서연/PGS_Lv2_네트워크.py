def solution(n, computers):
    answer = n
    # visited는 1차원배열.....
    visited = [False] * n
    
    def dfs(i):
        nonlocal answer
        visited[i] = True

        for j in range(n):
            if i != j:
                
                if not visited[j] and computers[i][j] == 1:
                    answer -= 1
                    dfs(j)
                    
    for i in range(n):
        if not visited[i]:
            dfs(i)
    return answer