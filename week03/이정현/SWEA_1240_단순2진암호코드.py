T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    b = 0
    c = 0
    num = 0
    # 2진수 배열에서 뒤에서 부터 1이 있는 위치를 찾아 56개의 비트 추출 후 7개씩 나누어 숫자 변환
    for i in range(n):
        for j in range(m-1, -1, -1):
            if arr[i][j] == '1':
                # 56개의 비트 추출
                p_arr = arr[i][j-55:j+1]
                # 7개씩 나누어 숫자 변환
                for k in range(8):
                    a = ''.join(map(str, p_arr[7*k:7*k+7]))
                    if a == '0001101':
                        num = 0
                    elif a == '0011001':
                        num = 1
                    elif a == '0010011':
                        num = 2
                    elif a == '0111101':
                        num = 3
                    elif a == '0100011':
                        num = 4
                    elif a == '0110001':
                        num = 5
                    elif a == '0101111':
                        num = 6
                    elif a == '0111011':
                        num = 7
                    elif a == '0110111':
                        num = 8
                    elif a == '0001011':
                        num = 9
                    if (k+1) % 2 == 0:
                        c += num
                    else:
                        b += num
                # 검증 코드 계산 후 출력
                if (b * 3 + c) % 10 == 0:
                    print(f"#{test_case} {b + c}")
                else:
                    print(f"#{test_case} {0}")
                break
        if b != 0:
            break