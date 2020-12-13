"""
Mod Inverse for single value
Given K, N, R, find x s.t. Kx mod N = R
"""


def mod_inverse(X, MOD):
    """
    return X^-1 mod MOD
    """
    return pow(X, MOD - 2, MOD)


# --- end of library ---
MOD1 = 1_000_000_007
MOD9 = 998_244_353

# included from libs/extended_euclidean.py
"""
Extended Euclidean algorithm
"""


def extended_euclidean(a, b, test=False):
    """
    Given a, b, solve:
    ax + by = gcd(a, b)
    Returns x, y, gcd(a, b)

    Other form, for a prime b:
    ax mod b = gcd(a, b) = 1

    >>> extended_euclidean(3, 5, test=True)
    3 * 2 + 5 * -1 = 1 True
    >>> extended_euclidean(240, 46, test=True)
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

def _mod_inverse_ee(a, m):
    """
    Solve ax mod m = 1 with extended euclidean.
    x = a^-1.
    """
    x, y, g = extended_euclidean(a, m)
    assert g == 1
    return x % m


def test1():
    """
    >>> test1()
    ok
    """
    for i in range(1, 10000):
        if mod_inverse(i, MOD1) != _mod_inverse_ee(i, MOD1):
            print(i)
    for i in range(1, 10000):
        if mod_inverse(i, MOD9) != _mod_inverse_ee(i, MOD9):
            print(i)
    print("ok")


def _test():
    import doctest
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
        print("testing")
        _test()
        sys.exit()
