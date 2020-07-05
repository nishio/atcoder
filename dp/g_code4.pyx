#!/usr/bin/env python3
"""
Cython test
"""
from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.buffer.readline
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")

cdef long[100010] longest

cdef get_longest(long start, dict edges):
    if longest[start] != -1:
        return longest[start]

    cdef list next_edges
    next_edges = edges[start]
    ret = 0
    for v in next_edges:
        x = get_longest(v, edges) + 1
        if x > ret:
            ret = x

    longest[start] = ret
    return ret


cdef solve(N, M, edges):
    for i in range(N + 1):
        if not edges.get(i):
            longest[i] = 0
        else:
            longest[i] = -1
    return max(get_longest(v, edges) for v in edges)


def main():
    N, M = map(int, input().split())
    edges = defaultdict(list)
    for i in range(M):
        v1, v2 = map(int, input().split())
        edges[v1].append(v2)

    print(solve(N, M, dict(edges)))


main()
