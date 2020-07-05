#!/usr/bin/env python3
"""
Cython test
"""
from collections import defaultdict
from heapq import heappush, heappop
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.buffer.readline
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")


def debug(*x):
    print(*x)


cdef get_longest(start):
    if longest[start] != -1:
        return longest[start]

    next_edges = edges.get(start)
    if not next_edges:
        ret = 0
    else:
        ret = max(get_longest(v) for v in edges[start]) + 1
    longest[start] = ret
    return ret


def solve(N, M, edges):
    longest = [-1] * (N + 1)

    return max(get_longest(v) for v in edges)


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


def main():
    N, M = map(int, input().split())
    edges = defaultdict(set)
    for i in range(M):
        v1, v2 = map(int, input().split())
        edges[v1].add(v2)

    print(solve(N, M, edges))


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
