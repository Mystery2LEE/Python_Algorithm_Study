T = int(input())

for tc in range(1, T + 1):
    N, setting_code = input().split()
    result = ""
    
    for code in setting_code:
        # result += bin(int(code, 16))[2:].zfill(4)
        # b: 2진수로 변환
        # 4: 4자리
        # 0: 빈 앞자리를 0으로 채움
        result += format(int(code, 16), '04b')
        
    print(f'#{tc} {result}')