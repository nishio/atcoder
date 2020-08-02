#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")
MOD = 10 ** 9 + 7


def debug(*x):
    print(*x, file=sys.stderr)


def solve(N, K, AS):
    left = 1
    right = min(AS)
    while left < right - 1:
        mid = (left + right) // 2
        s = sum(a // mid - 1 for a in AS)
        if s >= K:
            left = mid
        else:
            right = mid
    return right


def main():
    # parse input
    N, K = map(int, input().split())
    AS = list(map(int, input().split()))
    print(solve(N, K, AS))


# tests
T1 = """
2 3
7 9
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
4
"""

T2 = """
3 0
3 4 5
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
5
"""

T3 = """
10 10
158260522 877914575 602436426 24979445 861648772 623690081 433933447 476190629 262703497 211047202
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
292638192
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
