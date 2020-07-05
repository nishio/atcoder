#!/usr/bin/env python3
"""
Cython test
"""
from collections import defaultdict
import sys
from cpython cimport array
import array as pyarray

sys.setrecursionlimit(10**6)
input = sys.stdin.buffer.readline
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")


cdef get_longest(long start, dict edges, long[:] longest):
    if longest[start] != -1:
        return longest[start]

    cdef list next_edges
    next_edges = edges.get(start)
    if not next_edges:
        ret = 0
    else:
        #ret = max(get_longest(v, edges, longest) for v in edges[start]) + 1
        ret = 0
        for v in edges[start]:
            x = get_longest(v, edges, longest) + 1
            if x > ret:
                ret = x

    longest[start] = ret
    return ret


def solve(N, M, edges):
    cdef array.array longest = pyarray.array('l', [-1] * (N + 1))
    return max(get_longest(v, edges, longest) for v in edges)


def main():
    N, M = map(int, input().split())
    edges = defaultdict(list)
    for i in range(M):
        v1, v2 = map(int, input().split())
        edges[v1].append(v2)

    print(solve(N, M, dict(edges)))


main()
