# 다시 풀어보기

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    chr_list = list(input())
    
    arr_check = []
    for c in chr_list:
        if c == '(' or c == '{':
            arr_check.append(c)
        elif c == ')':
            if arr_check == []:
                arr_check.append(c)
                break
            elif arr_check[-1] == '(':
                arr_check.pop()
            else:
                break
        elif c == '}':
            if arr_check == []:
                arr_check.append(c)
                break
            elif arr_check[-1] == '{':
                arr_check.pop()
            else:
                break
            
    if arr_check == []:
        print(f'#{test_case} 1')
    else :
        print(f'#{test_case} 0')