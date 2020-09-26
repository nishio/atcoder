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


def solve(N):
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
    return blute(N)


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


def test2():
    """
    >>> test2()
    ok
    """
    for i in range(2, 100):
        debug("blute(i), solve(i)", blute(i), solve(i))
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
