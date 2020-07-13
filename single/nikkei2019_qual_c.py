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


def solve_wrong(N, AS, BS):
    XS = [
        (BS[i] - AS[i], AS[i], i)
        for i in range(N)
    ]
    XS.sort(reverse=True)

    YS = [
        (AS[i] - BS[i], BS[i], i)
        for i in range(N)
    ]
    YS.sort(reverse=True)

    A = B = 0
    used = set()
    for i in range(N):
        debug(": A,B", A, B)
        if i % 2 == 0:
            while True:
                v = XS.pop(0)
                if v[2] not in used:
                    break
            debug(": i, v", i, v, AS[i], BS[i])
            used.add(v[2])
            A += v[1]
        else:
            while True:
                v = YS.pop(0)
                if v[2] not in used:
                    break
            debug(": i, v", i, v)
            used.add(v[2])
            B += v[1]
    return A - B


def solve(N, AS, BS):
    XS = [
        (BS[i] + AS[i], i)
        for i in range(N)
    ]
    XS.sort(reverse=True)

    A = B = 0
    used = set()
    for i in range(N):
        debug(": A,B", A, B)
        if i % 2 == 0:
            while True:
                v = XS.pop(0)
                if v[2] not in used:
                    break
            debug(": i, v", i, v, AS[i], BS[i])
            used.add(v[2])
            A += v[1]
        else:
            while True:
                v = YS.pop(0)
                if v[2] not in used:
                    break
            debug(": i, v", i, v)
            used.add(v[2])
            B += v[1]
    return A - B


def main():
    # parse input
    N = int(input())
    AS = []
    BS = []
    for i in range(N):
        A, B = map(int, input().split())
        AS.append(A)
        BS.append(B)

    print(solve(N, AS, BS))


# tests

T1 = """
3
10 10
20 20
30 30
"""


def test_T1():
    """
    >>> as_input(T1)
    >>> main()
    20
    """


T2 = """
3
20 10
20 20
20 30
"""


def test_T2():
    """
    >>> as_input(T2)
    >>> main()
    20
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
