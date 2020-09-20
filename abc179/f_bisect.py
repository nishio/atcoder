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
    from bisect import bisect_left
    N, Q = map(int, input().split())
    ret = (N - 2) ** 2
    xs = [-N]
    xvals = [N - 2]
    ys = [-N]
    yvals = [N - 2]
    for _q in range(Q):
        q, x = map(int, input().split())
        if q == 1:
            i = bisect_left(xs, -x)
            ret -= xvals[i - 1]
            if i == len(xs) and yvals[-1] > x - 2:
                ys.append(-xvals[i - 1] - 2)
                yvals.append(x - 2)
        else:
            y = x
            i = bisect_left(ys, -y)
            ret -= yvals[i - 1]
            if i == len(ys) and xvals[-1] > y - 2:
                xs.append(-yvals[i - 1] - 2)
                xvals.append(y - 2)

    print(ret)


# tests
T1 = """
5 5
1 3
2 3
1 4
2 2
1 2
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
1
"""

T2 = """
200000 0
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
39999200004
"""

T3 = """
176527 15
1 81279
2 22308
2 133061
1 80744
2 44603
1 170938
2 139754
2 15220
1 172794
1 159290
2 156968
1 56426
2 77429
1 97459
2 71282
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
31159505795
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
