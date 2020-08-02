#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")
MOD = 10 ** 9 + 7


def debug(*x):
    print(*x, file=sys.stderr)


def solve(K):
    visited = [False] * K
    p = 7 % K
    for i in range(K):
        if p == 0:
            return i + 1
        if visited[p]:
            return - 1
        visited[p] = True
        p = (p * 10 + 7) % K


def main():
    # parse input
    K = int(input())
    print(solve(K))


# tests
T1 = """
101
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
4
"""
T2 = """
2
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
-1
"""
T3 = """
999983
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
999982
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
