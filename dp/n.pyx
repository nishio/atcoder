#!/usr/bin/env python3

#from collections import defaultdict
#from heapq import heappush, heappop
from itertools import accumulate
from functools import lru_cache
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.buffer.readline
INF = sys.maxsize  # float("inf")

cdef long long[400 * 400] table
cdef long long[410] accum

cdef sub(long L, long R):
    cdef long long ret
    if L == R:
        return 0
    ret = table[L * 400 + R]
    if ret != 0:
        return ret

    ret = INF
    for x in range(L, R):
        v = sub(L, x) + sub(x + 1, R)
        if v < ret:
            ret = v
    ret += accum[R + 1] - accum[L]
    table[L * 400 + R] = ret
    return ret

cdef solve(N, XS):
    cdef long i
    cdef long long v
    v = 0
    accum[0] = 0
    for i in range(N):
        v += XS[i]
        accum[i + 1] = v
    return sub(0, N - 1)


def main():
    # parse input
    N = int(input())
    XS = list(map(int, input().split()))
    print(solve(N, XS))


main()
