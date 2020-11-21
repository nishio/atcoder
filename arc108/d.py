# included from libs/combination.py
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


# end of libs/combination.py

# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(N, S):
    if N < 4:
        return 1
    MOD = 1_000_000_007
    S = [x[0] - ord("A") for x in S]
    AA, AB, BA, BB = 0, 1, 2, 3
    A, B = 0, 1
    c = Combination(N + 10, MOD)
    if S[AB] == A:
        # len(B) = 1
        if S[AA] == A:
            return 1
        if S[AB] == A and S[BA] == A:
            # inserted B = length 1
            M = N - 2
            ret = 0
            for i in range(M):
                if M - i < i:
                    break
                ret += c.comb(M - i, i)
                ret %= MOD
            return ret
        else:
            return pow(2, N - 3, MOD)
    else:
        if S[BB] == B:
            return 1
        if S[BA] == B and S[AB] == B:
            # inserted B = length 1
            M = N - 2
            ret = 0
            for i in range(M):
                if M - i < i:
                    break
                ret += c.comb(M - i, i)
                ret %= MOD
            return ret
        else:
            return pow(2, N - 3, MOD)


def main():
    # parse input
    N = int(input())
    S = read().split()
    print(solve(N, S))


# tests
T1 = """
4
A
B
B
A
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
2
"""

T2 = """
1000
B
B
B
B
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
1
"""

T3 = """
10
B
A
A
A
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
result
"""

T = """
1000
A
B
B
A
"""
TEST_T = """
>>> as_input(T)
>>> main()
result
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
