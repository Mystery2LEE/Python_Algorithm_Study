def solution(numbers):
    # 두수를 합친것을 서로 비교하여 어떤 수가 더 큰지 확인
    def custom_key(x, y):
        s_x = str(x)
        s_y = str(y)
        a = s_x + s_y
        b = s_y + s_x
        
        if int(a) > int(b):
            return 1
        elif int(a) < int(b):
            return -1
        else:
            return 0
    
    # 재귀를 이용해 퀵솔트 구현
    def sort_nums(arr):
        if len(arr) <= 1:
            return ''.join(map(str, arr))
        pivot = len(arr) // 2
        front_arr, pivot_arr, back_arr = [], [], []
        for value in arr:
            if custom_key(value, arr[pivot]) > 0:
                front_arr.append(value)
            elif custom_key(value, arr[pivot]) < 0:
                back_arr.append(value)
            else:
                pivot_arr.append(value)
        answer = sort_nums(front_arr) + ''.join(map(str, pivot_arr)) + sort_nums(back_arr)
        return answer
    result = sort_nums(numbers)
    # 입력값이 [0, 0, 0]인 경우를 대비
    if result[0] == '0':
        result = '0'
    return result