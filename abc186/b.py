# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    # parse input
    H, W = map(int, input().split())
    s = 0
    m = 999
    for _h in range(H):
        xs = list(map(int, input().split()))
        s += sum(xs)
        m = min(m, min(xs))
    print(s - m * H * W)


# tests
T1 = """
2 3
2 2 3
3 2 2
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
2
"""

T2 = """
3 3
99 99 99
99 0 99
99 99 99
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
792
"""

T3 = """
3 2
4 4
4 4
4 4
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
0
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
