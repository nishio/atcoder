#!/usr/bin/env python3

# from collections import defaultdict
from heapq import heappush, heappop
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


def solveOLD(N, XS):
    XS.sort()
    table = [0]
    for i in range(N):
        newtable = [0] * (i + 2)
        K, L, R = XS[i]
        for j in range(i + 1):
            if j < K:
                newtable[j + 1] = table[j] + L
            v = table[j] + R
            if v > newtable[j]:
                newtable[j] = v
        table = newtable
        debug(": table", table)
    return max(table)


def solveNG(N, XS):
    XS.sort()
    table = [0, 0]
    cursor = [0, 0]
    j = 0
    for i in range(N):
        newtable = [0] * 2
        K, L, R = XS[i]

        if cursor[1] < K:
            newtable[1] = table[1] + L
            cursor[1] += 1
        newtable[0] = table[1] + R
        if v > newtable[j]:
            newtable[j] = v
        table = newtable
        debug(": table", table)
    return max(table)


def solve(N, XS):
    head = []
    tail = []
    for i in range(N):
        K, L, R = XS[i]
        if L > R:
            heappush(head, (K, L, R))
        else:
            heappush(tail, (N - K, R, L))

    ret = 0
    selected = []
    for i in range(len(head)):
        K, L, R = heappop(head)
        heappush(selected, (L - R, K, L, R))
        ret += L
        if K <= i:
            worst = heappop(selected)
            ret -= worst[0]

    selected = []
    for i in range(len(tail)):
        K, L, R = heappop(tail)
        heappush(selected, (L - R, K, L, R))
        ret += L
        if K <= i:  # ?
            worst = heappop(selected)
            ret -= worst[0]

    return ret


def main():
    # parse input
    T = int(input())
    for i in range(T):
        N = int(input())
        XS = []
        for j in range(N):
            XS.append(tuple(map(int, input().split())))
        print(solve(N, XS))


# tests
T1 = """
3
2
1 5 10
2 15 5
3
2 93 78
1 71 59
3 57 96
19
19 23 16
5 90 13
12 85 70
19 67 78
12 16 60
18 48 28
5 4 24
12 97 97
4 57 87
19 91 74
18 100 76
7 86 46
9 100 57
3 76 73
6 84 93
1 6 84
11 75 94
19 15 3
12 11 34
"""


def test_T1():
    """
    >>> as_input(T1)
    >>> main()
    25
    221
    1354
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
