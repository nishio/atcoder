#!/usr/bin/env python3

from collections import defaultdict
from heapq import heappush, heappop
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.buffer.readline
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")


def debug(*x):
    print(*x)


def solve():
    "void()"
    pass


def main():
    solve()


def blute(N, M):
    """
    >>> blute(2, 2)
    2

    >>> blute(2, 3)
    18
    """
    from itertools import permutations
    nums = range(M)
    count = 0
    for a in permutations(nums, N):
        for b in permutations(nums, N):
            if all(a[i] != b[i] for i in range(N)):
                count += 1
    return count


def _test():
    import doctest
    doctest.testmod()
    # for M in range(1, 10):
    #     for N in range(1, M + 1):
    #         print("N, M, f = ", N, M, blute(N, M))

    ret = []
    for M in range(2, 10):
        r1 = blute(1, M)
        r2 = blute(2, M)
        r3 = blute(3, M)
        ret.append(r3/r1)
    print(ret)


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
