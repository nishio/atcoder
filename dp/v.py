#!/usr/bin/env python3

from collections import defaultdict
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


def solve(N, M, edges):
    cache = [-1] * ((N + 1) ** 2 + 10)
    for v in edges:
        if len(edges[v]) == 1:
            cache[v * (N + 1) + edges[v][0]] = (1, 0)

    def visit(parent, self):
        "return (blackroot, whiteroot)"
        cacheindex = self * (N + 1) + parent
        ret = cache[cacheindex]
        if ret != -1:
            return ret

        total = 1
        fw_b = 1  # full white or black
        one_black = 0  # only one black-root

        for child in edges[self]:
            if child == parent:
                continue
            b, w = visit(self, child)
            total *= (1 + w + b)
            fw_b *= (1 + b)
            one_black += b

        ret_b = ret_w = 0
        # when all child are fill-white, one black-root and one full-white
        ret_b += 1
        # when only one child is black-root and others are full-white
        # both white-root and black-root are OK
        ret_b += one_black
        ret_w += one_black
        # when multiple black-root and no white-root, it should be black
        ret_b += (fw_b - one_black - 1)
        # otherwise there are one or more white-root, it should be white
        ret_w += total - fw_b

        if parent != 0:
            ret = (ret_b, ret_w)
            cache[cacheindex] = ret
            return ret
        else:
            return ret_b

    ret = [visit(0, i + 1) % M for i in range(N)]
    return ret


def main():
    # parse input
    N, M = map(int, input().split())
    edges = defaultdict(list)
    for i in range(N - 1):
        x, y = map(int, input().split())
        edges[x].append(y)
        edges[y].append(x)

    #print(*solve(N, M, edges), sep="\n")
    for x in solve(N, M, edges):
        print(x)


# tests
T1 = """
3 100
1 2
2 3
"""


def test_T1():
    """
    >>> as_input(T1)
    >>> main()
    3
    4
    3
    """


T2 = """
4 100
1 2
1 3
1 4
"""


def test_T2():
    """
    >>> as_input(T2)
    >>> main()
    8
    5
    5
    5
    """


T3 = """
1 100
"""


def test_T3():
    """
    >>> as_input(T3)
    >>> main()
    1
    """


T4 = """
10 2
8 5
10 8
6 5
1 5
4 8
2 10
3 6
9 2
1 7
"""


def test_T4():
    """
    >>> as_input(T4)
    >>> main()
    0
    0
    1
    1
    1
    0
    1
    0
    1
    1
    """


# def test_T5():
#     """
#     >>> edges = defaultdict(list)
#     >>> for i in range(100000 - 1):
#     ...     edges[i + 1].append(i + 2)
#     ...     edges[i + 2].append(i + 1)
#     >>> solve(100000, 5, edges)
#     """
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
