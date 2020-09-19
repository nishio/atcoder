#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")
MOD = 10 ** 9 + 7


def debug(*x):
    print(*x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    N = int(input())
    ret = False
    count = 0
    for i in range(N):
        a, b = map(int, input().split())
        if a == b:
            count += 1
            if count == 3:
                ret = True
                break
        else:
            count = 0

    if ret:
        print("Yes")
    else:
        print("No")


# tests
T1 = """
5
1 2
6 6
4 4
3 3
3 2
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
Yes
"""

T2 = """
5
1 1
2 2
3 4
5 5
6 6
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
No
"""

T3 = """
6
1 1
2 2
3 3
4 4
5 5
6 6
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
Yes
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
