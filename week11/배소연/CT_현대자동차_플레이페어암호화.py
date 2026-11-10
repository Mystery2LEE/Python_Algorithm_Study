# 문제의 규칙에 따라 알파벳을 2개씩 묶어 쌍 만들기
def make_pairs(message):
    pairs = []
    i = 0

    while i < len(message):
        if i == len(message) - 1:
            pairs.append(message[i] + 'X')
            i += 1
        
        elif message[i] == message[i+1]:
            if message[i] == 'X':
                pairs.append(message[i] + 'Q')
                i += 1
            else:
                pairs.append(message[i] + 'X')
                i += 1

        else:
            pairs.append(message[i:i+2])
            i += 2
        
    return pairs


message = input()
key = input()

# 키에 대해 중복이 없도록, 빈 칸은 알파벳 순서대로 채워서 보드 만들기
seen = set()
chars = []
for ch in key:
    if ch not in seen:
        seen.add(ch)
        chars.append(ch)


alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
if len(chars) < 25:
    for ch in alphabet:
        if ch not in seen:
            seen.add(ch)
            chars.append(ch)


board = []
for i in range(0, 25, 5):
    board.append(chars[i:i+5])


# 각 알파벳의 좌표 위치 저장하기
positions = {}
for r in range(5):
    for c in range(5):
        positions[board[r][c]] = (r, c)


answer = ""
message_pair = make_pairs(message)

for pair in message_pair:
    a, b = pair

    r1, c1 = positions[a]
    r2, c2 = positions[b]

    if r1 == r2:
        answer += board[r1][(c1 + 1) % 5]
        answer += board[r2][(c2 + 1) % 5]

    elif c1 == c2:
        answer += board[(r1 + 1) % 5][c1]
        answer += board[(r2 + 1) % 5][c2]

    else:
        answer += board[r1][c2]
        answer += board[r2][c1]


print(answer)