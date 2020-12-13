# included from libs/combination.py
"""
Combination
Not fastest but PyPy compatible version
"""

MOD = 10 ** 9 + 7
K = 10 ** 6


def makeInverseTable(K=K, MOD=MOD):
    ret = [1] * (K + 1)
    for i in range(2, K + 1):
        q, r = divmod(MOD, i)
        ret[i] = -ret[r] * q % MOD
    return ret


def makeFactorialTable(K=K, MOD=MOD):
    ret = [1] * (K + 1)
    cur = 1
    for i in range(2, K + 1):
        cur *= i
        cur %= MOD
        ret[i] = cur
    return ret


def makeInvFactoTable(inv, K=K, MOD=MOD):
    ret = [1] * (K + 1)
    cur = 1
    for i in range(2, K + 1):
        cur *= inv[i]
        cur %= MOD
        ret[i] = cur
    return ret


def combination(n, k, facto, invf, MOD=MOD):
    assert n >= 0
    assert k >= 0
    if k > n:
        return 0
    return facto[n] * invf[k] % MOD * invf[n - k] % MOD


def comb_rep(n, k, facto, invf, MOD=MOD):
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


# included from libs/mod_inverse.py
"""
Mod Inverse for single value
Given K, N, R, find x s.t. Kx mod N = R
"""

MOD1 = 1_000_000_007
MOD9 = 998_244_353


def mod_inverse(X, MOD):
    """
    return X^-1 mod MOD
    """
    try:
        return pow(X, -1, MOD)
    except:
        return _mod_inverse_ee(X, MOD)


def _mod_inverse_py38(X, MOD):
    # since Python3.8
    return pow(X, -1, MOD)


def _mod_inverse_ee(a, m):
    """
    Solve ax mod m = 1 with extended euclidean.
    x = a^-1.
    """
    x, y, g = _extended_euclidean(a, m)
    assert g == 1
    return x % m


# included from libs/extended_euclidean.py
"""
Extended Euclidean algorithm
"""


def _extended_euclidean(a, b, test=False):
    """
    Given a, b, solve:
    ax + by = gcd(a, b)
    Returns x, y, gcd(a, b)

    Other form, for a prime b:
    ax mod b = gcd(a, b) = 1

    >>> _extended_euclidean(3, 5, test=True)
    3 * 2 + 5 * -1 = 1 True
    >>> _extended_euclidean(240, 46, test=True)
    240 * -9 + 46 * 47 = 2 True

    Derived from https://atcoder.jp/contests/acl1/submissions/16914912
    """
    init_a = a
    init_b = b
    s, u, v, w = 1, 0, 0, 1
    while b:
        q, r = divmod(a, b)
        a, b = b, r
        s, u, v, w = v, w, s - q * v, u - q * w

    if test:
        print(f"{init_a} * {s} + {init_b} * {u} = {a}",
              init_a * s + init_b * u == a)
    else:
        return s, u, a


# end of libs/extended_euclidean.py


# end of libs/mod_inverse.py
def naive_comb(n, k, MOD=MOD):
    assert n >= 0
    assert k >= 0
    if n < k:
        return 0
    k = min(k, n - k)
    a = 1
    b = 1
    for i in range(k):
        a *= (n - i)
        a %= MOD
        b *= (i + 1)
        b %= MOD
    return (a * mod_inverse(b, MOD)) % MOD

# end of libs/combination.py
# included from snippets/main.py


def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(N, M, AS):
    MOD = 1_000_000_007
    UP = N + M
    DOWN = N + sum(AS)
    return naive_comb(UP, DOWN, MOD)


def main():
    # parse input
    N, M = map(int, input().split())
    AS = list(map(int, input().split()))
    print(solve(N, M, AS))


# tests
T1 = """
3 5
1 2 1
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
8
"""

T2 = """
10 998244353
31 41 59 26 53 58 97 93 23 84
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
642612171
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
