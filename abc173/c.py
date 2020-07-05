#!/usr/bin/env python3

from collections import defaultdict
from heapq import heappush, heappop
import sys
import numpy as np
import itertools
sys.setrecursionlimit(10**6)
input = sys.stdin.buffer.readline
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")


def debug(*x):
    print(*x, file=sys.stderr)


def solve(H, W, K, data):
    "void()"
    data = (data == 35)
    ret = 0
    for x in itertools.product((0, 1), repeat=W):
        dX = data * x
        for y in itertools.product((0, 1), repeat=H):
            s = (dX.T * y).sum()
            if s == K:
                ret += 1
    return ret


def main():
    H, W, K = map(int, input().split())
    data = np.array([list(input().strip()) for i in range(H)])
    print(solve(H, W, K, data))


T1 = """
2 3 2
..#
###
"""


T2 = """
2 3 4
..#
###
"""

T3 = """
2 2 3
##
##
"""

T4 = """
6 6 8
..##..
.#..#.
#....#
######
#....#
#....#
"""


def test_T4():
    """
    >>> as_input(T4)
    >>> main()
    208
    """


def test_T3():
    """
    >>> as_input(T3)
    >>> main()
    0
    """


def test_T2():
    """
    >>> as_input(T2)
    >>> main()
    1
    """


def test_T1():
    """
    >>> as_input(T1)
    >>> main()
    5
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
        _test()
        sys.exit()
    elif sys.argv[-1] != '-p' and len(sys.argv) == 2:
        # input given as file
        input_as_file = open(sys.argv[1])
        input = input_as_file.buffer.readline
        read = input_as_file.buffer.read

    main()
