t = int(input())

for tc in range(1, t+1):
    N, K = map(int, input().split())
    # 행 -> 1~K 까지의 부피, 열 -> N개 물건
    knapsack = [[0]*(K+1) for _ in range(N+1)] 
    vol = [0]
    cost = [0]
    for _ in range(N):
        Vi, Ci = map(int, input().split())
        vol.append(Vi)
        cost.append(Ci)

    for i in range(1, N+1):
        for j in range(1, K+1):
            # 현재 물건이 돌고 있는 부피보다 작으면
            if j < vol[i]:
                knapsack[i][j] = knapsack[i-1][j]
            else:
            # max(현재 물건 가치 + knapsack[이전 물건][현재 가방 무게 - 현재 물건 무게], knapsack[이전 물건][현재 가방 무게])
                knapsack[i][j] = max(cost[i] + knapsack[i-1][j-vol[i]], knapsack[i-1][j])


