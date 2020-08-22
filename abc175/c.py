#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")
MOD = 10 ** 9 + 7


def debug(*x):
    print(*x, file=sys.stderr)


def solve(X, K, D):
    X = abs(X)
    a = X // D
    if a >= K:
        return X - K * D
    r = X % D
    K -= a
    if K % 2 == 0:
        return r
    else:
        return D - r


def main():
    # parse input
    X, K, D = map(int, input().split())
    print(solve(X, K, D))


# tests
T1 = """
6 2 4
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
2
"""

T2 = """
7 4 3
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
1
"""

T3 = """
10 1 2
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
8
"""

T4 = """
1000000000000000 1000000000000000 1000000000000000
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
1000000000000000
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
