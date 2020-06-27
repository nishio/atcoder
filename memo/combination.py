"""
Power, Inverse, Factorial, InvFactorial, Combination

best solution:

- Power: makePowerTableMaspyNumba 13msec
- Inverse: makeInverseTableNumba 47msec
- Factorial: makeFactorialTableMaspyNumba: 13msec (K is excluded)
- ...: makeFactorialTableMaspy2Numba: 13msec (K is included, x! == ret[n-1])
- InvFactorial: makeInvFactoTableMaspyOriginalNumba 17msec (Need to give (K - 1)!) 
- ...: makeInvFactoTableWoInvNumba: 53msec
- Combination: makeCombibationTableJointedNumba: 35msec (if you need C(n, r) for specific n)
- ...: makeCombibationTableMaspy: 19msec (need f and invf. 13 + 17 + 19 = 49msec)


"""

import numpy as np
import sys
import numba
import math

MOD = 10 ** 9 + 7
K = 10 ** 6


def makePowerTable(x, K=K, MOD=MOD):
    """calc x^i for i in [0, K] mod MOD
    >>> xs = makePowerTable(2, 20, 1000)
    >>> xs
    [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 24, 48, 96, 192, 384, 768, 536, 72, 144, 288, 576]
    >>> xs == [pow(2, i, 1000) for i in range(21)]
    True

    %timeit makePowerTable(23)
    165 ms ± 1.5 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
    166 ms ± 536 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)

    Numba-jit-ed
    %timeit makePowerTableNumba(23)
    45 ms ± 546 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)
    48.7 ms ± 3.12 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
    """
    ret = [1] * (K + 1)
    cur = 1
    for i in range(1, K + 1):
        cur *= x
        cur %= MOD
        ret[i] = cur
    return ret


makePowerTableNumba = numba.njit(makePowerTable)


def makePowerTableBin(x, K=K, MOD=MOD):
    """calc x^i for i in [1, K] mod MOD, K should be power of 2
    >>> xs = list(makePowerTableBin(2, 16, 1000))
    >>> xs
    [2, 4, 8, 16, 32, 64, 128, 256, 512, 24, 48, 96, 192, 384, 768, 536]
    >>> xs == [pow(2, i, 1000) for i in range(1, 17)]
    True

    %timeit makePowerTableBin(23)
    199 ms ± 2.11 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

    %timeit makePowerTableBinNumba(23)
    79.5 ms ± 4.84 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
    """
    ret = np.repeat(x, K)
    w = K // 2
    ret[w:] *= x
    w //= 2
    while w:
        ret[w:] *= ret[: - w]
        ret %= MOD
        w //= 2

    return ret


makePowerTableBinNumba = numba.njit(makePowerTableBin)


def makePowerTableMaspy(x, K=K, MOD=MOD):
    """calc x^i for i in [1, K] mod MOD, K should be power of 2
    >>> xs = list(makePowerTableMaspy(2, 16, 1000))
    >>> xs
    [2, 4, 8, 16, 32, 64, 128, 256, 512, 24, 48, 96, 192, 384, 768, 536]
    >>> xs == [pow(2, i, 1000) for i in range(1, 17)]
    True

    %timeit makePowerTableMaspy(23)
    36.3 ms ± 597 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)

    %timeit makePowerTableMaspyNumba(23)
    13 ms ± 748 µs per loop (mean ± std. dev. of 7 runs, 1 loop each)
    """
    rootK = math.ceil(math.sqrt(K))
    ret = np.repeat(x, K).reshape(rootK, rootK)
    for n in range(1, rootK):
        ret[:, n] *= ret[:, n-1]
        ret[:, n] %= MOD
    for n in range(1, rootK):
        ret[n] *= ret[n-1, -1]
        ret[n] %= MOD
    ret = ret.ravel()
    return ret


makePowerTableMaspyNumba = numba.njit(makePowerTableMaspy)


def makeInverseTable(K=K, MOD=MOD):
    """calc i^-1 for i in [1, K] mod MOD. MOD should be prime
    >>> invs = makeInverseTable(10)
    >>> [i * invs[i] % MOD for i in range(1, 10)]
    [1, 1, 1, 1, 1, 1, 1, 1, 1]

    %timeit makeInverseTable()
    516 ms ± 26.6 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
    525 ms ± 19.5 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

    Numba-jit-ed
    %timeit makeInverseTableNumba()
    47 ms ± 765 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)
    45.9 ms ± 1.98 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
    """
    ret = [1] * (K + 1)
    for i in range(2, K + 1):
        q, r = divmod(MOD, i)
        ret[i] = -ret[r] * q % MOD
    return ret


