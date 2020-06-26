#!/usr/bin/env python3
from collections import defaultdict
import pprint
import numpy as np
from heapq import heappush, heappop
N = int(input())
PS = [int(x) for x in input().split()]


person = [1] * (N * N)


def search(start):
    to_visit = [start]
    next_visit = []
    visited = [0] * (N * N)
    cost = 0
    while to_visit:
        while to_visit:
            p = to_visit.pop()
            if visited[p]:
                continue
            visited[p] = 1

            y, x = divmod(p, N)
            if x == 0 or x == (N - 1) or y == 0 or y == (N - 1):
                return cost
            for d in (-1, +1, -N, +N):
                if person[p + d]:
                    next_visit.append(p + d)
                else:
                    to_visit.append(p + d)
        to_visit = next_visit
        next_visit = []
        cost += 1


total_cost = 0
for p in PS:
    # print(p)
    p -= 1  # 0-origin
    total_cost += search(p)
    person[p] = 0
    # print("t", total_cost)

print(total_cost)
