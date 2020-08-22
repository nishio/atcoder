#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")
MOD = 10 ** 9 + 7


def debug(*x):
    print(*x, file=sys.stderr)


def solve(N, LS):
    # LS = list(sorted(set(LS)))
    # N = len(LS)
    LS.sort()
    ret = 0
    for i in range(N):
        for j in range(i + 1, N):
            if LS[i] == LS[j]:
                continue
            for k in range(j + 1, N):
                if LS[j] == LS[k]:
                    continue
                if LS[i] + LS[j] > LS[k]:
                    # debug(": i,j,k", i, j, k, "  ", LS[i], LS[j], LS[k])
                    ret += 1
    return ret


def main():
    # parse input
    N = int(input())
    LS = list(map(int, input().split()))
    print(solve(N, LS))


# tests
T1 = """
5
4 4 9 7 5
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
5
"""

T2 = """
6
4 5 4 3 3 5
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
8
"""

T3 = """
10
9 4 6 1 9 6 10 6 6 8
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
39
"""

T4 = """
2
1 1
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
0
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
