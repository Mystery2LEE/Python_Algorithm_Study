t = int(input())

for _ in range(1, t+1):
    num = int(input())
    score = list(map(int, input().split()))
    dict = {x: 0 for x in range(0, 101)}
    for i in score:
        dict[i]+=1
    # value가 가장 큰 key 찾기 -> max 함수의 key 매개변수로 최댓값을 비교할 기준을 정함
    # 각 key에 대해 (value, key) 형식의 튜플로 비교하게 함 -> 1. value 비교 2. value 같으면 key가 큰 값을 반환
    result = max(dict, key=lambda k:(dict[k],k))
    print(f'#{num} {result}')