t = int(input())
for case in range(1, t+1):
    s=input()
    result = 0
    if s == s[::-1]:
        result = 1
    print(f'#{case} {result}')