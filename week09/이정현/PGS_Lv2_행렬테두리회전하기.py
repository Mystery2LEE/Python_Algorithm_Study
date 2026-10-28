def solution(rows, columns, queries):
    result = []
    arr = [[0]*columns for _ in range(rows)]
    count = 1
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = count
            count += 1
    
    D = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    for a, b, c, d in queries:
        sr, sc, er, ec = a-1, b-1, c-1, d-1
        min_num = rows*columns
        current = 0
        last = arr[sr+1][sc]
        for i in range(sc, ec+1):
            if arr[sr][i] < min_num:
                min_num = arr[sr][i]
            current = arr[sr][i]
            arr[sr][i] = last
            last = current
        
        for j in range(sr+1, er+1):
            if arr[j][ec] < min_num:
                min_num = arr[j][ec]
            current = arr[j][ec]
            arr[j][ec] = last
            last = current
            
        for k in range(ec-1, sc-1, -1):
            if arr[er][k] < min_num:
                min_num = arr[er][k]
            current = arr[er][k]
            arr[er][k] = last
            last = current
            
        for l in range(er-1, sr-1, -1):
            if arr[l][sc] < min_num:
                min_num = arr[l][sc]
            current = arr[l][sc]
            arr[l][sc] = last
            last = current
        result.append(min_num)
                
    return result