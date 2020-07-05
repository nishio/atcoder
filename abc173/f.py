#!/usr/bin/env python3

from collections import defaultdict
from heapq import heappush, heappop
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.buffer.readline
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")


def debug(*x):
    print(*x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    "void()"
    pass


def main():
    v = 0
    e = 0
    N = int(input())
    for i in range(N):
        v += (N - i) * (i + 1)

    for i in range(N - 1):
        v1, v2 = sorted(map(int, input().split()))
        v1 -= 1
        v2 -= 1
        e += (N - v2) * (v1 + 1)

    debug(": e, v", e, v)
    print(v - e)


T1 = """
3
1 3
2 3
"""


def test_T1():
    """
    >>> as_input(T1)
    >>> main()
    7
    """


T2 = """
10
5 3
5 7
8 9
1 9
9 10
8 4
7 4
6 10
7 2
"""


def test_T2():
    """
    >>> as_input(T2)
    >>> main()
    113
    """


def _test():
    import doctest
    doctest.testmod()


def as_input(s):
    "use in test, use given string as input file"
    import io
    global read, input
    f = io.StringIO(s.strip())

    def input():
        return bytes(f.readline(), "ascii")

    def read():
        return bytes(f.read(), "ascii")


USE_NUMBA = False
if (USE_NUMBA and sys.argv[-1] == 'ONLINE_JUDGE') or sys.argv[-1] == '-c':
    print("compiling")
    from numba.pycc import CC
    cc = CC('my_module')
    cc.export('solve', solve.__doc__.strip().split()[0])(solve)
    cc.compile()
    exit()
else:
    input = sys.stdin.buffer.readline
    read = sys.stdin.buffer.read

    if (USE_NUMBA and sys.argv[-1] != '-p') or sys.argv[-1] == "--numba":
        # -p: pure python mode
        # if not -p, import compiled module
        from my_module import solve  # pylint: disable=all
    elif sys.argv[-1] == "-t":
        print("testing")
        _test()
        sys.exit()
    elif sys.argv[-1] != '-p' and len(sys.argv) == 2:
        # input given as file
        input_as_file = open(sys.argv[1])
        input = input_as_file.buffer.readline
        read = input_as_file.buffer.read

    main()
