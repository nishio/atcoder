# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    import sys
    sys.setrecursionlimit(10 ** 6)
    INF = sys.maxsize  # float("inf")
    MOD = 10 ** 9 + 7  # 998_244_353


def main():
    # parse input
    X, Y = map(int, input().split())
    if Y == 0:
        print("ERROR")
    else:
        print("%.2f" % (int(X / Y * 100) / 100))


# tests
T1 = """
100 3
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
33.33
"""

T2 = """
42 0
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
ERROR
"""

T3 = """
4 2
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
2.00
"""

T4 = """
2 3
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
0.66
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
