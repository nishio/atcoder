# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


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


def mod_inverse_ee(a, m):
    """
     Solve ax mod m = 1 with extended euclidean.
     x = a^-1.
     """
    x, y, g = extended_euclidean(a, m)
    assert g == 1
    return x % m
# end of libs/extended_euclidean.py


def solve(N, S, K):
    from math import gcd
    g = gcd(K, N)
    if g > 1:
        if S % g != 0:
            return -1
        N //= g
        K //= g
        S //= g

    invK = mod_inverse_ee(K, N)
    ret = (N - S) * invK % N

    return ret


def main():
    # parse input
    T = int(input())
    for _t in range(T):
        N, S, K = map(int, input().split())
        print(solve(N, S, K))


# tests
T1 = """
4
10 4 3
1000 11 2
998244353 897581057 595591169
10000 6 14
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
2
-1
249561088
3571
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
