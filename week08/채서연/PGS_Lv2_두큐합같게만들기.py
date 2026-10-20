from collections import deque
def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)

    sum1 = sum(q1)
    sum2 = sum(q2)
    # 전체 합이 홀수이면 불가능
    if (sum1 + sum2) % 2 != 0:
        return -1

    target = (sum1 + sum2)//2
    answer = 0
    isTrue = False
    n = len(queue1)
    if max(q1) > target or max(q2) > target:
        return -1
    else:
        # 무한 반복되지 않게 최대 반복 횟수를 4n으로 설정.. 처음에 설정 안 헀더니 시간초과됨
        while q1 and q2 and answer < 4 * n:

            if sum1 == target:
                isTrue = True
                break
            elif sum1 < target:
                item = q2.popleft()
                q1.append(item)
                sum1 += item
                sum2 -= item
                answer += 1
            else:
                item = q1.popleft()
                q2.append(item)
                sum1 -= item
                sum2 += item
                answer += 1

        if not isTrue:
            answer = -1
    
    return answer