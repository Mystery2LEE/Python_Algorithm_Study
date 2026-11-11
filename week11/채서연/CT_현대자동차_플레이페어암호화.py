
message = input()
key = input()

string = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
grid = [[0] * 5 for _ in range(5)]
positions = {}
key_set = set()



# 처음에 key랑 string이랑 따로 for문 돌렸는데 더해서 한번에 할 수도 있네..
i = j = 0
for s in key + string:
    if s not in key_set:
        if j == 5:
            j = 0
            i += 1

        key_set.add(s)
        grid[i][j] = s
        positions[s] = (i, j)
        j += 1


mlist = []
i = 0

while i < len(message):
    if i == len(message) - 1:
        mlist.append(message[i])
        mlist.append('X')
        break

    if message[i] != message[i+1]:
        mlist.append(message[i])
        mlist.append(message[i+1])
        i += 2

    else:
        if message[i] != 'X':
            mlist.append(message[i])
            mlist.append('X')
        else:
            mlist.append(message[i])
            mlist.append('Q')

        i += 1


result = []

for i in range(0, len(mlist), 2):
    s1, s2 = mlist[i], mlist[i+1]

    s1_r, s1_c = positions[s1]
    s2_r, s2_c = positions[s2]

    # 같은 행에 있을 때
    if s1_r == s2_r:
        result.append(grid[s1_r][(s1_c+1) % 5])
        result.append(grid[s2_r][(s2_c+1) % 5])

    # 같은 열에 있을 때
    elif s1_c == s2_c:
        result.append(grid[(s1_r+1) % 5][s1_c])
        result.append(grid[(s2_r+1) % 5][s2_c])

    # 둘 다 아닐 때
    else:
        result.append(grid[s1_r][s2_c])
        result.append(grid[s2_r][s1_c])

print(''.join(result))
