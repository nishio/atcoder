#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")
MOD = 10 ** 9 + 7


def debug(*x):
    print(*x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    import bisect
    # parse input
    N, Q = map(int, input().split())
    CS = list(map(int, input().split()))
    XS = [[] for _i in range(N + 1)]
    for i, c in enumerate(CS):
        XS[c].append(i)

    for _q in range(Q):
        L, R = map(int, input().split())
        ret = 0
        for c in range(1, N + 1):
            lc = bisect.bisect_left(XS[c], L - 1)
            rc = bisect.bisect_right(XS[c], R - 1)
            if lc != rc:
                ret += 1
        print(ret)


# tests
T1 = """
4 3
1 2 1 3
1 3
2 4
3 3
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
2
3
1
"""

T2 = """
10 10
2 5 6 5 2 1 7 9 7 2
5 5
2 4
6 7
2 2
7 8
7 9
1 8
6 9
8 10
6 8
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
1
2
2
1
2
2
6
3
3
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
