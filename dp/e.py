#!/usr/bin/env python3

from collections import defaultdict
from heapq import heappush, heappop
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.buffer.readline
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")


def debug(*x):
    print(*x)


def solve(N, W, WV):
    MAX_VALUE = N * 10 ** 3
    weights = [INF] * (MAX_VALUE + 1)
    weights[0] = 0
    for i in range(N):
        next_weights = weights[:]
        weight, value = WV[i]
        for j in range(MAX_VALUE - value + 1):
            next_weights[j + value] = min(
                weights[j + value],
                weights[j] + weight)
        weights = next_weights
    # print(weights)
    for i in range(MAX_VALUE, -1, -1):
        if weights[i] <= W:
            return i


T1 = """
3 8
3 30
4 50
5 60
"""


def main():
    N, W = map(int, input().split())
    WV = [
        list(map(int, input().split()))
        for i in range(N)
    ]
    print(solve(N, W, WV))


def _test():
    """
    >>> as_input(T1)
    >>> main()
    90
    """
    import doctest
    doctest.testmod()


def as_input(s):
    "use in test, use given string as input file"
    import io
    global read, input
    f = io.StringIO(s.strip())
    input = f.readline
    read = f.read


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
