# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    import math
    A, B, W = map(int, input().split())
    W *= 1000
    WB = math.ceil(W / B)
    WA = math.floor(W / A)
    if WA < WB:
        print("UNSATISFIABLE")
        return
    print(WB, WA)

# tests
T1 = """
100 200 2
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
10 20
"""
T2 = """
120 150 2
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
14 16
"""
T3 = """
300 333 1
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
UNSATISFIABLE
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