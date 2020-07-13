#!/usr/bin/env python3

#from collections import defaultdict
#from heapq import heappush, heappop
#import numpy as np
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.buffer.readline
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")
MOD = 10 ** 9 + 7

debug_indent = 0


def debug(*x):
    global debug_indent
    x = list(x)
    indent = 0
    if x[0].startswith("enter") or x[0][0] == ">":
        indent = 1
    if x[0].startswith("leave") or x[0][0] == "<":
        debug_indent -= 1
    x[0] = "  " * debug_indent + x[0]
    print(*x, file=sys.stderr)
    debug_indent += indent


def solve(N, XS):
    if N == 1:
        return 0
    a = abs(XS[1] - XS[0])
    if N == 2:
        return a
    b = abs(XS[2] - XS[0])
    if N == 3:
        return b
    for i in range(3, N):
        v = min(
            a + abs(XS[i - 2] - XS[i]),
            b + abs(XS[i - 1] - XS[i]),
        )
        a = b
        b = v
    return v


def main():
    # parse input
    N = int(input())
    XS = list(map(int, input().split()))
    print(solve(N, XS))


# tests
T1 = """
4
100 150 130 120
"""


def test_T1():
    """
    >>> as_input(T1)
    >>> main()
    40
    """


T2 = """
9
314 159 265 358 979 323 846 264 338
"""


def test_T2():
    """
    >>> as_input(T2)
    >>> main()
    310
    """


T4 = """
1
10
"""


def test_T4():
    """
    >>> as_input(T4)
    >>> main()
    0
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
