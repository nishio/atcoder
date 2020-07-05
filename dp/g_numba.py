#!/usr/bin/env python3

from collections import defaultdict
from heapq import heappush, heappop
import sys
import numpy as np

sys.setrecursionlimit(10**6)
input = sys.stdin.buffer.readline
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")


def debug(*x):
    print(*x)


def get_longest(start, values, next, head, longest):
    ret = longest[start]
    if ret != -1:
        return ret

    ret = 0
    p = head[start]
    while p:
        v = values[p]
        x = get_longest(v, values, next, head, longest) + 1
        if x > ret:
            ret = x
        p = next[p]

    longest[start] = ret
    return ret


def solve(N, M, data):
    longest = np.repeat(-1, N + 1)

    values = np.zeros(M + 1, np.int32)
    next = np.zeros(M + 1, np.int32)
    head = np.zeros(N + 1, np.int32)
    p = 1
    for i in range(0, 2 * M, 2):
        v1 = data[i]
        v2 = data[i + 1]
        values[p] = v2
        next[p] = head[v1]
        head[v1] = p
        p += 1

    for i in range(N + 1):
        if head[i] == 0:
            longest[i] = 0

    ret = 0
    for v in range(N + 1):
        x = get_longest(v, values, next, head, longest)
        if x > ret:
            ret = x
    return ret


def main():
    N, M = map(int, input().split())
    data = np.int32(read().split())
    print(solve(N, M, data))


T1 = """
4 5
1 2
1 3
3 2
2 4
3 4
"""

T2 = """
6 3
2 3
4 5
5 6
"""

T3 = """
5 8
5 3
2 3
2 4
5 2
5 1
1 4
4 3
1 3
"""


def _test():
    """
    # >>> as_input(T1)
    # >>> main()
    # 3

    # >>> as_input(T2)
    # >>> main()
    # 2

    >>> as_input(T3)
    >>> main()
    3
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
    import numba
    cc = CC('my_module')
    cc.export(
        'solve',
        "i4(i4,i4,i4[:])")(solve)
    cc.export(
        'get_longest',
        "i4(i4,i4[:],i4[:],i4[:],i4[:])")(get_longest)
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
