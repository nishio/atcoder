#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")
MOD = 10 ** 9 + 7


def debug(*x):
    print(*x, file=sys.stderr)


def solve(N, K, AS):
    for i in range(K, N):
        # debug("i: i,AS[i-K],AS[K]", i, AS[i-K], AS[K])
        if AS[i - K] < AS[i]:
            print("Yes")
        else:
            print("No")


def main():
    # parse input
    N, K = map(int, input().split())
    AS = list(map(int, input().split()))
    solve(N, K, AS)


# tests
T1 = """
5 3
96 98 95 100 20
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
Yes
No
"""

T3 = """
15 7
3 1 4 1 5 9 2 6 5 3 5 8 9 7 9
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
Yes
Yes
No
Yes
Yes
No
Yes
Yes
"""


def _test():
    import doctest
    doctest.testmod()
    g = globals()
    for k in sorted(g):
        if k.startswith("TEST_"):
            doctest.run_docstring_examples(g[k], g)


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
