digital_logic = input()
K, M = map(int, input().split())

# 해쉬를 저장할 딕셔너리 
cnt = {}
# 값이 너무 커질 것을 고려해 나머지를 구할 소수
P = 2**61 - 1
# 이진수(0, 1)
B = 2
# 롤링해시로 인해 앞으로 밀려난 글자의 자릿 값
high = pow(2, K, P)
# 해시값
h = 0

# 롤링해시
for i, c in enumerate(digital_logic):
    # 이진수이기에 자리수를 앞으로 밀고 뒤에 새로운 값을 더 한다, 새글자 붙이기
    h = ((h * 2) + int(c)) % P
    # 만약 넣은 글자가 K를 넘으면
    if i >= K:
        # 맨 앞글자를 밀어서 새로운 글자로 만든다
        h = (h - int(digital_logic[i - K]) * high) % P
    # 정확히 K개의 글자일 때 딕셔너리 개수 세서 조건에 맞으면 1출력
    if i >= K - 1:
        cnt[h] = cnt.get(h, 0) + 1
        if cnt[h] >= M:
            print(1)
            exit()

print(0)