T = int(input())
for tc in range(1, T+1):
    answer = 0
    arr, count = map(int, input().split())
    num_list = list(str(arr))
    L = len(num_list)
    v = set()
    def dfs(n):
        global answer
        # 현재 상금과 새로 계산한 상금 중에 큰 값 저장
        if n == count:
            answer = max(answer, int("".join(num_list)))
            return
        # 두 요소씩 교환해서 가능한 상금 찾아감
        for i in range(L - 1):
            for j in range(i + 1, L):
                num_list[i], num_list[j] = num_list[j], num_list[i]
                # 교환 횟수와 현재 상금을 튜플로 저장 -> 똑같은 상태 나왔을 때 dfs 진행하지 않음
                if (n, int("".join(num_list))) not in v:
                    v.add((n, int("".join(num_list))))
                    dfs(n+1)
                # 되돌리기
                num_list[j], num_list[i] = num_list[i], num_list[j]
    dfs(0)
    print(f'#{tc} {answer}')