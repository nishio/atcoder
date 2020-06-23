#!/usr/bin/env python3

from collections import defaultdict
from heapq import heappush, heappop
import sys
import numpy as np
import numba

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


@numba.jit
def bisect_left(a, x):
    """Return the index where to insert item x in list a, assuming a is sorted.
    The return value i is such that all e in a[:i] have e <= x, and all e in
    a[i:] have e > x.  So if x already appears in the list, a.insert(x) will
    insert just after the rightmost x already there.
    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """
    lo = 0
    hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        # Use __lt__ to match the logic in list.sort() and in heapq
        if x < a[mid]:
            hi = mid
        else:
            lo = mid+1
    return lo


def main(vticks, hticks, vlines, hlines):
    total_area = 0
    visited = set()

    maxH = len(hticks) - 2
    maxV = len(vticks) - 2
    # dp(": maxH, maxV", maxH, maxV)
    i = bisect_left(hticks, 0)
    j = bisect_left(vticks, 0)
    to_visit = [(i, j)]

    while to_visit:
        i, j = to_visit.pop()
        # dp(": (i,j)", (i, j))
        if i == 0 or i == maxH or j == 0 or j == maxV:
            print("INF")
            break

        if (i, j) in visited:
            continue

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
            for a, b in vlines[x]:
                if a <= y < b:
                    # blocked
                    break
            else:
                # can move left
                to_visit.append((l, j))

        u = j - 1
        if (i, u) not in visited:
            for a, b in hlines[y]:
                if a <= x < b:
                    # blocked
                    break
            else:
                # can move up
                to_visit.append((i, u))

        r = i + 1
        if (r, j) not in visited:
            for a, b in vlines[hticks[r]]:
                if a <= y < b:
                    # blocked
                    break
            else:
                # can move left
                to_visit.append((r, j))

        d = j + 1
        if (i, d) not in visited:
            for a, b in hlines[vticks[d]]:
                if a <= x < b:
                    # blocked
                    break
            else:
                # can move up
                to_visit.append((i, d))

        # dp(": to_visit", to_visit)
    else:
        print(total_area)


if sys.argv[-1] == 'ONLINE_JUDGE' or sys.argv[-1] == '-c':
    print("compiling")
    from numba.pycc import CC
    cc = CC('my_module')
    cc.export(
        'main',
        "void(i8[:], i8[:], "
        "DictType(int64,ListType(UniTuple(int64,2))),"
        "DictType(int64,ListType(UniTuple(int64,2))))")(main)
    # b1: bool, i4: int32, i8: int64, double: f8, [:], [:, :]
    cc.compile()
    exit()
else:
    if sys.argv[-1] != '-p':
        # -p: pure python mode
        # if not -p, import compiled module
        from my_module import main

    # read parameter
    import numba
    N, M = map(int, input().split())

    vlines = defaultdict(lambda: [(0, 0)])
    hlines = defaultdict(lambda: [(0, 0)])
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

    vticks = [-INF] + list(sorted(vticks)) + [INF, INF]
    hticks = [-INF] + list(sorted(hticks)) + [INF, INF]

    d = numba.typed.Dict()
    for k in hticks:
        d[k] = numba.typed.List()
        d[k].extends(vlines[k])
    vlines = d

    d = numba.typed.Dict()
    for k in vticks:
        d[k] = numba.typed.List()
        d[k].extends(hlines[k])
    hlines = d

    main(
        np.array(vticks), np.array(hticks),
        vlines, hlines
    )
