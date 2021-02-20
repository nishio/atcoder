# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    N, K = map(int, input().split())
    for _i in range(K):
        s = str(N)
        g1 = int("".join(sorted(s, reverse=True)))
        g2 = int("".join(sorted(s)))
        N = g1 - g2

    print(N)


# tests
T1 = """
314 2
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
693
"""
T2 = """
1000000000 100
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
0
"""
T3 = """
6174 100000
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
6174
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
