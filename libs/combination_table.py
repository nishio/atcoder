"""
Combination Table
Not fastest but PyPy compatible version
"""

MOD = 10 ** 9 + 7
K = 10 ** 6


def makeInverseTable(K=K, MOD=MOD):
    """calc i^-1 for i in [1, K] mod MOD. MOD should be prime
    >>> invs = makeInverseTable(10)
    >>> [i * invs[i] % MOD for i in range(1, 10)]
    [1, 1, 1, 1, 1, 1, 1, 1, 1]
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
    # >>> facto = makeFactorialTable()
    # >>> inv = makeInverseTable()
    # >>> invf = makeInvFactoTable(inv)
    # >>> [combination(10000, i, facto, invf) for i in range(7)]
    # [1, 10000, 49995000, 616668838, 709582588, 797500005, 2082363]
    """
    assert n >= 0
    assert k >= 0
    if k > n:
        return 0
    return facto[n] * invf[k] % MOD * invf[n - k] % MOD


def comb_rep(n, k, facto, invf, MOD=MOD):
    """combination with replacement Cr(n, k)
    # >>> facto = makeFactorialTable()
    # >>> inv = makeInverseTable()
    # >>> invf = makeInvFactoTable(inv)
    # >>> [comb_rep(3, i, facto, invf) for i in range(7)]
    # [1, 3, 6, 10, 15, 21, 28]
    """
    return facto[n + k - 1] * invf[k] % MOD * invf[n - 1] % MOD


class CombinationTable:
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
    c = CombinationTable(N, MOD)
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

TEST_T3 = """
>>> print_all()
  1   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
  1   1   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
  1   2   1   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
  1   3   3   1   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
  1   4   6   4   1   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
  1   5  10  10   5   1   0   0   0   0   0   0   0   0   0   0   0   0   0   0
  1   6  15  20  15   6   1   0   0   0   0   0   0   0   0   0   0   0   0   0
  1   7  21  35  35  21   7   1   0   0   0   0   0   0   0   0   0   0   0   0
  1   8  28  56  70  56  28   8   1   0   0   0   0   0   0   0   0   0   0   0
  1   9  36  84  23  23  84  36   9   1   0   0   0   0   0   0   0   0   0   0
  1  10  45  17   4  46   4  17  45  10   1   0   0   0   0   0   0   0   0   0
  1  11  55  62  21  50  50  21  62  55  11   1   0   0   0   0   0   0   0   0
  1  12  66  14  83  71 100  71  83  14  66  12   1   0   0   0   0   0   0   0
  1  13  78  80  97  51  68  68  51  97  80  78  13   1   0   0   0   0   0   0
  1  14  91  55  74  45  16  33  16  45  74  55  91  14   1   0   0   0   0   0
  1  15   2  43  26  16  61  49  49  61  16  26  43   2  15   1   0   0   0   0
  1  16  17  45  69  42  77   7  98   7  77  42  69  45  17  16   1   0   0   0
  1  17  33  62  11   8  16  84   2   2  84  16   8  11  62  33  17   1   0   0
  1  18  50  95  73  19  24 100  86   4  86 100  24  19  73  95  50  18   1   0
  1  19  68  42  65  92  43  21  83  90  90  83  21  43  92  65  42  68  19   1
"""


def print_all():
    c = CombinationTable(10000, 103)
    for i in range(20):
        print(*("%3d" % c.comb(i, j) for j in range(20)))


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
