# included from libs/crt.py
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
    >>> crt(1, 4, 3, 6)
    9
    """
    x, y, g = extended_euclidean(m, n)
    if g == 1:
        return (b * m * x + a * n * y) % (m * n)
    s = (b - a) // g
    return (a + s * m * x) % (m * n // g)
# end of libs/crt.py

# included from snippets/main.py


def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    from math import gcd
    T = int(input())
    for _t in range(T):
        X, Y, P, Q = map(int, input().split())

        m = 2 * X + 2 * Y
        n = P + Q
        ret = INF = 9223372036854775807
        g = gcd(n, m)
        for a in range(X, X+Y):
            for b in range(P, P + Q):
                if a % g == b % g:
                    x = crt(a, m, b, n)
                    ret = min(ret, x)

        if ret == INF:
            print("infinity")
        else:
            print(ret)


# tests
T1 = """
3
5 2 7 6
1 1 3 1
999999999 1 1000000000 1
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
20
infinity
1000000000999999999
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
