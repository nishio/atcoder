#!/usr/bin/env python3

from collections import defaultdict
from heapq import heappush, heappop
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.buffer.readline
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")


def debug(*x):
    print(*x)


def solve(N, K):
    """
    >>> solve(9, 1)
    9
    >>> solve(5, 1)
    5
    >>> solve(10, 1)
    10
    >>> solve(11, 1)
    10
    >>> solve(30, 1)
    12
    >>> solve(100, 1)
    19
    >>> solve(25, 2)
    14
    """
    x = N
    digits = []
    while x:
        x, r = divmod(x, 10)
        digits.append(r)
    digits.reverse()
    numDigits = len(digits)

    def f(isBorder, isHead, index):
        if index == numDigits - 1:
            if isHead:
                ret = [0] * 4
            else:
                ret = [1, 9, 0, 0]
        else:
            ret = f(False, True, index + 1)

        if isBorder:
            border = ditigs[index]
            if border > 1:
                xs = f(False, False, index + 1)
                ret[1] += xs[0] * (border - 1)
                ret[2] += xs[1] * (border - 1)
                ret[3] += xs[2] * (border - 1)

            xs = f(False, False, index + 1)

            ret[1] += 1
        else:
            xs = f(False, False, index + 1)
            ret[0] += xs[0]
            ret[1] += xs[1] + xs[0] * 9
            ret[2] += xs[2] + xs[1] * 9
            ret[3] += xs[3] + xs[2] * 9

            # debug("ret: ret, isBorder, isHead, index: ",
            #       ret, isBorder, isHead, index)
        return ret

    return f(True, True, 0)[K]


def main():
    N = int(input())
    K = int(input())
    print(solve(N, K))


def _test():
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
