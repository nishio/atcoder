#!/usr/bin/env python3
import sys
import numpy as np

from collections import defaultdict
from heapq import heappush, heappop
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.buffer.readline
# INF = sys.maxsize
INF = 10 ** 9 + 1
# INF = float("inf")


def debug(*x):
    print(*x)


def solve():
    "void()"
    pass


def main():
    N, M = map(int, input().split())
    from scipy.sparse import lil_matrix
    from scipy.sparse.csgraph import dijkstra
    graph = lil_matrix((N + 1, N + 1), dtype=np.int32)
    for i in range(M):
        v1, v2 = map(int, input().split())
        graph[v1, v2] = 1
        graph[v2, v1] = 1

    start = int(input())
    K = int(input())
    targets = list(map(int, input().split()))

    dist = dijkstra(graph)
    # debug(dist)

    costmemo = {}
    visited = 0
    t2i = {targets[i]: i for i in range(len(targets))}

    def f(visited, last):
        # debug(": visited, last", visited, last)
        if (visited, last) in costmemo:
            return costmemo[(visited, last)]

        mask = 1 << (t2i[last])
        buf = []
        prev = visited ^ mask
        if not prev:
            # it is first vertex
            c = dist[start, last]
            costmemo[(visited, last)] = c
            return c

        for v in targets:
            # debug(":: v", v)
            vmask = 1 << (t2i[v])
            # debug(":: vmask", vmask)
            if prev & vmask:  # v is in visited - last
                buf.append(
                    f(prev, v) + dist[v, last]
                )
        c = min(buf)
        costmemo[(visited, last)] = c
        return c

    fullbits = (1 << len(targets)) - 1
    print(int(min(f(fullbits, last) for last in targets)))
    # print(costmemo)
    solve()


def _test():
    import doctest
    doctest.testmod()
    as_input("""3 2
1 2
2 3
2
2
1 3 """)
    main()
    as_input("""
    5 5
1 2
1 3
1 4
1 5
2 3
1
3
2 3 5
""")
    main()


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
