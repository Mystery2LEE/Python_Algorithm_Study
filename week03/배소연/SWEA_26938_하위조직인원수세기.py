T = int(input())

for tc in range(1, T + 1):
    # E: 보고 관계의 개수
    # N: 하위 조직의 책임자가 될 직원 번호
    E, N = map(int, input().split())
    pair = list(map(int, input().split()))
    
    #각 직원의 부하 목록
    children = [[] for _ in range(E + 2)]
    
    for i in range(0, 2 * E, 2):
        parent = pair[i]
        child = pair[i + 1]
        
        if child != 0:
            children[parent].append(child)
            
    stack = [N]
    count = 0
    
    while stack:
        current = stack.pop()
        count += 1
        
        for child in children[current]:
            stack.append(child)
            
    print(f'#{tc} {count}')