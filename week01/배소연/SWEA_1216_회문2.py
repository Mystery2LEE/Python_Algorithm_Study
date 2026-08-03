for _ in range(10):
    tc = int(input())
    arr = [list(input().strip()) for _ in range(100)]

    answer = 1
    for length in range(100, 0, -1):
        found = False

        for i in range(100):
            for j in range(100 - length + 1):
                word = arr[i][j: j+length]

                if word == word[::-1]:
                    answer = length
                    found = True
                    break

                word = ''
                for k in range(length):
                    word += arr[j+k][i]
                
                if word == word[::-1]:
                    answer = length
                    found = True
                    break

            if found:
                break

        if found:
            break

    print(f'#{tc} {answer}')