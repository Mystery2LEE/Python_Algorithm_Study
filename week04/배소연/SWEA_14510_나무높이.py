T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    trees = list(map(int, input().split()))
    tallest_tree = max(trees)
    
    one = 0
    two = 0
    
    for tree in trees:
        diff = tallest_tree - tree
        
        two += diff // 2
        one += diff % 2
        
    while two > one + 1:
        two -= 1
        one += 2
        
    if one > two:
        answer = one * 2 - 1
    else:
        answer = two * 2
    
    print(f'#{tc} {answer}')