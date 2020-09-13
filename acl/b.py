#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")
MOD = 10 ** 9 + 7


def debug(*x):
    print(*x, file=sys.stderr)


# Fenwick Tree
def init(n):
    global N, bit
    N = n
    bit = [0] * (N + 1)  # 1-origin


def bit_add(pos, val):
    assert pos > 0
    x = pos
    while x <= N:
        bit[x] += val
        x += x & -x  # (x & -x) = rightmost 1 = block width


def bit_sum(pos):
    ret = 0
    x = pos
    while x > 0:
        ret += bit[x]
        x -= x & -x
    return ret


def bit_bisect(lower):
    "find a s.t. v1 + v2 + ... + va >= lower"
    x = 0
    k = 1 << (N.bit_length() - 1)  # largest 2^m <= N
    while k > 0:
        if (x + k <= N and bit[x + k] < lower):
            lower -= bit[x + k]
            x += k
        k //= 2
    return x + 1


def main():
    # parse input
    N, Q = map(int, input().split())
    init(N)
    AS = list(map(int, input().split()))
    for i, a in enumerate(AS):
        bit_add(i + 1, a)

    for _q in range(Q):
        a, b, c = map(int, input().split())
        if a == 0:
            bit_add(b + 1, c)
        else:
            print(bit_sum(c) - bit_sum(b))


# tests
T1 = """
5 5
1 2 3 4 5
1 0 5
1 2 4
0 3 10
1 0 5
1 0 3
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
15
7
25
6
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
