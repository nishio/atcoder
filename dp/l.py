#!/usr/bin/env python3

#from collections import defaultdict
#from heapq import heappush, heappop
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.buffer.readline
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")


def debug(*x):
    print(*x, file=sys.stderr)



def solve(N, XS):
    global memo
    memo = [0] * (N * N)
    global done
    done = [False] * (N * N)

    def first(L, R):
        # debug(": L, R", L, R)
        if L == R:
            return XS[L]
        pos = L * N + R
        if done[pos + N]:
            right = memo[pos + N]
        else:
            right = first(L + 1, R)

        if done[pos - 1]:
            left = memo[pos - 1]
        else:
            left = first(L, R - 1)

        ret = max(
            XS[L] - right,
            XS[R] - left
        )
        memo[pos] = ret
        done[pos] = True
        return ret

    return first(0, N - 1)


def main():
    # parse input
    N = int(input())
    XS = list(map(int, input().split()))
    print(solve(N, XS))


# tests
T1 = """
4
10 80 90 30
"""


def test_T1():
    """
    >>> as_input(T1)
    >>> main()
    10
    """


T2 = """
3
10 100 10
"""


def test_T2():
    """
    >>> as_input(T2)
    >>> main()
    -80
    """


T3 = """
1
10
"""


def test_T3():
    """
    >>> as_input(T3)
    >>> main()
    10
    """


T4 = """
10
1000000000 1 1000000000 1 1000000000 1 1000000000 1 1000000000 1
"""


def test_T4():
    """
    >>> as_input(T4)
    >>> main()
    4999999995
    """


T5 = """
6
4 2 9 7 1 5
"""


def test_T5():
    """
    >>> as_input(T5)
    >>> main()
    2
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
