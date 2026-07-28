memo = {2:[[1,2],[4,3]]}

def rotate_plus(n):
    if n in memo :
        return memo[n]
    else:
        ret = [[0] * n for _ in range(n)]
        ret[0] = [i for i in range(1, n + 1)]

        for i in range(1, n):
            ret[i][-1] = i + n

        for i in range(n - 1):
            for j in range(n - 1):
                ret[n - i - 1][-2 - j] = rotate_plus(n - 1)[i][j] + 2 * n - 1
        memo[n] = ret
        return ret

for testcase in range(1, int(input())+1):
    N = int(input())
    print(f'#{testcase}')
    for i in range(N):
        print(*rotate_plus(N)[i])