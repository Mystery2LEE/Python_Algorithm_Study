T = int(input())

for test_case in range(1, T + 1):
    t, num = input().split()
    num = int(num)
    arr = list(input().split())
    print(f"{t}")

    d = {0:"ZRO", 1:"ONE", 2:"TWO", 3:"THR", 4:"FOR", 5:"FIV", 6:"SIX", 7:"SVN", 8:"EGT", 9:"NIN"}
    for i in range(10):
        for c in arr:
            if d[i] == c:
                print(c, end=" ")