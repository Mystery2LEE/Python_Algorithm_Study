# 색칠하는 함수
def paint(region, color):
    # region이 n보다 크면 모든 지역을 색칠한 것이므로 1을 반환
    if region > n:
        return 1

    total = 0
    for c in range(1, k+1):
        ok = True
        # 이전 지역들과 인접한 지역이 같은 색인지 확인
        for other in range(1, region):
            if arr[region][other] and color[other] == c:
                ok = False
                break

        # 이전 지역들과 인접한 지역이 같은 색이 아니면 색칠하고 다음 지역으로 넘어감
        if ok:
            color[region] = c
            total += paint(region+1, color)
            # 이전 지역을 다시 색칠하지 않도록 0으로 초기화
            color[region] = 0
    return total

T = int(input())

for test_case in range(1, T + 1):
    n, m, k = map(int, input().split())
    # 인접 여부를 확인하는 배열
    arr = [[False] * (n+1) for _ in range(n+1)]
    # 색을 저장할 배열
    color = [0] * (n+1)
    # 입력값을 통해 인접 여부를 저장
    for _ in range(m):
        i, j = map(int, input().split())
        arr[i][j] = True
        arr[j][i] = True

    print(f"#{test_case} {paint(1, color)}")