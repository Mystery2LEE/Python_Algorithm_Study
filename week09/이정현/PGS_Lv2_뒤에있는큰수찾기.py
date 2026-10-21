from collections import deque

def solution(numbers):
    stack = deque()
    answer = deque()
    while numbers:
        n = numbers.pop()
        # 만약 stack에 남아 있는 값이 n보다 작으면 다 지운다
        while stack and stack[-1] <= n:
            stack.pop()
        # 스택에 값이 남아 있다면 결과 리스트에 추가
        if stack:
            answer.appendleft(stack[-1])
        # 없으면 -1 추가
        else:
            answer.appendleft(-1)
            
        stack.append(n)
        
    return list(answer)