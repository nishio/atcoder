# included from libs/combination_table.py
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

# end of libs/combination_table.py
# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(N, M):
    if M % 2:
        return 0
    M //= 2
    MOD = 998_244_353
    comb = CombinationTable(N + 10, MOD).comb

    cache = {}    
    def foo(x, start=11):
        # debug(x, start, msg=":x, start")
        if (x, start) in cache:
            return cache[(x, start)]
        if start == 0:
            if 2 * x > N:
                return 0
            else:
                ret = comb(N, 2 * x)
                cache[(x, start)] = ret
                return ret

        p = 2 ** start
        if p <= x:
            ret = 0
            # debug(x, p, msg=":x, p")
            for i in range(x // p + 1):
                # debug(i, x - i * p, comb(N, 2 * i), msg=":i, x - i * p, ")
                ret = (ret + foo(x - i * p, start - 1) * comb(N, 2 * i)) % MOD
        else:
            ret = foo(x, start - 1)
        cache[(x, start)] = ret
        return ret

    return foo(M)

def main():
    N, M = map(int, input().split())    
    print(solve(N, M))

# tests
T1 = """
5 20
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
475
"""
T2 = """
10 5
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
0
"""
T3 = """
3141 2718
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
371899128
"""
T4 = """
1 2
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
0
"""
T5 = """
2 6
"""
TEST_T5 = """
>>> as_input(T5)
>>> main()
1
"""
def _test():
    import doctest
    doctest.testmod()
    g = globals()
    for k in sorted(g):
        if k.startswith("TEST_"):
            print(k)
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
    sys.setrecursionlimit(10 ** 6)
    if sys.argv[-1] == "-t":
        print("testing")
        _test()
        sys.exit()
    main()
    sys.exit()

# end of snippets/main.py