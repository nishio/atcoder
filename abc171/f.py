#!/usr/bin/env python3

from collections import defaultdict
from heapq import heappush, heappop
import sys


def main(K, N):
    P = 10 ** 9 + 7

    P25 = [1] * (K + 1)
    P26 = [1] * (K + 1)
    F = [1] * (N + K)
    INV = [1] * (N + K)
    INVF = [1] * (N + K)

    p25 = 1
    p26 = 1
    for i in range(1, K + 1):
        p25 *= 25
        p25 %= P
        P25[i] = p25

        p26 *= 26
        p26 %= P
        P26[i] = p26

    f = 1
    invf = 1
    for i in range(2, N + K):
        f *= i
        f %= P
        F[i] = f
        q, r = divmod(P, i)
        INV[i] = -INV[r] * q % P
        invf *= INV[i]
        invf %= P
        INVF[i] = invf

    def comb_rep(n, r):
        return (F[n + r - 1] * INVF[r] % P) * INVF[n - 1] % P

    ret = 0
    for i in range(K + 1):
        ret += (
            P25[i] *
            P26[K - i] % P *
            comb_rep(N, i) % P
        )
    return (ret % P)


if sys.argv[-1] == 'ONLINE_JUDGE':
    print("compiling")
    from numba.pycc import CC
    cc = CC('my_module')
    cc.export('main', 'i8(i8,i8)')(main)
    # b1: bool, i4: int32, i8: int64, double: f8, [:], [:, :]
    cc.compile()
    exit()
else:
    # read parameter
    from my_module import main
    # K = int(input())
    # S = input()
    # print(main(K, len(S)))
    print(main(10 ** 6, 10 ** 6))
