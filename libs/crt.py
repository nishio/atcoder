"""
Chinese Remainder Theorem
"""

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

def crt(a, m, b, n):
    """
    Find x s.t. x % m == a and x % n == b

    >>> crt(2, 3, 1, 5)
    11
    """
    x, y, g = extended_euclidean(m, n)
    assert g == 1
    return (b * m * x + a * n * y) % (m * n)
