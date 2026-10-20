def solution(numbers):
    number_str = [str(x) for x in numbers]
    number_str.sort(key=lambda x: x * 3, reverse=True)

    return str(int("".join(number_str)))
