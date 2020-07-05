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
        ret = 0
        for v in edges[start]:
            x = get_longest(v, edges, longest) + 1
            if x > ret:
                ret = x
    # longest[start] = ret
    # return ret
    return 1


def main():
    edges = {1: []}
    cdef array.array longest = pyarray.array('l', [-1] * 10)
    return max(get_longest(v, edges, longest) for v in edges)


main()


cdef foo(int n):
    if n == 0:
        return 0
    return foo(n - 1) + n

print(foo(10))
