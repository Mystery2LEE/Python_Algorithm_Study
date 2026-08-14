def flower(n):
    tree = [0] * (n + 1)
    num = 1
    
    def inorder(node):
        nonlocal num
        
        if node > n:
            return
        
        
        inorder(node * 2)
        
        tree[node] = num
        num += 1
        
        inorder(node * 2 + 1)
        
    inorder(1)
    
    return tree
    

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    tree = flower(N)
    
    print(f'#{tc} {tree[1]} {tree[N//2]}')