#!/usr/bin/env python3

from collections import defaultdict
#from heapq import heappush, heappop
#import numpy as np
import sys
from collections import deque

sys.setrecursionlimit(10**6)
input = sys.stdin.buffer.readline
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")

debug_indent = 0


def debug(*x):
    global debug_indent
    x = list(x)
    indent = 0
    if x[0].startswith("enter") or x[0][0] == ">":
        indent = 1
    if x[0].startswith("leave") or x[0][0] == "<":
        debug_indent -= 1
    x[0] = "  " * debug_indent + x[0]
    print(*x, file=sys.stderr)
    debug_indent += indent


def solve(N, M, edges):
    # convert bidirectional graph to tree
    root = 1
    parent = [-1] * (N + 1)
    to_visit = deque([root])
    bfs_visited_order = []
    while to_visit:
        cur = to_visit.popleft()
        bfs_visited_order.append(cur)
        for child in edges[cur]:
            if child == parent[cur]:
                continue
            parent[child] = cur
            edges[child].remove(cur)  # remove back-link
            to_visit.append(child)

    # up-edge: v -> parent[v]
    # default: if no child, one black, one white (1 + 1)
    # f(x) = prod(f(c) for c in children) + 1
    upedge = [0] * (N + 1)
    # stores multiply result (1 is unity)
    multiply_of_upedge = [1] * (N + 1)
    for cur in reversed(bfs_visited_order[1:]):
        # visit vertexes except root, in reversed order
        upedge[cur] = multiply_of_upedge[cur] + 1
        p = parent[cur]
        multiply_of_upedge[p] *= upedge[cur]
        multiply_of_upedge[p] %= M
    # root: multiply children and don't add one
    # the one is "all-white" pattern
    upedge[root] = multiply_of_upedge[root]
    final_result = upedge[:]

    # down-edge: parent[v] -> v
    downedge = [1] * (N + 1)
    for cur in bfs_visited_order:
        prod = 1
        # left-to-right accumlated products (* downedge[cur])
        for child in edges[cur]:
            downedge[child] = prod
            prod *= upedge[child]
            prod %= M
        # multiply right-to-left accumlated products
        prod = 1
        for child in reversed(edges[cur]):
            downedge[child] = (downedge[cur] * downedge[child] * prod) % M + 1
            prod *= upedge[child]
            prod %= M

        for child in edges[cur]:
            # update final result
            final_result[child] = (
                multiply_of_upedge[child]
                * downedge[child]) % M

    return final_result[1:]


def main():
    # parse input
    N, M = map(int, input().split())
    edges = defaultdict(list)
    for i in range(N - 1):
        x, y = map(int, input().split())
        edges[x].append(y)
        edges[y].append(x)

    #print(*solve(N, M, edges), sep="\n")
    for x in solve(N, M, edges):
        print(x)


# tests
T1 = """
3 100
1 2
2 3
"""


def test_T1():
    """
    >>> as_input(T1)
    >>> main()
    3
    4
    3
    """


T2 = """
4 100
1 2
1 3
1 4
"""


def test_T2():
    """
    >>> as_input(T2)
    >>> main()
    8
    5
    5
    5
    """


T3 = """
1 100
"""


def test_T3():
    """
    >>> as_input(T3)
    >>> main()
    1
    """


T4 = """
10 2
8 5
10 8
6 5
1 5
4 8
2 10
3 6
9 2
1 7
"""


def test_T4():
    """
    >>> as_input(T4)
    >>> main()
    0
    0
    1
    1
    1
    0
    1
    0
    1
    1
    """


# def test_T5():
#     """
#     >>> edges = defaultdict(list)
#     >>> for i in range(100000 - 1):
#     ...     edges[i + 1].append(i + 2)
#     ...     edges[i + 2].append(i + 1)
#     >>> solve(100000, 5, edges)
#     """
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