makeInverseTableNumba = numba.njit(makeInverseTable)


def getSingleInverse(a, MOD=MOD):
    """
    get single inverse. O(log N).
    >>> [getSingleInverse(x) for x in range(1, 11)] ==  makeInverseTable(10)[1:]
    True

    %timeit getSingleInverse(1000)
    984 ns ± 10.4 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
    953 ns ± 15 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

    %timeit [getSingleInverse(x) for x in range(1, K + 1)]
    2.46 s ± 9.9 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
    2.55 s ± 26.1 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

    %timeit getSingleInverseNumba(1000)
    15.7 µs ± 278 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

    %timeit [getSingleInverseNumba(x) for x in range(1, K + 1)]
    16.6 s ± 1.3 s per loop (mean ± std. dev. of 7 runs, 1 loop each)

    """
    b = MOD
    u = 1
    v = 0
    while b:
        t = a // b
        a -= t * b
        a, b = b, a
        u -= t * v
        u, v = v, u
    u %= MOD
    return u


getSingleInverseNumba = numba.njit(getSingleInverse)


def makeFactorialTable(K=K, MOD=MOD):
    """calc i! for i in [0, K] mod MOD. MOD should be prime
    >>> fs = makeFactorialTable(10, 23)
    >>> fs
    [1, 1, 2, 6, 1, 5, 7, 3, 1, 9, 21]
    >>> import math
    >>> fs == [math.factorial(i) % 23 for i in range(11)]
    True

    %timeit makeFactorialTable()
    163 ms ± 805 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)
    169 ms ± 1.97 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)

    %timeit makeFactorialTableNumba()
    45 ms ± 1.18 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
    46.1 ms ± 1.43 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
    """
    ret = [1] * (K + 1)
    cur = 1
    for i in range(2, K + 1):
        cur *= i
        cur %= MOD
        ret[i] = cur
    return ret


makeFactorialTableNumba = numba.njit(makeFactorialTable)


def makeFactorialTableMaspy(K=K, MOD=MOD):
    """calc i! for i in [0, K) mod MOD.
    MOD should be prime, K should be squared number.
    *NOTICE* K is not included.
    see https://maspypy.com/numpyn-mod-p%e3%81%ae%e8%a8%88%e7%ae%97

    >>> xs = makeFactorialTableMaspy(100, 23)[:11]
    >>> xs
    array([ 1,  1,  2,  6,  1,  5,  7,  3,  1,  9, 21])
    >>> xs.tolist() == makeFactorialTable(10, 23)
    True

    %timeit makeFactorialTableMaspy()
    35.1 ms ± 582 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)
    33.6 ms ± 1.08 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)

    Numba-jit-ed
    %timeit makeFactorialTableMaspyNumba()
    14 ms ± 1.18 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
    12.3 ms ± 782 µs per loop (mean ± std. dev. of 7 runs, 1 loop each)
    """
    rootK = math.ceil(math.sqrt(K))

    ret = np.arange(K, dtype=np.int64).reshape(rootK, rootK)
    ret[0, 0] = 1
    for n in range(1, rootK):
        ret[:, n] *= ret[:, n-1]
        ret[:, n] %= MOD
    for n in range(1, rootK):
        ret[n] *= ret[n-1, -1]
        ret[n] %= MOD
    ret = ret.ravel()

    return ret


makeFactorialTableMaspyNumba = numba.njit(makeFactorialTableMaspy)


def makeFactorialTableMaspy2(K=K, MOD=MOD):
    """calc i! for i in [1, K] mod MOD.
    MOD should be prime, K should be squared number.
    see https://maspypy.com/numpyn-mod-p%e3%81%ae%e8%a8%88%e7%ae%97

    >>> xs = makeFactorialTableMaspy2(100, 23)[:11]
    >>> xs
    array([ 1,  2,  6,  1,  5,  7,  3,  1,  9, 21,  1])
    >>> xs.tolist() == makeFactorialTable(11, 23)[1:]
    True

    %timeit makeFactorialTableMaspy2()
    32.2 ms ± 601 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)

    Numba-jit-ed
    %timeit makeFactorialTableMaspy2Numba()
    12.5 ms ± 938 µs per loop (mean ± std. dev. of 7 runs, 1 loop each)
    """
    rootK = math.ceil(math.sqrt(K))

    ret = np.arange(1, K + 1, dtype=np.int64).reshape(rootK, rootK)
    ret[0, 0] = 1
    for n in range(1, rootK):
        ret[:, n] *= ret[:, n-1]
        ret[:, n] %= MOD
    for n in range(1, rootK):
        ret[n] *= ret[n-1, -1]
        ret[n] %= MOD
    ret = ret.ravel()

    return ret


