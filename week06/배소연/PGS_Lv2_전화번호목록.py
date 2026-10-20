def solution(phone_book):
    phone_set = set(phone_book)

    for phone_number in phone_book:
        prefix = ""

        for number_char in phone_number:
            prefix += number_char
            if prefix in phone_set and prefix != phone_number:
                return False

    return True
