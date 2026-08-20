T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    test_case = int(input())
    score = list(map(int, input().split()))
    num2 = 0
    many = 0
    for i in range(1000):
        num1 = 0
        for j in range(999):
            if score[i] == score[j+1]:
                num1 += 1
        if num1 > num2:
            many = score[i]
            num2 = num1
        elif num1 == num2:
            if score[i] > many:
                many =score[i]
    print(f"#{test_case} {many}")