makeFactorialTableMaspy2Numba = numba.njit(makeFactorialTableMaspy2)


def makeFactorialTableMaspyNoReshape(K=K, MOD=MOD):
    """calc i! for i in [0, K) mod MOD.
    MOD should be prime, K should be squared number.
    *NOTICE* K is not included.
    see https://maspypy.com/numpyn-mod-p%e3%81%ae%e8%a8%88%e7%ae%97

    >>> xs = makeFactorialTableMaspyNoReshape(100, 23)[:11]
    >>> xs
    array([ 1,  1,  2,  6,  1,  5,  7,  3,  1,  9, 21])
    >>> xs.tolist() == makeFactorialTable(10, 23)
    True

    %timeit makeFactorialTableMaspyNoReshape()
    31.4 ms ± 333 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)

    Numba-jit-ed
    %timeit makeFactorialTableMaspyNoReshape()

    %timeit makeFactorialTableMaspyNoReshapeNumba()
    12.3 ms ± 428 µs per loop (mean ± std. dev. of 7 runs, 1 loop each)
    """
    rootK = math.ceil(math.sqrt(K))
    K = rootK ** 2

    ret = np.arange(K, dtype=np.int64)
    ret[0] = 1
    for i in range(1, rootK):
        ret[i::rootK] *= ret[i-1::rootK]
        ret[i::rootK] %= MOD
    for i in range(1, rootK):
        ret[i * rootK:i * rootK + rootK] *= ret[i * rootK - 1]
        ret[i * rootK:i * rootK + rootK] %= MOD

    return ret


makeFactorialTableMaspyNoReshapeNumba = numba.njit(
    makeFactorialTableMaspyNoReshape)


def makeInvFactoTable(inv, K=K, MOD=MOD):
    """calc i!^-1 for i in [0, K] mod MOD. MOD should be prime
    You can not do inv[f[i]], because f[i] may greater than K.

    inv = makeInverseTable()
    %timeit makeInvFactoTable(inv)
    182 ms ± 1.08 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
    189 ms ± 1.56 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)

    inva = np.array(makeInverseTable())
    %timeit makeInvFactoTable(inva)
    329 ms ± 5.22 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
    339 ms ± 4 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
    """
    ret = [1] * (K + 1)
    cur = 1
    for i in range(2, K + 1):
        cur *= inv[i]
        cur %= MOD
        ret[i] = cur
    return ret


@numba.njit
def makeInvFactoTableNumba(inv, K=K, MOD=MOD):
    """calc i!^-1 for i in [0, K] mod MOD. MOD should be prime
    You can not do inv[f[i]], because f[i] may greater than K.

    inva = np.array(makeInverseTable())
    %timeit makeInvFactoTableNumba(inva, K, MOD)
    12.5 ms ± 93.5 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
    """
    ret = np.ones(K + 1, dtype=np.int64)
    cur = 1
    for i in range(2, K + 1):
        cur *= inv[i]
        cur %= MOD
        ret[i] = cur
    return ret


def makeInvFactoTableWoInv(K=K, MOD=MOD):
    """calc i!^-1 for i in [0, K] mod MOD. MOD should be prime.
    You can not do inv[f[i]], because f[i] may greater than K.

    No need to pass inv. Make inv and inv_facto in single loop.

    >>> makeInvFactoTableWoInv(10) == makeInvFactoTable(makeInverseTable(10), 10)
    True

    %timeit makeInvFactoTableWoInv()
    749 ms ± 30.6 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
    729 ms ± 54.4 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

    %timeit makeInvFactoTable(makeInverseTable())
    743 ms ± 22.2 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

    %timeit makeInvFactoTable(makeInverseTableNumba())
    233 ms ± 5.02 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
    226 ms ± 2.4 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

    %timeit makeInvFactoTableNumba(np.array(makeInverseTableNumba()))
    111 ms ± 1.85 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

    %timeit makeInvFactoTableWoInvNumba()
    53.7 ms ± 1.62 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
    53 ms ± 743 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)
    """

    inv = [1] * (K + 1)
    invf = [1] * (K + 1)
    cur = 1
    for i in range(2, K + 1):
        q, r = divmod(MOD, i)
        inv[i] = -inv[r] * q % MOD
        cur *= inv[i]
        cur %= MOD
        invf[i] = cur
    return invf


