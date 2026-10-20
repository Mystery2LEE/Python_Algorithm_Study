import math

def solution(progresses, speeds):
    # 스택을 담는 리스트
    stack = []
    # 결과값을 담는 리스트
    result = []
    # 한번에 나갈 숫자를 담는 변수
    count = 0
    # 리스트의 길이만큼 반복
    for i in range(len(progresses)):
        # 100에서 작업 개수를 빼고 작업 속도로 나눈 후 올림한 숫자
        s = math.ceil((100 - progresses[i]) / speeds[i])
        # 스택이 비었을 때 스택에 값을 담음
        if not stack:
            stack.append(s)
        # 스택이 차있을 때
        elif stack:
            # 만약 스택의 마지막 값 보다 크다면
            if stack[-1] < s:
                # 스택 마지막 값 팝
                stack.pop()
                # 카운트를 결과값에 추가
                result.append(count)
                # s를 스택에 담음
                stack.append(s)
                # 카운트 초기화
                count = 0
        # 카운트 증가
        count += 1
    # 마지막 값 결과 값에 추가
    result.append(count)
    # 결과 값 리턴
    return result