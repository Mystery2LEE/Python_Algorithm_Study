T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    boxes = list(map(int, input().split()))
    human = list(map(int, input().split()))
    ok = [False] * n
    result = []

    boxes.sort()
    human.sort()
    # human과 boxes를 내림차순으로 정렬한 후, human의 능력치가 boxes의 상자 무게보다 크거나 같은 경우에만 상자를 옮길 수 있도록 구현
    for h in range(len(human) - 1, -1, -1):
        # human의 능력치가 boxes의 상자 무게보다 크거나 같은 경우에만 상자를 옮길 수 있도록 구현
        for b in range(len(boxes) - 1, -1, -1):
            # 이미 옮긴 상자는 건너뛰도록 구현
            if ok[b]:
                continue

            if human[h] >= boxes[b]:
                result.append(boxes[b])
                ok[b] = True
                break

    print(f"#{test_case} {sum(result)}")