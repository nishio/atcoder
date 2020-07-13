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


def solve(N, X):
    o1 = ord("1")

    def f(n):
        p = bin(n).count("1")
        return n % p

    table = [0] * 20
    for i in range(1, 20):
        x = f(i)
        if x == 0:
            table[i] = 1
        else:
            table[i] = table[x] + 1

    numOne = X.count(o1)
    ret = [0] * N

    # debug(": numOne", numOne)
    v = 0
    mod = numOne + 1
    p2mod_p1 = [0] * N
    p = 1
    for j in range(N):
        v *= 2
        v %= mod
        if (X[j] == o1):
            v += 1
        p2mod_p1[j] = p
        p *= 2
        p %= mod

    xmod_p1 = v % mod  # X mod (bc(X) + 1)
    xmod_m1 = 0  # X mod (bc(X) - 1)
    if numOne > 1:
        p = 1
        p2mod_m1 = [0] * N
        v = 0
        mod = numOne - 1
        for j in range(N):
            v *= 2
            v %= mod
            if (X[j] == o1):
                v += 1
            xmod_m1 = v % mod
            p2mod_m1[j] = p
            p *= 2
            p %= mod

    # debug(": xmod_p1, xmod_m1", xmod_p1, xmod_m1)
    # debug(": p2mod_p1, p2mod_m1", p2mod_p1, p2mod_m1)

    for i in range(N):
        if X[i] == o1:
            mod = numOne - 1
            if mod == 0:
                # already 0
                ret[i] = 0
                continue
            v2 = (xmod_m1 - p2mod_m1[-1-i]) % mod
        else:
            mod = numOne + 1
            v2 = (xmod_p1 + p2mod_p1[-1-i]) % mod
        # v = 0
        # for j in range(N):
        #     v *= 2
        #     v %= mod
        #     if (X[j] == o1) ^ (i == j):
        #         v += 1
        # v %= mod
        # debug(": v, v2", v, v2)
        # assert v == v2
        v = v2

        # debug(": v", v)
        if v == 0:
            ret[i] = 1
            continue
        if v < 20:
            ret[i] = table[v] + 1
            continue

        v = f(v)
        ret[i] = table[v] + 2

    # debug(": table", table)
    # debug(": ret", ret)
    return ret


def main():
    # parse input
    N = int(input())
    X = input().strip()
    print(*solve(N, X), sep="\n")


# tests
T1 = """
3
011
"""


def test_T1():
    """
    >>> as_input(T1)
    >>> main()
    2
    1
    1
    """


T2 = """
23
00110111001011011001110
"""


def test_T2():
    """
    >>> as_input(T2)
    >>> main()
    2
    1
    2
    2
    1
    2
    2
    2
    2
    2
    2
    2
    2
    2
    2
    2
    2
    2
    2
    2
    2
    1
    3
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
