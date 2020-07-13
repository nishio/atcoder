#!/usr/bin/env python3

# from collections import defaultdict
# from heapq import heappush, heappop
# import numpy as np
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


def solve(N, K, XS):
    import bisect
    from itertools import accumulate
    acc = [0] + list(accumulate(XS))
    ret = 0
    for i in range(N):
        lb = acc[i] + K
        j = bisect.bisect_left(acc, lb)
        ret += N + 1 - j
    return ret


def main():
    # parse input
    N, K = map(int, input().split())
    XS = list(map(int, input().split()))
    print(solve(N, K, XS))


# tests
T1 = """
4 10
6 1 2 7
"""


def test_T1():
    """
    >>> as_input(T1)
    >>> main()
    2
    """


T2 = """
3 5
3 3 3
"""


def test_T2():
    """
    >>> as_input(T2)
    >>> main()
    3
    """


T3 = """
10 53462
103 35322 232 342 21099 90000 18843 9010 35221 19352
"""


def test_T3():
    """
    >>> as_input(T3)
    >>> main()
    36
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
