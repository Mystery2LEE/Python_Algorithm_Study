T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, num_str = input().split()
    n = int(n)
    num_str = str(num_str)

    num_list = [-1]
    for num in num_str:
        if num_list[-1] == num:
            num_list.pop()
        else:
            num_list.append(num)
    num_list.pop(0)

    print(f'#{test_case} ', *num_list, sep='')