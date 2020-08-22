#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")
MOD = 10 ** 9 + 7


def debug(*x):
    print(*x, file=sys.stderr)


def solve(N, AS):
    ret = 0
    prevStep = 0
    for i in range(1, N):
        if prevStep + AS[i - 1] > AS[i]:
            prevStep = prevStep + AS[i - 1] - AS[i]
            ret += prevStep
        else:
            prevStep = 0
    return ret


def main():
    N = int(input())
    AS = list(map(int, input().split()))
    print(solve(N, AS))


# tests
T1 = """
5
2 1 5 4 3
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
4
"""

T2 = """
5
3 3 3 3 3
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
0
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
