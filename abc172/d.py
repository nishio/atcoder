#!/usr/bin/env python3

from functools import reduce
from operator import mul
from collections import defaultdict, Counter
from heapq import heappush, heappop
import sys
from math import sqrt, floor

sys.setrecursionlimit(10**6)
input = sys.stdin.buffer.readline
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")


def debug(*x):
    print(*x)


def solve(N):
    "void(i8)"
    ret = 0
    i = 2
    while True:
        step = i // 2
        start = (i + 1) // 2 * step
        if start > N:
            break
        end = N // step * step
        ret += (start + end) * ((end - start) // step + 1) // 2
        i += 1
    print(ret)


def main():
    N = int(input())
    solve(N)


def _test():
    """
    >>> solve(4)
    23

    >>> solve(100)
    26879

    >>> solve(10000000)
    838627288460105
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
