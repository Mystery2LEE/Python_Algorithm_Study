T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(m)]
    result = arr[0]
    for i in range(1, m):
        for j in range(len(result)):
            if j==0 and result[j] > arr[i][0]:
                result[0:0] = arr[i]
                break
            elif j != 0 and result[j] > arr[i][0]:
                result[j:j] = arr[i]
                break
            elif j == len(result) - 1 and result[j] <= arr[i][0]:
                result.extend(arr[i])

    print(f'#{tc}', *result[-10:][::-1])