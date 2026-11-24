N = int(input())
scores = [list(map(int, input().split())) for _ in range(3)]


def get_ranking(contest):
    max_score = max(contest)

    # 점수별 인원 수
    count = [0] * (max_score + 1)
    for score in contest:
        count[score] += 1

    # 점수별 등수
    ranking = [0] * (max_score + 1)
    higher = 0
    for score in range(max_score, -1, -1):
        ranking[score] = higher + 1
        higher += count[score]

    return [ranking[score] for score in contest]


# 각 대회별 등수
for contest in scores:
    print(*get_ranking(contest))


# 최종 점수
total_score = [0] * N

for i in range(3):
    for j in range(N):
        total_score[j] += scores[i][j]


# 최종 등수
print(*get_ranking(total_score))
