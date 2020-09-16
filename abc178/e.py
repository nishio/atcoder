#!/usr/bin/env python3
import numpy as np
import sys
sys.setrecursionlimit(10**6)
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")
MOD = 10 ** 9 + 7


def debug(*x):
    print(*x, file=sys.stderr)


def blute(N, XY):
    ret = np.zeros(N, np.int64)
    for i in range(N):
        ret[i] = np.max(np.abs(XY - XY[i]).sum(axis=1))
    return np.max(ret)


def solve(N, XY):
    S = XY.sum(axis=1)
    p1 = np.argmax(S)
    p2 = np.argmin(S)
    D = XY[:, 0] - XY[:, 1]
    p3 = np.argmax(D)
    p4 = np.argmin(D)
    return max(S[p1] - S[p2], D[p3] - D[p4])


def main():
    # parse input
    N = int(input())
    XY = np.int64(read().split())
    XY = XY.reshape((N, 2))
    print(solve(N, XY))


# tests
T1 = """
3
1 1
2 4
3 2
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
4
"""

T2 = """
2
1 1
1 1
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
0
"""

TEST_T3 = """
>>> N = 100
>>> np.random.seed(1)
>>> solve(N, np.random.randint(1, 100, (N, 2)))
189
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
