#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")
MOD = 10 ** 9 + 7


def debug(*x):
    print(*x, file=sys.stderr)


def solve(S, T):
    buf = []
    for i in range(len(S) - len(T) + 1):
        diff = 0
        for j in range(len(T)):
            if S[i + j] != T[j]:
                diff += 1
        buf.append(diff)
    return min(buf)


def main():
    # parse input
    S = input().strip()
    T = input().strip()
    print(solve(S, T))


# tests
T1 = """
cabacc
abc
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
1
"""

T2 = """
codeforces
atcoder
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
6
"""

T3 = """
aaa
bbb
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
