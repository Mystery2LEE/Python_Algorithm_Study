for tc in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))
    
    answer = 0
    for _ in range(dump):
        boxes.sort()
        boxes[-1] -= 1
        boxes[0] += 1
    
    boxes.sort()
    answer = boxes[-1] - boxes[0]

    print(f'#{tc} {answer}')