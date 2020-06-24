#!/usr/bin/env python3

from heapq import heappush, heappop
import sys
import numpy as np

sys.setrecursionlimit(10**6)
input = sys.stdin.buffer.readline
# INF = sys.maxsize
INF = 10 ** 10
# INF = float("inf")


def dp(*x):  # debugprint
    print(*x)


try:
    profile
except:
    def profile(f): return f


@profile
def main(N, M, data):
    # vlines = defaultdict(lambda: [(0, 0)])
    vlines = {}
    # hlines = defaultdict(lambda: [(0, 0)])
    hlines = {}
    # vticks = {0}
    vticks = {0}
    # hticks = {0}
    hticks = {0}

    ABC = data[:3 * N]
    DEF = data[3 * N:]
    A, B, C = [ABC[i::3] for i in range(3)]
    D, E, F = [DEF[i::3] for i in range(3)]

    xticks = np.unique(np.concatenate((E, F, C, np.array([-INF, 0, INF]))))
    yticks = np.unique(np.concatenate((A, B, D, np.array([-INF, 0, INF]))))
    width = xticks[1:] - xticks[:-1]
    height = yticks[1:] - yticks[:-1]

    # compress
    A = np.searchsorted(yticks, A)
    B = np.searchsorted(yticks, B)
    C = np.searchsorted(xticks, C)
    D = np.searchsorted(yticks, D)
    E = np.searchsorted(xticks, E)
    F = np.searchsorted(xticks, F)

    GRAPH_WIDTH = len(xticks)
    GRAPH_HEIGHT = len(yticks)
    NUM_VERTEXES = GRAPH_HEIGHT * GRAPH_WIDTH

    ng_egdes = np.zeros((NUM_VERTEXES, 4), dtype=np.bool_)
    #ng_egdes = csr_matrix((NUM_VERTEXES, 4), dtype=np.bool_)
    direction = (-1, +1, -GRAPH_WIDTH, +GRAPH_WIDTH)

    # vertical lines A,C-B,C
    for i in range(N):
        x = C[i]
        for y in range(A[i], B[i]):
            pos = y * GRAPH_WIDTH + x
            ng_egdes[pos, 0] = 1  # left
            ng_egdes[pos - 1, 1] = 1  # right

    # horizontal lines D,E-D,F
    for i in range(M):
        y = D[i]
        for x in range(E[i], F[i]):
            pos = y * GRAPH_WIDTH + x
            ng_egdes[pos, 2] = 1
            ng_egdes[pos - GRAPH_WIDTH, 3] = 1

    A = B = C = D = E = F = 0

    total_area = 0
    #visited = np.zeros(N)
    visited = set()
    x = np.searchsorted(xticks, 0)
    y = np.searchsorted(yticks, 0)
    start = y * GRAPH_WIDTH + x
    to_visit = [start]

    while to_visit:
        pos = to_visit.pop()
        y, x = divmod(pos, GRAPH_WIDTH)
        if pos in visited:
            continue
        if y == 0 or y == GRAPH_HEIGHT - 1 or x == 0 or x == GRAPH_WIDTH - 1:
            print("INF")
            break

        total_area += width[x] * height[y]
        visited.add(pos)
        # plan to visit neighbors
        for i in range(4):
            if not ng_egdes[pos, i]:
                to_visit.append(pos + direction[i])
    else:
        print(total_area)


if sys.argv[-1] == 'ONLINE_JUDGE' or sys.argv[-1] == '-c':
    print("compiling")
    from numba.pycc import CC
    cc = CC('my_module')
    cc.export(
        'main',
        "void(i4, i4, i4[:])"
    )(main)
    # b1: bool, i4: int32, i8: int64, double: f8, [:], [:, :]
    cc.compile()
    exit()
else:
    if sys.argv[-1] != '-p':
        # -p: pure python mode
        # if not -p, import compiled module
        from my_module import main  # pylint: disable=all

    # read parameter
    import numba
    N, M = map(int, input().split())
    data = np.int32(sys.stdin.read().split())
    main(N, M, data)
