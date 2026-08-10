T = int(input())

for test_case in range(1, T + 1):
    # 타일 개수, 띠의 수 입력
    n, m = map(int, input().split())
    # 초기 띠 입력
    arr = list(map(int, input().split()))

    for _ in range(m-1):
        # 새로운 띠 입력
        new_arr = list(map(int, input().split()))
        # 전체 띠 순환
        for i in range(len(arr)):
            # 기존 띠의 첫번째 값이 새로운 띠으 첫번째 값보다 크면 앞에 삽입
            if arr[0] > new_arr[0]:
                new_arr.extend(arr)
                arr = new_arr
                break
            # 중간값과 새로운 띠의 처음값을 비교해서 큰 값이 나오면 앞에 삽입
            elif arr[i] > new_arr[0]:
                arr[i:i] = new_arr
                break
            # 끝까지 큰 값이 나오지 않으면 새로운 띠를 마지막에 삽입
            elif i == len(arr)-1:
                arr.extend(new_arr)

    print(f"#{test_case}", " ".join(map(str, arr[:10][:10]))) # 띠를 뒤집고 10개만 출력