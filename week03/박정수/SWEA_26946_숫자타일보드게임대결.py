T = int(input())


for test_case in range(1, T + 1):

    card1 = [0] * 10
    card2 = [0] * 10

    shuffle = input().split()
    result = 0
    for i in range(12):
        idx = int(shuffle[i])
        if i % 2 == 0:
            card1[idx] += 1
            if (
                (idx - 1 >= 0 and idx + 1 < 10 and card1[idx - 1] != 0 and card1[(idx + 1) % 10] != 0)
                or (idx -2 >= 0 and card1[idx - 2] != 0 and card1[idx - 1] != 0)
                or (idx + 2 < 10 and card1[(idx + 1) % 10] != 0 and card1[(idx + 2) % 10] != 0)
            ):

                result = 1
                break
            if card1[idx] == 3:
                result = 1
                break
        else:
            card2[idx] += 1
            if (
                (idx - 1 >= 0 and idx + 1 < 10 and card2[idx - 1] != 0 and card2[(idx + 1) % 10] != 0)
                or (idx -2 >= 0 and card2[idx - 2] != 0 and card2[idx - 1] != 0)
                or (idx + 2 < 10 and card2[(idx + 1) % 10] != 0 and card2[(idx + 2) % 10] != 0)
            ):
                result = 2
                break
            if card2[idx] == 3:
                result = 2
                break

    print(f"#{test_case} {result}")
