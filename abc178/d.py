#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")
MOD = 10 ** 9 + 7


def debug(*x):
    print(*x, file=sys.stderr)


def solve(S):
    table = [0] * 2020
    table[0] = 1
    # [1], [2] = 0
    for i in range(3, S + 1):
        # table[i] = sum(table[i - d] for d in range(3, 10)) % MOD
        table[i] = sum(table[i - d] for d in range(3, i + 1))
    # debug("table[:S + 1]", table[:S + 1])
    return table[S] % MOD


def main():
    # parse input
    S = int(input())
    print(solve(S))


# tests
T1 = """
7
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
3
"""

T2 = """
2
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
0
"""

T3 = """
1729
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
294867501
"""

T4 = """
4
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
1
"""

T4 = """
5
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
1
"""

T5 = """
6
"""
TEST_T5 = """
>>> as_input(T5)
>>> main()
2
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
