"""
Simple Cython
"""
from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)


def solve(N, M, edges):
    longest = {}

    def get_longest(start):
        if start in longest:
            return longest[start]

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
