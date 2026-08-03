T = 10

for test_case in range(1, T + 1):
    t = int(input())
    special = input().rstrip()
    arr = input().rstrip()

    length = len(special)

    count = 0
    for i in range(len(arr)-length+1):
        if ''.join(arr[i:i+length]) == special:
            count += 1

    print(f"#{t} {count}")