def open_book(p, n):
    count = 0
    r = p
    l = 1
    while True:
        count += 1
        page = (r + l) // 2
        if page == n:
            break
        elif page < n:
            l = page
        elif page > n:
            r = page

    return count


for test_case in range(1, T + 1):
    p, j, h = map(int, input().split())

    j_count = open_book(p, j)
    h_count = open_book(p, h)
    result = ''

    if j_count == h_count:
        result = '0'
    elif j_count < h_count:
        result = 'A'
    elif j_count > h_count:
        result = 'B'

    print(f"#{test_case} {result}")