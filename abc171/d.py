#!/usr/bin/env python3

from collections import defaultdict
from heapq import heappush, heappop
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.buffer.readline
# INF = sys.maxsize
INF = 10 ** 10
# INF = float("inf")

count = [0] * (10 ** 5 + 10)


def dp(*x):  # debugprint
    print(*x)


def main():
    N = int(input())
    AS = map(int, input().split())
    sum = 0
    for a in AS:
        count[a] += 1
        sum += a
    Q = int(input())
    for q in range(Q):
        B, C = map(int, input().split())
        sum += (C - B) * count[B]
        count[C] += count[B]
        count[B] = 0
        print(sum)


def _test():
    import doctest
    doctest.testmod()


if __name__ == "__main__":
    import sys
    argv = sys.argv
    if len(sys.argv) == 1:
        # no option
        main()
    elif sys.argv[1] == "-t":
        _test()
    else:
        input = open(sys.argv[1]).buffer.readline
