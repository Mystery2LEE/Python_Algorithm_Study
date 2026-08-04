T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    nums = [0]*101
    maxScore = 0

    for i in range(N-1, -1, -1):
        h = arr[i]
        if h != 0:
            score = sum(nums[0:h]) 
            maxScore = max(maxScore, score)
        nums[h] += 1

    print(f"#{test_case} {maxScore}")
