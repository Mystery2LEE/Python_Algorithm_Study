# SWEA에 python이 없네

t = int(input())
for tc in range(1, t+1):
    k = int(input())
    result = []
    for _ in range(k):
        n = int(input())
        if result and n == 0:
            result.pop()
        else:
            result.append(n)
    print(f'#{tc} {sum(result)}')
