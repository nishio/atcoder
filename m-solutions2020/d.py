#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")
MOD = 10 ** 9 + 7


def debug(*x):
    print(*x, file=sys.stderr)


def solve(N, XS):
    cash = 1000
    stock = 0
    for i in range(N - 1):
        price = XS[i]
        if cash >= price:
            if XS[i + 1] > price:
                # buy
                s = cash // price
                stock += s
                cash -= s * price
                continue
        if stock > 0:
            if XS[i + 1] < price:
                # sell
                cash += stock * price
                stock = 0
    # last day
    cash += stock * XS[-1]
    return cash


def main():
    # parse input
    N = int(input())
    XS = list(map(int, input().split()))
    print(solve(N, XS))


# tests
T1 = """
7
100 130 130 130 115 115 150
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
1685
"""

T2 = """
6
200 180 160 140 120 100
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
1000
"""


def _test():
    import doctest
    doctest.testmod()
    g = globals()
    for k in sorted(g):
        if k.startswith("TEST_"):
            doctest.run_docstring_examples(g[k], g)


def as_input(s):
    "use in test, use given string as input file"
    import io
    f = io.StringIO(s.strip())
    g = globals()
    g["input"] = lambda: bytes(f.readline(), "ascii")
    g["read"] = lambda: bytes(f.read(), "ascii")


input = sys.stdin.buffer.readline
read = sys.stdin.buffer.read

if sys.argv[-1] == "-t":
    print("testing")
    _test()
    sys.exit()

main()
