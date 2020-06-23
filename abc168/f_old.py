#!/usr/bin/env python3

from collections import defaultdict
from heapq import heappush, heappop
import sys
import bisect

sys.setrecursionlimit(10**6)
input = sys.stdin.buffer.readline
# INF = sys.maxsize
INF = 10 ** 10
# INF = float("inf")


def dp(*x):  # debugprint
    print(*x)


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

vticks = [-INF] + list(sorted(vticks)) + [INF, INF]
hticks = [-INF] + list(sorted(hticks)) + [INF, INF]


def up(y):
    return vticks[bisect.bisect_left(vticks, y) - 1]


def down(y):
    return vticks[bisect.bisect_left(vticks, y) + 1]


def left(x):
    return hticks[bisect.bisect_left(hticks, x) - 1]


def right(x):
    return hticks[bisect.bisect_left(hticks, x) + 1]


def area(x, y):
    i = bisect.bisect_left(hticks, x)
    width = hticks[i + 1] - hticks[i]
    j = bisect.bisect_left(vticks, y)
    height = vticks[j + 1] - vticks[j]
    return width * height


total_area = 0
visited = set()


def visit(x, y):
    global total_area
    if (x, y) in visited:
        return
    # dp("visited: x,y", x, y)
    a = area(x, y)
    total_area += a
    visited.add((x, y))
    # visit neighbors
    l = left(x)
    if (l, y) not in visited:
        for a, b in vlines[x]:
            if a <= y < b:
                # blocked
                break
        else:
            # can move left
            to_visit.append((l, y))

    u = up(y)
    if (x, u) not in visited:
        for a, b in hlines[y]:
            if a <= x < b:
                # blocked
                break
        else:
            # can move up
            to_visit.append((x, u))

    r = right(x)
    if (r, y) not in visited:
        for a, b in vlines[r]:
            if a <= y < b:
                # blocked
                break
        else:
            # can move left
            to_visit.append((r, y))

    d = down(y)
    if (x, d) not in visited:
        for a, b in hlines[d]:
            if a <= x < b:
                # blocked
                break
        else:
            # can move up
            to_visit.append((x, d))


to_visit = [(0, 0)]
while to_visit:
    x, y = to_visit.pop()
    if x == INF or x == -INF or y == INF or y == -INF:
        print("INF")
        break
    visit(x, y)
else:
    print(total_area)
