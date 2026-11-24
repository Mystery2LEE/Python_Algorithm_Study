N = int(input())
scores = [list(map(int, input().split())) for _ in range(3)]

l = []
for i in range(3):
    s_l = []
    for j in range(N):
        s_l.append((j, scores[i][j]))
    s_l.sort(key = lambda x : x[1], reverse=True)
    arr = [0] * N
    for k in range(N):
        if k > 0 and s_l[k][1] == s_l[k-1][1]:     
            arr[s_l[k][0]] = arr[s_l[k-1][0]]       
        else:
            arr[s_l[k][0]] = k+1
    l.append(arr)

result = [x + y + z for x, y, z in zip(scores[0], scores[1], scores[2])]
r = []
for i in range(N):
    r.append((i, result[i]))
r.sort(key = lambda x : x[1], reverse=True)
arr2 = [0] * N
for k in range(N):
    if k > 0 and r[k][1] == r[k-1][1]:
        arr2[r[k][0]] = arr2[r[k-1][0]]
    else:
        arr2[r[k][0]] = k+1
l.append(arr2)

for i in range(4):
    print(*l[i])