#!/usr/bin/env python3

#from collections import defaultdict
#from heapq import heappush, heappop
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.buffer.readline
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")
MOD = 10 ** 9 + 7


def debug(*x):
    print(*x, file=sys.stderr)


def solve(N, D):
    less = [0] * D
    equal = 0
    for digit in N:
        new_less = [0] * D
        for new_digit in range(10):
            for d in range(D):
                new_less[(d + new_digit) % D] += less[d]
            if new_digit < digit:
                new_less[(equal + new_digit) % D] += 1
        equal += digit
        equal %= D
        for d in range(D):
            new_less[d] %= MOD
        less = new_less

    ret = less[0]
    ret -= 1  # for x = 0
    if equal == 0:  # for x = N
        ret += 1
    return ret % MOD


def main():
    # parse input
    N = [x - ord('0') for x in input().strip()]
    D = int(input())
    print(solve(N, D))


# tests
T1 = """
30
4
"""


def test_T1():
    """
    >>> as_input(T1)
    >>> main()
    6
    """


T2 = """
1000000009
1
"""


def test_T2():
    """
    >>> as_input(T2)
    >>> main()
    2
    """


T3 = """
98765432109876543210
58
"""


def test_T3():
    """
    >>> as_input(T3)
    >>> main()
    635270834
    """


T4 = """
555
1
"""


def test_T4():
    """
    >>> as_input(T4)
    >>> main()
    555
    """


T6 = """
5
1
"""


def test_T6():
    """
    >>> as_input(T6)
    >>> main()
    5
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
