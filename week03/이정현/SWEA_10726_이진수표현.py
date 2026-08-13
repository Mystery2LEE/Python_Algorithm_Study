T = int(input())

# 10진수를 2진수로 변환하는 재귀함수
def bit_trans(num, bit):
    if num == 0:
        return bit.append(0)
    bit_trans(num//2, bit)
    bit.append(num % 2)


for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    bit = []
    is_on = True
    bit_trans(m, bit)
    # 2진수 배열에서 뒤에서 부터 n개의 비트가 모두 1인지 확인
    for b in bit[::-1][:n]:
        if b != 1:
            is_on = False

    if is_on:
        print(f"#{test_case} ON")
    else:
        print(f"#{test_case} OFF")