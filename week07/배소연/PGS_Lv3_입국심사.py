def solution(n, times):
    left = 0
    right = min(times) * n
    
    while left < right:
        mid = (left + right) // 2
        people = 0
        
        for t in times:
            people += mid // t
            
        if people >= n:
            right = mid
        else:
            left = mid + 1
    
    return left