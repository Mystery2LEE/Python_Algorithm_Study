def solution(book_time):
    # 예약 내역 저장 배열
    book = [[0]*60 for _ in range(24)]
    # 예약 시간, 분을 나눠 해당 시간 내에 있으면 값 + 1
    for s, e in book_time:
        max_num = 0
        sr, sc = map(int, s.split(':'))
        er, ec = map(int, e.split(':'))
        ec += 9
        if ec >= 60:
            er += 1
            ec -= 60
        if er > 23:
            er = 23
            ec = 59
        for r in range(sr, er + 1):
            for c in range(60):
                is_not = False
                if r == sr and c < sc:
                    is_not = True
                if r == er and c > ec:
                    is_not = True
                if is_not:
                    continue
                book[r][c] += 1              
    # 배열 내 최대값이 필요한 객실 개수
    return max(map(max, book))