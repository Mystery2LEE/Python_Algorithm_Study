def solution(people, limit):
    # 구명보트의 개수를 세는 변수
    count = 0
    # 현재 처리 중인 사람의 인덱스
    curr = 0
    # 사람들의 무게를 오름차순으로 정렬
    people.sort()

    # 무거운 사람부터 처리
    for i in range(len(people)-1, -1, -1):
        # 현재 처리 중인 사람의 인덱스가 i보다 작으면 반복문 종료
        if i < curr:
            break
        # 현재 처리 중인 사람과 가장 가벼운 사람의 무게 합이 제한을 초과하지 않으면, 두 사람을 한 보트에 태움
        if people[i] + people[curr] <= limit:
            curr += 1
        count += 1

    return count