# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    # parse input
    N, S, D = map(int, input().split())
    for _i in range(N):
        x, y = map(int, input().split())
        if x < S and y > D:
            print("Yes")
            return
    print("No")


# tests
T1 = """
4 9 9
5 5
15 5
5 15
15 15
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
Yes
"""

T2 = """
3 691 273
691 997
593 273
691 273
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
No
"""

T3 = """
7 100 100
10 11
12 67
192 79
154 197
142 158
20 25
17 108
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
