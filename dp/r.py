#!/usr/bin/env python3

#from collections import defaultdict
#from heapq import heappush, heappop
import sys
import numpy as np

sys.setrecursionlimit(10**6)
input = sys.stdin.buffer.readline
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")
MOD = 10 ** 9 + 7


def debug(*x):
    print(*x, file=sys.stderr)


def solve(N, K, X):
    def modmul(x, y):
        ret = np.zeros(x.shape, np.int64)
        for i in range(N):
            for j in range(N):
                v = x[i, :] * y[:, j]
                v %= MOD
                ret[i, j] = v.sum() % MOD
        return ret

    powK = np.eye(N, dtype=np.int64)
    while K:
        if K & 1:
            powK = modmul(powK, X)
        X = modmul(X, X)
        K //= 2
    return powK.sum() % MOD


def main():
    # parse input
    N, K = map(int, input().split())
    X = np.int64(read().split())
    X = X.reshape((N, N))
    print(solve(N, K, X))


# tests
T1 = """
4 2
0 1 0 0
0 0 1 1
0 0 0 1
1 0 0 0
"""


def test_T1():
    """
    >>> as_input(T1)
    >>> main()
    6
    """


T2 = """
3 3
0 1 0
1 0 1
0 0 0
"""


def test_T2():
    """
    >>> as_input(T2)
    >>> main()
    3
    """


T3 = """
6 2
0 0 0 0 0 0
0 0 1 0 0 0
0 0 0 0 0 0
0 0 0 0 1 0
0 0 0 0 0 1
0 0 0 0 0 0
"""


def test_T3():
    """
    >>> as_input(T3)
    >>> main()
    1
    """


T4 = """
1 1
0
"""


def test_T4():
    """
    >>> as_input(T4)
    >>> main()
    0
    """


T5 = """
10 1000000000000000000
0 0 1 1 0 0 0 1 1 0
0 0 0 0 0 1 1 1 0 0
0 1 0 0 0 1 0 1 0 1
1 1 1 0 1 1 0 1 1 0
0 1 1 1 0 1 0 1 1 1
0 0 0 1 0 0 1 0 1 0
0 0 0 1 1 0 0 1 0 1
1 0 0 0 1 0 1 0 0 0
0 0 0 0 0 1 0 0 0 0
1 0 1 1 1 0 1 1 1 0
"""


def test_T5():
    """
    >>> as_input(T5)
    >>> main()
    957538352
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
