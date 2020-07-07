#!/usr/bin/env python3

#from collections import defaultdict
#from heapq import heappush, heappop
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.buffer.readline
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")


def debug(*x):
    print(*x, file=sys.stderr)


def solve(N, K, AS):
    AS.sort()
    MIN = AS[0]

    table = [0] * (K + 1)
    for i in range(MIN):
        table[i] = -1  # LOSE

    for i in range(MIN, K + 1):
        for a in AS:
            if table[i - a] == -1:
                table[i] = 1
                break
        else:
            table[i] = -1

    # debug(": table", table)

    if table[K] == 1:
        return "First"

    else:
        return "Second"


def main():
    # parse input
    N, K = map(int, input().split())
    AS = list(map(int, input().split()))
    print(solve(N, K, AS))


# tests
T1 = """
2 4
2 3
"""


def test_T1():
    """
    >>> as_input(T1)
    >>> main()
    First
    """


T2 = """
2 5
2 3
"""


def test_T2():
    """
    >>> as_input(T2)
    >>> main()
    Second
    """


T3 = """
2 7
2 3
"""


def test_T3():
    """
    >>> as_input(T3)
    >>> main()
    First
    """


T4 = """
3 20
1 2 3
"""


def test_T4():
    """
    >>> as_input(T4)
    >>> main()
    Second
    """


T5 = """
3 21
1 2 3
"""


def test_T5():
    """
    >>> as_input(T5)
    >>> main()
    First
    """


T6 = """
1 100000
1
"""


def test_T6():
    """
    >>> as_input(T6)
    >>> main()
    Second
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
