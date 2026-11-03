def solution(land):
    for i in range(1, len(land)):
        for j in range(0, len(land[0])):
            max_num = 0
            for k in range(0, len(land[0])):
                if j == k:
                    continue
                if land[i-1][k] > max_num:
                    max_num = land[i-1][k]
            land[i][j] += max_num
    
    answer = max(land[len(land)-1])
    return answer