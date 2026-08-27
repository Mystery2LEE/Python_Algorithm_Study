count = [0] * 1000001

for num in map(int, input().split()):
    count[num] += 1

cnt = 0

for num in range(1, 1000001):
    cnt += count[num]

    if cnt > 500000:
        print(num)
        break