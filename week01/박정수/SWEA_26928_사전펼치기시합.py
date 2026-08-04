T = int(input())

def getScore(left, right, goal):
    score = 1
    mid = (left + right) // 2
    while mid != goal :
        if goal > mid :
            left = mid
        else :
            right = mid 
        #이거 되는건가
        mid = (left + right) // 2
        score += 1
    return score

for test_case in range(1, T + 1):
    N, A, B = map(int, input().split())

    A_score = getScore(1, N, A)
    B_score = getScore(1, N, B)
    print(f'A : {A_score}   B : {B_score}')
    winner = 0
    if A_score < B_score :
        winner = 'A'
    elif A_score == B_score :
        winner = 0