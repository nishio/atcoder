#!/usr/bin/env python3
import string
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.buffer.readline
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")
MOD = 10 ** 9 + 7


def debug(*x):
    print(*x, file=sys.stderr)


def parse(s, i):
    if s[i] in string.digits:
        while s[i] in string.digits:
            i += 1
    else:
        bracket = 1
        i += 1
        while bracket:
            if s[i] == "{":
                bracket += 1
            elif s[i] == "}":
                bracket -= 1
            i += 1
    if s[i] == ":":
        return "dict"
    else:
        return "set"


def solve(s):
    if s == "{}":
        return "dict"
    assert s[0] == "{"
    return parse(s, 1)


def main():
    # parse input
    s = input().strip().decode('ascii')
    print(solve(s))


# tests
T1 = """
{}
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
dict
"""

T2 = """
{1,2}
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
set
"""

T3 = """
{1:2}
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
dict
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
    global read, input
    f = io.StringIO(s.strip())

    def input():
        return bytes(f.readline(), "ascii")

    def read():
        return bytes(f.read(), "ascii")


input = sys.stdin.buffer.readline
read = sys.stdin.buffer.read

if sys.argv[-1] == "-t":
    print("testing")
    _test()
    sys.exit()

main()
