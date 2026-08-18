############################################################################################
# 시간 초과ㅜㅜ (답은 맞음, 최적화를 해야할듯)

# 공장 설립
# > 100 n m B_NUM1 B_NUM2 ... B_NUMm
# n개의 벨트, m개의 물건
# 각각 선물의 번호는 오름차순으로 벨트에 쌓임


# 물건 모두 옮기기
# > 200 m_src m_dst
# m_src번째 벨트에서 m_dst번째 벨트로 물건 옮기기
# m_src번째 벨트에 선물이 없는 경우 -> 아무것도 옮기지 않음
# m_src번째 벨트에 선물이 있는 경우 -> 옮겨진 선물은 m_dst 벨트 앞에 위치, 옮긴 뒤 m_dst번째 벨트에 있는 선물들의 개수 출력


# 앞 물건만 교체하기
# > 300 m_src m_dst
# 둘 중 하나의 벨트에 선물이 아예 없을 경우 -> 교체하지 않고, 해당 벨트로 선물을 옮기기만 하기
# 선물이 있을 경우
# -> m_src번째 벨트와 m_dst번째 벨트의 맨 앞 선물들 교환
# -> m_dst번째 벨트의 선물 개수 출력


# 물건 나누기 (n: m_src 번째 벨트의 선물 개수)
# > 400 m_src m_dst
# m_src 벨트에 선물이 1개인 경우 -> 선물을 옮기지 않음
# m_src 벨트에 선물이 2개 이상인 경우
# -> m_src번째 벨트의 floor(n/2)번째까지의 선물을 m_dst번째 벨트 앞으로 옮기기
# -> 옮긴 뒤 m_dst번째 벨트의 선물 개수 출력


# 선물 정보 얻기
# > 500 p_num
# p_num: 선물 번호
# a: 해당 선물의 앞 선물 번호 (앞 선물이 없는 경우 -> a = -1)
# b: 해당 선물의 뒤 선물 번호 (뒤 선물이 없는 경우 -> b = -1)
# -> a + 2 * b 출력


# 벨트 정보 얻기
# > 600 b_num
# b_num: 벨트 번호
# a: 해당 벨트의 맨 앞에 있는 선물의 번호 (선물이 없는 벨트일 경우, a=-1)
# b: 해당 벨트의 맨 뒤에 있는 선물의 번호 (선물이 없는 벨트일 경우, b=-1)
# c: 해당 벨트에 있는 선물의 개수 (선물이 없는 벨트일 경우, c=0)
# -> a + 2 * b + 3 * c 출력
############################################################################################


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