# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(XS):
    from math import gcd
    from functools import reduce
    return reduce(gcd, XS)


def main():
    # parse input
    N = int(input())
    XS = list(map(int, input().split()))
    print(solve(XS))


# tests
T1 = """
3
2 6 6
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
2
"""

T2 = """
15
546 3192 1932 630 2100 4116 3906 3234 1302 1806 3528 3780 252 1008 588
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
42
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


if __name__ == "__main__":
    import sys
    input = sys.stdin.buffer.readline
    read = sys.stdin.buffer.read
    if sys.argv[-1] == "-t":
        print("testing")
        _test()
        sys.exit()
    main()

# end of snippets/main.py
