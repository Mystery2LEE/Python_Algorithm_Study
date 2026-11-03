from collections import deque

def solution(priorities, location):
    # 인덱스 용 큐와 값 용 큐를 2개 생성해서 돌린다
    queue = deque(priorities)
    index = deque([i for i in range(len(priorities))])
    count = 1
    max_num = max(queue)
    while queue:
        l = queue.popleft()
        i = index.popleft()
        if l == max_num:
            if i == location:
                break
            count += 1
            max_num = max(queue)
        else:
            queue.append(l)
            index.append(i)
    return count