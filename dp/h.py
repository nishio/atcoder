#!/usr/bin/env python3

from collections import defaultdict
from heapq import heappush, heappop
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.buffer.readline
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")
MOD = 10 ** 9 + 7


def debug(*x):
    print(*x)


def solve(H, W, data):
    "void()"
    score = [[0] * (W + 1) for i in range(H + 1)]
    score[0][1] = 1
    for y in range(1, H + 1):
        for x in range(1, W + 1):
            if data[y - 1][x - 1] == ord("#"):
                score[y][x] = 0
            else:
                score[y][x] = (score[y - 1][x] + score[y][x - 1]) % MOD
    # print(score)
    return score[H][W]


def main():
    H, W = map(int, input().split())
    data = [input() for i in range(H)]
    print(solve(H, W, data))


T1 = """
3 4
...#
.#..
....
"""

T2 = """
5 5
..#..
.....
#...#
.....
..#..
"""

T3 = """
20 20
....................
....................
....................
....................
....................
....................
....................
....................
....................
....................
....................
....................
....................
....................
....................
....................
....................
....................
....................
....................
"""

T4 = """
5 2
..
#.
..
.#
..
"""


def test_T4():
    """
    >>> as_input(T4)
    >>> main()
    0
    """


def test_T3():
    """
    >>> as_input(T3)
    >>> main()
    345263555
    """


def test_T2():
    """
    >>> as_input(T2)
    >>> main()
    24
    """


def _test():
    """
    >>> as_input(T1)
    >>> main()
    3
    """
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
