#!/usr/bin/env python3
import pprint
N = int(input())
M = [[
    min(i, N + 1 - i, j, N + 1 - j) - 1
    for i in range(N + 2)] for j in range(N + 2)]


def id2pos(i):
    "i: 1-origin"
    i -= 1
    x = i % N
    y = i // N
    return (y + 1, x + 1)


PS = [int(x) for x in input().split()]
cost = 0
for p in PS:
    i, j = id2pos(p)
    cost += M[i][j]
    # update
    m = min(M[i + 1][j], M[i - 1][j], M[i][j + 1], M[i][j - 1])
    M[i + 1][j] = min(m + 1, M[i + 1][j])
    M[i - 1][j] = min(m + 1, M[i - 1][j])
    M[i][j + 1] = min(m + 1, M[i][j + 1])
    M[i][j - 1] = min(m + 1, M[i][j - 1])
    pprint.pprint(M)
print(cost)
