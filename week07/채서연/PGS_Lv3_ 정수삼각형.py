def solution(triangle):
    answer = 0
    n  = len(triangle)
    dp = [[0] * n for _ in range(n)]
    dp[0][0] = triangle[0][0]
    
    for r in range(1, n):
        for c in range(r + 1):
            # 왼쪽 변에 있는 요소는 오른쪽 위에 값(같은 컬럼)만 더해짐
            if c == 0:
                dp[r][c] = dp[r-1][c] + triangle[r][c]
            # 오른쪽 변에 있는 요소는 왼쪽 위에 값(같은 컬럼)만 더해짐
            elif c == r:
                dp[r][c] = dp[r-1][c-1] + triangle[r][c]
            else:
                dp[r][c] = max(dp[r-1][c], dp[r-1][c-1]) + triangle[r][c]
                
    answer = max(dp[-1])
    return answer