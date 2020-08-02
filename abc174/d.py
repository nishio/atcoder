#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")
MOD = 10 ** 9 + 7


def debug(*x):
    print(*x, file=sys.stderr)


def solve(N, CS):
    left = 0
    right = N - 1
    R = ord("R")
    W = ord("W")
    ret = 0
    while left < right:
        if CS[left] == R:
            left += 1
            continue
        if CS[right] == W:
            right -= 1
            continue
        # swap
        left += 1
        right -= 1
        ret += 1
    return ret


def main():
    # parse input
    N = int(input())
    CS = input().strip()
    print(solve(N, CS))


# tests
T1 = """
4
WWRR
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
2
"""

T2 = """
2
RR
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
0
"""

T3 = """
8
WRWWRWRR
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
3
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
