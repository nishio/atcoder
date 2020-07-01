#!/usr/bin/env python3

from collections import defaultdict
from heapq import heappush, heappop
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.buffer.readline
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")


def debug(*x):
    print(*x)


def solve(S, T):
    sizeS = len(S)
    sizeT = len(T)
    m = [[0] * (sizeT + 1) for _i in range(sizeS + 1)]
    for i in range(1, sizeS + 1):
        for j in range(1, sizeT + 1):
            m[i][j] = max(
                m[i - 1][j],
                m[i][j - 1],
                m[i - 1][j - 1] + 1 if S[i - 1] == T[j - 1] else 0
            )
    result = []
    i = sizeS
    j = sizeT
    while i > 0 and j > 0:
        if m[i][j] == m[i - 1][j]:
            i -= 1
        elif m[i][j] == m[i][j - 1]:
            j -= 1
        else:
            result.append(chr(S[i - 1]))
            i -= 1
            j -= 1
    print("".join(reversed(result)))


def main():
    S = input().strip()
    T = input().strip()
    solve(S, T)


def _test():
    """
    >>> solve("axyb", "abyxb")
    axb
    """
    global chr
    import doctest
    def chr(x): return x
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
