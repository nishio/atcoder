#!/usr/bin/env python3

from collections import defaultdict
from heapq import heappush, heappop
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.buffer.readline
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")


def debug(*x):
    print(*x)


def solve1(N, K, heights):
    heights += [INF] * K
    costs = [INF] * (N + K)
    costs[0] = 0
    for i in range(N - 1):
        for k in range(1, K + 1):
            newcost = costs[i] + abs(heights[i + k] - heights[i])
            if newcost < costs[i + k]:
                costs[i + k] = newcost
    return costs[N - 1]


def solve(N, K, heights):
    costs = [0] * N
    costs[0] = 0
    for i in range(1, N):
        costs[i] = min(
            costs[j] + abs(heights[i] - heights[j])
            for j in range(max(i - K, 0), i)
        )

    return costs[-1]


def solve3(N, K, heights):
    costs = [None] * N
    costs[0] = 0

    def get_cost(i):
        if costs[i] != None:
            return costs[i]

        c = min(
            get_cost(j) + abs(heights[i] - heights[j])
            for j in range(max(i - K, 0), i)
        )
        costs[i] = c
        return c

    return get_cost(N - 1)


def main():
    N, K = map(int, input().split())
    heights = list(map(int, input().split()))
    print(solve(N, K, heights))


def _test():
    """
    >>> solve(5, 3, [10, 30, 40, 50, 20])
    30
    >>> solve(3, 1, [10, 20, 10])
    20
    >>> solve(2, 100, [10, 10])
    0
    >>> solve(10, 4, [40, 10, 20, 70, 80, 10, 20, 70, 80, 60])
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