makeInvFactoTableWoInvNumba = numba.njit(makeInvFactoTableWoInv)


def makeInvFactoTableMaspy(inva, K=K, MOD=MOD):
    """calc i!^-1 for i in [0, K) mod MOD.
    MOD should be prime, K should be squared number.
    *NOTICE* K is not included.
    see https://maspypy.com/numpyn-mod-p%e3%81%ae%e8%a8%88%e7%ae%97

    >>> inva = np.array(makeInverseTable(100))
    >>> list(makeInvFactoTableMaspy(inva, 100)) == makeInvFactoTable(inva, 99)
    True

    %timeit makeInvFactoTableMaspy(np.array(makeInverseTable()))
    612 ms ± 9.57 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
    613 ms ± 14.3 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

    %timeit makeInvFactoTableMaspyNumba(np.array(makeInverseTable()))
    617 ms ± 20.3 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
    """
    rootK = math.ceil(math.sqrt(K))

    ret = inva[np.arange(K, dtype=np.int64)].reshape(rootK, rootK)
    ret[0, 0] = 1
    for n in range(1, rootK):
        ret[:, n] *= ret[:, n-1]
        ret[:, n] %= MOD
    for n in range(1, rootK):
        ret[n] *= ret[n-1, -1]
        ret[n] %= MOD
    ret = ret.ravel()

    return ret


makeInvFactoTableMaspyNumba = numba.njit(makeInvFactoTableMaspy)


def makeInvFactoTableMaspyOriginal(factKm1, K=K, MOD=MOD):
    """calc i!^-1 for i in [0, K) mod MOD.
    MOD should be prime, K should be squared number.
    *NOTICE* K is not included.
    Need to give factKm1 = (K - 1)!

    see https://maspypy.com/numpyn-mod-p%e3%81%ae%e8%a8%88%e7%ae%97

    >>> f = bestFactorial()
    >>> f[99]
    104379182
    >>> xs = list(makeInvFactoTableMaspyOriginal(f[99], 100)[:5])
    >>> xs
    [1, 1, 500000004, 166666668, 41666667]
    >>> xs == makeInvFactoTableWoInvNumba(4)
    True
    >>> list(makeInvFactoTableMaspyOriginalNumba(f[99], 100)) == list(makeInvFactoTableMaspyOriginal(f[99], 100))
    True

    %timeit makeInvFactoTableMaspyOriginal(f[K - 1])
    35.2 ms ± 543 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)
    33.1 ms ± 312 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)

    %timeit makeInvFactoTableMaspyOriginalNumba(f[K - 1])
    16.6 ms ± 2.01 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
    """
    rootK = math.ceil(math.sqrt(K))
    ret = np.arange(1, K + 1, dtype=np.int64)[::-1].reshape(rootK, rootK)
    ret[0, 0] = pow(int(factKm1), MOD-2, MOD)  # inverse of (k-1)!
    for n in range(1, rootK):
        ret[:, n] *= ret[:, n-1]
        ret[:, n] %= MOD
    for n in range(1, rootK):
        ret[n] *= ret[n-1, -1]
        ret[n] %= MOD
    ret = ret.ravel()[::-1]
    return ret


@numba.njit
def makeInvFactoTableMaspyOriginalNumba(factKm1, K=K, MOD=MOD):
    rootK = math.ceil(math.sqrt(K))
    ret = np.ascontiguousarray(
        np.arange(1, K + 1, dtype=np.int64)[::-1]
    ).reshape(rootK, rootK)
    ret[0, 0] = getSingleInverseNumba(factKm1)  # inverse of (k-1)!
    for n in range(1, rootK):
        ret[:, n] *= ret[:, n-1]
        ret[:, n] %= MOD
    for n in range(1, rootK):
        ret[n] *= ret[n-1, -1]
        ret[n] %= MOD
    ret = ret.ravel()[::-1]
    return ret


def combination(n, k, f, invf):
    """combination C(n, k)
    >>> f = makeFactorialTable()
    >>> inv = makeInverseTable()
    >>> invf = makeInvFactoTable(inv)
    >>> [combination(10000, i, f, invf) for i in range(7)]
    [1, 10000, 49995000, 616668838, 709582588, 797500005, 2082363]

    %timeit combination(10000, 100, f, invf)
    814 ns ± 6.5 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
    """
    return f[n] * invf[k] % MOD * invf[n - k] % MOD


