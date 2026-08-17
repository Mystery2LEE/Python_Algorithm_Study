"""
링크: https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AZ87c1z6yFHHBITH
난이도: D2
유형: backtracking
시간복잡도: 
소요시간: 45분
복습필요: Y
회고: gpt이용해서 이해함 복습 필요 재귀함수 활용을 잘 못하겠음
"""

import sys

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n, m, k = map(int, input().split())
    adj_list = [[] for _ in range(n)]
    
    for _ in range(m):
        a, b = list(map(int, input().split()))
        adj_list[a - 1].append(b-1)
        adj_list[b - 1].append(a-1)
        
    painted = [0] * n
    colors = list(range(1, k + 1))
    count = 0
    
    def can_paint(area, color):
        for neighbor in adj_list[area]:
            if painted[neighbor] == color:
                return False
            
        return True
    
    def backtracking(area):
        global count
        
        if area == n:
            count += 1
            return
        
        for color in colors:
            if can_paint(area, color):
                painted[area] = color
                backtracking(area + 1)
                painted[area] = 0
                
    backtracking(0)
        
    print(f'#{test_case} {count}')
    