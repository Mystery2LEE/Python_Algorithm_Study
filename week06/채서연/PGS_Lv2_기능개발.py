import math
def solution(progresses, speeds):
    n = len(progresses)
    answer = []
    deploy = math.ceil((100 - progresses[0]) / speeds[0])
    cnt = 1
    for i in range(1, n):
        date = math.ceil((100 - progresses[i]) / speeds[i])

        # 날짜 같을 때도 포함해야 함!!!!
        if deploy >= date:
            cnt += 1
            
        else:
            answer.append(cnt)
            deploy = date
            cnt = 1
            
    answer.append(cnt) 
    return answer