import heapq
from itertools import permutations
graph = []
n = 0

def init(N, K, sCity, eCity, mLimit):
	global graph, n
	n = N
	# N개 도시
	graph = [[] for _ in range(n)]
	# K개 도로
	# sCity[i] <-> eCity[i] 연결, mLimit[i] -> i 도로의 최대 중량
	for i in range(K):
		graph[sCity[i]].append((eCity[i],mLimit[i]))
		graph[eCity[i]].append((sCity[i], mLimit[i]))



def add(sCity, eCity, mLimit):
	# 새로운 도로 추가
	graph[sCity].append((eCity, mLimit))
	graph[eCity].append((sCity, mLimit))


def calculate(sCity, eCity, M, mStopover):
	# sCity에서 M개의 경유지를 거쳐 eCity까지 운송할 수 있는 최대 중량 반환

	answer = -1
	# M의 최대 개수가 3 -> 경유지를 거치는 경우의 수 3! -> 6개밖에 없음, 모든 경우 확인해도 됨
	# 가능한 모든 경로 중에서 limit가 최대인 것을 고르고 싶음
	for order in permutations(mStopover):
		# 실제로 방문해야 하는 도시 순서
		path = [sCity] + list(order) + [eCity]

		# 각 구간의 최대 운송 가능 중량
		total_weight = 99999

		possible = True

		# path[i] -> path[i+1]을 하나씩 계산
		for i in range(M + 1):
			start = path[i]
			end = path[i + 1]

			# start에서 각 도시까지 이동할 때 운반할 수 있는 최대 중량
			best = [0] * n
			best[start] = 99999 # start..에서는 아직 도로를 지나지 않았으니까

			pq = [(-best[start], start)]

			while pq:
				# limit, 현재 도시
				weight, now = heapq.heappop(pq)
				weight = -weight

				if weight < best[now]:
					continue

				if now == end:
					break
				# 현재 도시랑 연결된 다른 도시들
				for nxt, limit in graph[now]:
					new_weight = min(weight, limit)

					if new_weight > best[nxt]:
						best[nxt] = new_weight
						heapq.heappush(pq, (-new_weight, nxt))

			# start와 end를 연결하는 도로가 없으면
			if best[end] == 0:
				possible = False
				break

			# 전체 경로에서 가장 작은 구간 중량
			total_weight = min(total_weight, best[end])

		if possible:
			answer = max(answer, total_weight)

	return answer