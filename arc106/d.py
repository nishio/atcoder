# included from libs/combination.py
"""
Combination
Not fastest but PyPy compatible version
"""

MOD = 998_244_353
K = 301


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
    return facto[n] * invf[k] % MOD * invf[n - k] % MOD


def comb_rep(n, k, facto, invf, MOD=MOD):
    return facto[n + k - 1] * invf[k] % MOD * invf[n - 1] % MOD


class Comb:
    def __init__(self, maxValue, modulo):
        self.maxValue = maxValue
        self.modulo = modulo
        self.facto = makeFactorialTable(maxValue, modulo)
        self.inv = makeInverseTable(maxValue, modulo)
        self.invf = makeInvFactoTable(self.inv, maxValue, modulo)

    def comb(self, n, k):
        return combination(n, k, self.facto, self.invf, self.modulo)


# end of libs/combination.py
# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(N, K, AS):
    MOD = 998_244_353
    div2 = pow(2, MOD - 2, MOD)
    sumTable = [N] * (K + 2)
    for x in range(1, K + 1):
        s = 0
        for a in AS:
            s += pow(a, x, MOD)
            s %= MOD
        sumTable[x] = s

    c = Comb(K + 1, MOD)
    for x in range(1, K + 1):
        ret = 0
        for i in range(x + 1):
            ret += c.comb(x, i) * sumTable[x - i] * sumTable[i]
            ret %= MOD
        p = pow(2, x, MOD)
        ret -= sumTable[x] * p
        ret %= MOD
        ret *= div2
        ret %= MOD
        print(ret)


def main():
    # parse input
    N, K = map(int, input().split())
    AS = list(map(int, input().split()))
    solve(N, K, AS)


# tests
T1 = """
3 3
1 2 3
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
12
50
216
"""

T2 = """
10 10
1 1 1 1 1 1 1 1 1 1
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
90
180
360
720
1440
2880
5760
11520
23040
46080
"""

T3 = """
2 5
1234 5678
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
6912
47775744
805306038
64822328
838460992
"""


def _test():
    import doctest
    doctest.testmod()
    g = globals()
    for k in sorted(g):
        if k.startswith("TEST_"):
            doctest.run_docstring_examples(g[k], g, name=k)


def as_input(s):
    "use in test, use given string as input file"
    import io
    f = io.StringIO(s.strip())
    g = globals()
    g["input"] = lambda: bytes(f.readline(), "ascii")
    g["read"] = lambda: bytes(f.read(), "ascii")


if __name__ == "__main__":
    import sys
    input = sys.stdin.buffer.readline
    read = sys.stdin.buffer.read
    if sys.argv[-1] == "-t":
        print("testing")
        _test()
        sys.exit()
    main()

# end of snippets/main.py
