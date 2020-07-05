#!/usr/bin/env python3

from collections import defaultdict
from heapq import heappush, heappop
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.buffer.readline
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")


def debug(*x):
    print(*x, file=sys.stderr)


def solve(N, K, AS):
    for _i in range(K):
        d = [0] * (N + 1)
        for i in range(N):
            x = AS[i]
            d[max(i - x, 0)] += 1
            d[min(i + x + 1, N)] -= 1
        cur = 0
        ret = [0] * N
        for i in range(N):
            cur += d[i]
            ret[i] = cur
        AS = ret
        if all(x == N for x in ret):
            return ret

    return ret


def main():
    N, K = map(int, input().split())
    AS = list(map(int, input().split()))

    print(*solve(N, K, AS))


T1 = """
5 1
1 0 0 1 0
"""


def test_T1():
    """
    >>> as_input(T1)
    >>> main()
    1 2 2 1 2
    """


T2 = """
5 2
1 0 0 1 0
"""


def test_T2():
    """
    >>> as_input(T2)
    >>> main()
    3 3 4 4 3
    """


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
