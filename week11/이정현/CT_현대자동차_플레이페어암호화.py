message = input()
key = input()

# 해쉬를 통한 키 변환
def chart(key):
    chart = [['']*5 for _ in range(5)]
    dict = {'A': [0, 0, 0],
            'B': [0, 0, 0],
            'C': [0, 0, 0],
            'D': [0, 0, 0],
            'E': [0, 0, 0],
            'F': [0, 0, 0],
            'G': [0, 0, 0],
            'H': [0, 0, 0],
            'I': [0, 0, 0],
            'K': [0, 0, 0],
            'L': [0, 0, 0],
            'M': [0, 0, 0],
            'N': [0, 0, 0],
            'O': [0, 0, 0],
            'P': [0, 0, 0],
            'Q': [0, 0, 0],
            'R': [0, 0, 0],
            'S': [0, 0, 0],
            'T': [0, 0, 0],
            'U': [0, 0, 0],
            'V': [0, 0, 0],
            'W': [0, 0, 0],
            'X': [0, 0, 0],
            'Y': [0, 0, 0],
            'Z': [0, 0, 0]}
    
    r, c = 0, 0
    for m in key:
        if dict[m][0] == 0:
            dict[m][0] += 1
            chart[r][c] = m
            dict[m][1], dict[m][2] = r, c
            c = (c+1)%5
            if c == 0:
                r += 1
    
    if r <= 4:
        for d in dict:
            if dict[d][0] == 0:
                chart[r][c] = d
                dict[d][1], dict[d][2] = r, c
                c += 1
                if c == 5:
                    r += 1
                    if r > 4:
                        break
                c = c % 5
    
    return chart, dict

# 스택을 통한 메시지 생성
def pair(message):
    stack = []
    for k in message:
        if not stack:
            stack.append(k)
        else:
            if len(stack) % 2 != 0 and stack[-1] == k:
                if k != 'X':
                    stack.append('X')
                else:
                    stack.append('Q')
            stack.append(k)
    if len(stack) % 2 == 1:
        stack.append('X')

    return stack

# 스택 내 문자 2개 씩을 이용하여 암호문 변환
def cipher(chart, dict, x, y):
    if dict[x][1] == dict[y][1]:
        return chart[dict[x][1]][(dict[x][2] + 1) % 5], chart[dict[y][1]][(dict[y][2] + 1) % 5]
    else:
        if dict[x][2] == dict[y][2]:
            return chart[(dict[x][1] + 1) % 5][dict[x][2]], chart[(dict[y][1] + 1) % 5][dict[y][2]]
        else:
            return chart[dict[x][1]][dict[y][2]], chart[dict[y][1]][dict[x][2]]

num_chart, num_dict = chart(key)
new_key = pair(message)

answer = []
for i in range(0, len(new_key) - 1, 2):
    c1, c2 = cipher(num_chart, num_dict, new_key[i], new_key[i+1])
    answer.append(c1)
    answer.append(c2)

print(''.join(map(str, answer)))