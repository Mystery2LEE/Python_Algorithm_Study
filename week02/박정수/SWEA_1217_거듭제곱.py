for test_case in range(1, 11):
    N = int(input())

    n, c = map(int, input().split())

    stack=[n] * c

    if n == 0:
        print(f"#{test_case} 0")
        continue
    
    total = 1

    while stack :
        total *= stack.pop()
    
    print(f"#{test_case} {total}")