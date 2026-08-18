#######################
# 시간 초과ㅜㅜ (답은 맞음, 최적화를 해야할듯)
#######################

q = int(input())
belts = []


def create_factory(n, m , b_nums):
    global belts

    belts = [[] for _ in range(n + 1)]

    for p_num in range(1, m + 1):
        b_num = b_nums[p_num - 1]
        belts[b_num].append(p_num)

def move_all(m_src, m_dst):
    if len(belts[m_src]) == 0:
        print(len(belts[m_dst]))
        return

    belts[m_dst] = belts[m_src] + belts[m_dst]
    belts[m_src] = []

    print(len(belts[m_dst]))
    return

def change_front_products(m_src, m_dst):
    if len(belts[m_src]) == 0 and len(belts[m_dst]) == 0:
        pass

    elif len(belts[m_src]) == 0:
        gift = belts[m_dst].pop(0)
        belts[m_src].insert(0, gift)

    elif len(belts[m_dst]) == 0:
        gift = belts[m_src].pop(0)
        belts[m_dst].insert(0, gift)
    
    else:
        temp = belts[m_dst][0]
        belts[m_dst][0] = belts[m_src][0]
        belts[m_src][0] = temp
    
    print(len(belts[m_dst]))
    return


def divide_products(m_src, m_dst):
    n = len(belts[m_src])

    if n <= 1:
        print(len(belts[m_dst]))
        return

    here = n // 2
    products = belts[m_src][:here]
    belts[m_src] = belts[m_src][here:]
    belts[m_dst] = products + belts[m_dst]
     
    print(len(belts[m_dst]))
    return


def get_product_info(p_num):
    a = -1
    b = -1

    for belt in belts[1:]:
        if p_num in belt:
            idx = belt.index(p_num)

            if idx > 0:
                a = belt[idx - 1]
            if idx < len(belt) - 1:
                b = belt[idx + 1]
            
            break

    print(a + 2 * b)
    return


def get_belt_info(b_num):
    belt = belts[b_num]

    if len(belt) == 0:
        a = -1
        b = -1
        c = 0
    else:
        a = belt[0]
        b = belt[-1]
        c = len(belt)

    print(a + b * 2 + 3 * c)
    return


for _ in range(q):
    line = input().split()
    command = int(line[0])

    if command == 100:
        n = int(line[1])
        m = int(line[2])
        b_nums = list(map(int, line[3:]))

        create_factory(n, m, b_nums)

    elif command == 200:
        m_src = int(line[1])
        m_dst = int(line[2])
        move_all(m_src, m_dst)

    elif command == 300:
        m_src = int(line[1])
        m_dst = int(line[2])

        change_front_products(m_src, m_dst)

    elif command == 400:
        m_src = int(line[1])
        m_dst = int(line[2])

        divide_products(m_src, m_dst)
    
    elif command == 500:
        p_num = int(line[1])
        get_product_info(p_num)

    elif command == 600:
        b_num = int(line[1])
        get_belt_info(b_num)