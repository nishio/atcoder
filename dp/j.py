#!/usr/bin/env python3

import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.buffer.readline
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")


def debug(*x):
    print(*x)


def solve(N, AS):
    from collections import Counter
    count = Counter(AS)
    expect = [[[-1] * (N + 1) for i in range(N + 1)] for j in range(N + 1)]
    expect[0][0][0] = 0

    def f(a, b, c):
        p = N
        if a > 0:
            v = expect[a - 1][b][c]
            if v == -1:
                v = f(a - 1, b, c)
            p += v * a
        if b > 0:
            v = expect[a + 1][b - 1][c]
            if v == -1:
                v = f(a + 1, b - 1, c)
            p += v * b
        if c > 0:
            v = expect[a][b + 1][c - 1]
            if v == -1:
                v = f(a, b + 1, c - 1)
            p += v * c
        p /= (a + b + c)

        # debug("f: a,b,c,p", a, b, c, p)
        expect[a][b][c] = p
        return p

    return f(count[1], count[2], count[3])


def main():
    N = int(input())
    AS = list(map(int, input().split()))
    print(solve(N, AS))


T1 = """
3
1 1 1
"""


def test_T1():
    """
    >>> as_input(T1)
    >>> main()
    5.5
    """


T2 = """
1
3
"""


def test_T2():
    """
    >>> as_input(T2)
    >>> main()
    3.0
    """


T3 = """
2
1 2
"""


def test_T3():
    """
    >>> as_input(T3)
    >>> main()
    4.5
    """


# T4 = """
# 10
# 1 3 2 3 3 2 3 2 1 3
# """


# def test_T4():
#     """
#     >>> as_input(T4)
#     >>> N = int(input())
#     >>> AS = list(map(int, input().split()))
#     >>> abs(solve(N, AS) - 54.48064457488221)  < 10 ** -9
#     """


def _test():
    import doctest
    doctest.testmod()


def as_input(s):
    "use in test, use given string as input file"
    import io
    global read, input
    f = io.StringIO(s.strip())
    input = f.readline
    read = f.read


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
        _test()
        sys.exit()
    elif sys.argv[-1] != '-p' and len(sys.argv) == 2:
        # input given as file
        input_as_file = open(sys.argv[1])
        input = input_as_file.buffer.readline
        read = input_as_file.buffer.read

    main()
