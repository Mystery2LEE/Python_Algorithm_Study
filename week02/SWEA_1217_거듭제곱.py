T = 10

# 재귀함수 생성
def power(n, m):
    # m이 0일 때 재귀를 종료하고 값을 리턴
    if m == 0:
        return 1
    # 재귀 함수를 통해 거듭제곱 실행
    return n * power(n, m-1)

for test_case in range(1, T + 1):
    # 테스트 케이스 입력
    t = int(input())

    # n, m 입력
    n, m = map(int, input().split())

    print(f"#{t} {power(n,m)}")