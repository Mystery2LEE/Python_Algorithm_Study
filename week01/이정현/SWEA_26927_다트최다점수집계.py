T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    arr = list((input().strip()))
    d = {}
    for i in arr:
        if int(i) in d:
            d[int(i)] += 1
        else:
            d[int(i)] = 1

    key = max(d, key=d.get)
    count = d[key]
    keys = [k for k, v in d.items() if v == count]
    max_key = max(keys)

    print(f"#{test_case} {max_key} {count}")