#!/usr/bin/env python3

from collections import defaultdict
from heapq import heappush, heappop
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.buffer.readline
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")


def debug(*x):
    print(*x)


def solve1(N, heights):
    heights += [INF]
    costs = [INF] * (N + 1)
    costs[0] = 0
    for i in range(N - 1):
        costs[i + 1] = min(
            costs[i + 1],
            costs[i] + abs(heights[i + 1] - heights[i]))
        costs[i + 2] = min(
            costs[i + 2],
            costs[i] + abs(heights[i + 2] - heights[i]))
    return costs[N - 1]


def solve2(N, heights):
    costs = [0] * N
    costs[0] = 0
    costs[1] = abs(heights[1] - heights[0])
    for i in range(2, N):
        costs[i] = min(
            costs[i - 2] + abs(heights[i] - heights[i - 2]),
            costs[i - 1] + abs(heights[i] - heights[i - 1]),
        )
    return costs[-1]


def solve(N, heights):
    costs = [None] * N
    costs[0] = 0
    costs[1] = abs(heights[1] - heights[0])

    def get_cost(i):
        if costs[i] != None:
            return costs[i]

        c = min(
            get_cost(i - 2) + abs(heights[i] - heights[i - 2]),
            get_cost(i - 1) + abs(heights[i] - heights[i - 1]),
        )
        costs[i] = c
        return c

    return get_cost(N - 1)


def main():
    N = int(input())
    heights = list(map(int, input().split()))
    print(solve(N, heights))


def _test():
    """
    >>> solve(4, [10, 30, 40, 20])
    30
    >>> solve(2, [10, 10])
    0
    >>> solve(6, [30, 10, 60, 10, 60, 50])
    40
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
