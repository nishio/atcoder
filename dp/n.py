#!/usr/bin/env python3

#from collections import defaultdict
#from heapq import heappush, heappop
from itertools import accumulate
from functools import lru_cache
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.buffer.readline
INF = sys.maxsize  # float("inf")


def debug(*x):
    print(*x, file=sys.stderr)


def solve(N, XS):
    accum = list(accumulate(XS)) + [0]
    @lru_cache(maxsize=None)
    def sub(L, R):
        # debug(": L,R", L, R)
        if L == R:
            return 0
        ret = INF
        for x in range(L, R):
            v = sub(L, x) + sub(x + 1, R)
            if v < ret:
                ret = v
            # debug("loop: ", XS[L:x+1], XS[x+1: R+1],  v)
        # debug(": ret, ", ret, accum[R] - accum[L - 1])
        return ret + accum[R] - accum[L - 1]
    return sub(0, N - 1)


def main():
    # parse input
    N = int(input())
    XS = list(map(int, input().split()))
    print(solve(N, XS))


# tests
T0 = """
2
10 20
"""


def test_T0():
    """
    >>> as_input(T0)
    >>> main()
    30
    """


T01 = """
3
10 20 30
"""


def test_T01():
    """
    >>> as_input(T01)
    >>> main()
    90
    """


T1 = """
4
10 20 30 40
"""


def test_T1():
    """
    >>> as_input(T1)
    >>> main()
    190
    """


T2 = """
5
10 10 10 10 10
"""


def test_T2():
    """
    >>> as_input(T2)
    >>> main()
    120
    """


T3 = """
3
1000000000 1000000000 1000000000
"""


def test_T3():
    """
    >>> as_input(T3)
    >>> main()
    5000000000
    """


T4 = """
6
7 6 8 6 1 1
"""


def test_T4():
    """
    >>> as_input(T4)
    >>> main()
    68
    """
# add tests above


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
