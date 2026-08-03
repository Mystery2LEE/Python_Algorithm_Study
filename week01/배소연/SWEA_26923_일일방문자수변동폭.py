T = int(input())
 
for tc in range(1, T + 1):
    _ = int(input())
    ai = list(map(int, input().split()))
    ai.sort()
     
    print(f"#{tc} {ai[-1] - ai[0]}")