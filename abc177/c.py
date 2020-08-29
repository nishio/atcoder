#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")
MOD = 10 ** 9 + 7


def debug(*x):
    print(*x, file=sys.stderr)


def solve(N, AS):
    sum = 0
    sumSq = 0
    for i in range(N):
        sum += AS[i]
        sum %= MOD
        sumSq += AS[i] * AS[i]
        sumSq %= MOD

    ret = (sum * sum - sumSq) % MOD
    if ret % 2 == 0:
        return ret // 2
    else:
        return (ret + MOD) // 2


def main():
    # parse input
    N = int(input())
    AS = list(map(int, input().split()))
    print(solve(N, AS))


# tests
T1 = """
3
1 2 3
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
11
"""

T2 = """
4
141421356 17320508 22360679 244949
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
437235829
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
