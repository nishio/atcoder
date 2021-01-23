# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    N, X = map(int, input().split())
    X *= 100
    total = 0
    for i in range(N):
        V, P = map(int, input().split())
        total += V * P
        if total > X:
            print(i + 1)
            return
    print(-1)


# tests
T1 = """
2 15
200 5
350 3
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
2
"""

T2 = """
3 1000000
1000 100
1000 100
1000 100
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
-1
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
