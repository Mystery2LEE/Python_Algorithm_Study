digital_logic = input()
K, M = map(int, input().split())

# Please write your code here.
n = len(digital_logic)

# 패턴 길이가 문자열 길이보다 길 때
if K > n:
    print(0)

# 문자열 패턴은 무조건 1개는 있으니까 M이 1일때는 불안정하다.
elif M == 1:
    print(1)

else:
    counts = {}
    pattern = 0
    answer = 0
    # K==3일 때 mask = 1000 - 0001 -> 111
    mask = (1 << K) -1

    # 기존에 작성한 코드.... 메모리 초과 발생
    # for i in range(n-K+1):
    #     p = digital_logic[i:i+K]
    #     if p in dict:
    #         dict[p] += 1
    #         if dict[p] == M:
    #             isUnstable = True
    #             break
    #     else:
    #         dict[p] = 1
    
    for i in range(n):
        pattern = ((pattern << 1) | int(digital_logic[i])) & mask

        if i >= K - 1:
            counts[pattern] = counts.get(pattern, 0) + 1

            if counts[pattern] >= M:
                answer = 1
                break

    print(answer)
