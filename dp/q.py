#!/usr/bin/env python3

#from collections import defaultdict
from heapq import heappush, heappop
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.buffer.readline
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")


def debug(*x):
    print(*x, file=sys.stderr)


def solve(N, HS, VS):
    bit = [0] * (N + 1)  # 1-origin

    def bit_put(pos, val):
        assert pos > 0
        x = pos
        while x <= N:
            bit[x] = max(bit[x], val)
            x += x & -x  # (x & -x) = rightmost 1 = block width

    def bit_max(pos):
        assert pos > 0
        ret = 0
        x = pos
        while x > 0:
            ret = max(ret, bit[x])
            x -= x & -x
        return ret

    for i in range(N):
        h = HS[i]
        m = bit_max(h)
        bit_put(h, m + VS[i])

    return bit_max(N)


def main():
    # parse input
    N = int(input())
    HS = list(map(int, input().split()))
    VS = list(map(int, input().split()))
    print(solve(N, HS, VS))


# tests
T1 = """
4
3 1 4 2
10 20 30 40
"""


def test_T1():
    """
    >>> as_input(T1)
    >>> main()
    60
    """


T2 = """
1
1
10
"""


def test_T2():
    """
    >>> as_input(T2)
    >>> main()
    10
    """


T3 = """
5
1 2 3 4 5
1000000000 1000000000 1000000000 1000000000 1000000000
"""


def test_T3():
    """
    >>> as_input(T3)
    >>> main()
    5000000000
    """


T4 = """
9
4 2 5 8 3 6 1 7 9
6 8 8 4 6 3 5 7 5
"""


def test_T4():
    """
    >>> as_input(T4)
    >>> main()
    31
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
