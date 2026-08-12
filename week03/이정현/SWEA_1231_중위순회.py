# 트리 문제를 풀 때 첫번째 트리의 모양을 확인한다
# 부모 노드와 자식 노드의 인덱스 관계를 이용한 중위 순회
def alpha(i, N, word, tree):
    if i > N:
        return word
    alpha(2*i, N, word, tree)
    word.append(tree[i])
    alpha(2*i+1, N, word, tree)
    return word

T = 10

for test_case in range(1, T + 1):
    n = int(input())
    tree = [0]
    word = []

    for _ in range(n):
        arr = list(input().split())
        tree.append(arr[1])

    alpha(1, n, word, tree)

    print(f"#{test_case}", "".join(map(str, word)))