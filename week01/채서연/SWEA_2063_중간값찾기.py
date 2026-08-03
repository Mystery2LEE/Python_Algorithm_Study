n = int(input())
score = list(map(int,input().split()))
score = sorted(score)
print(score[n//2])