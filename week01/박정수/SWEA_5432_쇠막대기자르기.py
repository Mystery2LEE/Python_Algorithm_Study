T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    S = input()

    # "(" 체크해야되는데 흠
    # 만약에 ( 일때 다음도 ) 라면 기존에 있던 (의 개수만큼 더하기?
    # 위의 경우가 맞을려면 문자열은 항상 올바른 괄호를 가지고 있어야함 
    total = 0
    steal = 0
    i = 0
    while i < len(S) :
        c = S[i]
        if c == '(':
            nextC = S[i+1]
            if nextC == ')':
                total += steal 
                i += 1
            else :
                steal += 1
                total += 1
        else :
            steal -= 1
        i += 1
    print(f"#{test_case} {total}")