T = int(input())

for tc in range(1, T + 1):
    N, X = map(int, input().split())

    arr = []

    for _ in range(N):
        a = list(map(int, input().split()))
        arr.append(a)

    result = 0

    for i in range(N):
        used = [False] * N
        for j in range(N-1):
            if arr[i][j] == arr[i][j + 1]:
                pass
            elif arr[i][j] - arr[i][j + 1] == 1:
                check = 0
                if N - 1 - j >= X:
                    for k in range(X):
                        if arr[i][j + 1] == arr[i][j + 1 + k]:
                            continue
                        else:
                            check = 1
                            break
                    if check == 0:
                        for k in range(X):
                            if used[j + 1 + k] == False:
                                used[j + 1 + k] = True
                            else:
                                check = 1
                                break
                    else:
                        break
                    if check == 1:
                        break
                else:
                    break
            elif arr[i][j] - arr[i][j + 1] == -1:
                check = 0
                if j + 1 >= X:
                    for k in range(X):
                        if arr[i][j] == arr[i][j - k]:
                            continue
                        else:
                            check = 1
                            break
                    if check == 0:
                        for k in range(X):
                            if used[j - k] == False:
                                used[j - k] = True
                            else:
                                check = 1
                                break
                    else:
                        break
                    if check == 1:
                        break
                else:
                    break
            else:
                break
            if j == N - 2:
                result += 1

    for i in range(N):
        used = [False] * N
        for j in range(N-1):
            if arr[j][i] == arr[j + 1][i]:
                pass
            elif arr[j][i] - arr[j + 1][i] == 1:
                check = 0
                if N - 1 - j >= X:
                    for k in range(X):
                        if arr[j + 1][i] == arr[j + 1 + k][i]:
                            continue
                        else:
                            check = 1
                            break
                    if check == 0:
                        for k in range(X):
                            if used[j + 1 + k] == False:
                                used[j + 1 + k] = True
                            else:
                                check = 1
                                break
                    else:
                        break
                    if check == 1:
                        break
                else:
                    break
            elif arr[j][i] - arr[j + 1][i] == -1:
                check = 0
                if j + 1 >= X:
                    for k in range(X):
                        if arr[j][i] == arr[j - k][i]:
                            continue
                        else:
                            check = 1
                            break
                    if check == 0:
                        for k in range(X):
                            if used[j - k] == False:
                                used[j - k] = True
                            else:
                                check = 1
                                break
                    else:
                        break
                    if check == 1:
                        break
                else:
                    break
            else:
                break
            if j == N - 2:
                result += 1


    print(f'#{tc} {result}')