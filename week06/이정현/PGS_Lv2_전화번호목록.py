def solution(phone_book):
    # 리스트 정렬
    phone_book.sort()
    # 리스트 탐색
    for i in range(len(phone_book)-1):
        # 접두어의 길이
        s = len(phone_book[i])
        # 만약 다음것과 같으면 False = 이유는 숫자를 정렬시 접두어를 포함한 숫자가 바로 뒤에 와야하기 때문
        if phone_book[i+1][:s] == phone_book[i]:
            return False
    return True

# hash를 사용하기 위한 set으로 변경
    book = set(phone_book)
    
    # set 내부의 값을 선정
    for number in book:
        # number의 길이만 큼 돌면서 해당 단어가 접두사를 포함하는지 확인
        for i in range(1, len(number)):
            if number[:i] in book:
                return False
    return True