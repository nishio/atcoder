#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")
MOD = 10 ** 9 + 7


def debug(*x):
    print(*x, file=sys.stderr)


def solve(A, B, C, K):
    while A >= B:
        K -= 1
        B *= 2
    while B >= C:
        K -= 1
        C *= 2
    if K >= 0:
        return "Yes"
    return "No"


def main():
    # parse input
    A, B, C = map(int, input().split())
    K = int(input())
    print(solve(A, B, C, K))


# tests
T1 = """
7 2 5
3
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
Yes
"""

T2 = """
7 4 2
3
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
No
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
