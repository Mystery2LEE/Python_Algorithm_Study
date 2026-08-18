def founded_factory():
    foundation = list(map(int, input().split()))
    n = foundation[1]
    m = foundation[2]
    prev = [-1] * (m + 1)
    nxt = [-1] * (m + 1)
    head = [-1] * (n + 1)
    tail = [-1] * (n + 1)
    count = [0] * (n + 1)

    for i, belt_num in enumerate(foundation[3:]):
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

    print(count[dst])

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

    print(count[dst])

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
    print(count[dst])

def get_gift_info(p_num, prev, nxt):
    a = prev[p_num]
    b = nxt[p_num]

    print(a + 2 * b)

def get_belt_info(b_num, head, tail, count):
    a = head[b_num]
    b = tail[b_num]
    c = count[b_num]

    print(a + 2 * b + 3 * c)

T = int(input())

n, m, prev, nxt, head, tail, count = founded_factory()

for _ in range(T-1):
    control = list(map(int, input().split()))
    c = control[0]
    if c == 200:
        src = control[1]
        dst = control[2]
        move_gift(src, dst, prev, nxt, head, tail, count)

    elif c == 300:
        src = control[1]
        dst = control[2]
        move_front_gift(src, dst, prev, nxt, head, tail, count)

    elif c == 400:
        src = control[1]
        dst = control[2]
        divide_gift(src, dst, prev, nxt, head, tail, count)

    elif c == 500:
        p_num = control[1]
        get_gift_info(p_num, prev, nxt)

    elif c == 600:
        b_num = control[1]
        get_belt_info(b_num, head, tail, count)