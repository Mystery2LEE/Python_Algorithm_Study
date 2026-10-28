def solution(prices):
    result = []
    for i in range(len(prices)):
        count = 0
        for j in range(i, len(prices)):
            count += 1
            if prices[i] > prices[j]:
                break
        result.append(count-1)
    return result