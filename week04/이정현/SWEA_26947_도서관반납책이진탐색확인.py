T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()

    l = 0
    r = len(A) - 1
    count = 0

    # B의 각 원소에 대해 이분 탐색을 수행하여 A에 존재하는지 확인
    for b in B:
        bl = l
        br = r
        # 같은 방향을 연속 탐지 방지를 위한 변수
        is_left = None
        # 이분 탐색 수행
        while True:
            m = (bl + br) // 2
            if A[m] < b:
                if is_left is None:
                    is_left = True
                else:
                    if is_left:
                        break
                    else:
                        is_left = True
                bl = m + 1

            elif A[m] > b:
                if is_left is None:
                    is_left = False
                else:
                    if is_left:
                        is_left = False
                    else:
                        break
                br = m - 1

            else:
                count += 1
                break

    print(f"#{test_case} {count}")