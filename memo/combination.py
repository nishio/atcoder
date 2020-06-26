import numpy as np
import sys
import numba
import math

MOD = 10 ** 9 + 7
K = 10 ** 6


@numba.njit
def makePowerTable(x, K=K, MOD=MOD):
    """calc x^i for i in [0, K] mod MOD
    >>> xs = makePowerTable(2, 20, 1000)
    >>> xs
    [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 24, 48, 96, 192, 384, 768, 536, 72, 144, 288, 576]
    >>> xs == [pow(2, i, 1000) for i in range(21)]
    True

    %timeit makePowerTable(23)
    165 ms ± 1.5 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)

    Numba-jit-ed
    %timeit makePowerTable(23)
    45 ms ± 546 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)
    """
    ret = [1] * (K + 1)
    cur = 1
    for i in range(1, K + 1):
        cur *= x
        cur %= MOD
        ret[i] = cur
    return ret


@numba.njit
def makeInverseTable(K=K, MOD=MOD):
    """calc i^-1 for i in [1, K] mod MOD. MOD should be prime
    >>> invs = makeInverseTable(10)
    >>> [i * invs[i] % MOD for i in range(1, 10)]
    [1, 1, 1, 1, 1, 1, 1, 1, 1]

    %timeit makeInverseTable()
    516 ms ± 26.6 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

    Numba-jit-ed
    %timeit makeInverseTable()
    47 ms ± 765 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)
    """
    ret = [1] * (K + 1)
    invf = 1
    for i in range(2, K + 1):
        q, r = divmod(MOD, i)
        ret[i] = -ret[r] * q % MOD
    return ret


def getSingleInverse(a, MOD=MOD):
    """
    >>> [getSingleInverse(x) for x in range(1, 11)] ==  makeInverseTable(10)[1:]
    True

    %timeit getSingleInverse(1000)
    984 ns ± 10.4 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

    %timeit [getSingleInverse(x) for x in range(1, K + 1)]
    2.46 s ± 9.9 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
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


@numba.njit
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

    Numba-jit-ed
    %timeit makeFactorialTable()
    45 ms ± 1.18 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
    """
    ret = [1] * (K + 1)
    cur = 1
    for i in range(2, K + 1):
        cur *= i
        cur %= MOD
        ret[i] = cur
    return ret


@numba.njit
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

    Numba-jit-ed
    %timeit makeFactorialTableMaspy()
    14 ms ± 1.18 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
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


def makeInvFactoTable(inv, K=K, MOD=MOD):
    """calc i!^-1 for i in [0, K] mod MOD. MOD should be prime
    You can not do inv[f[i]], because f[i] may greater than K.

    %timeit makeInvFactoTable(inv)
    182 ms ± 1.08 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)

    inva = np.array(inv)
    %timeit makeInvFactoTable(inva)
    329 ms ± 5.22 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
    """
    ret = [1] * (K + 1)
    cur = 1
    for i in range(2, K + 1):
        cur *= inv[i]
        cur %= MOD
        ret[i] = cur
    return ret


@numba.njit("i8[:](i8[::1], i8, i8)")
def makeInvFactoTableNumba(inv, K=K, MOD=MOD):
    """calc i!^-1 for i in [0, K] mod MOD. MOD should be prime
    You can not do inv[f[i]], because f[i] may greater than K.

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


def combination(n, k, f, invf):
    """combination C(n, k)
    >>> f = makeFactorialTable()
    >>> inv = makeInverseTable()
    >>> invf = makeInvFactoTable(inv)
    >>> [combination(10000, i, f, invf) for i in range(7)]
    [1, 10000, 49995000, 616668838, 709582588, 797500005, 2082363]
    """
    return f[n] * invf[k] % MOD * invf[n - k] % MOD


def comb_rep(n, k, f, invf):
    """combination with replacement Cr(n, k)
    >>> f = makeFactorialTable()
    >>> inv = makeInverseTable()
    >>> invf = makeInvFactoTable(inv)
    >>> [comb_rep(3, i, f, invf) for i in range(7)]
    [1, 3, 6, 10, 15, 21, 28]
    """
    return f[n + k - 1] * invf[k] % MOD * invf[n - 1] % MOD


def makeCombibationTable(n, f, invf):
    """make table of C(n, i) for i in [0, N]

    %timeit makeCombibationTable(K, f, invf)
    356 ms ± 10.8 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
    """
    return [
        f[n] * invf[k] % MOD * invf[n - k] % MOD
        for k in range(n + 1)
    ]


def makeCombRepTable(n, f, invf):
    """make table of C(n, i) for i in [0, N]

    """
    return [
        f[n + k - 1] * invf[k] % MOD * invf[n - 1] % MOD
        for k in range(n + 1)
    ]


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