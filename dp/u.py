#!/usr/bin/env python3

#from collections import defaultdict
#from heapq import heappush, heappop
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


def solve(N, M):
    FULLBIT = (1 << N) - 1

    def calcScore(S):
        # debug("enter calcScore: S", S)
        x = S
        ret = 0
        i = 0
        while x:
            if x & 1:
                # debug(": i", i)
                for j in range(i):
                    if (S >> j) & 1:
                        # debug(": i, j, M[i,j]", i, j, M[i, j])
                        ret += M[i * N + j]
            x //= 2
            i += 1
        # debug("leave calcScore: ret", ret)
        return ret
    groupScore = [calcScore(i) for i in range(1 << N)]
    # debug(": groupScore", groupScore)

    table = [None] * (1 << N)

    def sub(S):
        ret = table[S]
        if ret != None:
            return ret
        ret = groupScore[S]
        x = (S - 1) & S
        while x > 0:
            y = (~x) & S
            v = sub(x) + sub(y)
            if v > ret:
                ret = v
            x = (x - 1) & S
        table[S] = ret
        return ret

    return sub(FULLBIT)


def main():
    # parse input
    N = int(input())
    M = [int(x) for x in read().split()]
    print(solve(N, M))


# tests
T1 = """
3
0 10 20
10 0 -100
20 -100 0
"""


def test_T1():
    """
    >>> as_input(T1)
    >>> main()
    20
    """


T2 = """
2
0 -10
-10 0
"""


def test_T2():
    """
    >>> as_input(T2)
    >>> main()
    0
    """


T3 = """
4
0 1000000000 1000000000 1000000000
1000000000 0 1000000000 1000000000
1000000000 1000000000 0 -1
1000000000 1000000000 -1 0
"""


def test_T3():
    """
    >>> as_input(T3)
    >>> main()
    4999999999
    """


T4 = """
16
0 5 -4 -5 -8 -4 7 2 -4 0 7 0 2 -3 7 7
5 0 8 -9 3 5 2 -7 2 -7 0 -1 -4 1 -1 9
-4 8 0 -9 8 9 3 1 4 9 6 6 -6 1 8 9
-5 -9 -9 0 -7 6 4 -1 9 -3 -5 0 1 2 -4 1
-8 3 8 -7 0 -5 -9 9 1 -9 -6 -3 -8 3 4 3
-4 5 9 6 -5 0 -6 1 -2 2 0 -5 -2 3 1 2
7 2 3 4 -9 -6 0 -2 -2 -9 -3 9 -2 9 2 -5
2 -7 1 -1 9 1 -2 0 -6 0 -6 6 4 -1 -7 8
-4 2 4 9 1 -2 -2 -6 0 8 -6 -2 -4 8 7 7
0 -7 9 -3 -9 2 -9 0 8 0 0 1 -3 3 -6 -6
7 0 6 -5 -6 0 -3 -6 -6 0 0 5 7 -1 -5 3
0 -1 6 0 -3 -5 9 6 -2 1 5 0 -2 7 -8 0
2 -4 -6 1 -8 -2 -2 4 -4 -3 7 -2 0 -9 7 1
-3 1 1 2 3 3 9 -1 8 3 -1 7 -9 0 -6 -8
7 -1 8 -4 4 1 2 -7 7 -6 -5 -8 7 -6 0 -9
7 9 9 1 3 2 -5 8 7 -6 3 0 1 -8 -9 0
"""


def test_T4():
    """
    >>> as_input(T4)
    >>> main()
    132
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
