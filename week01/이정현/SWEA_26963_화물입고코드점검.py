T = int(input())

for test_case in range(1, T + 1):
    arr1 = input().strip()
    arr2 = input().strip()
    d = {}
    for c1 in arr1:
        d[c1] = 0

    for c2 in arr2:
        if c2 in d:
            d[c2] += 1

    print(f"#{test_case} {d[max(d, key=d.get)]}")