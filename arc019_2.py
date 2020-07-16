#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.buffer.readline
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")
MOD = 10 ** 9 + 7


def debug(*x):
    print(*x, file=sys.stderr)


def solve(S):
    ret = 0
    N = len(S)
    if N == 1:
        return 0
    xs = [S[i] != S[-1-i] for i in range(N // 2)]
    sums = sum(xs)
    for x in xs:
        if x:
            if sums == 1:
                ret += 24 * 2
            else:
                ret += 25 * 2
        else:
            ret += 25 * 2
    if N & 1:
        if sums != 0:
            ret += 25
    return ret


def main():
    # parse input
    S = input().strip().decode('ascii')
    print(solve(S))


# tests
T2 = """
ARC
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
73
"""

T3 = """
NOLEMONNOMELON
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
350
"""

T4 = """
ABA
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
50
"""

T5 = """
AA
"""
TEST_T5 = """
>>> as_input(T5)
>>> main()
50
"""

T6 = """
AB
"""
TEST_T6 = """
>>> as_input(T6)
>>> main()
48
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
    global read, input
    f = io.StringIO(s.strip())

    def input():
        return bytes(f.readline(), "ascii")

    def read():
        return bytes(f.read(), "ascii")


input = sys.stdin.buffer.readline
read = sys.stdin.buffer.read

if sys.argv[-1] == "-t":
    print("testing")
    _test()
    sys.exit()

main()
