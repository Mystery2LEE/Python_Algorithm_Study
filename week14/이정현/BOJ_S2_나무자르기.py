N, M = map(int, input().split())
trees = list(map(int, input().split()))

low = 0
high = max(trees)
answer = 0

while low <= high:
    v = (low + high)//2
    H = 0
    for t in trees:
        if t > v:
            H += (t - v)
        if H > M: 
            break
    
    if H >= M:
        answer = v
        low = v + 1
    else:
        high = v - 1
print(answer)