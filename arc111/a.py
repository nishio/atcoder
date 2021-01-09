# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    # parse input
    N, M = map(int, input().split())
    M2 = M * M
    doubling = [10 % M2]
    for i in range(60):
        doubling.append(
            (doubling[-1] ** 2) % M2
        )
    ret = 1
    for i in range(60):
        if N % 2:
            ret *= doubling[i]
            ret %= M2
        N //= 2

    print(ret // M)


# tests
T1 = """
1 2
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
1
"""

T2 = """
2 7
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
0
"""

T3 = """
1000000000000000000 9997
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
9015
"""


def _test():
    import doctest
    doctest.testmod()
    g = globals()
    for k in sorted(g):
        if k.startswith("TEST_"):
            print(k)
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
    sys.setrecursionlimit(10 ** 6)
    if sys.argv[-1] == "-t":
        print("testing")
        _test()
        sys.exit()
    main()
    sys.exit()

# end of snippets/main.py
