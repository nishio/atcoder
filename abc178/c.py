#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")
MOD = 10 ** 9 + 7


def debug(*x):
    print(*x, file=sys.stderr)


def solve(N):
    nn, pn, np, pp = [8, 1, 1, 0]
    for i in range(N - 1):
        pp = (pp * 10 + np + pn) % MOD
        pn = (pn * 9 + nn) % MOD
        np = (np * 9 + nn) % MOD
        nn = (nn * 8) % MOD

    return pp


def main():
    # parse input
    N = int(input())
    print(solve(N))


# tests
T1 = """
2
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
2
"""

T2 = """
1
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
0
"""

T3 = """
869121
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
2511445
"""

T4 = """
3
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
54
"""


def _test():
    import doctest
    doctest.testmod()
    g = globals()
    for k in sorted(g):
        if k.startswith("TEST_"):
            doctest.run_docstring_examples(g[k], g, name=k)


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
