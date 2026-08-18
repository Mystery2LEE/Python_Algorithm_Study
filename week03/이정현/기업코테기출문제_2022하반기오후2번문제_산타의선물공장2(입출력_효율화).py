import sys
# 입력 속도를 빠르게 하기 위해 sys.stdin.buffer.read()를 사용하여 입력을 한 번에 읽어옴
data = sys.stdin.buffer.read().split()
idx = 0

# 입력값을 읽어오는 함수
def read_int():
    global idx
    v = int(data[idx])
    idx += 1
    return v

# 공장 초기화 함수
def founded_factory():
    read_int()
    n = read_int()
    m = read_int()
    prev = [-1] * (m + 1)
    nxt = [-1] * (m + 1)
    head = [-1] * (n + 1)
    tail = [-1] * (n + 1)
    count = [0] * (n + 1)

    for i in range(m):
        belt_num = read_int()
        if head[belt_num] != -1:
            nxt[tail[belt_num]] = i + 1
            prev[i + 1] = tail[belt_num]
            tail[belt_num] = i + 1
            count[belt_num] += 1
        else:
            head[belt_num] = i + 1
            tail[belt_num] = i + 1
            count[belt_num] = 1

    return n, m, prev, nxt, head, tail, count

# 선물 이동 함수
def move_gift(src, dst, prev, nxt, head, tail, count):
    if head[src] != -1:
        if head[dst] != -1:
            prev[head[dst]] = tail[src]
            nxt[tail[src]] = head[dst]
            head[dst] = head[src]
            count[dst] += count[src]
        else:
            head[dst] = head[src]
            tail[dst] = tail[src]
            count[dst] = count[src]
        head[src] = -1
        tail[src] = -1
        count[src] = 0

    return count[dst]

# 맨 앞 선물 이동 함수 (앞쪽으로 이동)
def move_front_gift(src, dst, prev, nxt, head, tail, count):
    if head[src] != -1 or head[dst] != -1:
        if head[src] == -1:
            x = head[dst]
            head[src] = x
            tail[src] = x
            head[dst] = nxt[x]
            if head[dst] != -1:
                prev[head[dst]] = -1
            else:
                tail[dst] = -1
            nxt[x] = -1
            count[src] = 1
            count[dst] -= 1
        elif head[dst] == -1:
            y = head[src]
            head[dst] = y
            tail[dst] = y
            head[src] = nxt[y]
            if head[src] != -1:
                prev[head[src]] = -1
            else:
                tail[src] = -1
            nxt[y] = -1
            count[dst] = 1
            count[src] -= 1
        else:
            a = head[src]
            b = head[dst]
            x = nxt[a]
            y = nxt[b]
            head[dst] = a
            nxt[head[dst]] = y
            head[src] = b
            nxt[head[src]] = x
            if x != -1:
                prev[x] = b
            else:
                tail[src] = b

            if y != -1:
                prev[y] = a
            else:
                tail[dst] = a

    return count[dst]

# 선물 나눠 이동 함수 (절반 이동)
def divide_gift(src, dst, prev, nxt, head, tail, count):
    n = count[src]
    if n//2 > 0:
        curr = head[src]
        for _ in range(n//2 - 1):
            curr = nxt[curr]
        a, b, c = nxt[curr], head[src], head[dst]
        if head[dst] != -1:
            head[dst] = b
            nxt[curr] = c
            head[src] = a
            prev[a] = -1
            prev[c] = curr
        else:
            head[dst] = b
            tail[dst] = curr
            head[src] = a
            prev[a] = -1
            nxt[curr] = -1

        count[src] -= n//2
        count[dst] += n//2
    return count[dst]

# 선물 정보 조회 함수
def get_gift_info(p_num, prev, nxt):
    a = prev[p_num]
    b = nxt[p_num]

    return a + 2 * b

# 벨트 정보 조회 함수
def get_belt_info(b_num, head, tail, count):
    a = head[b_num]
    b = tail[b_num]
    c = count[b_num]

    return a + 2 * b + 3 * c

T = read_int()
n, m, prev, nxt, head, tail, count = founded_factory()

out = []

for _ in range(T-1):
    c = read_int()
    if c == 200:
        src = read_int()
        dst = read_int()
        out.append(move_gift(src, dst, prev, nxt, head, tail, count))

    elif c == 300:
        src = read_int()
        dst = read_int()
        out.append(move_front_gift(src, dst, prev, nxt, head, tail, count))

    elif c == 400:
        src = read_int()
        dst = read_int()
        out.append(divide_gift(src, dst, prev, nxt, head, tail, count))

    elif c == 500:
        p_num = read_int()
        out.append(get_gift_info(p_num, prev, nxt))

    elif c == 600:
        b_num = read_int()
        out.append(get_belt_info(b_num, head, tail, count))

print('\n'.join(map(str, out)))