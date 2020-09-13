#!/usr/bin/env python3
import sys


def floor_sum(n, m, a, b):
    ret = 0
    while True:
        if a >= m:
            ret += (a // m) * (n - 1) * n // 2
            a %= m
        if b >= m:
            ret += n * (b // m)
            b %= m
        if a * n + b < m:
            return ret
        y_max = (a * n + b) // m
        x_max = y_max * m - b
        ret += (n - (x_max + a - 1) // a) * y_max
        n, m, a, b = y_max, a, m, -x_max % a


input = sys.stdin.buffer.readline

T = int(input())
for _t in range(T):
    N, M, A, B = map(int, input().split())
    print(floor_sum(N, M, A, B))