def comb_rep(n, k, f, invf):
    """combination with replacement Cr(n, k)
    >>> f = makeFactorialTable()
    >>> inv = makeInverseTable()
    >>> invf = makeInvFactoTable(inv)
    >>> [comb_rep(3, i, f, invf) for i in range(7)]
    [1, 3, 6, 10, 15, 21, 28]

    %timeit comb_rep(10000, 100, f, invf)
    881 ns ± 8.53 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
    """
    return f[n + k - 1] * invf[k] % MOD * invf[n - 1] % MOD


def makeCombibationTable(n, f, invf):
    """make table of C(n, i) for i in [0, N]

    %timeit makeCombibationTable(K, f, invf)
    356 ms ± 10.8 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

    %timeit makeCombibationTable(10000, f, invf)
    7.43 ms ± 60.7 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

    %timeit makeCombibationTableNumba(K, f, invf)
    27.2 ms ± 365 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)
    """
    return [
        f[n] * invf[k] % MOD * invf[n - k] % MOD
        for k in range(n + 1)
    ]


makeCombibationTableNumba = numba.njit(makeCombibationTable)


def makeCombibationTableMaspy(n, f, invf):
    """make table of C(n, i) for i in [0, N)
    >>> f = makeFactorialTableMaspyNumba()
    >>> f[:4]
    array([1, 1, 2, 6])
    >>> N = 10000
    >>> UBOUND = math.ceil(math.sqrt(N + 1)) ** 2
    >>> UBOUND
    10201
    >>> invf = makeInvFactoTableMaspyOriginalNumba(f[UBOUND - 1], UBOUND)
    >>> invf[:4]
    array([        1,         1, 500000004, 166666668])
    >>> list(makeCombibationTableMaspy(N, f, invf)[:5])
    [1, 10000, 49995000, 616668838, 709582588]

    >>> f = makeFactorialTableMaspyNumba()
    >>> invf = makeInvFactoTableMaspyOriginalNumba(f[K - 1], K)
    >>> list(makeCombibationTableMaspy(K - 1, f, invf)[:5])
    [1, 999999, 998496508, 501840344, 583281443]

    %timeit makeCombibationTableMaspy(K - 1, f, invf)
    18.5 ms ± 231 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)
    """
    return f[n] * invf[: n + 1] % MOD * invf[n::-1] % MOD


def makeCombibationTableJointed(N):
    """ make table of C(n, i) for i in [0, N)
    Jointed version of makeFactorialTableMaspy, 
    makeInvFactoTableMaspyOriginal, and makeCombibationTableMaspy.

    >>> list(makeCombibationTableJointed(10000)[:5])
    [1, 10000, 49995000, 616668838, 709582588]

    %timeit makeCombibationTableJointed(K)
    89.5 ms ± 1.15 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
    """
    K = math.ceil(math.sqrt(N + 1)) ** 2
    rootK = math.ceil(math.sqrt(K))

    facto = np.arange(K, dtype=np.int64).reshape(rootK, rootK)
    facto[0, 0] = 1
    for n in range(1, rootK):
        facto[:, n] *= facto[:, n-1]
        facto[:, n] %= MOD
    for n in range(1, rootK):
        facto[n] *= facto[n-1, -1]
        facto[n] %= MOD
    facto = facto.ravel()

    invf = np.arange(1, K + 1, dtype=np.int64)[::-1].reshape(rootK, rootK)
    invf[0, 0] = pow(int(facto[K - 1]), MOD-2, MOD)  # inverse of (k-1)!
    for n in range(1, rootK):
        invf[:, n] *= invf[:, n-1]
        invf[:, n] %= MOD
    for n in range(1, rootK):
        invf[n] *= invf[n-1, -1]
        invf[n] %= MOD
    invf = invf.ravel()[::-1]

    return facto[N] * invf[: N + 1] % MOD * invf[N::-1] % MOD


