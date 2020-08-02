#!/usr/bin/env python3
import sys
import numpy as np
sys.setrecursionlimit(10**6)
INF = 10 ** 11  # sys.maxsize # float("inf")
MOD = 10 ** 9 + 7


def debug(*x):
    print(*x, file=sys.stderr)


def solve(N, data):
    xs, ys, ps = data.reshape((N, 3)).T

    candidate = [(0, x) for x in xs]
    candidate += [(1, y) for y in ys]
    candidate = list(sorted(set(candidate)))

    NUM_LINES = len(candidate)
    dist = np.minimum(np.abs(xs), np.abs(ys))
    # debug(": dist", dist)

    start = 0
    # distmemo = [None] * ((1 << NUM_LINES) + 10)
    distmemo = np.zeros((1 << NUM_LINES, N), dtype=np.int64)
    scorememo = [INF] * (N + 1)
    distmemo[start] = dist
    scorememo[start] = (dist * ps).sum()
    # debug(": (dist * ps).sum()", (dist * ps).sum())

    def f(cursor, parent, numbits):
        if cursor == N:
            return

        # add no lines
        f(cursor + 1, parent, numbits)

        # add vertical (x) line
        x = xs[cursor]
        lineid = candidate.index((0, x))
        new_parent = parent | (1 << lineid)
        if parent != new_parent:
            parent_dist = distmemo[parent]
            dist = np.minimum(parent_dist, np.abs(xs - x))
            distmemo[new_parent] = dist
            # debug(": ", f"{new_parent:05b}", dist)
            score = (dist * ps).sum()
            n = numbits + 1
            scorememo[n] = min(scorememo[n], score)
            f(cursor + 1, new_parent, n)

        # add vertical (x) line
        y = ys[cursor]
        lineid = candidate.index((1, y))
        new_parent = parent | (1 << lineid)
        if parent != new_parent:
            parent_dist = distmemo[parent]
            dist = np.minimum(parent_dist, np.abs(ys - y))
            distmemo[new_parent] = dist
            # debug(": ", f"{new_parent:05b}", dist)
            score = (dist * ps).sum()
            n = numbits + 1
            scorememo[n] = min(scorememo[n], score)
            f(cursor + 1, new_parent, n)

    f(0, start, 0)
    # debug(": scorememo", scorememo)
    return scorememo


def main():
    # parse input
    N = int(input())
    data = np.int64(read().split())
    print(*solve(N, data), sep="\n")


# tests
T1 = """
3
1 2 300
3 3 600
1 4 800
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
2900
900
0
0
"""

T2 = """
5
3 5 400
5 3 700
5 5 1000
5 7 700
7 5 400
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
13800
1600
0
0
0
0
"""

T3 = """
6
2 5 1000
5 2 1100
5 5 1700
-2 -5 900
-5 -2 600
-5 -5 2200
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
26700
13900
3200
1200
0
0
0
"""

T4 = """
8
2 2 286017
3 1 262355
2 -2 213815
1 -3 224435
-2 -2 136860
-3 -1 239338
-2 2 217647
-1 3 141903
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
2576709
1569381
868031
605676
366338
141903
0
0
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
