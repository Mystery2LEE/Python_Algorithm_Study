N = int(input())
nums = [int(input()) for _ in range(N)]

stack = []
result = []
curr = 0
for i in range(1, N+1):
    stack.append(i)
    result.append('+')
    while stack and nums[curr] == stack[-1]:
        stack.pop()
        curr += 1
        result.append('-')

if curr != N:
    print("NO")
else:
    print('\n'.join(result))