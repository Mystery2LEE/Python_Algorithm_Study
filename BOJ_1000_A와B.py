"""
링크: https://www.acmicpc.net/problem/1000
난이도: Lv1
유형: 구현, 수학
시간복잡도: O(1)
소요시간: 3분
복습필요: N
회고: 입력 파싱만 주의하면 끝. split() 후 map(int) 습관화.
"""

import sys


def solve():
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)


if __name__ == "__main__":
    solve()
