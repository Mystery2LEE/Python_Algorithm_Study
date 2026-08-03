for _ in range(10):
    tc = int(input())

    target = input().strip()
    string = input().strip()

    answer = 0

    for i in range(len(string) - len(target) + 1):
        if string[i:i+len(target)] == target:
            answer += 1


    print(f'#{tc} {answer}')