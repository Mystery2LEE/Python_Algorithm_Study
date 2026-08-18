# 퀸을 놓는 함수
def put_queens(n):
    # 퀸이 놓일 수 있는지 확인하는 함수
    def is_valid(queen_positions, row, col):
        # 이전에 놓인 퀸들과 같은 열에 있는지, 대각선에 있는지 확인
        for r, c in enumerate(queen_positions):
            # 같은 열 및 대각선에 있는지 확인
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True
    # 백트래킹을 이용하여 퀸을 놓는 함수
    def backtrack(queen_positions):
        if len(queen_positions) == n:
            return 1

        total = 0
        for col in range(n):
            # 이전에 놓인 퀸들과 같은 열이나 대각선에 있는지 확인
            if is_valid(queen_positions, len(queen_positions), col):
                # 퀸을 놓고 다음 행으로 넘어감
                queen_positions.append(col)
                # 다음 행으로 넘어가서 퀸을 놓는 경우의 수를 더함
                total += backtrack(queen_positions)
                # 퀸을 놓은 위치를 제거하여 다른 경우의 수를 탐색
                queen_positions.pop()
        return total
    # 퀸을 놓는 경우의 수를 반환
    return backtrack([])

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    result = put_queens(n)
    print(f"#{test_case} {result}")