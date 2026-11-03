import heapq

def solution(jobs):
    jobs = sorted(
        (request, duration, i)
        for i, (request, duration) in enumerate(jobs)
    )
    
    n = len(jobs)
    heap = []
    
    time = 0
    idx = 0
    total = 0
    
    while idx < n or heap:
        while idx < n and jobs[idx][0] <= time:
            request, duration, number = jobs[idx]
            heapq.heappush(heap, (duration, request, number))
            idx += 1
            
        if heap:
            duration, request, number = heapq.heappop(heap)
            
            time += duration
            total += time - request
            
        else:
            time = jobs[idx][0]
    
    return total // n