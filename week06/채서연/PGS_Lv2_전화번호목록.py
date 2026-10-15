def solution(phone_book):
    answer = True
    # 길이순으로 정렬하고 현재 번호의 다음부터 끝까지 검사하게 했는데 시간초과 발생함...
    # 사전순으로 정렬하고 바로 다음 번호만 비교하게 변경
    phone_book.sort()
    book_len = len(phone_book)
    
    for i in range(book_len - 1):
        n = len(phone_book[i])
        
        # 바로 다음 번호만 비교
        if phone_book[i] == phone_book[i+1][:n]:
            answer = False
            break

    return answer