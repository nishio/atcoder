#!/usr/bin/env python3
import pprint
from collections import defaultdict
N = int(input())
edges = defaultdict(set)
for i in range(1, N * N + 1):
    e = []
    if i <= N:
        e.append(0)
    else:
        e.append(i - N)

    if i % N == 0:
        e.append(0)
    else:
        e.append(i + 1)

    if i % N == 1:
        e.append(0)
    else:
        e.append(i - 1)

    if i > N * (N - 1):
        e.append(0)
    else:
        e.append(i + N)
    e = set(e)
    for v in e:
        edges[v].add(i)
        edges[i].add(v)

# print(edges)
vcost = {0: -1}
front = [0]
cost = 0
while front:
    newFront = []
    for p in front:
        for n in edges[p]:
            if n not in vcost:
                vcost[n] = cost
                newFront.append(n)
    front = newFront
    cost += 1

# print(vcost)


def update(xs, newcost):
    for x in xs:
        if vcost[x] > newcost:
            vcost[x] = newcost
            update(edges[x], newcost + 1)


PS = [int(x) for x in input().split()]
cost = 0
for p in PS:
    cost += vcost[p]
    newcost = min(vcost[i] for i in edges[p]) + 1
    update(edges[p], newcost)
    for n in edges[p]:
        edges[n].update(edges[p])

print(cost)
