#!/usr/bin/env python3
"""
Simple Version
Python TLE https://atcoder.jp/contests/dp/submissions/14906600
PyPy TLE https://atcoder.jp/contests/dp/submissions/14906630
"""
from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)


def solve(N, M, edges):
    longest = [-1] * (N + 1)

    stack = [v for v in edges]

    while stack:
        v = stack.pop()
        if v > 0:
            if v in longest:
                continue
            next_edges = edges.get(v)
            stack.append(-v)
            if next_edges:
                stack.extend(next_edges)
        else:
            next_edges = edges.get(-v)
            if not next_edges:
                ret = 0
            else:
                ret = max(longest[x] for x in next_edges) + 1
            longest[-v] = ret

    return max(longest[v] for v in edges)


def main():
    N, M = map(int, input().split())
    edges = defaultdict(set)
    for i in range(M):
        v1, v2 = map(int, input().split())
        edges[v1].add(v2)

    print(solve(N, M, edges))


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
