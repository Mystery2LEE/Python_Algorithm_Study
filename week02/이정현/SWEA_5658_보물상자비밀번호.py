T = int(input())

for test_case in range(1, T + 1):
    # 숫자의 개수와 출력할 숫자의 순서를 입력
    n, k = map(int, input().split())
    # 숫자열 입력
    arr = list(input())
    # 16진수로 나눌 한 숫자 개수
    count_num = n // 4
    # 16진수를 입력할 배열
    num_list = []
    # 16진구로 이루어진 숫자 개수만큼 반복
    for i in range(count_num):
        # 입력 받은 숫자열을 count_num개수 만큼 끊어서 16진수로 만든 후 16진수를 10진수로
        # 변환 후 리스트에 push
        for j in range(4):
            num = int(''.join(map(str, arr[j*count_num:(j+1)*count_num])), 16)
            # 만약 숫자가 리스트에 있을 시 건너뛰기
            if num in num_list:
                continue
            num_list.append(num)
        # 리스트에 맨앞 수를 빼고 맨 뒤에 넣음 qeue
        arr.insert(0, arr.pop())
    # 리스트 내림차수 정렬
    num_list.sort(reverse=True)
    # k번째 숫자 출력
    print("#{} {}".format(test_case, num_list[k-1]))
