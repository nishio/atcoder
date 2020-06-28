#!/usr/bin/env python3
import sys
from itertools import accumulate
import numba
import numpy as np


def debug(*x):
    print(*x)


@numba.njit
def solve(N, M, K, sA, sB):
    "void()"

    last_can_read = 0
    for ij in range(1, N + M + 2):
        # debug(": ij", ij)
        for i in range(0, ij + 1):
            j = ij - i
            # debug(": i,j", i, j)
            if j > M:
                # debug("cont: ", )
                continue
            if i > N:
                # debug("break: ", )
                break
            cost = sA[i] + sB[j]
            # debug(": cost", cost)
            if cost <= K:
                # can read
                # debug("can read: ", i, j, cost)
                last_can_read = ij
                break
        else:
            # no break = can't read
            break

    print(last_can_read)


def main():
    N, M, K = map(int, input().split())

    AS = list(map(int, input().split()))
    BS = list(map(int, input().split()))

    sA = np.array([0] + list(accumulate(AS)))
    sB = np.array([0] + list(accumulate(BS)))
    # debug("s:sA,sB", sA, sB)
    solve(N, M, K, sA, sB)


def _test():
    """
    >>> 
    >>> main()
    """
    import doctest
    as_input('''
    3 4 240
    60 90 120
    80 150 80 150
    ''')
    main()
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
