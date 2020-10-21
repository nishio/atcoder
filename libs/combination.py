"""
Combination
Not fastest but PyPy compatible version
"""

MOD = 10 ** 9 + 7
K = 10 ** 6


def makeInverseTable(K=K, MOD=MOD):
    """calc i^-1 for i in [1, K] mod MOD. MOD should be prime
    >>> invs = makeInverseTable(10)
    >>> [i * invs[i] % MOD for i in range(1, 10)]
    [1, 1, 1, 1, 1, 1, 1, 1, 1]

    %timeit makeInverseTable()
    516 ms ± 26.6 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
    525 ms ± 19.5 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
    """
    ret = [1] * (K + 1)
    for i in range(2, K + 1):
        q, r = divmod(MOD, i)
        ret[i] = -ret[r] * q % MOD
    return ret


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
    """
    ret = [1] * (K + 1)
    cur = 1
    for i in range(2, K + 1):
        cur *= i
        cur %= MOD
        ret[i] = cur
    return ret


def makeInvFactoTable(inv, K=K, MOD=MOD):
    """calc i!^-1 for i in [0, K] mod MOD. MOD should be prime
    You can not do inv[facto[i]], because facto[i] may greater than K.

    inv = makeInverseTable()
    %timeit makeInvFactoTable(inv)
    182 ms ± 1.08 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
    189 ms ± 1.56 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
    """
    ret = [1] * (K + 1)
    cur = 1
    for i in range(2, K + 1):
        cur *= inv[i]
        cur %= MOD
        ret[i] = cur
    return ret


def combination(n, k, facto, invf, MOD=MOD):
    """combination C(n, k)
    >>> facto = makeFactorialTable()
    >>> inv = makeInverseTable()
    >>> invf = makeInvFactoTable(inv)
    >>> [combination(10000, i, facto, invf) for i in range(7)]
    [1, 10000, 49995000, 616668838, 709582588, 797500005, 2082363]

    %timeit combination(10000, 100, facto, invf)
    814 ns ± 6.5 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
    """
    assert n >= 0
    assert k >= 0
    if k > n:
        return 0
    return facto[n] * invf[k] % MOD * invf[n - k] % MOD


def comb_rep(n, k, facto, invf, MOD=MOD):
    """combination with replacement Cr(n, k)
    >>> facto = makeFactorialTable()
    >>> inv = makeInverseTable()
    >>> invf = makeInvFactoTable(inv)
    >>> [comb_rep(3, i, facto, invf) for i in range(7)]
    [1, 3, 6, 10, 15, 21, 28]

    %timeit comb_rep(10000, 100, facto, invf)
    881 ns ± 8.53 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
    """
    return facto[n + k - 1] * invf[k] % MOD * invf[n - 1] % MOD


class Combination:
    def __init__(self, maxValue, modulo):
        self.maxValue = maxValue
        self.modulo = modulo
        self.facto = makeFactorialTable(maxValue, modulo)
        self.inv = makeInverseTable(maxValue, modulo)
        self.invf = makeInvFactoTable(self.inv, maxValue, modulo)

    def comb(self, n, k):
        return combination(n, k, self.facto, self.invf, self.modulo)

# --- end of library ---


def main():
    # verified: https://scrapbox.io/nishio/ABC132D
    N, K = map(int, input().split())
    MOD = 1_000_000_007
    c = Combination(N, MOD)
    for i in range(1, K + 1):
        r = c.comb(K - 1, i - 1)
        r *= c.comb(N - K + 1, i)
        r %= MOD
        print(r)


def as_input(s):
    "use in test, use given string as input file"
    import io
    g = globals()
    f = io.StringIO(s.strip())

    g["input"] = lambda: bytes(f.readline(), "ascii")
    g["read"] = lambda: bytes(f.read(), "ascii")


T1 = """
5 3
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
3
6
1
"""

T2 = """
2000 3
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
1998
3990006
327341989
"""


def _test():
    import doctest
    print("testing")
    doctest.testmod()
    g = globals()
    for k in sorted(g):
        if k.startswith("TEST_"):
            doctest.run_docstring_examples(g[k], g, name=k)


if __name__ == "__main__":
    import sys
    input = sys.stdin.buffer.readline
    read = sys.stdin.buffer.read
    if sys.argv[-1] == "-t":
        _test()
        sys.exit()
    main()
