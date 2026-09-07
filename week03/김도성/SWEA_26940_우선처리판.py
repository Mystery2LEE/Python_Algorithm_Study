T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    arr = [0]

    for a in map(int, input().split()):
        arr.append(a)

        idx = len(arr) - 1

        while idx > 0:
            pa_idx = idx // 2
            if arr[pa_idx] > arr[idx]:
                value = arr[idx]
                arr[idx] = arr[pa_idx]
                arr[pa_idx] = value
            idx = idx // 2

    idx = len(arr) - 1
    result = 0

    while idx > 0:

        result += arr[idx//2]

        idx = idx // 2

    print(f'#{tc} {result}')