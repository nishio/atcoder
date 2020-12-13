"""
naive_comb(N, K): O(K)
"""
MOD = 1_000_000_007


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
