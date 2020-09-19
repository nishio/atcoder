#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")
MOD = 10 ** 9 + 7


def debug(*x):
    print(*x, file=sys.stderr)


def solve(N):
    ret = N - 1
    for i in range(2, N + 1):
        ret += (N - 1) // i
    return ret


def main():
    # parse input
    N = int(input())
    print(solve(N))


# tests
T1 = """
3
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
3
"""

T2 = """
100
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
473
"""

T3 = """
1000000
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
13969985
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
