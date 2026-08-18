# 트리플이 있는지 확인하는 함수
def has_triple(counts):
    return any(c >= 3 for c in counts.values())
# 스트레이트가 있는지 확인하는 함수
def has_straight(counts):
    vals = set(counts.keys()) # set을 사용하는건 중복을 제거하고, O(1)로 존재 여부를 확인하기 위해서임
    for v in vals:
        if v in vals and (v+1) in vals and (v+2) in vals:
            return True
    return False

T = int(input())

for test_case in range(1, T + 1):
    origin_arr = list(map(int, input().split()))
    hands = [{}, {}]
    result = 0

    # 이전 값들의 합을 구해서 더해주기
    for i, num in enumerate(origin_arr): # enumerate를 사용하면 index와 value를 동시에 가져올 수 있음
        player = i % 2
        hands[player][num] = hands[player].get(num, 0) + 1

        if has_triple(hands[player]) or has_straight(hands[player]):
            result = player + 1
            break

    print(f"#{test_case} {result}")
