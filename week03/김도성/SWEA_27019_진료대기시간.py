# 완전탐색과 그리디 개념 확인

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    person = int(input())
    time = list(map(int, input().split()))
    
    count_min = 999999999999999
    '''
    for i in range(len(time)):
        time_test = time[:]
        time_test.pop(i)
        time_test.sort()
        count = 0
        count_all = 0
        for t in time_test:
            # count = count + count + t -> 사실 2*count + t라 의도한 바와 다름
            count = count + t
            count_all += count
        if count_min > count_all:
            count_min = count_all
    '''
    # 완전 탐색을 구현하려고 했으나 그리디를 쓰고 있음
    # 이 문제는 그리디로 구현하는 것이 좋음
    # 앞 부분의 시간은 매번 중복되어 더해지므로 앞 시간이 적을 수록 유리 -> 정렬하여 더하는 것이 최솟값임

    time.sort()
    time.pop()
    count_all = 0
    count = 0
    for t in time:
        count += t
        count_all += count
        
    print(f'#{test_case} {count_all}')