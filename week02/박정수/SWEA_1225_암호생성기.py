T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int,input().split()))

    count = 0
    while arr:
        num = arr.pop(0) - (count % 5 + 1)
        #문제에서는 0보다 작아지는 경우 0으로 유지되며, 프로그램은 종료 뭐임;
        if num > 0:
            arr.append(num)
        else :
            arr.append(0)
            break
        count += 1
    print(f"#{test_case} {' '.join(map(str, arr))}")  