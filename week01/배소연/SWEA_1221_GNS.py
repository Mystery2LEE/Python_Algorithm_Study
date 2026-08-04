T = int(input())

word_to_num = {
    'ZRO': 0,
    'ONE': 1,
    'TWO': 2,
    'THR': 3,
    'FOR': 4,
    'FIV': 5,
    'SIX': 6,
    'SVN': 7,
    'EGT': 8,
    'NIN': 9
}

for _ in range(T):
    tc, length = input().split()
    words = input().split()

    words.sort(key=lambda word: word_to_num[word])

    print(tc)
    print(words)