T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    
    K, SIZE, M = map(int, input().split())
    water = map(int,input().split())
    #도달할수없으면 0
    
    #급수대 위치ㅣㅣㅣ
    arr = [0] * (SIZE + 1)
    for i in water:
        arr[i] = 1

    start = 0
    count = 0
    find = False
    while True :
        if start + K >= SIZE:
            find = True
            break
        lastIdx = 0
        for i in range(1, K + 1):
    
            if arr[start+i] == 1:
                lastIdx = start+i

        if lastIdx == 0:
            break

        start = lastIdx
        count += 1

    if find: 
        print(f"#{test_case} {count}")
    else:
        print(f"#{test_case} 0")
    