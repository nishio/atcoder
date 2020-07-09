#!/usr/bin/env python3

from collections import defaultdict
#from heapq import heappush, heappop
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.buffer.readline
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")
MOD = 10 ** 9 + 7


def debug(*x):
    print(*x, file=sys.stderr)


def solve(N, edges):
    ret_white = 0
    ret_total = 0

    def visit(parent, self):
        nonlocal ret_white, ret_total
        if parent != 0 and len(edges[self]) == 1:
            # self is leaf
            ret_white = 1
            ret_total = 2
            return

        black = 1
        white = 1
        for child in edges[self]:
            if child == parent:
                continue
            visit(self, child)
            black *= ret_white
            black %= MOD
            white *= ret_total
            white %= MOD
        ret_white = white
        ret_total = white + black
        return

    visit(0, 1)
    return ret_total % MOD


def main():
    # parse input
    N = int(input())
    edges = defaultdict(list)
    for i in range(N - 1):
        x, y = map(int, input().split())
        edges[x].append(y)
        edges[y].append(x)
    print(solve(N, edges))


# tests
T1 = """
3
1 2
2 3
"""


def test_T1():
    """
    >>> as_input(T1)
    >>> main()
    5
    """


T2 = """
4
1 2
1 3
1 4
"""


def test_T2():
    """
    >>> as_input(T2)
    >>> main()
    9
    """


T3 = """
1
"""


def test_T3():
    """
    >>> as_input(T3)
    >>> main()
    2
    """


T4 = """
10
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
    157
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
