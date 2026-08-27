import sys
from solution import init, oneYearLater

def run():
    # n: 바다 가로/세로 길이
    # m: 빙하의 개수
    # k: oneYearLater() 호출 횟수
    n, m, k = map(int, input().split())

    # 좌표의 얼음 높이 정보 (n x n)
    mIceBlock = []
    for i in range(n):
        mIceBlock.append(list(map(int, input().split())))

    # 빙하의 X좌표, Y좌표, 빙하 이동 방향
    mIceGroup = []
    for i in range(m):
        mIceGroup.append(list(map(int, input().split())))

    # solution.py에 초기 상태 전달
    init(n, m, mIceBlock, mIceGroup)

    okay = True

    # 한 번 호출할 때마다 1년 경과 (k년 후)
    for q in range(k):
        user_ans = oneYearLater()
        
        # 해당 연도의 정답 높이 정보
        correctAns = list(map(int, input().split()))
        
        # 내가 계산한 값과 정답 비교
        for y in range(n):
            for x in range(n):
                if user_ans.heights[y][x] != correctAns[y*n+x]:
                    okay = False


    return okay


sys.stdin = open('sample_input.txt', 'r')

# T: 테스트케이스 개수
# MARK: 테스트케이스를 맞혔을 때의 점수
T, MARK = map(int, input().split())

for tc in range(1, T + 1):
    score = MARK if run() else 0
    print("#%d %d" % (tc, score), flush = True)