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
    for i in range(N + 1):
        if not edges[i]:
            longest[i] = 0

    def get_longest(start):
        ret = longest[start]
        if ret != -1:
            return ret

        next_edges = edges.get(start)
        if not next_edges:
            ret = 0
        else:
            ret = max(get_longest(v) for v in edges[start]) + 1
        longest[start] = ret
        return ret

    return max(get_longest(v) for v in edges)


def main():
    N, M = map(int, input().split())
    edges = defaultdict(set)
    for i in range(M):
        v1, v2 = map(int, input().split())
        edges[v1].add(v2)

    print(solve(N, M, edges))


main()
