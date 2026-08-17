# SWEA에 파이썬 없어서 c++로 변환해서 제출햇음

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    n_arr = list(map(int, input().split()))
    arr = [0] * N
    result = "No"
    for x in n_arr:
        arr[x-1] += 1
    if 0 not in arr:
        result = "Yes"
    print(f'#{tc} {result}')