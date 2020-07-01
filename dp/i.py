#!/usr/bin/env python3

from collections import defaultdict
from heapq import heappush, heappop
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.buffer.readline
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")


def debug(*x):
    print(*x)


def solve(N, probs):
    m = [0.0] * (N + 1)
    m[0] = 1.0

    for i in range(N):
        n = [0.0] * (N + 1)
        for j in range(N):
            n[j + 1] += m[j] * probs[i]
        for j in range(N + 1):
            n[j] += m[j] * (1 - probs[i])
        m = n
    return sum(m[N // 2 + 1:])


def main():
    N = int(input())
    probs = list(map(float, input().split()))
    print(solve(N, probs))


T1 = """
3
0.30 0.60 0.80
"""


def test_T1():
    """
    >>> as_input(T1)
    >>> main()
    0.612
    """


T3 = """
5
0.42 0.01 0.42 0.99 0.42
"""


def test_T3():
    """
    >>> as_input(T3)
    >>> main()
    0.3821815872
    """


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
