#!/usr/bin/env python3
import numba
import sys
sys.setrecursionlimit(10**6)
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")
MOD = 10 ** 9 + 7


def debug(*x):
    print(*x, file=sys.stderr)


def solve(N, AS):
    is_pairwise = True
    maxAS = max(AS)
    sieved = [False] * (maxAS + 10)
    for p in range(2, maxAS + 1):
        if sieved[p]:
            continue
        # p is prime
        x = p + p
        while x <= maxAS:
            sieved[x] = True
            x += p
        sum_div = 0
        for i, a in enumerate(AS):
            dividable = 0
            while a % p == 0:
                a //= p
                dividable = 1
            AS[i] = a
            sum_div += dividable
        if sum_div >= 2:
            is_pairwise = False
        if sum_div == N:
            return "not coprime"

    if is_pairwise:
        return "pairwise coprime"
    return "setwise coprime"


def main():
    # parse input
    N = int(input())
    AS = list(map(int, input().split()))
    print(solve(N, AS))


# tests
T1 = """
3
3 4 5
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
pairwise coprime
"""

T2 = """
3
6 10 15
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
setwise coprime
"""

T3 = """
3
6 10 16
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
not coprime
"""


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
