for tc in range(1, 11):
    N = int(input()) # 정점의 개수
    tree = [None] * (N + 1)
    
    for _ in range(N):
        line = input().split()
        node_num = int(line[0])
        
        if line[1].isdigit():
            num = int(line[1])
            tree[node_num] = num
        else:
            operator = line[1]
            left = int(line[2])
            right = int(line[3])
            
            tree[node_num] = (operator, left, right)
            
    def calc(node):
        if isinstance(tree[node], int):
            return float(tree[node])
        
        operator, left, right = tree[node]
        
        left_value = calc(left)
        right_value = calc(right)
        
        if operator == '+':
            return left_value + right_value
        elif operator == '-':
            return left_value - right_value
        elif operator == '*':
            return left_value * right_value
        elif operator == '/':
            return left_value // right_value
        
    result = calc(1)
    print(f'#{tc} {int(result)}')