from itertools import permutations

def is_demical(n):
    # 0과 1은 소수가 아닙니다
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  # n//2+1보다 효율적입니다
        if n % i == 0:
            return False
    return True

def solution(numbers):
    # 'numbers' 문자열의 각 글자를 리스트로 쪼갭니다 (예: ['1', '7'])
    number_list = list(numbers)
    com_num = set()
    
    # 1개짜리 조합부터 전체 개수(len)짜리 조합까지 모두 생성
    for i in range(1, len(number_list) + 1):
        for p in permutations(number_list, i):
            # p는 ('1', '7') 같은 튜플입니다. 이를 '17'로 합친 후 int로 변환합니다.
            com_num.add(int(''.join(p)))
            
    answer = 0
    for c in com_num:
        if is_demical(c):
            answer += 1
            
    return answer
