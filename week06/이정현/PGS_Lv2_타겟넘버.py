def solution(numbers, target):
    # 깊이 변수
    dep = 0
    # 그래프 초기화
    graph = [[] for _ in range(len(numbers)+1)]
    # 시작점 초기화
    graph[dep].append(0)

    # 반복문을 통해 그래프 구성
    while dep < len(numbers):
        # 현재 깊이에 있는 값들을 다음 깊이로 확장
        for g in graph[dep]:
            graph[dep+1].append(g + numbers[dep])
            graph[dep+1].append(g - numbers[dep])
        # 깊이 증가
        dep += 1
    # 최종 깊이에서 target 값의 개수 반환
    return graph[dep].count(target)