@numba.njit
def makeCombibationTableJointedNumba(N):
    """ make table of C(n, i) for i in [0, N)
    Jointed version of makeFactorialTableMaspy, 
    makeInvFactoTableMaspyOriginal, and makeCombibationTableMaspy.

    >>> list(makeCombibationTableJointedNumba(10000)[:5])
    [1, 10000, 49995000, 616668838, 709582588]

    %timeit makeCombibationTableJointedNumba(K)
    35.5 ms ± 410 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)
    """
    K = math.ceil(math.sqrt(N + 1)) ** 2
    rootK = math.ceil(math.sqrt(K))

    facto = np.arange(K, dtype=np.int64).reshape(rootK, rootK)
    facto[0, 0] = 1
    for n in range(1, rootK):
        facto[:, n] *= facto[:, n-1]
        facto[:, n] %= MOD
    for n in range(1, rootK):
        facto[n] *= facto[n-1, -1]
        facto[n] %= MOD
    facto = facto.ravel()

    invf = np.ascontiguousarray(
        np.arange(1, K + 1, dtype=np.int64)[::-1]
    ).reshape(rootK, rootK)

    invf[0, 0] = getSingleInverseNumba(facto[K - 1])  # inverse of (k-1)!
    for n in range(1, rootK):
        invf[:, n] *= invf[:, n-1]
        invf[:, n] %= MOD
    for n in range(1, rootK):
        invf[n] *= invf[n-1, -1]
        invf[n] %= MOD
    invf = invf.ravel()[::-1]

    return facto[N] * invf[: N + 1] % MOD * invf[N::-1] % MOD


@numba.njit
def makeCombibationTableJointedNoReshapeNumba(N):
    """ make table of C(n, i) for i in [0, N)
    Jointed version of makeFactorialTableMaspy, 
    makeInvFactoTableMaspyOriginal, and makeCombibationTableMaspy.

    >>> list(makeCombibationTableJointedNumba(10000)[:5])
    [1, 10000, 49995000, 616668838, 709582588]

    %timeit makeCombibationTableJointedNoReshapeNumba(K)
    33 ms ± 809 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)
    """
    K = math.ceil(math.sqrt(N + 1)) ** 2
    rootK = math.ceil(math.sqrt(K))

    facto = np.arange(K, dtype=np.int64)
    facto[0] = 1
    for i in range(1, rootK):
        facto[i::rootK] *= facto[i-1::rootK]
        facto[i::rootK] %= MOD
    for start in range(rootK, K, rootK):
        end = start + rootK
        facto[start:end] *= facto[start - 1]
        facto[start:end] %= MOD

    invf = np.arange(1, K + 1, dtype=np.int64)
    invf[-1] = getSingleInverseNumba(facto[K - 1])  # inverse of (k-1)!
    for pos in range(rootK - 2, -1, -1):
        invf[pos::rootK] *= invf[pos + 1::rootK]
        invf[pos::rootK] %= MOD

    for end in range(-rootK, -K, -rootK):
        start = end - rootK
        invf[start:end] *= invf[end]
        invf[start:end] %= MOD
    return facto[N] * invf[:N + 1] % MOD * invf[N::-1] % MOD


def makeCombRepTable(n, f, invf):
    """make table of C(n, i) for i in [0, N]

    """
    return [
        f[n + k - 1] * invf[k] % MOD * invf[n - 1] % MOD
        for k in range(n + 1)
    ]


bestPower = makePowerTableMaspyNumba
bestInverse = makeInverseTableNumba
bestFactorial = makeFactorialTableMaspyNumba
bestInvFactorial = makeInvFactoTableMaspyOriginalNumba
bestCombination = makeCombibationTableJointedNumba


def solve():
    "void()"
    pass


def main():
    solve()


def _test():
    import doctest
    doctest.testmod()


def as_input(s):
    "use in test, use given string as input file"
    import io
    global read, input
    f = io.StringIO(s.strip())
    input = f.readline
    read = f.read


USE_NUMBA = False
if (USE_NUMBA and sys.argv[-1] == 'ONLINE_JUDGE') or sys.argv[-1] == '-c':
    print("compiling")
    from numba.pycc import CC
    cc = CC('my_module')
    cc.export('solve', solve.__doc__.strip().split()[0])(solve)
    cc.compile()
    exit()
else:
    input = sys.stdin.buffer.readline
    read = sys.stdin.buffer.read

    if (USE_NUMBA and sys.argv[-1] != '-p') or sys.argv[-1] == "--numba":
        # -p: pure python mode
        # if not -p, import compiled module
        from my_module import solve  # pylint: disable=all
    elif sys.argv[-1] == "-t":
        _test()
        sys.exit()
    elif sys.argv[-1] != '-p' and len(sys.argv) == 2:
        # input given as file
        input_as_file = open(sys.argv[1])
        input = input_as_file.buffer.readline
        read = input_as_file.buffer.read

    main()
