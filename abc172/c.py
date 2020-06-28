#!/usr/bin/env python3
import sys
from itertools import accumulate
import numba
import numpy as np


def debug(*x):
    print(*x)


# @numba.njit
# def solve(N, M, K, sA, sB):
#     "void()"

#     last_can_read = 0
#     for i in range(N + 1):
#         for j in range(M + 1):
#             if sA[i] + sB[j] <= K:
#                 if last_can_read < i + j:
#                     last_can_read = i + j
#             else:
#                 break

#     print(last_can_read)


@numba.njit
def solve(N, M, K, sA, sB):
    max_can_read = 0
    last_max_j = M
    for i in range(N + 1):
        j = last_max_j
        while j >= 0:
            if sA[i] + sB[j] <= K:
                if max_can_read < i + j:
                    max_can_read = i + j
                last_max_j = j
                break
            j -= 1

    print(max_can_read)


def main():
    N, M, K = map(int, input().split())

    AS = list(map(int, input().split()))
    BS = list(map(int, input().split()))

    sA = np.array([0] + list(accumulate(AS)))
    sB = np.array([0] + list(accumulate(BS)))
    # debug("s:sA,sB", sA, sB)
    solve(N, M, K, sA, sB)


T1 = '''
3 4 240
60 90 120
80 150 80 150
'''

T2 = '''
3 4 730
60 90 120
80 150 80 150
'''


def _test():
    """
    >>> as_input(T1)
    >>> main()
    3
    >>> as_input(T2)
    >>> main()

    """
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
