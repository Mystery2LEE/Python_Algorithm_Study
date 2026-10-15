def solution(numbers):
    numbers = list(map(str, numbers))
    # numbers = sorted(numbers, key=lambda x:x[0], reverse=True)
    # 각 원소 크기가 1000이하라고 했으니까....최소 문자열 자릿수를 4개로 맞추고 소팅하기
    numbers = sorted(numbers, key=lambda x:x*4, reverse=True)
    answer = ''.join(numbers)
    if answer[0] == '0':
        return '0'
    else:
        return answer