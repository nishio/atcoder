#!/usr/bin/env python3

from collections import defaultdict
from heapq import heappush, heappop
import sys
import bisect
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
def main(vticks, hticks, vlens, vstarts, v_a, v_b, hlens, hstarts, h_a, h_b):
    total_area = 0
    visited = set()

    maxH = len(hticks) - 2
    maxV = len(vticks) - 2
    # dp(": maxH, maxV", maxH, maxV)
    i = bisect.bisect_left(hticks, 0)
    j = bisect.bisect_left(vticks, 0)
    to_visit = [(i, j)]

    while to_visit:
        i, j = to_visit.pop()
        # dp(": (i,j)", (i, j))
        if i == 0 or i == maxH or j == 0 or j == maxV:
            print("INF")
            break

        if (i, j) in visited:
            return

        # dp("visit: (i,j)", (i, j))
        x = hticks[i]
        y = vticks[j]
        width = hticks[i + 1] - hticks[i]
        height = vticks[j + 1] - vticks[j]
        total_area += width * height
        visited.add((i, j))
        # visit neighbors
        l = i - 1
        if (l, j) not in visited:
            for k in range(vstarts[i], vstarts[i] + vlens[i]):
                if v_a[k] <= y < v_b[k]:
                    # blocked
                    break
            else:
                # can move left
                to_visit.append((l, j))

        u = j - 1
        if (i, u) not in visited:
            for k in range(hstarts[j], hstarts[j] + hlens[j]):
                if h_a[k] <= x < h_b[k]:
                    # blocked
                    break
            else:
                # can move up
                to_visit.append((i, u))

        r = i + 1
        if (r, j) not in visited:
            for k in range(vstarts[r], vstarts[r] + vlens[r]):
                if v_a[k] <= y < v_b[k]:
                    # blocked
                    break
            else:
                # can move left
                to_visit.append((r, j))

        d = j + 1
        if (i, d) not in visited:
            for k in range(hstarts[d], hstarts[d] + hlens[d]):
                if h_a[k] <= x < h_b[k]:
                    # blocked
                    break
            else:
                # can move up
                to_visit.append((i, d))

        # dp(": to_visit", to_visit)
    else:
        print(total_area)


if sys.argv[-1] == 'ONLINE_JUDGE':
    print("compiling")
    from numba.pycc import CC
    cc = CC('my_module')
    cc.export(
        'main', 'void(i8[:],i8[:],i8[:],i8[:],i8[:],i8[:],i8[:],i8[:],i8[:],i8[:])')(main)
    # b1: bool, i4: int32, i8: int64, double: f8, [:], [:, :]
    cc.compile()
    exit()
else:
    # read parameter
    # A, B = map(int, input().split())
    # from my_module import main
    N, M = map(int, input().split())

    vlines = defaultdict(list)
    hlines = defaultdict(list)
    vticks = {0}
    hticks = {0}

    for i in range(N):
        A, B, C = map(int, input().split())
        vlines[C].append((A, B))
        hticks.add(C)
        vticks.update((A, B))

    for i in range(M):
        D, E, F = map(int, input().split())
        hlines[D].append((E, F))
        vticks.add(D)
        hticks.update((E, F))

    vticks = [-INF] + list(sorted(vticks)) + [INF]
    hticks = [-INF] + list(sorted(hticks)) + [INF]

    def to_array(lines, ticks):
        lens = [len(lines[i]) for i in sorted(ticks)]
        import itertools
        starts = itertools.accumulate([0] + lens)
        value_a = []
        value_b = []
        for k in sorted(lines):
            for A, B in lines[k]:
                value_a.append(A)
                value_b.append(B)
        return map(np.array, (
            [0] + lens,
            [0] + list(starts),
            value_a,
            value_b
        ))

    main(np.array(vticks), np.array(hticks),
         *to_array(vlines, vticks), *to_array(hlines, hticks))
