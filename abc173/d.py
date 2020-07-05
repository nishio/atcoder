#!/usr/bin/env python3

import itertools
from collections import defaultdict
from heapq import heappush, heappop
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.buffer.readline
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")


def debug(*x):
    print(*x, file=sys.stderr)


def blute_solve(N, AS):
    "void()"
    buf = []

    def blute(xs, buf):
        debug("blute: xs, buf", xs, buf)
        if not xs:
            return 0
        if not buf:
            # first player score 0
            return blute(xs[1:], [xs[0]])
        # insert
        candidate = []
        for i in range(len(buf)):
            s = min(buf[i - 1], buf[i])
            newBuf = buf[:]
            newBuf.insert(0, xs[0])
            candidate.append(blute(xs[1:], newBuf) + s)
        return max(candidate)

    candidate = []
    for xs in itertools.permutations(range(N)):
        candidate.append(blute(xs, buf))
    return max(candidate)


def solve(N, AS):
    buf = []
    AS.sort(reverse=True)
    ret = AS[0]
    for i in range(N - 2):
        ret += AS[1 + i // 2]
    return ret


def main():
    N = int(input())
    AS = list(map(int, input().split()))
    print(solve(N, AS))


T1 = """
4
2 2 1 3
"""


def test_T1():
    """
    >>> as_input(T1)
    >>> main()
    7
    """


T0 = """
3
3 2 1
"""


def test_T0():
    """
    >>> as_input(T0)
    >>> main()
    5
    """


T2 = """
7
1 1 1 1 1 1 1
"""


def test_T2():
    """
    >>> as_input(T2)
    >>> main()
    6
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
        _test()
        sys.exit()
    elif sys.argv[-1] != '-p' and len(sys.argv) == 2:
        # input given as file
        input_as_file = open(sys.argv[1])
        input = input_as_file.buffer.readline
        read = input_as_file.buffer.read

    main()
