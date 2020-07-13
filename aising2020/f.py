#!/usr/bin/env python3

#from collections import defaultdict
#from heapq import heappush, heappop
#import numpy as np
import sys
from functools import reduce
import numpy as np

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


def solve(N):
    Q = reduce(
        np.convolve,
        [[1, -1]] * 16 + [[1, 1]] * 5,
        np.array([1], dtype=np.int64))
    P = np.zeros(6, dtype=np.int64)
    P[5] = 1

    def conv(X, Y):
        n = X.shape[0]
        m = Y.shape[0]
        ret = np.zeros(n + m - 1, dtype=np.int64)
        for i in range(n):
            ret[i:i + m] += X[i] * Y
            ret[i:i + m] %= MOD
        return ret

    while N:
        Qm = Q.copy()
        Qm[1::2] *= -1
        QQm = conv(Q, Qm)

        PQm = conv(P, Qm)
        if N % 2:
            P = PQm[1::2]
        else:
            P = PQm[::2]
        Q = QQm[::2]
        N //= 2
    return P[0]


def main():
    # parse input
    T = int(input())
    for i in range(T):
        N = int(input())
        print(solve(N))


# tests
T1 = """
4
4
6
10
1000000000
"""


def test_T1():
    """
    >>> as_input(T1)
    >>> main()
    0
    11
    4598
    257255556
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
