# 푸는 중

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())

    tree = [-1]
    for _ in range(n):
        arr = list(input().split())
        index = int(arr.pop(0))
        if index == len(tree):
            if len(arr) > 1:
                tree.append(arr)
            else:
                tree.append(arr[0])
        else:
            while len(tree) < index:
                tree.append(0)
            tree[index] = arr 

    print(tree)
    index = 1
    while True:
        print(index)
        print(tree)
        if len(tree) <= 2:
            break
        if len(tree[index]) > 1:
            cal = tree[index][0]
            left = int(tree[index][1])
            right = int(tree[index][2])
            print(left, right)
            print(tree[left], tree[right])
            if isinstance(tree[right], list):
                index = right
            elif isinstance(tree[left], list):
                index = left
            elif tree[left] == 0 and tree[right] == 0:
                tree.pop(right)
                tree.pop(left)
                index = index // 2
            else:
                num2 = int(tree[right])
                num1 = int(tree[left])
                if cal == '+':
                    tree[index] = num1 + num2
                elif cal == '-':
                    tree[index] = num1 - num2
                elif cal == '*':
                    tree[index] = num1 * num2
                elif cal == '/':
                    tree[index] = num1 / num2
                index = index // 2
                tree[right] = 0
                tree[left] = 0
        check = tree.pop()
        while check == 0:
            check = tree.pop()
        tree.append(check)

    print(f'#{test_case} {int(tree[1])}')

