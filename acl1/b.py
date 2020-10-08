import sys


def debug(*x):
    print(*x, file=sys.stderr)


def ex():
    for i in range(2, 100):
        for j in range(1, i - 1):
            if (j * (j + 1) // 2) % i == 0:
                # debug("i, j", i, j)
                break
        else:
            debug("i", i)


def extended_euclidean(a, b, test=False):
    """
    Extended Euclidean algorithm
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


def crt(a, m, b, n):
    """
    Find x s.t. x % m == a and x % n == b

    >>> crt(2, 3, 1, 5)
    11
    """
    x, y, g = extended_euclidean(m, n)
    assert g == 1
    return (b * m * x + a * n * y) % (m * n)


def blute(N):
    for i in range(1, N):
        if (i * (i + 1) // 2) % N == 0:
            return i
    return N - 1


#!/usr/bin/env python3
sys.setrecursionlimit(10**6)
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")
MOD = 10 ** 9 + 7


def factor(n):
    """
    >>> factor(100)
    defaultdict(<class 'int'>, {2: 2, 5: 2})
    >>> factor(103)
    defaultdict(<class 'int'>, {103: 1})
    """
    from math import sqrt
    from collections import defaultdict
    ret = defaultdict(int)
    SQRTN = int(sqrt(n)) + 1
    p = 2
    while p < SQRTN and n > 1:
        while n % p == 0:
            ret[p] += 1
            n //= p
        p += 1
    if n > 1:
        ret[n] += 1
    return ret


def solve_0(N):
    """
    not return minimum answer
    """
    f = factor(N)
    if len(f) == 1:
        return N - 1
    xs = [p ** f[p] for p in f]
    maxx = max(xs)
    rest = N // maxx
    debug("N, maxx, rest", N, maxx, rest)
    for p in range(maxx, N, maxx):
        if (p + 1) % rest == 0:
            return p
        if (p - 1) % rest == 0:
            return p - 1


def all_divisor_naive(N, includeN=True):
    """
    >>> list(all_divisor(28))
    [1, 2, 4, 7, 14, 28]
    """
    UP = N + 1 if includeN else N
    for i in range(1, UP):
        if N % i == 0:
            yield i


def all_divisor(n, includeN=True):
    """
    >>> all_divisor(28)
    [1, 2, 4, 7, 14, 28]
    >>> all_divisor(28, includeN=False)
    [1, 2, 4, 7, 14]

    Derived from https://qiita.com/LorseKudos/items/9eb560494862c8b4eb56
    """
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    upper_divisors = upper_divisors[::-1]
    if not includeN:
        upper_divisors.pop()
    return lower_divisors + upper_divisors

###
# https://qiita.com/Kiri8128/items/eca965fe86ea5f4cbb98


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def isPrimeMR(n):
    d = n - 1
    d = d // (d & -d)
    L = [2]
    for a in L:
        t = d
        y = pow(a, t, n)
        if y == 1:
            continue
        while y != n - 1:
            y = (y * y) % n
            if y == 1 or t == n - 1:
                return 0
            t <<= 1
    return 1


def findFactorRho(n):
    m = 1 << n.bit_length() // 8
    for c in range(1, 99):
        def f(x): return (x * x + c) % n
        y, r, q, g = 2, 1, 1, 1
        while g == 1:
            x = y
            for i in range(r):
                y = f(y)
            k = 0
            while k < r and g == 1:
                ys = y
                for i in range(min(m, r - k)):
                    y = f(y)
                    q = q * abs(x - y) % n
                g = gcd(q, n)
                k += m
            r <<= 1
        if g == n:
            g = 1
            while g == 1:
                ys = f(ys)
                g = gcd(abs(x - ys), n)
        if g < n:
            if isPrimeMR(g):
                return g
            elif isPrimeMR(n // g):
                return n // g
            return findFactorRho(g)


def primeFactor(n):
    i = 2
    ret = {}
    rhoFlg = 0
    while i*i <= n:
        k = 0
        while n % i == 0:
            n //= i
            k += 1
        if k:
            ret[i] = k
        i += 1 + i % 2
        if i == 101 and n >= 2 ** 20:
            while n > 1:
                if isPrimeMR(n):
                    ret[n], n = 1, 1
                else:
                    rhoFlg = 1
                    j = findFactorRho(n)
                    k = 0
                    while n % j == 0:
                        n //= j
                        k += 1
                    ret[j] = k

    if n > 1:
        ret[n] = 1
    if rhoFlg:
        ret = {x: ret[x] for x in sorted(ret)}
    return ret
###


def solve_CRT(N):
    from math import gcd
    if N == 1:
        return 1
    ret = N - 1
    for n in all_divisor(2 * N, includeN=False):
        m = (2 * N) // n
        if gcd(m, n) != 1:
            continue
        k = crt(0, n, -1, m)
        if k < ret:
            ret = k
    return ret


def solve(N):
    if N == 1:
        return 1
    factors = primeFactor(2 * N)
    num_factors = len(factors)
    if num_factors == 1:
        return N - 1
    factors = [p ** factors[p] for p in factors]
    ret = N - 1
    for i in range(2 ** num_factors - 1):
        prod = 1
        j = 0
        while i:
            if i & 1:
                prod *= factors[j]
            j += 1
            i >>= 1

        rest = (2 * N) // prod
        k = (-pow(prod, -1, rest) * prod) % (2 * N)
        if k < ret:
            ret = k

    return ret


def main():
    N = int(input())
    print(solve(N))


# tests
T1 = """
11
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
10
"""

T2 = """
13
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
12
"""

T3 = """
16
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
15
"""


T4 = """
1
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
1
"""

T5 = """
210
"""
TEST_T5 = """
>>> as_input(T5)
>>> main()
20
"""


def test2():
    """
    #>>> test2()
    ok
    """
    for i in range(2, 100):
        debug("blute(i), solve(i)", i, blute(i), solve(i))
        assert blute(i) == solve(i)
    print("ok")


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


input = sys.stdin.buffer.readline
read = sys.stdin.buffer.read

if sys.argv[-1] == "-t":
    print("testing")
    _test()
    sys.exit()

main()
