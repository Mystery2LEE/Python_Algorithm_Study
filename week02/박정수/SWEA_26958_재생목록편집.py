T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M, L = map(int, input().split())

    records = list(map(int, input().split()))

    for i in range(M):
        command = input().split()
        if command[0] == 'I' :
            records.insert(int(command[1]), int(command[2]))
        elif command[0] == 'D' :
            del records[int(command[1])]
        else :
            records[int(command[1])] = int(command[2])

    if L >= len(records) :
        print(f"#{test_case} -1")
    else :
        print(f"#{test_case} {records[L]}")