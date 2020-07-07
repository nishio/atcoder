#!/usr/bin/env python3

# from collections import defaultdict
# from heapq import heappush, heappop
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.buffer.readline
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")
MOD = 10 ** 9 + 7


def debug(*x):
    print(*x, file=sys.stderr)


def solve(N, K, XS):
    table = [0] * (K + 1)
    for i in range(XS[0] + 1):
        table[i] = 1

    for i in range(1, N):
        v = 0
        newtable = [0] * (K + 1)
        for j in range(K + 1):
            v = 0
            for k in range(XS[i] + 1):
                if j - k < 0:
                    break
                v += table[j - k]
                v %= MOD

            newtable[j] = v
        table = newtable

    return table[K]


def main():
    # parse input
    N, K = map(int, input().split())
    XS = list(map(int, input().split()))

    print(solve(N, K, XS))


# tests
T1 = """
3 4
1 2 3
"""


def test_T1():
    """
    >>> as_input(T1)
    >>> main()
    5
    """


T2 = """
1 10
9
"""


def test_T2():
    """
    >>> as_input(T2)
    >>> main()
    0
    """


T3 = """
2 0
0 0
"""


def test_T3():
    """
    >>> as_input(T3)
    >>> main()
    1
    """


T4 = """
4 100000
100000 100000 100000 100000
"""


# def test_T4():
#     """
#     >>> as_input(T4)
#     >>> main()
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
