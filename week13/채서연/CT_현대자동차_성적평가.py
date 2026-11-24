N = int(input())
scores = [list(map(int, input().split())) for _ in range(3)]

# 최종 등수용 점수 저장
total = [0] * N

for i in range(N):
    total[i] = scores[0][i] + scores[1][i] + scores[2][i]

scores.append(total)

# 대회별 등수 및 최종 등수 계산
for s in scores:
    # (참가자 번호, 점수) 점수 기준 내림차순 정렬
    sorted_scores = sorted(
        enumerate(s), key=lambda x: x[1], reverse=True
    )

    ranks = [0] * N
    rank = 1

    for i in range(N):
        idx, score = sorted_scores[i]

        # 이전 참가자와 점수가 다르면 등수 갱신
        if i > 0 and score != sorted_scores[i - 1][1]:
            rank = i + 1

        # 원래 참가자의 위치에 등수 저장
        ranks[idx] = rank

    print(*ranks)