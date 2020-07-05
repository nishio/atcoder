#!/usr/bin/env python3

import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.buffer.readline
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")
MOD = 10 ** 9 + 7


def debug(*x):
    print(*x, file=sys.stderr)


def solve(N, K, XS):
    "void()"

    posi = [x for x in XS if x >= 0]
    nega = [x for x in XS if x < 0]

    nega.sort(reverse=True)
    posi.sort()

    if K == N:
        # no choice
        ret = 1
        for i in range(N):
            ret *= XS[i]
            ret %= MOD
        return ret

    if not posi and K % 2:
        # negative answer
        # find smallest abs
        ret = 1
        for i in range(K):
            ret *= nega[i]
            ret %= MOD
        return ret

    ret = 1
    while K:
        # debug(": K, nega, posi", K, nega, posi)
        if K >= 2:
            if len(posi) >= 2:
                v = posi[-1] * posi[-2]
                if len(nega) >= 2:
                    w = nega[-1] * nega[-2]
                else:
                    w = -INF
                if v > w:
                    posi.pop()
                    posi.pop()
                    ret *= v
                    ret %= MOD
                else:
                    nega.pop()
                    nega.pop()
                    ret *= w
                    ret %= MOD

            else:
                w = nega[-1] * nega[-2]
                nega.pop()
                nega.pop()
                ret *= w
                ret %= MOD

            K -= 2
        else:
            if posi:
                ret *= posi[-1]
                ret %= MOD
            else:
                ret *= nega[0]
                ret %= MOD
            K -= 1

    return ret


def main():
    N, K = map(int, input().split())
    XS = list(map(int, input().split()))
    print(solve(N, K, XS))


T1 = """
4 2
1 2 -3 -4
"""


def test_T1():
    """
    >>> as_input(T1)
    >>> main()
    12
    """


T2 = """
4 3
-1 -2 -3 -4
"""


def test_T2():
    """
    >>> as_input(T2)
    >>> main()
    1000000001
    """


T3 = """
2 1
-1 1000000000
"""


def test_T3():
    """
    >>> as_input(T3)
    >>> main()
    1000000000
    """


T4 = """
10 10
1000000000 100000000 10000000 1000000 100000 10000 1000 100 10 1
"""


def test_T4():
    """
    >>> as_input(T4)
    >>> main()
    999983200
    """


def _test():
    import doctest
    doctest.testmod()


T5 = """
3 2
1 1 -1
"""


def test_T5():
    """
    >>> as_input(T5)
    >>> main()
    1
    """


T6 = """
3 2
1 -1 -1
"""


def test_T6():
    """
    >>> as_input(T6)
    >>> main()
    1
    """


T7 = """
3 2
2 -1 -1
"""


def test_T7():
    """
    >>> as_input(T7)
    >>> main()
    1
    """


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
        _test()
        sys.exit()
    elif sys.argv[-1] != '-p' and len(sys.argv) == 2:
        # input given as file
        input_as_file = open(sys.argv[1])
        input = input_as_file.buffer.readline
        read = input_as_file.buffer.read

    main()
